#!/usr/bin/env python3
"""
CISA KEV Query Tool

CLI tool to search and filter the CISA KEV database.
"""

import csv
import sys
from datetime import datetime, timedelta
import argparse
from collections import defaultdict
from pathlib import Path

def load_kev_data(csv_path='data/raw/cisa-kev.csv'):
    """Load the CISA KEV CSV file."""
    try:
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            return list(reader)
    except Exception as e:
        print(f"❌ Error loading CSV: {e}")
        return []

def load_scannable_list(txt_path='data/lists/CISA-Scannable-List.txt'):
    """Load the list of scannable CVEs."""
    try:
        with open(txt_path, 'r') as f:
            return set(line.strip() for line in f if line.strip())
    except Exception as e:
        print(f"❌ Error loading scannable list: {e}")
        return set()

def load_poc_list(txt_path='data/lists/CISA-POC-List.txt'):
    """Load the list of CVEs with public PoCs."""
    try:
        poc_file = Path(txt_path)
        if poc_file.exists():
            with open(poc_file, 'r') as f:
                return set(line.strip() for line in f if line.strip())
        return set()
    except Exception as e:
        print(f"❌ Error loading PoC list: {e}")
        return set()

def format_cve(cve, scannable_set, poc_set=None, show_details=False):
    """Format a CVE entry for display."""
    is_scannable = cve['cveID'] in scannable_set
    scannable_icon = "✅" if is_scannable else "❌"
    ransomware_icon = "🦠" if cve['knownRansomwareCampaignUse'] == 'Known' else "  "

    # Add PoC indicator
    has_poc = cve['cveID'] in poc_set if poc_set else False
    poc_icon = "💣" if has_poc else "  "

    output = f"{scannable_icon} {ransomware_icon} {poc_icon} {cve['cveID']} - {cve['vendorProject']} {cve['product']}"

    if show_details:
        output += f"\n    📝 {cve['vulnerabilityName']}"
        output += f"\n    📅 Added: {cve['dateAdded']}"
        output += f"\n    📋 {cve['shortDescription'][:150]}..."
        if cve['cwes']:
            output += f"\n    🔍 CWE: {cve['cwes']}"
        if poc_set:
            output += f"\n    💣 Public PoC: {'Yes' if has_poc else 'No'}"

    return output

def query_by_vendor(data, vendor, scannable_set, poc_set=None, show_details=False):
    """Query CVEs by vendor."""
    results = [cve for cve in data if vendor.lower() in cve['vendorProject'].lower()]
    print(f"\n🔍 Found {len(results)} CVEs for vendor containing '{vendor}':\n")
    for cve in results:
        print(format_cve(cve, scannable_set, poc_set, show_details))

def query_by_product(data, product, scannable_set, poc_set=None, show_details=False):
    """Query CVEs by product."""
    results = [cve for cve in data if product.lower() in cve['product'].lower()]
    print(f"\n🔍 Found {len(results)} CVEs for product containing '{product}':\n")
    for cve in results:
        print(format_cve(cve, scannable_set, poc_set, show_details))

def query_by_cve_id(data, cve_id, scannable_set, poc_set=None):
    """Query specific CVE by ID."""
    cve_id = cve_id.upper()
    for cve in data:
        if cve['cveID'] == cve_id:
            is_scannable = cve['cveID'] in scannable_set
            has_poc = cve['cveID'] in poc_set if poc_set else False
            print(f"\n{'='*70}")
            print(f"CVE ID: {cve['cveID']}")
            print(f"{'='*70}")
            print(f"Vendor/Project: {cve['vendorProject']}")
            print(f"Product: {cve['product']}")
            print(f"Vulnerability: {cve['vulnerabilityName']}")
            print(f"Date Added: {cve['dateAdded']}")
            print(f"Due Date: {cve['dueDate']}")
            print(f"Scannable: {'✅ Yes' if is_scannable else '❌ No'}")
            print(f"Ransomware: {'🦠 Known' if cve['knownRansomwareCampaignUse'] == 'Known' else '❌ Unknown'}")
            if poc_set:
                print(f"Public PoC: {'💣 Yes' if has_poc else '❌ No'}")
            if cve['cwes']:
                print(f"CWE: {cve['cwes']}")
            print(f"\nDescription:")
            print(f"  {cve['shortDescription']}")
            print(f"\nRequired Action:")
            print(f"  {cve['requiredAction']}")
            if cve['notes']:
                print(f"\nNotes:")
                print(f"  {cve['notes'][:200]}...")
            print(f"{'='*70}\n")
            return
    print(f"\n❌ CVE {cve_id} not found in KEV database.\n")

def query_recent(data, days, scannable_set, poc_set=None, show_details=False):
    """Query CVEs added in the last N days."""
    cutoff = datetime.now() - timedelta(days=days)
    results = []
    for cve in data:
        try:
            date_added = datetime.strptime(cve['dateAdded'], '%Y-%m-%d')
            if date_added >= cutoff:
                results.append(cve)
        except:
            pass

    results.sort(key=lambda x: x['dateAdded'], reverse=True)
    print(f"\n🔍 Found {len(results)} CVEs added in the last {days} days:\n")
    for cve in results:
        print(format_cve(cve, scannable_set, poc_set, show_details))

def query_ransomware(data, scannable_set, poc_set=None, show_details=False):
    """Query CVEs associated with ransomware."""
    results = [cve for cve in data if cve['knownRansomwareCampaignUse'] == 'Known']
    print(f"\n🦠 Found {len(results)} CVEs associated with ransomware campaigns:\n")
    for cve in results:
        print(format_cve(cve, scannable_set, poc_set, show_details))

def query_scannable_only(data, scannable_set, poc_set=None, show_details=False):
    """Show only scannable CVEs."""
    results = [cve for cve in data if cve['cveID'] in scannable_set]
    print(f"\n✅ Found {len(results)} scannable CVEs:\n")
    for cve in results:
        print(format_cve(cve, scannable_set, poc_set, show_details))

def query_unscannable_only(data, scannable_set, poc_set=None, show_details=False):
    """Show only unscannable CVEs."""
    results = [cve for cve in data if cve['cveID'] not in scannable_set]
    print(f"\n❌ Found {len(results)} unscannable CVEs:\n")
    for cve in results:
        print(format_cve(cve, scannable_set, poc_set, show_details))

def query_poc_only(data, poc_set, scannable_set, show_details=False):
    """Show only CVEs with public PoCs."""
    if not poc_set:
        print("\n⚠️  No PoC data available. Run 'python scripts/fetch_poc_data.py' first.\n")
        return

    results = [cve for cve in data if cve['cveID'] in poc_set]
    print(f"\n💣 Found {len(results)} CVEs with public PoCs:\n")
    for cve in results:
        print(format_cve(cve, scannable_set, poc_set, show_details))

def query_poc_gap(data, poc_set, scannable_set, show_details=False):
    """Show CVEs with PoC but no Nuclei template (testing gap)."""
    if not poc_set:
        print("\n⚠️  No PoC data available. Run 'python scripts/fetch_poc_data.py' first.\n")
        return

    gap_cves = poc_set - scannable_set
    results = [cve for cve in data if cve['cveID'] in gap_cves]
    print(f"\n🔓 Found {len(results)} CVEs with PoC but no Nuclei template (priority testing gap):\n")
    for cve in results:
        print(format_cve(cve, scannable_set, poc_set, show_details))

def show_stats(data, scannable_set, poc_set=None):
    """Show overall statistics."""
    total = len(data)
    scannable = len([cve for cve in data if cve['cveID'] in scannable_set])
    ransomware = len([cve for cve in data if cve['knownRansomwareCampaignUse'] == 'Known'])

    # Count by vendor
    vendors = defaultdict(int)
    for cve in data:
        vendors[cve['vendorProject']] += 1

    print(f"\n{'='*70}")
    print(f"📊 CISA KEV STATISTICS")
    print(f"{'='*70}")
    print(f"Total CVEs: {total}")
    print(f"Scannable CVEs: {scannable} ({scannable/total*100:.1f}%)")
    print(f"Unscannable CVEs: {total-scannable} ({(total-scannable)/total*100:.1f}%)")

    if poc_set:
        with_poc = len([cve for cve in data if cve['cveID'] in poc_set])
        both = len(scannable_set & poc_set)
        gap = len(poc_set - scannable_set)
        print(f"CVEs with public PoCs: {with_poc} ({with_poc/total*100:.1f}%)")
        print(f"CVEs with PoC + Nuclei: {both} ({both/total*100:.1f}%)")
        print(f"Testing gap (PoC no template): {gap} ({gap/total*100:.1f}%)")

    print(f"Ransomware-associated: {ransomware} ({ransomware/total*100:.1f}%)")
    print(f"Unique vendors: {len(vendors)}")
    print(f"\nTop 10 vendors:")
    for vendor, count in sorted(vendors.items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f"  • {vendor}: {count} CVEs")
    print(f"{'='*70}\n")

def main():
    parser = argparse.ArgumentParser(
        description='CISA KEV Query Tool - Search and filter the KEV database',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --vendor Microsoft
  %(prog)s --product Chrome
  %(prog)s --cve CVE-2024-1234
  %(prog)s --recent 7
  %(prog)s --ransomware
  %(prog)s --scannable
  %(prog)s --poc           # Show CVEs with public PoCs
  %(prog)s --poc-gap       # Show CVEs with PoC but no Nuclei template
  %(prog)s --stats

Icon Legend:
  ✅ = Scannable with Nuclei
  ❌ = Not scannable
  🦠 = Ransomware-associated
  💣 = Public PoC available
        """
    )

    parser.add_argument('--vendor', '-v', help='Search by vendor name')
    parser.add_argument('--product', '-p', help='Search by product name')
    parser.add_argument('--cve', '-c', help='Lookup specific CVE ID')
    parser.add_argument('--recent', '-r', type=int, metavar='DAYS', help='Show CVEs added in last N days')
    parser.add_argument('--ransomware', '-R', action='store_true', help='Show ransomware-associated CVEs')
    parser.add_argument('--scannable', '-s', action='store_true', help='Show only scannable CVEs')
    parser.add_argument('--unscannable', '-u', action='store_true', help='Show only unscannable CVEs')
    parser.add_argument('--poc', '-P', action='store_true', help='Show only CVEs with public PoCs')
    parser.add_argument('--poc-gap', '-G', action='store_true', help='Show CVEs with PoC but no Nuclei template (testing gap)')
    parser.add_argument('--stats', '-S', action='store_true', help='Show overall statistics')
    parser.add_argument('--details', '-d', action='store_true', help='Show detailed information')
    parser.add_argument('--csv', default='data/raw/cisa-kev.csv', help='Path to KEV CSV file (default: cisa-kev.csv)')

    args = parser.parse_args()

    # Load data
    data = load_kev_data(args.csv)
    if not data:
        sys.exit(1)

    scannable_set = load_scannable_list()
    poc_set = load_poc_list()

    # If no arguments, show help
    if not any([args.vendor, args.product, args.cve, args.recent, args.ransomware,
                args.scannable, args.unscannable, args.poc, args.poc_gap, args.stats]):
        parser.print_help()
        show_stats(data, scannable_set, poc_set)
        return

    # Process queries
    if args.stats:
        show_stats(data, scannable_set, poc_set)

    if args.vendor:
        query_by_vendor(data, args.vendor, scannable_set, poc_set, args.details)

    if args.product:
        query_by_product(data, args.product, scannable_set, poc_set, args.details)

    if args.cve:
        query_by_cve_id(data, args.cve, scannable_set, poc_set)

    if args.recent:
        query_recent(data, args.recent, scannable_set, poc_set, args.details)

    if args.ransomware:
        query_ransomware(data, scannable_set, poc_set, args.details)

    if args.scannable:
        query_scannable_only(data, scannable_set, poc_set, args.details)

    if args.unscannable:
        query_unscannable_only(data, scannable_set, poc_set, args.details)

    if args.poc:
        query_poc_only(data, poc_set, scannable_set, args.details)

    if args.poc_gap:
        query_poc_gap(data, poc_set, scannable_set, args.details)

if __name__ == '__main__':
    main()
