#!/usr/bin/env python3
"""
Fetch VulnCheck KEV data and integrate with existing pipeline

VulnCheck maintains a comprehensive KEV list that includes additional
vulnerabilities beyond CISA's official KEV catalog.
"""

import os
import json
import csv
import requests
from pathlib import Path
from datetime import datetime

# API Configuration
VULNCHECK_API_URL = "https://api.vulncheck.com/v3/index/vulncheck-kev"
API_KEY = os.getenv('VULNCHECK_API_KEY')
REQUEST_TIMEOUT = 30
PAGE_SIZE = 100  # Fetch in batches

def fetch_all_vulncheck_kev():
    """Fetch complete VulnCheck KEV dataset with pagination"""
    if not API_KEY:
        raise ValueError("VULNCHECK_API_KEY environment variable not set")

    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Accept': 'application/json'
    }

    all_data = []
    page = 1

    print("🔍 Fetching VulnCheck KEV data...")

    # First request to get total count
    try:
        response = requests.get(
            VULNCHECK_API_URL,
            headers=headers,
            params={'limit': PAGE_SIZE, 'page': 1},
            timeout=REQUEST_TIMEOUT
        )
        response.raise_for_status()
        data = response.json()

        total_docs = data.get('_meta', {}).get('total_documents', 0)
        total_pages = (total_docs + PAGE_SIZE - 1) // PAGE_SIZE  # Ceiling division

        print(f"  Total vulnerabilities: {total_docs}")
        print(f"  Total pages: {total_pages}\n")

        # Add first page data
        batch = data.get('data', [])
        all_data.extend(batch)
        print(f"  Page {page}/{total_pages}: Fetched {len(batch)} vulnerabilities (Total: {len(all_data)})")

        # Fetch remaining pages
        for page in range(2, total_pages + 1):
            try:
                response = requests.get(
                    VULNCHECK_API_URL,
                    headers=headers,
                    params={'limit': PAGE_SIZE, 'page': page},
                    timeout=REQUEST_TIMEOUT
                )
                response.raise_for_status()

                data = response.json()
                batch = data.get('data', [])
                all_data.extend(batch)

                print(f"  Page {page}/{total_pages}: Fetched {len(batch)} vulnerabilities (Total: {len(all_data)})")

                if len(batch) == 0:
                    break

            except requests.exceptions.RequestException as e:
                print(f"⚠️  Error fetching page {page}: {e}")
                continue

    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching VulnCheck data: {e}")
        raise

    print(f"✅ Fetched {len(all_data)} total vulnerabilities from VulnCheck KEV")
    return all_data

def save_raw_data(data):
    """Save raw VulnCheck data as JSON"""
    output_path = Path('data/raw/vulncheck-kev.json')
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

    print(f"💾 Saved raw data to {output_path}")

def extract_cve_list(data):
    """Extract CVE IDs from VulnCheck data"""
    cves = []
    for vuln in data:
        cve_list = vuln.get('cve', [])
        # CVE field can be a list of CVEs
        if isinstance(cve_list, list):
            for cve in cve_list:
                if cve and isinstance(cve, str) and cve.startswith('CVE-'):
                    cves.append(cve)
        elif isinstance(cve_list, str) and cve_list.startswith('CVE-'):
            cves.append(cve_list)

    # Remove duplicates and sort
    unique_cves = sorted(set(cves))

    # Save CVE list
    list_path = Path('data/lists/VulnCheck-KEV-List.txt')
    list_path.parent.mkdir(parents=True, exist_ok=True)

    with open(list_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(unique_cves))

    print(f"📝 Saved {len(unique_cves)} unique CVEs to {list_path}")
    return unique_cves

def convert_to_csv(data):
    """Convert VulnCheck data to CSV format similar to CISA KEV"""
    csv_path = Path('data/raw/vulncheck-kev.csv')

    # Define CSV structure similar to CISA KEV
    fieldnames = [
        'cveID',
        'vendorProject',
        'product',
        'vulnerabilityName',
        'dateAdded',
        'shortDescription',
        'requiredAction',
        'dueDate',
        'knownRansomwareCampaignUse',
        'notes'
    ]

    with open(csv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for vuln in data:
            # Get CVE(s) - can be a list
            cve_list = vuln.get('cve', [])
            if isinstance(cve_list, list):
                cve_id = ', '.join(cve_list) if cve_list else ''
            else:
                cve_id = cve_list

            # Map VulnCheck fields to CISA KEV format
            row = {
                'cveID': cve_id,
                'vendorProject': vuln.get('vendorProject', ''),
                'product': vuln.get('product', ''),
                'vulnerabilityName': vuln.get('vulnerabilityName', ''),
                'dateAdded': vuln.get('date_added', ''),
                'shortDescription': vuln.get('shortDescription', ''),
                'requiredAction': vuln.get('required_action', ''),
                'dueDate': vuln.get('due_date', ''),
                'knownRansomwareCampaignUse': vuln.get('knownRansomwareCampaignUse', 'Unknown'),
                'notes': f"Source: VulnCheck KEV"
            }
            writer.writerow(row)

    print(f"📊 Converted to CSV format: {csv_path}")

def generate_statistics(data, cve_list):
    """Generate basic statistics about VulnCheck KEV"""
    stats = {
        'total_vulnerabilities': len(data),
        'unique_cves': len(cve_list),
        'fetched_at': datetime.utcnow().isoformat(),
        'source': 'VulnCheck KEV',
        'api_version': 'v3'
    }

    # Count ransomware-associated
    ransomware_count = sum(
        1 for v in data
        if v.get('knownRansomwareCampaignUse', '').lower() == 'known'
    )
    stats['ransomware_associated'] = ransomware_count

    # Save stats
    stats_path = Path('data/raw/vulncheck-stats.json')
    with open(stats_path, 'w', encoding='utf-8') as f:
        json.dump(stats, f, indent=2)

    print(f"\n📊 VulnCheck KEV Statistics:")
    print(f"  Total Vulnerabilities: {stats['total_vulnerabilities']}")
    print(f"  Unique CVEs: {stats['unique_cves']}")
    print(f"  Ransomware-Associated: {stats['ransomware_associated']}")

def main():
    """Main execution function"""
    try:
        # Fetch all data
        data = fetch_all_vulncheck_kev()

        # Save raw data
        save_raw_data(data)

        # Extract CVE list
        cve_list = extract_cve_list(data)

        # Convert to CSV
        convert_to_csv(data)

        # Generate statistics
        generate_statistics(data, cve_list)

        print("\n✅ VulnCheck KEV data fetch completed successfully!")

    except Exception as e:
        print(f"\n❌ Error: {e}")
        raise

if __name__ == '__main__':
    main()
