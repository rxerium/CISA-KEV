#!/usr/bin/env python3
"""
Generate useful statistics for README.md
This script analyzes the CISA KEV database and outputs markdown stats
"""

import csv
import json
from collections import Counter, defaultdict
from datetime import datetime, timedelta
from pathlib import Path

def load_kev_data():
    """Load the CISA KEV CSV file."""
    with open('cisa-kev.csv', 'r', encoding='utf-8') as f:
        return list(csv.DictReader(f))

def load_scannable_list():
    """Load the list of scannable CVEs."""
    with open('CISA-Scannable-List.txt', 'r') as f:
        return set(line.strip() for line in f if line.strip())

def load_poc_list():
    """Load the list of CVEs with public PoCs."""
    poc_file = Path('CISA-POC-List.txt')
    if poc_file.exists():
        with open(poc_file, 'r') as f:
            return set(line.strip() for line in f if line.strip())
    return set()

def load_poc_data():
    """Load detailed PoC data from JSON file."""
    poc_data_file = Path('poc-data.json')
    if poc_data_file.exists():
        with open(poc_data_file, 'r') as f:
            return json.load(f)
    return {}

def export_gap_csv(gap_cve_details, poc_data):
    """Export priority gap CVEs to detailed CSV file."""
    csv_path = Path('CISA-Priority-Gap.csv')

    try:
        with open(csv_path, 'w', newline='', encoding='utf-8') as f:
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
                'notes',
                'cwes',
                'poc_url',
                'poc_count',
                'epss_score',
                'epss_percentile',
                'cvss_score',
                'severity',
                'is_remote',
                'is_auth',
                'vulnerability_type'
            ]

            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()

            for cve_detail in gap_cve_details:
                cve_id = cve_detail['cveID']

                # Get PoC data if available
                poc_info = poc_data.get(cve_id, {}) if poc_data else {}

                # Build row with all available data
                row = {
                    'cveID': cve_id,
                    'vendorProject': cve_detail['vendorProject'],
                    'product': cve_detail['product'],
                    'vulnerabilityName': cve_detail['vulnerabilityName'],
                    'dateAdded': cve_detail['dateAdded'],
                    'shortDescription': cve_detail['shortDescription'],
                    'requiredAction': cve_detail['requiredAction'],
                    'dueDate': cve_detail['dueDate'],
                    'knownRansomwareCampaignUse': cve_detail['knownRansomwareCampaignUse'],
                    'notes': cve_detail.get('notes', ''),
                    'cwes': cve_detail.get('cwes', ''),
                    'poc_url': poc_info.get('poc_url', ''),
                    'poc_count': poc_info.get('poc_count', ''),
                    'epss_score': poc_info.get('epss_score', ''),
                    'epss_percentile': poc_info.get('epss_percentile', ''),
                    'cvss_score': poc_info.get('cvss_score', ''),
                    'severity': poc_info.get('severity', ''),
                    'is_remote': poc_info.get('is_remote', ''),
                    'is_auth': poc_info.get('is_auth', ''),
                    'vulnerability_type': poc_info.get('vulnerability_type', '')
                }

                writer.writerow(row)

        print(f"✅ Exported {len(gap_cve_details)} priority gap CVEs to {csv_path}", flush=True)

    except Exception as e:
        print(f"❌ Error exporting gap CSV: {e}", flush=True)

def generate_stats():
    """Generate comprehensive statistics."""
    data = load_kev_data()
    scannable = load_scannable_list()
    poc_list = load_poc_list()
    poc_data = load_poc_data()

    total_cves = len(data)
    scannable_count = len(scannable)
    coverage = (scannable_count / total_cves * 100) if total_cves > 0 else 0

    # PoC statistics
    poc_count = len(poc_list)
    poc_coverage = (poc_count / total_cves * 100) if total_cves > 0 else 0

    # CVEs with both PoC and Nuclei template
    both_poc_and_nuclei = len(scannable & poc_list)

    # CVEs with PoC but no Nuclei template (gap)
    poc_gap = len(poc_list - scannable)
    
    # Ransomware stats
    ransomware = [cve for cve in data if cve['knownRansomwareCampaignUse'] == 'Known']
    ransomware_count = len(ransomware)
    ransomware_pct = (ransomware_count / total_cves * 100) if total_cves > 0 else 0
    
    # Vendor stats
    vendor_counts = Counter(cve['vendorProject'] for cve in data)
    top_vendors = vendor_counts.most_common(10)
    
    # Product stats
    product_counts = Counter(cve['product'] for cve in data)
    top_products = product_counts.most_common(10)
    
    # CWE stats
    all_cwes = []
    for cve in data:
        if cve['cwes']:
            all_cwes.extend([c.strip() for c in cve['cwes'].split(',')])
    cwe_counts = Counter(all_cwes)
    top_cwes = cwe_counts.most_common(5)
    
    # Scannable by top vendors
    scannable_by_vendor = []
    for vendor, count in top_vendors[:5]:
        vendor_cves = [cve for cve in data if cve['vendorProject'] == vendor]
        vendor_scannable = len([cve for cve in vendor_cves if cve['cveID'] in scannable])
        vendor_coverage = (vendor_scannable / count * 100) if count > 0 else 0
        scannable_by_vendor.append((vendor, vendor_scannable, count, vendor_coverage))
    
    # Recent additions (last 30 days)
    thirty_days_ago = datetime.now() - timedelta(days=30)
    recent = []
    for cve in data:
        try:
            date_added = datetime.strptime(cve['dateAdded'], '%Y-%m-%d')
            if date_added >= thirty_days_ago:
                recent.append(cve)
        except:
            pass
    
    recent_count = len(recent)
    recent_scannable = len([cve for cve in recent if cve['cveID'] in scannable])
    
    # Generate markdown
    poc_status = f"**{poc_count:,} ({poc_coverage:.1f}%)**" if poc_count > 0 else "⏳ *Data collection pending*"

    stats_md = f"""
## 📊 Database Statistics

### Overview
- **Total CVEs in KEV**: {total_cves:,}
- **Scannable with Nuclei**: {scannable_count:,} ({coverage:.1f}%)
- **With Public PoCs**: {poc_status}
- **Unscannable**: {total_cves - scannable_count:,} ({100 - coverage:.1f}%)
- **Ransomware-Associated**: {ransomware_count:,} ({ransomware_pct:.1f}%)
- **Unique Vendors**: {len(vendor_counts):,}
- **Unique Products**: {len(product_counts):,}

### Key Insights
- 🎯 **{top_vendors[0][0]}** is the most represented vendor with **{top_vendors[0][1]} CVEs**
- 🔍 **{scannable_count:,} CVEs** can be actively scanned with Nuclei templates"""

    if poc_count > 0:
        stats_md += f"""
- 💣 **{poc_count:,} CVEs** ({poc_coverage:.1f}%) have public proof-of-concept exploits available
- 🎯 **{both_poc_and_nuclei} CVEs** have both PoC and Nuclei template (fully testable)
- 🔓 **{poc_gap} CVEs** have PoC but no Nuclei template (testing gap)"""

    stats_md += f"""
- 🦠 **{ransomware_count:,} CVEs** ({ransomware_pct:.1f}%) are known to be used in ransomware campaigns
- 📅 **{recent_count} new CVEs** were added in the last 30 days
- 🔒 Most common vulnerability type: **{top_cwes[0][0]}** ({top_cwes[0][1]} occurrences)
- ⚠️ **{scannable_by_vendor[0][0]}** has the highest scanning coverage at {scannable_by_vendor[0][3]:.1f}%, while **{[v[0] for v in scannable_by_vendor if v[3] == 0.0][0] if any(v[3] == 0.0 for v in scannable_by_vendor) else 'N/A'}** and **{[v[0] for v in scannable_by_vendor if v[3] == 0.0][1] if len([v for v in scannable_by_vendor if v[3] == 0.0]) > 1 else 'N/A'}** have 0%

### Recent Activity (Last 30 Days)
- **CVEs Added**: {recent_count}
- **Scannable Added**: {recent_scannable}
- **New Coverage**: {(recent_scannable / recent_count * 100) if recent_count > 0 else 0:.1f}%

### Top 10 Affected Vendors
| Rank | Vendor | CVE Count | Scannable | With PoC | Scanning Coverage |
|------|--------|-----------|-----------|----------|-------------------|
"""

    for i, (vendor, count) in enumerate(top_vendors, 1):
        vendor_cves = [cve for cve in data if cve['vendorProject'] == vendor]
        vendor_scannable = len([cve for cve in vendor_cves if cve['cveID'] in scannable])
        vendor_poc = len([cve for cve in vendor_cves if cve['cveID'] in poc_list]) if poc_count > 0 else 0
        vendor_coverage = (vendor_scannable / count * 100) if count > 0 else 0
        poc_display = str(vendor_poc) if poc_count > 0 else "-"
        stats_md += f"| {i} | {vendor} | {count} | {vendor_scannable} | {poc_display} | {vendor_coverage:.1f}% |\n"
    
    stats_md += """
### Top 10 Vulnerable Products
| Rank | Product | CVE Count |
|------|---------|-----------|
"""
    
    for i, (product, count) in enumerate(top_products, 1):
        stats_md += f"| {i} | {product} | {count} |\n"
    
    stats_md += """
### Top 5 Vulnerability Types (CWEs)
| Rank | CWE | Count |
|------|-----|-------|
"""
    
    for i, (cwe, count) in enumerate(top_cwes, 1):
        stats_md += f"| {i} | {cwe} | {count} |\n"
    
    stats_md += """
### Ransomware-Associated CVEs
| Vendor | Ransomware CVEs |
|--------|-----------------|
"""
    
    ransomware_vendors = Counter(cve['vendorProject'] for cve in ransomware)
    for vendor, count in ransomware_vendors.most_common(10):
        stats_md += f"| {vendor} | {count} |\n"
    
    # Priority Gap Table - CVEs with PoC but no Nuclei template
    if poc_count > 0:
        gap_cves = poc_list - scannable
        gap_cve_details = [cve for cve in data if cve['cveID'] in gap_cves]

        # Sort by date added (most recent first)
        gap_cve_details.sort(key=lambda x: x['dateAdded'], reverse=True)

        # Export detailed CSV
        export_gap_csv(gap_cve_details, poc_data)

        stats_md += f"""
### 🔓 Priority Gap: CVEs with Public PoCs but No Nuclei Template

**Total Gap CVEs:** {len(gap_cves)} vulnerabilities have public exploits but lack automated detection templates.

📥 **Download Full Data:** [CISA-Priority-Gap.csv](CISA-Priority-Gap.csv) - Detailed CSV export with PoC URLs, EPSS scores, CVSS scores, severity levels, and vulnerability metadata.

**All {len(gap_cves)} gap CVEs** listed below (sorted by date added to KEV, most recent first):

| CVE ID | Vendor | Product | Date Added | PoC | Ransomware |
|--------|--------|---------|------------|-----|------------|
"""

        for cve_detail in gap_cve_details:
            cve_id = cve_detail['cveID']
            ransomware_indicator = "🦠" if cve_detail['knownRansomwareCampaignUse'] == 'Known' else ""
            vendor = cve_detail['vendorProject'][:25]  # Truncate long names
            product = cve_detail['product'][:25]

            # Get PoC URL from poc_data if available
            poc_link = ""
            if poc_data and cve_id in poc_data:
                poc_url = poc_data[cve_id].get('poc_url', '')
                if poc_url:
                    poc_link = f"[PoC]({poc_url})"
                else:
                    poc_link = "✓"
            else:
                poc_link = "✓"

            stats_md += f"| {cve_id} | {vendor} | {product} | {cve_detail['dateAdded']} | {poc_link} | {ransomware_indicator} |\n"

    stats_md += f"""
*Last updated: {datetime.now().strftime('%Y-%m-%d')}*
"""

    return stats_md

if __name__ == '__main__':
    print(generate_stats())
