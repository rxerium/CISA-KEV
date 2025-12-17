#!/usr/bin/env python3
"""
Fetch PoC (Proof of Concept) availability data from ProjectDiscovery API

This script enriches CISA KEV data with PoC availability information from
ProjectDiscovery's vulnerability database.
"""

import csv
import json
import time
import requests
from pathlib import Path
from collections import defaultdict

# API Configuration
PDCP_API_BASE = "https://api.projectdiscovery.io/v2/vulnerability"
REQUEST_TIMEOUT = 10
RATE_LIMIT_DELAY = 0.5  # Delay between requests to avoid rate limiting

def load_kev_cves(csv_path='data/raw/cisa-kev.csv'):
    """Load CVE IDs from CISA KEV CSV."""
    cves = []
    try:
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                cves.append(row['cveID'])
        print(f"✅ Loaded {len(cves)} CVEs from CISA KEV", flush=True)
        return cves
    except Exception as e:
        print(f"❌ Error loading KEV CSV: {e}", flush=True)
        return []

def fetch_poc_info(cve_id):
    """
    Fetch PoC information from ProjectDiscovery API for a given CVE.

    Returns dict with:
    - is_poc: Boolean indicating if public PoC exists
    - poc_count: Number of PoCs available
    - epss_score: EPSS (Exploit Prediction Scoring System) score
    - is_kev: Boolean from ProjectDiscovery (should be True)
    - is_template: Boolean if Nuclei template exists
    """
    url = f"{PDCP_API_BASE}/{cve_id}"

    try:
        response = requests.get(url, timeout=REQUEST_TIMEOUT)

        if response.status_code == 200:
            data = response.json().get('data', {})

            # Get first PoC URL if available
            pocs = data.get('pocs', [])
            poc_url = pocs[0].get('url', '') if pocs else ''

            return {
                'cve_id': cve_id,
                'is_poc': data.get('is_poc', False),
                'poc_count': data.get('poc_count', 0),
                'poc_url': poc_url,
                'epss_score': data.get('epss_score', 0.0),
                'epss_percentile': data.get('epss_percentile', 0.0),
                'is_template': data.get('is_template', False),
                'cvss_score': data.get('cvss_score', 0.0),
                'severity': data.get('severity', 'unknown'),
                'is_remote': data.get('is_remote', False),
                'is_auth': data.get('is_auth', True),
                'vulnerability_type': data.get('vulnerability_type', ''),
                'status': 'success'
            }
        elif response.status_code == 404:
            return {
                'cve_id': cve_id,
                'is_poc': False,
                'poc_count': 0,
                'status': 'not_found'
            }
        else:
            print(f"⚠️  API returned status {response.status_code} for {cve_id}")
            return {
                'cve_id': cve_id,
                'status': 'error',
                'error_code': response.status_code
            }

    except requests.Timeout:
        print(f"⏱️  Timeout fetching {cve_id}")
        return {
            'cve_id': cve_id,
            'status': 'timeout'
        }
    except Exception as e:
        print(f"❌ Error fetching {cve_id}: {e}")
        return {
            'cve_id': cve_id,
            'status': 'error',
            'error': str(e)
        }

def fetch_all_poc_data(cves, output_file='data/raw/poc-data.json', checkpoint_file='logs/poc-checkpoint.json'):
    """
    Fetch PoC data for all CVEs with progress tracking and checkpointing.
    """
    results = {}

    # Load checkpoint if exists
    checkpoint_path = Path(checkpoint_file)
    if checkpoint_path.exists():
        try:
            with open(checkpoint_path, 'r') as f:
                results = json.load(f)
            print(f"📂 Loaded checkpoint with {len(results)} existing entries")
        except Exception as e:
            print(f"⚠️  Could not load checkpoint: {e}")

    total = len(cves)
    processed = len(results)
    failed = 0
    poc_found = sum(1 for r in results.values() if r.get('is_poc', False))

    print(f"\n🚀 Starting PoC data collection")
    print(f"   Total CVEs: {total}")
    print(f"   Already processed: {processed}")
    print(f"   Remaining: {total - processed}")
    print(f"   PoCs found so far: {poc_found}\n")

    for i, cve in enumerate(cves, 1):
        # Skip if already processed
        if cve in results:
            continue

        # Fetch data
        poc_info = fetch_poc_info(cve)
        results[cve] = poc_info

        if poc_info.get('is_poc'):
            poc_found += 1
            print(f"✅ [{i}/{total}] {cve} - PoC available ({poc_info.get('poc_count', 0)} sources)", flush=True)
        elif poc_info.get('status') == 'success':
            print(f"   [{i}/{total}] {cve} - No PoC", flush=True)
        else:
            failed += 1
            print(f"⚠️  [{i}/{total}] {cve} - {poc_info.get('status')}", flush=True)

        # Rate limiting
        time.sleep(RATE_LIMIT_DELAY)

        # Save checkpoint every 50 CVEs
        if i % 50 == 0:
            try:
                with open(checkpoint_path, 'w') as f:
                    json.dump(results, f, indent=2)
                print(f"💾 Checkpoint saved ({i}/{total})")
            except Exception as e:
                print(f"⚠️  Could not save checkpoint: {e}")

    # Save final results
    output_path = Path(output_file)
    try:
        with open(output_path, 'w') as f:
            json.dump(results, f, indent=2)
        print(f"\n✅ Final results saved to {output_path}")
    except Exception as e:
        print(f"❌ Error saving results: {e}")

    # Clean up checkpoint
    if checkpoint_path.exists():
        checkpoint_path.unlink()

    # Generate summary
    print("\n" + "="*70)
    print("📊 POC DATA COLLECTION SUMMARY")
    print("="*70)
    print(f"  Total CVEs processed: {len(results)}")
    print(f"  CVEs with PoCs: {poc_found} ({poc_found/len(results)*100:.1f}%)")
    print(f"  CVEs without PoCs: {len(results) - poc_found}")
    print(f"  Failed/Errors: {failed}")
    print("="*70)

    return results

def generate_poc_list(poc_data, output_file='data/lists/CISA-POC-List.txt'):
    """
    Generate a text file listing CVEs that have public PoCs available.
    Similar format to CISA-Scannable-List.txt
    """
    poc_cves = [
        cve for cve, data in poc_data.items()
        if data.get('is_poc', False)
    ]

    poc_cves.sort()

    output_path = Path(output_file)
    try:
        with open(output_path, 'w') as f:
            for cve in poc_cves:
                f.write(f"{cve}\n")
        print(f"✅ PoC list saved to {output_path} ({len(poc_cves)} CVEs)")
    except Exception as e:
        print(f"❌ Error saving PoC list: {e}")

    return poc_cves

def generate_enhanced_stats(poc_data):
    """Generate statistics about PoC availability."""
    total = len(poc_data)
    with_poc = sum(1 for d in poc_data.values() if d.get('is_poc', False))
    without_poc = total - with_poc

    # EPSS statistics for CVEs with PoCs
    epss_scores = [
        d.get('epss_score', 0)
        for d in poc_data.values()
        if d.get('is_poc', False) and d.get('epss_score')
    ]

    avg_epss = sum(epss_scores) / len(epss_scores) if epss_scores else 0

    # Severity breakdown for PoC CVEs
    severity_counts = defaultdict(int)
    for d in poc_data.values():
        if d.get('is_poc', False):
            severity = d.get('severity', 'unknown')
            severity_counts[severity] += 1

    # Remote vs Local for PoC CVEs
    remote_count = sum(1 for d in poc_data.values() if d.get('is_poc') and d.get('is_remote'))

    # Auth required statistics
    no_auth_count = sum(1 for d in poc_data.values() if d.get('is_poc') and not d.get('is_auth'))

    print("\n" + "="*70)
    print("📊 POC AVAILABILITY STATISTICS")
    print("="*70)
    print(f"  Total KEV CVEs analyzed: {total}")
    print(f"  CVEs with public PoCs: {with_poc} ({with_poc/total*100:.1f}%)")
    print(f"  CVEs without public PoCs: {without_poc} ({without_poc/total*100:.1f}%)")

    if epss_scores:
        print(f"\n  Average EPSS score (PoC CVEs): {avg_epss:.4f}")

    if severity_counts:
        print(f"\n  Severity distribution (PoC CVEs):")
        for severity in ['critical', 'high', 'medium', 'low', 'unknown']:
            count = severity_counts.get(severity, 0)
            if count > 0:
                print(f"    {severity.capitalize()}: {count}")

    print(f"\n  Remote exploitable (PoC CVEs): {remote_count} ({remote_count/with_poc*100:.1f}%)")
    print(f"  No authentication required: {no_auth_count} ({no_auth_count/with_poc*100:.1f}%)")
    print("="*70)

def main():
    """Main execution function."""
    print("="*70)
    print("🔍 CISA KEV PoC Data Collector")
    print("   Powered by ProjectDiscovery API")
    print("="*70)

    # Load CVEs from CISA KEV
    cves = load_kev_cves()
    if not cves:
        print("❌ No CVEs loaded. Exiting.")
        return

    # Fetch PoC data
    poc_data = fetch_all_poc_data(cves)

    # Generate PoC list file
    generate_poc_list(poc_data)

    # Generate enhanced statistics
    generate_enhanced_stats(poc_data)

    print("\n✅ PoC data collection complete!")
    print("   - poc-data.json: Full PoC data")
    print("   - CISA-POC-List.txt: CVEs with public PoCs")

if __name__ == '__main__':
    main()
