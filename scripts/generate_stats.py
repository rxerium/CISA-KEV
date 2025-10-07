#!/usr/bin/env python3
"""
Generate useful statistics for README.md
This script analyzes the CISA KEV database and outputs markdown stats
"""

import csv
from collections import Counter, defaultdict
from datetime import datetime, timedelta

def load_kev_data():
    """Load the CISA KEV CSV file."""
    with open('cisa-kev.csv', 'r', encoding='utf-8') as f:
        return list(csv.DictReader(f))

def load_scannable_list():
    """Load the list of scannable CVEs."""
    with open('CISA-Scannable-List.txt', 'r') as f:
        return set(line.strip() for line in f if line.strip())

def generate_stats():
    """Generate comprehensive statistics."""
    data = load_kev_data()
    scannable = load_scannable_list()
    
    total_cves = len(data)
    scannable_count = len(scannable)
    coverage = (scannable_count / total_cves * 100) if total_cves > 0 else 0
    
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
    stats_md = f"""
## 📊 Database Statistics

### Overview
- **Total CVEs in KEV**: {total_cves:,}
- **Scannable with Nuclei**: {scannable_count:,} ({coverage:.1f}%)
- **Unscannable**: {total_cves - scannable_count:,} ({100 - coverage:.1f}%)
- **Ransomware-Associated**: {ransomware_count:,} ({ransomware_pct:.1f}%)
- **Unique Vendors**: {len(vendor_counts):,}
- **Unique Products**: {len(product_counts):,}

### Key Insights
- 🎯 **{top_vendors[0][0]}** is the most represented vendor with **{top_vendors[0][1]} CVEs**
- 🔍 **{scannable_count:,} CVEs** can be actively scanned with Nuclei templates
- 🦠 **{ransomware_count:,} CVEs** ({ransomware_pct:.1f}%) are known to be used in ransomware campaigns
- 📅 **{recent_count} new CVEs** were added in the last 30 days
- 🔒 Most common vulnerability type: **{top_cwes[0][0]}** ({top_cwes[0][1]} occurrences)
- ⚠️ **{scannable_by_vendor[0][0]}** has the highest scanning coverage at {scannable_by_vendor[0][3]:.1f}%, while **{[v[0] for v in scannable_by_vendor if v[3] == 0.0][0] if any(v[3] == 0.0 for v in scannable_by_vendor) else 'N/A'}** and **{[v[0] for v in scannable_by_vendor if v[3] == 0.0][1] if len([v for v in scannable_by_vendor if v[3] == 0.0]) > 1 else 'N/A'}** have 0%

### Recent Activity (Last 30 Days)
- **CVEs Added**: {recent_count}
- **Scannable Added**: {recent_scannable}
- **New Coverage**: {(recent_scannable / recent_count * 100) if recent_count > 0 else 0:.1f}%

### Top 10 Affected Vendors
| Rank | Vendor | CVE Count | Scannable | Scanning Coverage |
|------|--------|-----------|-----------|-------------------|
"""
    
    for i, (vendor, count) in enumerate(top_vendors, 1):
        vendor_cves = [cve for cve in data if cve['vendorProject'] == vendor]
        vendor_scannable = len([cve for cve in vendor_cves if cve['cveID'] in scannable])
        vendor_coverage = (vendor_scannable / count * 100) if count > 0 else 0
        stats_md += f"| {i} | {vendor} | {count} | {vendor_scannable} | {vendor_coverage:.1f}% |\n"
    
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
    
    stats_md += f"""
*Last updated: {datetime.now().strftime('%Y-%m-%d')}*
"""
    
    return stats_md

if __name__ == '__main__':
    print(generate_stats())
