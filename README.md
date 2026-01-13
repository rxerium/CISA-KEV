# CISA-KEV

[![CISA KEV](https://github.com/rxerium/CISA-KEV/actions/workflows/CISA.yaml/badge.svg)](https://github.com/rxerium/CISA-KEV/actions/workflows/CISA.yaml)
![Views](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Frxerium%2FCISA-KEV&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=Views&edge_flat=false)


## Executive Summary

This repository provides automated tracking and analysis of both **CISA's KEV** and **VulnCheck KEV** catalogs, cross-referenced with Nuclei security templates and public proof-of-concept exploits. By integrating VulnCheck KEV, coverage expands from 1,487 to **4,466 total unique CVEs** - a **3x increase**. The combined dataset reveals that 35.3% of all KEV vulnerabilities can be actively scanned with Nuclei templates (1,578 CVEs). VulnCheck's extended coverage adds **2,979 additional vulnerabilities** not found in CISA's official list, providing comprehensive visibility into exploited vulnerabilities. With automated daily updates and dual-source intelligence, this repository delivers the most complete KEV tracking available.

**Quick Stats (Combined):** 4,466 total CVEs | 1,578 scannable with Nuclei | 2,979 VulnCheck-exclusive | 1,487 in both sources

## 🔀 KEV Source Comparison: CISA vs VulnCheck

### Overview
This repository tracks vulnerabilities from **two authoritative KEV sources**:

| Metric | CISA KEV | VulnCheck KEV | Combined/Comparison |
|--------|----------|---------------|---------------------|
| **Total CVEs** | 1,487 | 4,466 | 4,466 unique |
| **Scannable with Nuclei** | 421 (28.3%) | 1,578 (35.3%) | 1,578 (35.3%) |
| **Overlap** | - | - | 1,487 (100% of CISA) |
| **Source-Exclusive CVEs** | 0 | 2,979 | - |
| **Coverage Increase** | - | - | **+200% more CVEs** |

### Key Insights
- ✅ **All CISA KEV vulnerabilities are included in VulnCheck KEV**
- 🚀 **VulnCheck provides 3x more vulnerability coverage** (2,979 additional CVEs)
- 🔍 **1,578 CVEs can be actively scanned** with Nuclei templates (35.3% coverage)
- 📈 **+1,157 additional scannable CVEs** from VulnCheck vs CISA alone
- 🎯 VulnCheck's extended dataset captures vulnerabilities exploited in the wild but not yet on CISA's official list

### Source Characteristics

**CISA KEV (Official U.S. Government List)**
- Authoritative U.S. federal agency catalog
- Focus on vulnerabilities actively exploited against federal systems
- Required remediation for U.S. federal agencies (BOD 22-01)
- Updated regularly with careful vetting process
- 1,487 CVEs with mandatory remediation deadlines

**VulnCheck KEV (Extended Commercial Intelligence)**
- Comprehensive threat intelligence aggregation
- Includes CISA KEV plus additional exploitation evidence
- Broader international exploitation tracking
- Community and research-driven vulnerability additions
- 4,466 CVEs with verified exploitation evidence

### Nuclei Template Coverage by Source

| Source | Total CVEs | Scannable | Coverage % | Unscannable |
|--------|-----------|-----------|------------|-------------|
| **CISA KEV** | 1,487 | 421 | 28.3% | 1,066 |
| **VulnCheck KEV** | 4,466 | 1,578 | 35.3% | 2,888 |
| **VulnCheck-Exclusive** | 2,979 | 1,157 | 38.8% | 1,822 |

**Insight:** VulnCheck-exclusive CVEs have a higher Nuclei coverage rate (38.8%) compared to the overall dataset, suggesting strong community security tool support for these additional vulnerabilities.

---

## 📊 CISA KEV Statistics

### Overview
- **Total CVEs in KEV**: 1,487
- **Scannable with Nuclei**: 421 (28.3%)
- **With Public PoCs**: **985 (66.2%)**
- **Unscannable**: 1,066 (71.7%)
- **Ransomware-Associated**: 304 (20.4%)
- **Unique Vendors**: 245
- **Unique Products**: 604

### Key Insights
- 🎯 **Microsoft** is the most represented vendor with **351 CVEs**
- 🔍 **421 CVEs** can be actively scanned with Nuclei templates
- 💣 **985 CVEs** (66.2%) have public proof-of-concept exploits available
- 🎯 **392 CVEs** have both PoC and Nuclei template (fully testable)
- 🔓 **593 CVEs** have PoC but no Nuclei template (testing gap)
- 🦠 **304 CVEs** (20.4%) are known to be used in ransomware campaigns
- 📅 **12 new CVEs** were added in the last 30 days
- 🔒 Most common vulnerability type: **CWE-20** (113 occurrences)
- ⚠️ **Microsoft** has the highest scanning coverage at 4.6%, while **Apple** and **Google** have 0%

### Recent Activity (Last 30 Days)
- **CVEs Added**: 12
- **Scannable Added**: 3
- **New Coverage**: 25.0%

### Top 10 Affected Vendors
| Rank | Vendor | CVE Count | Scannable | With PoC | Scanning Coverage |
|------|--------|-----------|-----------|----------|-------------------|
| 1 | Microsoft | 351 | 16 | 218 | 4.6% |
| 2 | Apple | 86 | 0 | 30 | 0.0% |
| 3 | Cisco | 82 | 12 | 24 | 14.6% |
| 4 | Adobe | 76 | 12 | 44 | 15.8% |
| 5 | Google | 67 | 0 | 48 | 0.0% |
| 6 | Oracle | 42 | 18 | 33 | 42.9% |
| 7 | Apache | 38 | 35 | 38 | 92.1% |
| 8 | Ivanti | 30 | 18 | 23 | 60.0% |
| 9 | VMware | 26 | 13 | 18 | 50.0% |
| 10 | D-Link | 25 | 10 | 24 | 40.0% |

### Top 10 Vulnerable Products
| Rank | Product | CVE Count |
|------|---------|-----------|
| 1 | Windows | 159 |
| 2 | Multiple Products | 70 |
| 3 | Chromium V8 | 37 |
| 4 | Internet Explorer | 34 |
| 5 | Flash Player | 33 |
| 6 | Office | 26 |
| 7 | Kernel | 26 |
| 8 | Win32k | 25 |
| 9 | Exchange Server | 16 |
| 10 | ColdFusion | 15 |

### Top 5 Vulnerability Types (CWEs)
| Rank | CWE | Count |
|------|-----|-------|
| 1 | CWE-20 | 113 |
| 2 | CWE-78 | 97 |
| 3 | CWE-787 | 96 |
| 4 | CWE-416 | 86 |
| 5 | CWE-119 | 80 |

### Top 10 Ransomware-Associated CVEs by Vendor
| Vendor | Ransomware CVEs |
|--------|-----------------|
| Microsoft | 100 |
| Fortinet | 13 |
| Ivanti | 12 |
| Oracle | 11 |
| SonicWall | 10 |
| Adobe | 10 |
| QNAP | 9 |
| VMware | 8 |
| Atlassian | 8 |
| Citrix | 7 |

<details>
<summary>View all ransomware-associated CVEs (304 total)</summary>

Run `python scripts/kev_query.py --ransomware` to see the complete list of all ransomware-associated vulnerabilities.
</details>

### 🔓 Priority Gap: CVEs with Public PoCs but No Nuclei Template

**Total Gap CVEs:** 593 vulnerabilities have public exploits but lack automated detection templates.

📥 **Download Full Data:** [data/processed/CISA-Priority-Gap.csv](data/processed/CISA-Priority-Gap.csv) - Detailed CSV export with PoC URLs, EPSS scores, CVSS scores, severity levels, and vulnerability metadata.

**Showing first 10 of 593 gap CVEs** (sorted by date added to KEV, most recent first):

| CVE ID | Vendor | Product | Date Added | PoC | Ransomware |
|--------|--------|---------|------------|-----|------------|
| CVE-2025-59718 | Fortinet | Multiple Products | 2025-12-16 | ✓ |  |
| CVE-2018-4063 | Sierra Wireless | AirLink ALEOS | 2025-12-12 | ✓ |  |
| CVE-2025-14174 | Google | Chromium | 2025-12-12 | ✓ |  |
| CVE-2025-6218 | RARLAB | WinRAR | 2025-12-09 | ✓ |  |
| CVE-2025-62221 | Microsoft | Windows | 2025-12-09 | ✓ |  |
| CVE-2022-37055 | D-Link | Routers | 2025-12-08 | ✓ |  |
| CVE-2025-66644 | Array Networks  | ArrayOS AG | 2025-12-08 | ✓ |  |
| CVE-2021-26828 | OpenPLC | ScadaBR | 2025-12-03 | ✓ |  |
| CVE-2025-48633 | Android | Framework | 2025-12-02 | ✓ |  |
| CVE-2021-26829 | OpenPLC | ScadaBR | 2025-11-28 | ✓ |  |

<details>
<summary>View complete priority gap list (593 CVEs)</summary>

Download the full dataset: [data/processed/CISA-Priority-Gap.csv](data/processed/CISA-Priority-Gap.csv)

Or query using: `python scripts/kev_query.py --poc-gap`
</details>

*Last updated: 2026-01-13*

---

## 🔧 Using VulnCheck KEV Integration

### Setup
1. Get a free VulnCheck API key from [vulncheck.com](https://vulncheck.com)
2. Set the environment variable:
   ```bash
   export VULNCHECK_API_KEY="your_api_key_here"
   ```

### Manual Usage
```bash
# Fetch VulnCheck KEV data
make vulncheck-fetch

# Match with Nuclei templates
make vulncheck-match

# Compare CISA vs VulnCheck
make compare-kevs

# Run everything
make vulncheck-all
```

### Automated Updates
The GitHub Actions workflow automatically:
- **Weekly (Sundays 3 AM UTC)**: Fetches VulnCheck KEV data
- Matches VulnCheck CVEs against Nuclei templates
- Generates comparison analysis between CISA and VulnCheck
- Updates README with latest statistics

### Generated Files
```
data/
├── raw/
│   ├── vulncheck-kev.json          # Raw VulnCheck data
│   └── vulncheck-kev.csv           # Normalized CSV format
├── lists/
│   ├── VulnCheck-KEV-List.txt      # All VulnCheck CVEs
│   ├── VulnCheck-Scannable-List.txt # Nuclei-scannable VulnCheck CVEs
│   ├── Common-CVEs.txt             # CVEs in both CISA & VulnCheck
│   ├── CISA-Only-CVEs.txt          # CISA-exclusive CVEs
│   └── VulnCheck-Only-CVEs.txt     # VulnCheck-exclusive CVEs (2,979)
└── processed/
    └── kev-comparison.json         # Detailed comparison analytics
```

---
