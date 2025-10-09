# CISA-KEV

[![CISA KEV](https://github.com/rxerium/CISA-KEV/actions/workflows/CISA.yaml/badge.svg)](https://github.com/rxerium/CISA-KEV/actions/workflows/CISA.yaml)

A repository that automatically tracks and cross-references CISA's Known Exploitable Vulnerabilities (KEV) list with available Nuclei templates for vulnerability scanning.







## 📊 Database Statistics

### Overview
- **Total CVEs in KEV**: 1,435
- **Scannable with Nuclei**: 364 (25.4%)
- **Unscannable**: 1,071 (74.6%)
- **Ransomware-Associated**: 299 (20.8%)
- **Unique Vendors**: 235
- **Unique Products**: 583

### Key Insights
- 🎯 **Microsoft** is the most represented vendor with **344 CVEs**
- 🔍 **364 CVEs** can be actively scanned with Nuclei templates
- 🦠 **299 CVEs** (20.8%) are known to be used in ransomware campaigns
- 📅 **22 new CVEs** were added in the last 30 days
- 🔒 Most common vulnerability type: **CWE-20** (111 occurrences)
- ⚠️ **Microsoft** has the highest scanning coverage at 3.8%, while **Apple** and **Google** have 0%

### Recent Activity (Last 30 Days)
- **CVEs Added**: 22
- **Scannable Added**: 7
- **New Coverage**: 31.8%

### Top 10 Affected Vendors
| Rank | Vendor | CVE Count | Scannable | Scanning Coverage |
|------|--------|-----------|-----------|-------------------|
| 1 | Microsoft | 344 | 13 | 3.8% |
| 2 | Apple | 84 | 0 | 0.0% |
| 3 | Cisco | 81 | 11 | 13.6% |
| 4 | Adobe | 74 | 9 | 12.2% |
| 5 | Google | 65 | 0 | 0.0% |
| 6 | Oracle | 40 | 13 | 32.5% |
| 7 | Apache | 38 | 35 | 92.1% |
| 8 | Ivanti | 30 | 18 | 60.0% |
| 9 | VMware | 26 | 10 | 38.5% |
| 10 | D-Link | 24 | 10 | 41.7% |

### Top 10 Vulnerable Products
| Rank | Product | CVE Count |
|------|---------|-----------|
| 1 | Windows | 153 |
| 2 | Multiple Products | 66 |
| 3 | Chromium V8 | 36 |
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
| 1 | CWE-20 | 111 |
| 2 | CWE-78 | 94 |
| 3 | CWE-787 | 93 |
| 4 | CWE-416 | 84 |
| 5 | CWE-119 | 80 |

### Ransomware-Associated CVEs
| Vendor | Ransomware CVEs |
|--------|-----------------|
| Microsoft | 100 |
| Fortinet | 13 |
| Ivanti | 12 |
| Oracle | 10 |
| Adobe | 10 |
| SonicWall | 9 |
| QNAP | 9 |
| VMware | 8 |
| Atlassian | 8 |
| Citrix | 7 |

*Last updated: 2025-10-09*


---
