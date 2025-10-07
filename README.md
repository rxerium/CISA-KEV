# CISA-KEV Scanning Capabilities

[![CISA KEV](https://github.com/rxerium/CISA-KEV/actions/workflows/CISA.yaml/badge.svg)](https://github.com/rxerium/CISA-KEV/actions/workflows/CISA.yaml)

A repository that automatically tracks and cross-references CISA's Known Exploitable Vulnerabilities (KEV) list with available Nuclei templates for vulnerability scanning.

## 📊 Database Statistics

### Overview
- **Total CVEs in KEV**: 1,434
- **Scannable with Nuclei**: 361 (25.2%)
- **Unscannable**: 1,073 (74.8%)
- **Ransomware-Associated**: 295 (20.6%)
- **Unique Vendors**: 235
- **Unique Products**: 583

### Key Insights
- 🎯 **Microsoft** is the most represented vendor with **344 CVEs**
- 🔍 **361 CVEs** can be actively scanned with Nuclei templates
- 🦠 **295 CVEs** (20.6%) are known to be used in ransomware campaigns
- 📅 **21 new CVEs** were added in the last 30 days
- 🔒 Most common vulnerability type: **CWE-20 (Improper Input Validation)** with 111 occurrences
- ⚠️ **Apache** has the highest scanning coverage at 92.1%, while **Apple** and **Google** have 0%

### Recent Activity (Last 30 Days)
- **CVEs Added**: 21
- **Scannable Added**: 6
- **New Coverage**: 28.6%

### Top 10 Affected Vendors
| Rank | Vendor | CVE Count | Scannable | Scanning Coverage |
|------|--------|-----------|-----------|-------------------|
| 1 | Microsoft | 344 | 13 | 3.8% |
| 2 | Apple | 84 | 0 | 0.0% |
| 3 | Cisco | 81 | 11 | 13.6% |
| 4 | Adobe | 74 | 9 | 12.2% |
| 5 | Google | 65 | 0 | 0.0% |
| 6 | Oracle | 40 | 12 | 30.0% |
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
| 1 | CWE-20 (Improper Input Validation) | 111 |
| 2 | CWE-78 (OS Command Injection) | 94 |
| 3 | CWE-787 (Out-of-bounds Write) | 93 |
| 4 | CWE-416 (Use After Free) | 84 |
| 5 | CWE-119 (Buffer Errors) | 80 |

### Ransomware-Associated CVEs (Top 10 Vendors)
| Vendor | Ransomware CVEs |
|--------|-----------------|
| Microsoft | 99 |
| Fortinet | 13 |
| Oracle | 10 |
| Adobe | 10 |
| Ivanti | 9 |
| SonicWall | 9 |
| QNAP | 9 |
| VMware | 8 |
| Atlassian | 8 |
| Citrix | 7 |

*Statistics last updated: 2025-10-07*

---

## Overview

This project maintains an up-to-date copy of CISA's KEV catalog and identifies which vulnerabilities can be scanned using [Project Discovery's Nuclei](https://github.com/projectdiscovery/nuclei-templates) templates.

## Features

- **Automated Updates**: Runs twice daily (6 AM and 3 PM UTC) on weekdays to fetch the latest CISA KEV data
- **Auto-Updated Statistics**: README statistics automatically regenerate when KEV data changes via GitHub Actions
- **Nuclei Template Matching**: Cross-references CISA KEV entries with available Nuclei scanning templates
- **Slack Notifications**: Sends alerts when new vulnerabilities are added to the KEV list
- **Scannable CVE List**: Generates `CISA-Scannable-List.txt` containing KEV entries that have corresponding Nuclei templates

## Repository Structure

```
.
├── cisa-kev.csv                    # Complete CISA KEV catalog
├── NucleiList.txt                  # CVE IDs with Nuclei templates
├── CISA-Scannable-List.txt         # Scannable vulnerabilities
├── scripts/                        # Analytics and query tools
│   ├── kev_analytics.py            # Comprehensive analytics dashboard
│   ├── kev_query.py                # CLI search and query tool
│   └── generate_stats.py           # Statistics generator for README
├── outputs/                        # Generated outputs
│   ├── graphs/                     # Visualization outputs (PNG files)
│   └── data/                       # Exported data files
├── docs/                           # Documentation
│   ├── QUICKSTART.md               # Quick start guide
│   ├── IDEAS.md                    # Future enhancement ideas
│   └── SUMMARY.md                  # Feature summary
├── requirements.txt                # Python dependencies
├── setup.sh                        # Environment setup script
├── Makefile                        # Convenient command shortcuts
└── README.md                       # This file
```

## Data Files

- **`cisa-kev.csv`**: The complete CISA Known Exploitable Vulnerabilities catalog
- **`NucleiList.txt`**: List of CVE IDs that have Nuclei templates available
- **`CISA-Scannable-List.txt`**: Intersection of CISA KEV and Nuclei templates - vulnerabilities you can actively scan for

## How It Works

1. Downloads the latest KEV catalog from CISA
2. Clones the Nuclei templates repository
3. Extracts all CVE identifiers from Nuclei templates
4. Matches Nuclei-scannable CVEs against the CISA KEV list
5. Generates a scannable list for security teams
6. Sends Slack notifications if new vulnerabilities are detected
7. Commits and pushes updates to the repository

## Usage

You can use the generated files to:

- Monitor which CISA KEV vulnerabilities can be scanned with Nuclei
- Integrate with your vulnerability scanning pipeline
- Track changes to the KEV list over time

## Workflow Schedule

The automation runs on:
- **Schedule**: 6 AM and 3 PM UTC, Monday through Friday
- **Manual**: Can be triggered via workflow dispatch

### What Gets Updated Automatically:
1. ✅ KEV CSV data from CISA
2. ✅ Nuclei template list
3. ✅ Scannable CVE list
4. ✅ **README statistics** (all tables and metrics)
5. ✅ Slack notifications (if new CVEs added)

The GitHub Actions workflow automatically:
- Downloads latest KEV data
- Matches with Nuclei templates
- Runs `generate_stats.py` to create fresh statistics
- Updates the README with new data
- Commits and pushes changes

## 📊 Analytics Tools

This repository now includes powerful analytics tools to visualize and analyze the KEV database:

### 1. 🔍 KEV Query Tool (`scripts/kev_query.py`)
Interactive CLI tool to search and filter the KEV database.

```bash
# Search by vendor
python scripts/kev_query.py --vendor Microsoft

# Search by product
python scripts/kev_query.py --product Chrome

# Look up specific CVE
python scripts/kev_query.py --cve CVE-2024-1234

# Show CVEs added in last 7 days
python scripts/kev_query.py --recent 7

# Show ransomware-associated CVEs
python scripts/kev_query.py --ransomware

# Show only scannable CVEs
python scripts/kev_query.py --scannable

# Show detailed statistics
python scripts/kev_query.py --stats

# Combine with --details flag for more info
python scripts/kev_query.py --vendor Microsoft --details
```

### 2.  Comprehensive Analytics Dashboard (`scripts/kev_analytics.py`)
Deep-dive analytics with multiple visualizations.

```bash
python scripts/kev_analytics.py
# or
make analytics
```

Generates:
- **Vendor Analysis**: Top vendors by CVE count
- **Product Analysis**: Most vulnerable products
- **Temporal Trends**: Monthly additions and cumulative growth
- **Ransomware Analysis**: CVEs associated with ransomware campaigns
- **CWE Distribution**: Most common vulnerability types
- **Coverage Analysis**: Scanning coverage by vendor

All visualizations are saved as high-resolution PNG files in `outputs/graphs/`.

### 3. 📈 Statistics Generator (`scripts/generate_stats.py`)
Automatically generates comprehensive statistics for the README.

```bash
python scripts/generate_stats.py
# or
make show-stats
```

This tool is **automatically run by GitHub Actions** when the KEV data updates, ensuring the README statistics are always current!

### Setup

Install dependencies:

```bash
# Option 1: Using Make (easiest!)
make setup

# Option 2: Using the setup script
chmod +x setup.sh
./setup.sh

# Option 3: Manual installation
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Quick Commands with Make

```bash
make analytics                        # Generate all analytics visualizations
make stats                            # Show database statistics
make query-vendor VENDOR="Microsoft"  # Search by vendor
make recent DAYS=7                    # Show recent CVEs
make ransomware                       # Show ransomware CVEs
make all                              # Generate everything
make help                             # Show all available commands
```

### Requirements

- Python 3.7+
- matplotlib
- pandas
- seaborn
- numpy

All dependencies are listed in `requirements.txt`.

## Contact

If you have any questions feel free to reach out to me on [Signal](https://signal.me/#eu/0Qd68U1ivXNdWCF4hf70UYFo7tB0w-GQqFpYcyV6-yr4exn2SclB6bFeP7wTAxQw) or via email: rishi@rxerium.com.
