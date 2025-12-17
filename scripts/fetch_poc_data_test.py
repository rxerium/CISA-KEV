#!/usr/bin/env python3
"""
Quick test of PoC data fetching - fetches only first 10 CVEs for demonstration
"""

import csv
import json
import time
import requests
import sys
from pathlib import Path

PDCP_API_BASE = "https://api.projectdiscovery.io/v2/vulnerability"
REQUEST_TIMEOUT = 10
RATE_LIMIT_DELAY = 0.5

def load_kev_cves(csv_path='cisa-kev.csv', limit=10):
    """Load first N CVE IDs from CISA KEV CSV."""
    cves = []
    try:
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for i, row in enumerate(reader):
                if i >= limit:
                    break
                cves.append(row['cveID'])
        print(f"✅ Loaded {len(cves)} CVEs for testing", flush=True)
        return cves
    except Exception as e:
        print(f"❌ Error loading KEV CSV: {e}", flush=True)
        return []

def fetch_poc_info(cve_id):
    """Fetch PoC information from ProjectDiscovery API."""
    url = f"{PDCP_API_BASE}/{cve_id}"

    try:
        response = requests.get(url, timeout=REQUEST_TIMEOUT)

        if response.status_code == 200:
            data = response.json().get('data', {})

            return {
                'cve_id': cve_id,
                'is_poc': data.get('is_poc', False),
                'poc_count': data.get('poc_count', 0),
                'epss_score': data.get('epss_score', 0.0),
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
            return {
                'cve_id': cve_id,
                'status': 'error',
                'error_code': response.status_code
            }

    except Exception as e:
        return {
            'cve_id': cve_id,
            'status': 'error',
            'error': str(e)
        }

def main():
    print("🔍 CISA KEV PoC Data Collector - TEST MODE (First 10 CVEs)")
    print("="*70, flush=True)

    # Load first 10 CVEs
    cves = load_kev_cves(limit=10)
    if not cves:
        print("❌ No CVEs loaded. Exiting.", flush=True)
        return

    results = {}
    poc_found = 0

    print(f"\n🚀 Fetching PoC data for {len(cves)} CVEs...\n", flush=True)

    for i, cve in enumerate(cves, 1):
        poc_info = fetch_poc_info(cve)
        results[cve] = poc_info

        if poc_info.get('is_poc'):
            poc_found += 1
            print(f"✅ [{i}/{len(cves)}] {cve} - PoC available ({poc_info.get('poc_count', 0)} sources)", flush=True)
        elif poc_info.get('status') == 'success':
            print(f"   [{i}/{len(cves)}] {cve} - No PoC", flush=True)
        else:
            print(f"⚠️  [{i}/{len(cves)}] {cve} - {poc_info.get('status')}", flush=True)

        # Rate limiting
        if i < len(cves):
            time.sleep(RATE_LIMIT_DELAY)

    # Save results
    with open('poc-data-test.json', 'w') as f:
        json.dump(results, f, indent=2)

    # Generate PoC list
    poc_cves = [cve for cve, data in results.items() if data.get('is_poc', False)]
    with open('CISA-POC-List-test.txt', 'w') as f:
        for cve in sorted(poc_cves):
            f.write(f"{cve}\n")

    print("\n" + "="*70)
    print("📊 TEST RESULTS")
    print("="*70)
    print(f"  CVEs processed: {len(results)}")
    print(f"  CVEs with PoCs: {poc_found} ({poc_found/len(results)*100:.1f}%)")
    print(f"  CVEs without PoCs: {len(results) - poc_found}")
    print("\n  Files created:")
    print("    - poc-data-test.json")
    print("    - CISA-POC-List-test.txt")
    print("="*70, flush=True)

if __name__ == '__main__':
    main()
