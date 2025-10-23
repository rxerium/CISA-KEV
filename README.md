# CISA-KEV

[![CISA KEV](https://github.com/rxerium/CISA-KEV/actions/workflows/CISA.yaml/badge.svg)](https://github.com/rxerium/CISA-KEV/actions/workflows/CISA.yaml)

A repository that automatically tracks and cross-references CISA's Known Exploitable Vulnerabilities (KEV) list with available Nuclei templates for vulnerability scanning.



























## 📊 Database Statistics

### Overview
- **Total CVEs in KEV**: 1,447
- **Scannable with Nuclei**: 384 (26.5%)
- **Unscannable**: 1,063 (73.5%)
- **Ransomware-Associated**: 300 (20.7%)
- **Unique Vendors**: 238
- **Unique Products**: 588

### Key Insights
- 🎯 **Microsoft** is the most represented vendor with **347 CVEs**
- 🔍 **384 CVEs** can be actively scanned with Nuclei templates
- 🦠 **300 CVEs** (20.7%) are known to be used in ransomware campaigns
- 📅 **32 new CVEs** were added in the last 30 days
- 🔒 Most common vulnerability type: **CWE-20** (111 occurrences)
- ⚠️ **Microsoft** has the highest scanning coverage at 4.0%, while **Apple** and **Google** have 0%

### Recent Activity (Last 30 Days)
- **CVEs Added**: 32
- **Scannable Added**: 7
- **New Coverage**: 21.9%

### Top 10 Affected Vendors
| Rank | Vendor | CVE Count | Scannable | Scanning Coverage |
|------|--------|-----------|-----------|-------------------|
| 1 | Microsoft | 347 | 14 | 4.0% |
| 2 | Apple | 85 | 0 | 0.0% |
| 3 | Cisco | 81 | 12 | 14.8% |
| 4 | Adobe | 75 | 9 | 12.0% |
| 5 | Google | 65 | 0 | 0.0% |
| 6 | Oracle | 41 | 15 | 36.6% |
| 7 | Apache | 38 | 35 | 92.1% |
| 8 | Ivanti | 30 | 18 | 60.0% |
| 9 | VMware | 26 | 11 | 42.3% |
| 10 | D-Link | 24 | 10 | 41.7% |

### Top 10 Vulnerable Products
| Rank | Product | CVE Count |
|------|---------|-----------|
| 1 | Windows | 156 |
| 2 | Multiple Products | 67 |
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
| Oracle | 11 |
| Adobe | 10 |
| SonicWall | 9 |
| QNAP | 9 |
| VMware | 8 |
| Atlassian | 8 |
| Citrix | 7 |

*Last updated: 2025-10-23*


---
