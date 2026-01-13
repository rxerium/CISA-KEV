#!/usr/bin/env python3
"""
Compare CISA KEV and VulnCheck KEV datasets

This script analyzes the overlap and differences between the two KEV sources,
providing insights into coverage gaps and unique vulnerabilities.
"""

import csv
import json
from pathlib import Path
from collections import Counter

def load_cisa_kev():
    """Load CISA KEV dataset"""
    cisa_path = Path('data/raw/cisa-kev.csv')
    if not cisa_path.exists():
        print("❌ CISA KEV file not found")
        return set(), []

    with open(cisa_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = list(reader)
        cves = {row['cveID'] for row in data if row.get('cveID')}

    print(f"📋 Loaded {len(cves)} CVEs from CISA KEV")
    return cves, data

def load_vulncheck_kev():
    """Load VulnCheck KEV dataset"""
    vc_path = Path('data/lists/VulnCheck-KEV-List.txt')
    if not vc_path.exists():
        print("❌ VulnCheck KEV list not found. Run fetch_vulncheck_kev.py first.")
        return set()

    with open(vc_path, 'r', encoding='utf-8') as f:
        cves = {line.strip() for line in f if line.strip()}

    print(f"📋 Loaded {len(cves)} CVEs from VulnCheck KEV")
    return cves

def load_scannable_cves():
    """Load list of CVEs scannable with Nuclei"""
    scannable_path = Path('data/lists/CISA-Scannable-List.txt')
    if not scannable_path.exists():
        return set()

    with open(scannable_path, 'r', encoding='utf-8') as f:
        return {line.strip() for line in f if line.strip()}

def load_nuclei_templates():
    """Load list of available Nuclei templates"""
    nuclei_path = Path('data/lists/NucleiList.txt')
    if not nuclei_path.exists():
        return set()

    with open(nuclei_path, 'r', encoding='utf-8') as f:
        return {line.strip() for line in f if line.strip()}

def analyze_overlap(cisa_cves, vulncheck_cves, nuclei_templates):
    """Analyze the overlap between KEV sources and Nuclei coverage"""

    # Basic set operations
    overlap = cisa_cves & vulncheck_cves
    cisa_only = cisa_cves - vulncheck_cves
    vulncheck_only = vulncheck_cves - cisa_cves
    total_unique = cisa_cves | vulncheck_cves

    # Nuclei coverage analysis
    nuclei_coverage_cisa = cisa_cves & nuclei_templates
    nuclei_coverage_vc = vulncheck_cves & nuclei_templates
    nuclei_coverage_total = total_unique & nuclei_templates

    analysis = {
        'cisa_total': len(cisa_cves),
        'vulncheck_total': len(vulncheck_cves),
        'overlap': len(overlap),
        'cisa_exclusive': len(cisa_only),
        'vulncheck_exclusive': len(vulncheck_only),
        'total_unique': len(total_unique),
        'nuclei_coverage_cisa': len(nuclei_coverage_cisa),
        'nuclei_coverage_vc': len(nuclei_coverage_vc),
        'nuclei_coverage_total': len(nuclei_coverage_total),
        'overlap_percentage': (len(overlap) / len(cisa_cves) * 100) if cisa_cves else 0
    }

    return analysis, {
        'overlap': overlap,
        'cisa_only': cisa_only,
        'vulncheck_only': vulncheck_only,
        'nuclei_coverage_cisa': nuclei_coverage_cisa,
        'nuclei_coverage_vc': nuclei_coverage_vc
    }

def save_comparison_lists(sets):
    """Save comparison lists to files"""
    lists_dir = Path('data/lists')

    # Save overlap
    with open(lists_dir / 'Common-CVEs.txt', 'w') as f:
        f.write('\n'.join(sorted(sets['overlap'])))

    # Save CISA-only
    with open(lists_dir / 'CISA-Only-CVEs.txt', 'w') as f:
        f.write('\n'.join(sorted(sets['cisa_only'])))

    # Save VulnCheck-only
    with open(lists_dir / 'VulnCheck-Only-CVEs.txt', 'w') as f:
        f.write('\n'.join(sorted(sets['vulncheck_only'])))

    # Save Nuclei coverage for VulnCheck
    with open(lists_dir / 'VulnCheck-Scannable-List.txt', 'w') as f:
        f.write('\n'.join(sorted(sets['nuclei_coverage_vc'])))

    print("\n💾 Saved comparison lists:")
    print(f"  - Common-CVEs.txt ({len(sets['overlap'])} CVEs)")
    print(f"  - CISA-Only-CVEs.txt ({len(sets['cisa_only'])} CVEs)")
    print(f"  - VulnCheck-Only-CVEs.txt ({len(sets['vulncheck_only'])} CVEs)")
    print(f"  - VulnCheck-Scannable-List.txt ({len(sets['nuclei_coverage_vc'])} CVEs)")

def save_comparison_json(analysis):
    """Save analysis results as JSON"""
    output_path = Path('data/processed/kev-comparison.json')
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, 'w') as f:
        json.dump(analysis, f, indent=2)

    print(f"\n📊 Saved comparison analysis to {output_path}")

def print_summary(analysis):
    """Print comparison summary"""
    print("\n" + "="*60)
    print("📊 KEV SOURCES COMPARISON SUMMARY")
    print("="*60)
    print(f"\n🔵 CISA KEV:")
    print(f"   Total CVEs: {analysis['cisa_total']}")
    print(f"   Scannable with Nuclei: {analysis['nuclei_coverage_cisa']} ({analysis['nuclei_coverage_cisa']/analysis['cisa_total']*100:.1f}%)")

    print(f"\n🟢 VulnCheck KEV:")
    print(f"   Total CVEs: {analysis['vulncheck_total']}")
    print(f"   Scannable with Nuclei: {analysis['nuclei_coverage_vc']} ({analysis['nuclei_coverage_vc']/analysis['vulncheck_total']*100:.1f}%)")

    print(f"\n🔄 Overlap & Unique:")
    print(f"   Common CVEs (both sources): {analysis['overlap']} ({analysis['overlap_percentage']:.1f}% of CISA)")
    print(f"   CISA-exclusive CVEs: {analysis['cisa_exclusive']}")
    print(f"   VulnCheck-exclusive CVEs: {analysis['vulncheck_exclusive']}")

    print(f"\n📈 Combined Coverage:")
    print(f"   Total unique CVEs: {analysis['total_unique']}")
    print(f"   Scannable with Nuclei: {analysis['nuclei_coverage_total']} ({analysis['nuclei_coverage_total']/analysis['total_unique']*100:.1f}%)")
    print(f"   Coverage increase from VulnCheck: +{analysis['vulncheck_exclusive']} CVEs")

    print("\n" + "="*60)

def main():
    """Main execution function"""
    print("🔍 Comparing CISA KEV and VulnCheck KEV datasets...\n")

    # Load datasets
    cisa_cves, _ = load_cisa_kev()
    vulncheck_cves = load_vulncheck_kev()
    nuclei_templates = load_nuclei_templates()

    if not cisa_cves or not vulncheck_cves:
        print("\n❌ Missing required datasets. Exiting.")
        return

    # Analyze
    analysis, sets = analyze_overlap(cisa_cves, vulncheck_cves, nuclei_templates)

    # Save results
    save_comparison_lists(sets)
    save_comparison_json(analysis)

    # Print summary
    print_summary(analysis)

    print("\n✅ Comparison complete!")

if __name__ == '__main__':
    main()
