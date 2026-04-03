#!/usr/bin/env python3
"""
Enrich KEV CSV files with additional metadata:
- PoC availability
- EPSS scores
- CVSS scores
- Severity levels
- Nuclei template availability
"""

import csv
import json
from pathlib import Path
from collections import defaultdict


def load_poc_data(json_path="data/raw/poc-data.json"):
    """Load PoC data from JSON file."""
    try:
        with open(json_path, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"⚠️  Could not load PoC data: {e}")
        return {}


def load_scannable_list(txt_path):
    """Load list of scannable CVEs."""
    try:
        with open(txt_path, "r") as f:
            return set(line.strip() for line in f if line.strip())
    except Exception as e:
        print(f"⚠️  Could not load scannable list: {e}")
        return set()


def enrich_cisa_kev():
    """Create enriched CISA KEV CSV."""
    print("🔧 Enriching CISA KEV CSV...")

    # Load supporting data
    poc_data = load_poc_data()
    scannable = load_scannable_list("data/lists/CISA-Scannable-List.txt")

    # Read original CISA KEV
    input_path = Path("data/raw/cisa-kev.csv")
    output_path = Path("data/processed/cisa-kev-enriched.csv")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    enriched_rows = []

    with open(input_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        original_fields = reader.fieldnames

        # Add new fields
        new_fields = list(original_fields) + [
            "has_nuclei_template",
            "has_public_poc",
            "poc_count",
            "epss_score",
            "cvss_score",
            "severity",
            "is_remote",
            "is_auth_required",
        ]

        for row in reader:
            cve_id = row["cveID"]

            # Add enrichment data
            row["has_nuclei_template"] = "Yes" if cve_id in scannable else "No"

            # Add PoC data if available
            poc_info = poc_data.get(cve_id, {})
            row["has_public_poc"] = "Yes" if poc_info.get("is_poc", False) else "No"
            row["poc_count"] = poc_info.get("poc_count", 0)
            row["epss_score"] = poc_info.get("epss_score", "")
            row["cvss_score"] = poc_info.get("cvss_score", "")
            row["severity"] = poc_info.get("severity", "")
            row["is_remote"] = "Yes" if poc_info.get("is_remote", False) else "No"
            row["is_auth_required"] = "Yes" if poc_info.get("is_auth", False) else "No"

            enriched_rows.append(row)

    # Write enriched CSV
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=new_fields)
        writer.writeheader()
        writer.writerows(enriched_rows)

    print(f"✅ Enriched CISA KEV saved to {output_path}")
    print(f"   Total CVEs: {len(enriched_rows)}")
    print(
        f"   With Nuclei templates: {sum(1 for r in enriched_rows if r['has_nuclei_template'] == 'Yes')}"
    )
    print(
        f"   With public PoCs: {sum(1 for r in enriched_rows if r['has_public_poc'] == 'Yes')}"
    )

    return len(enriched_rows)


def enrich_vulncheck_kev():
    """Create enriched VulnCheck KEV CSV."""
    print("\n🔧 Enriching VulnCheck KEV CSV...")

    # Load supporting data
    scannable = load_scannable_list("data/lists/VulnCheck-Scannable-List.txt")

    # Read original VulnCheck KEV
    input_path = Path("data/raw/vulncheck-kev.csv")
    output_path = Path("data/processed/vulncheck-kev-enriched.csv")

    enriched_rows = []

    with open(input_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        original_fields = reader.fieldnames

        # Add new field
        new_fields = list(original_fields) + ["has_nuclei_template"]

        for row in reader:
            cve_id = row["cveID"]

            # Add Nuclei template availability
            row["has_nuclei_template"] = "Yes" if cve_id in scannable else "No"

            enriched_rows.append(row)

    # Write enriched CSV
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=new_fields)
        writer.writeheader()
        writer.writerows(enriched_rows)

    print(f"✅ Enriched VulnCheck KEV saved to {output_path}")
    print(f"   Total CVEs: {len(enriched_rows)}")
    print(
        f"   With Nuclei templates: {sum(1 for r in enriched_rows if r['has_nuclei_template'] == 'Yes')}"
    )

    return len(enriched_rows)


def main():
    print("=" * 70)
    print("📊 KEV CSV Enrichment")
    print("=" * 70)

    cisa_count = enrich_cisa_kev()
    vc_count = enrich_vulncheck_kev()

    print("\n" + "=" * 70)
    print("✅ Enrichment Complete!")
    print("=" * 70)
    print(f"  CISA KEV enriched: {cisa_count} CVEs")
    print(f"  VulnCheck KEV enriched: {vc_count} CVEs")
    print("\nEnriched files:")
    print("  - data/processed/cisa-kev-enriched.csv")
    print("  - data/processed/vulncheck-kev-enriched.csv")
    print("=" * 70)


if __name__ == "__main__":
    main()
