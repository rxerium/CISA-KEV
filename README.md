# CISA-KEV

[![CISA KEV](https://github.com/rxerium/CISA-KEV/actions/workflows/CISA.yaml/badge.svg)](https://github.com/rxerium/CISA-KEV/actions/workflows/CISA.yaml)
![Views](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Frxerium%2FCISA-KEV&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=Views&edge_flat=false)

A repository that automatically tracks and cross-references CISA's Known Exploitable Vulnerabilities (KEV) list with available Nuclei templates for vulnerability scanning.












































✅ Exported 597 priority gap CVEs to data/processed/CISA-Priority-Gap.csv

## 📊 Database Statistics

### Overview
- **Total CVEs in KEV**: 1,478
- **Scannable with Nuclei**: 412 (27.9%)
- **With Public PoCs**: **985 (66.6%)**
- **Unscannable**: 1,066 (72.1%)
- **Ransomware-Associated**: 303 (20.5%)
- **Unique Vendors**: 242
- **Unique Products**: 598

### Key Insights
- 🎯 **Microsoft** is the most represented vendor with **350 CVEs**
- 🔍 **412 CVEs** can be actively scanned with Nuclei templates
- 💣 **985 CVEs** (66.6%) have public proof-of-concept exploits available
- 🎯 **388 CVEs** have both PoC and Nuclei template (fully testable)
- 🔓 **597 CVEs** have PoC but no Nuclei template (testing gap)
- 🦠 **303 CVEs** (20.5%) are known to be used in ransomware campaigns
- 📅 **18 new CVEs** were added in the last 30 days
- 🔒 Most common vulnerability type: **CWE-20** (112 occurrences)
- ⚠️ **Microsoft** has the highest scanning coverage at 4.6%, while **Apple** and **Google** have 0%

### Recent Activity (Last 30 Days)
- **CVEs Added**: 18
- **Scannable Added**: 3
- **New Coverage**: 16.7%

### Top 10 Affected Vendors
| Rank | Vendor | CVE Count | Scannable | With PoC | Scanning Coverage |
|------|--------|-----------|-----------|----------|-------------------|
| 1 | Microsoft | 350 | 16 | 218 | 4.6% |
| 2 | Apple | 86 | 0 | 30 | 0.0% |
| 3 | Cisco | 81 | 12 | 24 | 14.8% |
| 4 | Adobe | 76 | 12 | 44 | 15.8% |
| 5 | Google | 67 | 0 | 48 | 0.0% |
| 6 | Oracle | 42 | 18 | 33 | 42.9% |
| 7 | Apache | 38 | 35 | 38 | 92.1% |
| 8 | Ivanti | 30 | 18 | 23 | 60.0% |
| 9 | VMware | 26 | 12 | 18 | 46.2% |
| 10 | D-Link | 25 | 10 | 24 | 40.0% |

### Top 10 Vulnerable Products
| Rank | Product | CVE Count |
|------|---------|-----------|
| 1 | Windows | 159 |
| 2 | Multiple Products | 69 |
| 3 | Chromium V8 | 37 |
| 4 | Internet Explorer | 34 |
| 5 | Flash Player | 33 |
| 6 | Kernel | 26 |
| 7 | Office | 25 |
| 8 | Win32k | 25 |
| 9 | Exchange Server | 16 |
| 10 | ColdFusion | 15 |

### Top 5 Vulnerability Types (CWEs)
| Rank | CWE | Count |
|------|-----|-------|
| 1 | CWE-20 | 112 |
| 2 | CWE-78 | 97 |
| 3 | CWE-787 | 95 |
| 4 | CWE-416 | 86 |
| 5 | CWE-119 | 80 |

### Ransomware-Associated CVEs
| Vendor | Ransomware CVEs |
|--------|-----------------|
| Microsoft | 100 |
| Fortinet | 13 |
| Ivanti | 12 |
| Oracle | 11 |
| Adobe | 10 |
| SonicWall | 9 |
| QNAP | 9 |
| VMware | 8 |
| Atlassian | 8 |
| Citrix | 7 |

### 🔓 Priority Gap: CVEs with Public PoCs but No Nuclei Template

**Total Gap CVEs:** 597 vulnerabilities have public exploits but lack automated detection templates.

📥 **Download Full Data:** [data/processed/CISA-Priority-Gap.csv](data/processed/CISA-Priority-Gap.csv) - Detailed CSV export with PoC URLs, EPSS scores, CVSS scores, severity levels, and vulnerability metadata.

**Showing first 20 of 597 gap CVEs** (sorted by date added to KEV, most recent first):

| CVE ID | Vendor | Product | Date Added | PoC | Ransomware |
|--------|--------|---------|------------|-----|------------|
| CVE-2025-59718 | Fortinet | Multiple Products | 2025-12-16 | ✓ |  |
| CVE-2025-14611 | Gladinet | CentreStack and Triofox | 2025-12-15 | ✓ |  |
| CVE-2018-4063 | Sierra Wireless | AirLink ALEOS | 2025-12-12 | ✓ |  |
| CVE-2025-14174 | Google | Chromium | 2025-12-12 | ✓ |  |
| CVE-2025-6218 | RARLAB | WinRAR | 2025-12-09 | ✓ |  |
| CVE-2025-62221 | Microsoft | Windows | 2025-12-09 | ✓ |  |
| CVE-2022-37055 | D-Link | Routers | 2025-12-08 | ✓ |  |
| CVE-2025-66644 | Array Networks  | ArrayOS AG | 2025-12-08 | ✓ |  |
| CVE-2021-26828 | OpenPLC | ScadaBR | 2025-12-03 | ✓ |  |
| CVE-2025-48633 | Android | Framework | 2025-12-02 | ✓ |  |
| CVE-2021-26829 | OpenPLC | ScadaBR | 2025-11-28 | ✓ |  |
| CVE-2025-13223 | Google | Chromium V8 | 2025-11-19 | ✓ |  |
| CVE-2025-58034 | Fortinet | FortiWeb | 2025-11-18 | ✓ |  |
| CVE-2025-62215 | Microsoft | Windows | 2025-11-12 | ✓ |  |
| CVE-2025-21042 | Samsung | Mobile Devices | 2025-11-10 | ✓ |  |
| CVE-2025-41244 | Broadcom | VMware Aria Operations an | 2025-10-30 | ✓ |  |
| CVE-2025-61932 | Motex | LANSCOPE Endpoint Manager | 2025-10-22 | ✓ |  |
| CVE-2025-33073 | Microsoft | Windows | 2025-10-20 | ✓ |  |
| CVE-2025-47827 | IGEL | IGEL OS | 2025-10-14 | ✓ |  |
| CVE-2025-24990 | Microsoft | Windows | 2025-10-14 | ✓ |  |

*View complete list in [data/processed/CISA-Priority-Gap.csv](data/processed/CISA-Priority-Gap.csv)*

*Last updated: 2025-12-17*

---

## 💣 PoC (Proof-of-Concept) Tracking

This repository now tracks the availability of **public proof-of-concept exploits** for CISA KEV vulnerabilities using data from the [ProjectDiscovery API](https://api.projectdiscovery.io). This helps prioritize which vulnerabilities have actively circulating exploits.

### Why Track PoCs?

Understanding which KEV vulnerabilities have publicly available exploits helps organizations:
- **Prioritize patching** - Focus on vulnerabilities with known working exploits
- **Identify coverage gaps** - Find CVEs that have PoCs but no automated scanning templates
- **Assess real-world risk** - Public exploits significantly increase exploitation likelihood
- **Guide template development** - Highlight high-priority vulnerabilities needing Nuclei templates

### PoC Data Sources

The PoC tracking leverages ProjectDiscovery's comprehensive vulnerability database which aggregates:
- GitHub repositories with exploit code
- Security research publications
- Exploit databases (Exploit-DB, Packet Storm, etc.)
- Vulnerability disclosures with PoC code
- Security blog posts and writeups

### Using PoC Data

**Query CVEs with public PoCs:**
```bash
# Show all CVEs with public PoCs
python scripts/kev_query.py --poc

# Show CVEs with PoC but no Nuclei template (priority gap)
python scripts/kev_query.py --poc-gap

# Filter by vendor and show PoC status
python scripts/kev_query.py --vendor Microsoft --details
```

**Fetch latest PoC data:**
```bash
# Collect PoC availability data from ProjectDiscovery API
python scripts/fetch_poc_data.py

# This generates:
# - poc-data.json: Full PoC metadata for all KEV CVEs
# - CISA-POC-List.txt: Simple list of CVEs with public PoCs
```

**Visualize PoC coverage:**
```bash
# Generate analytics including PoC coverage analysis
python scripts/kev_analytics.py

# Creates visualization showing:
# - PoC vs Nuclei template coverage
# - Coverage gaps (PoC without templates)
# - PoC availability by vendor
# - Testing capability distribution
```

### Icon Legend

When querying the database, you'll see these indicators:
- ✅ = Scannable with Nuclei template
- ❌ = Not scannable
- 🦠 = Associated with ransomware campaigns
- 💣 = Public PoC exploit available

### Automated Updates

The GitHub Actions workflow automatically:
1. Fetches the latest CISA KEV data
2. Matches against Nuclei templates
3. **Collects PoC availability from ProjectDiscovery API**
4. Updates statistics and visualizations
5. Commits changes back to the repository

### Files Generated

- `CISA-POC-List.txt` - List of CVEs with public PoCs
- `poc-data.json` - Detailed PoC metadata (EPSS scores, severity, etc.)
- `outputs/graphs/poc_coverage_analysis.png` - PoC coverage visualizations

---
