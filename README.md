# CISA-KEV

[![CISA KEV](https://github.com/rxerium/CISA-KEV/actions/workflows/CISA.yaml/badge.svg)](https://github.com/rxerium/CISA-KEV/actions/workflows/CISA.yaml)
![Views](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Frxerium%2FCISA-KEV&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=Views&edge_flat=false)

A repository that automatically tracks and cross-references CISA's Known Exploitable Vulnerabilities (KEV) list with available Nuclei templates for vulnerability scanning.












































✅ Exported 597 priority gap CVEs to data/processed/CISA-Priority-Gap.csv

✅ Exported 597 priority gap CVEs to data/processed/CISA-Priority-Gap.csv

✅ Exported 597 priority gap CVEs to data/processed/CISA-Priority-Gap.csv

✅ Exported 597 priority gap CVEs to data/processed/CISA-Priority-Gap.csv

✅ Exported 596 priority gap CVEs to data/processed/CISA-Priority-Gap.csv

✅ Exported 596 priority gap CVEs to data/processed/CISA-Priority-Gap.csv

## 📊 Database Statistics

### Overview
- **Total CVEs in KEV**: 1,481
- **Scannable with Nuclei**: 413 (27.9%)
- **With Public PoCs**: **985 (66.5%)**
- **Unscannable**: 1,068 (72.1%)
- **Ransomware-Associated**: 303 (20.5%)
- **Unique Vendors**: 242
- **Unique Products**: 600

### Key Insights
- 🎯 **Microsoft** is the most represented vendor with **350 CVEs**
- 🔍 **413 CVEs** can be actively scanned with Nuclei templates
- 💣 **985 CVEs** (66.5%) have public proof-of-concept exploits available
- 🎯 **389 CVEs** have both PoC and Nuclei template (fully testable)
- 🔓 **596 CVEs** have PoC but no Nuclei template (testing gap)
- 🦠 **303 CVEs** (20.5%) are known to be used in ransomware campaigns
- 📅 **19 new CVEs** were added in the last 30 days
- 🔒 Most common vulnerability type: **CWE-20** (113 occurrences)
- ⚠️ **Microsoft** has the highest scanning coverage at 4.6%, while **Apple** and **Google** have 0%

### Recent Activity (Last 30 Days)
- **CVEs Added**: 19
- **Scannable Added**: 4
- **New Coverage**: 21.1%

### Top 10 Affected Vendors
| Rank | Vendor | CVE Count | Scannable | With PoC | Scanning Coverage |
|------|--------|-----------|-----------|----------|-------------------|
| 1 | Microsoft | 350 | 16 | 218 | 4.6% |
| 2 | Apple | 86 | 0 | 30 | 0.0% |
| 3 | Cisco | 82 | 12 | 24 | 14.6% |
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
| 2 | Multiple Products | 70 |
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
| 1 | CWE-20 | 113 |
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

**Total Gap CVEs:** 596 vulnerabilities have public exploits but lack automated detection templates.

📥 **Download Full Data:** [CISA-Priority-Gap.csv](CISA-Priority-Gap.csv) - Detailed CSV export with PoC URLs, EPSS scores, CVSS scores, severity levels, and vulnerability metadata.

**All 596 gap CVEs** listed below (sorted by date added to KEV, most recent first):

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
| CVE-2025-13223 | Google | Chromium V8 | 2025-11-19 | ✓ |  |
| CVE-2025-58034 | Fortinet | FortiWeb | 2025-11-18 | ✓ |  |
| CVE-2025-62215 | Microsoft | Windows | 2025-11-12 | ✓ |  |
| CVE-2025-21042 | Samsung | Mobile Devices | 2025-11-10 | ✓ |  |
| CVE-2025-41244 | Broadcom | VMware Aria Operations an | 2025-10-30 | ✓ |  |
| CVE-2025-61932 | Motex | LANSCOPE Endpoint Manager | 2025-10-22 | ✓ |  |
| CVE-2025-33073 | Microsoft | Windows | 2025-10-20 | ✓ |  |
| CVE-2025-47827 | IGEL | IGEL OS | 2025-10-14 | ✓ |  |
| CVE-2025-24990 | Microsoft | Windows | 2025-10-14 | ✓ |  |
| CVE-2025-59230 | Microsoft | Windows | 2025-10-14 | ✓ |  |
| CVE-2016-7836 | SKYSEA | Client View | 2025-10-14 | ✓ |  |
| CVE-2021-22555 | Linux | Kernel | 2025-10-06 | ✓ |  |
| CVE-2010-3962 | Microsoft | Internet Explorer | 2025-10-06 | ✓ |  |
| CVE-2021-43226 | Microsoft | Windows | 2025-10-06 | ✓ |  |
| CVE-2013-3918 | Microsoft | Windows | 2025-10-06 | ✓ |  |
| CVE-2010-3765 | Mozilla | Multiple Products | 2025-10-06 | ✓ |  |
| CVE-2014-6278 | GNU | GNU Bash | 2025-10-02 | ✓ |  |
| CVE-2015-7755 | Juniper | ScreenOS | 2025-10-02 | ✓ |  |
| CVE-2025-32463 | Sudo | Sudo | 2025-09-29 | ✓ |  |
| CVE-2025-20352 | Cisco | IOS and IOS XE | 2025-09-29 | ✓ |  |
| CVE-2025-20333 | Cisco | Secure Firewall Adaptive  | 2025-09-25 | ✓ |  |
| CVE-2025-10585 | Google | Chromium V8 | 2025-09-23 | ✓ |  |
| CVE-2025-48543 | Android | Runtime | 2025-09-04 | ✓ |  |
| CVE-2025-53690 | Sitecore | Multiple Products | 2025-09-04 | ✓ |  |
| CVE-2025-7775 | Citrix | NetScaler | 2025-08-26 | ✓ |  |
| CVE-2025-48384 | Git | Git | 2025-08-25 | ✓ |  |
| CVE-2024-8069 | Citrix | Session Recording | 2025-08-25 | ✓ |  |
| CVE-2025-43300 | Apple | iOS, iPadOS, and macOS | 2025-08-21 | ✓ |  |
| CVE-2025-54948 | Trend Micro | Apex One | 2025-08-18 | ✓ |  |
| CVE-2025-8875 | N-able | N-Central | 2025-08-13 | ✓ |  |
| CVE-2025-8088 | RARLAB | WinRAR | 2025-08-12 | ✓ |  |
| CVE-2013-3893 | Microsoft | Internet Explorer | 2025-08-12 | ✓ |  |
| CVE-2020-25079 | D-Link | DCS-2530L and DCS-2670L D | 2025-08-05 | ✓ |  |
| CVE-2022-40799 | D-Link | DNR-322L | 2025-08-05 | ✓ |  |
| CVE-2023-2533 | PaperCut | NG/MF | 2025-07-28 | ✓ |  |
| CVE-2025-20337 | Cisco | Identity Services Engine | 2025-07-28 | ✓ |  |
| CVE-2025-6558 | Google | Chromium | 2025-07-22 | ✓ |  |
| CVE-2025-49704 | Microsoft | SharePoint | 2025-07-22 | ✓ | 🦠 |
| CVE-2014-3931 | Looking Glass | Multi-Router Looking Glas | 2025-07-07 | ✓ |  |
| CVE-2025-6554 | Google | Chromium V8 | 2025-07-02 | ✓ |  |
| CVE-2025-6543 | Citrix | NetScaler ADC and Gateway | 2025-06-30 | ✓ |  |
| CVE-2019-6693 | Fortinet | FortiOS | 2025-06-25 | ✓ | 🦠 |
| CVE-2024-0769 | D-Link | DIR-859 Router | 2025-06-25 | ✓ |  |
| CVE-2024-54085 | AMI | MegaRAC SPx | 2025-06-25 | ✓ |  |
| CVE-2023-0386 | Linux | Kernel | 2025-06-17 | ✓ |  |
| CVE-2023-33538 | TP-Link | Multiple Routers | 2025-06-16 | ✓ |  |
| CVE-2025-33053 | Microsoft | Windows | 2025-06-10 | ✓ |  |
| CVE-2025-5419 | Google | Chromium V8 | 2025-06-05 | ✓ |  |
| CVE-2025-21479 | Qualcomm | Multiple Chipsets | 2025-06-03 | ✓ |  |
| CVE-2023-39780 | ASUS | RT-AX55 Routers | 2025-06-02 | ✓ |  |
| CVE-2025-4428 | Ivanti | Endpoint Manager Mobile ( | 2025-05-19 | ✓ |  |
| CVE-2025-42999 | SAP | NetWeaver | 2025-05-15 | ✓ |  |
| CVE-2025-32756 | Fortinet | Multiple Products | 2025-05-14 | ✓ |  |
| CVE-2025-32709 | Microsoft | Windows | 2025-05-13 | ✓ |  |
| CVE-2025-30397 | Microsoft | Windows | 2025-05-13 | ✓ |  |
| CVE-2025-32706 | Microsoft | Windows | 2025-05-13 | ✓ |  |
| CVE-2025-30400 | Microsoft | Windows | 2025-05-13 | ✓ |  |
| CVE-2024-11120 | GeoVision | Multiple Devices | 2025-05-07 | ✓ |  |
| CVE-2024-6047 | GeoVision | Multiple Devices | 2025-05-07 | ✓ |  |
| CVE-2025-27363 | FreeType | FreeType | 2025-05-06 | ✓ |  |
| CVE-2025-24054 | Microsoft | Windows | 2025-04-17 | ✓ |  |
| CVE-2025-31201 | Apple | Multiple Products | 2025-04-17 | ✓ |  |
| CVE-2025-31200 | Apple | Multiple Products | 2025-04-17 | ✓ |  |
| CVE-2025-29824 | Microsoft | Windows | 2025-04-08 | ✓ | 🦠 |
| CVE-2025-2783 | Google | Chromium Mojo | 2025-03-27 | ✓ |  |
| CVE-2019-9875 | Sitecore | CMS and Experience Platfo | 2025-03-26 | ✓ |  |
| CVE-2025-30154 | reviewdog | action-setup GitHub Actio | 2025-03-24 | ✓ |  |
| CVE-2025-30066 | tj-actions | changed-files GitHub Acti | 2025-03-18 | ✓ |  |
| CVE-2025-24201 | Apple | Multiple Products | 2025-03-13 | ✓ |  |
| CVE-2025-24985 | Microsoft | Windows | 2025-03-11 | ✓ |  |
| CVE-2025-26633 | Microsoft | Windows | 2025-03-11 | ✓ | 🦠 |
| CVE-2024-57968 | Advantive | VeraCore | 2025-03-10 | ✓ |  |
| CVE-2025-25181 | Advantive | VeraCore | 2025-03-10 | ✓ |  |
| CVE-2018-8639 | Microsoft | Windows | 2025-03-03 | ✓ | 🦠 |
| CVE-2017-3066 | Adobe | ColdFusion | 2025-02-24 | ✓ |  |
| CVE-2025-24200 | Apple | iOS and iPadOS | 2025-02-12 | ✓ |  |
| CVE-2024-41710 | Mitel | SIP Phones | 2025-02-12 | ✓ |  |
| CVE-2025-0994 | Trimble | Cityworks | 2025-02-07 | ✓ |  |
| CVE-2024-21413 | Microsoft | Office Outlook | 2025-02-06 | ✓ |  |
| CVE-2025-0411 | 7-Zip | 7-Zip | 2025-02-06 | ✓ |  |
| CVE-2018-9276 | Paessler | PRTG Network Monitor | 2025-02-04 | ✓ |  |
| CVE-2025-24085 | Apple | Multiple Products | 2025-01-29 | ✓ |  |
| CVE-2020-11023 | JQuery | JQuery | 2025-01-23 | ✓ |  |
| CVE-2025-21333 | Microsoft | Windows | 2025-01-14 | ✓ |  |
| CVE-2024-3393 | Palo Alto Networks | PAN-OS | 2024-12-30 | ✓ |  |
| CVE-2021-40407 | Reolink | RLC-410W IP Camera | 2024-12-18 | ✓ |  |
| CVE-2019-11001 | Reolink | Multiple IP Cameras | 2024-12-18 | ✓ |  |
| CVE-2022-23227 | NUUO | NVRmini2 Devices | 2024-12-18 | ✓ |  |
| CVE-2024-35250 | Microsoft | Windows | 2024-12-16 | ✓ |  |
| CVE-2024-49138 | Microsoft | Windows | 2024-12-10 | ✓ |  |
| CVE-2024-44308 | Apple | Multiple Products | 2024-11-21 | ✓ |  |
| CVE-2024-43451 | Microsoft | Windows | 2024-11-12 | ✓ |  |
| CVE-2024-49039 | Microsoft | Windows | 2024-11-12 | ✓ |  |
| CVE-2024-8956 | PTZOptics | PT30X-SDI/NDI Cameras | 2024-11-04 | ✓ |  |
| CVE-2024-8957 | PTZOptics | PT30X-SDI/NDI Cameras | 2024-11-04 | ✓ |  |
| CVE-2024-37383 | Roundcube | Webmail | 2024-10-24 | ✓ |  |
| CVE-2024-9680 | Mozilla | Firefox | 2024-10-15 | ✓ |  |
| CVE-2024-30088 | Microsoft | Windows  | 2024-10-15 | ✓ |  |
| CVE-2024-23113 | Fortinet | Multiple Products | 2024-10-09 | ✓ |  |
| CVE-2022-21445 | Oracle | ADF Faces | 2024-09-18 | ✓ |  |
| CVE-2014-0502 | Adobe | Flash Player | 2024-09-17 | ✓ |  |
| CVE-2014-0497 | Adobe | Flash Player | 2024-09-17 | ✓ |  |
| CVE-2024-8190 | Ivanti | Cloud Services Appliance | 2024-09-13 | ✓ |  |
| CVE-2024-38217 | Microsoft | Windows | 2024-09-10 | ✓ |  |
| CVE-2017-1000253 | Linux | Kernel | 2024-09-09 | ✓ | 🦠 |
| CVE-2016-3714 | ImageMagick | ImageMagick | 2024-09-09 | ✓ |  |
| CVE-2024-7965 | Google | Chromium V8 | 2024-08-28 | ✓ |  |
| CVE-2024-7971 | Google | Chromium V8 | 2024-08-26 | ✓ |  |
| CVE-2024-39717 | Versa | Director | 2024-08-23 | ✓ |  |
| CVE-2022-0185 | Linux | Kernel | 2024-08-21 | ✓ |  |
| CVE-2024-38193 | Microsoft | Windows | 2024-08-13 | ✓ |  |
| CVE-2024-36971 | Android | Kernel | 2024-08-07 | ✓ |  |
| CVE-2018-0824 | Microsoft | Windows | 2024-08-05 | ✓ |  |
| CVE-2024-37085 | VMware | ESXi | 2024-07-30 | ✓ | 🦠 |
| CVE-2012-4792 | Microsoft | Internet Explorer | 2024-07-23 | ✓ |  |
| CVE-2022-22948 | VMware | vCenter Server | 2024-07-17 | ✓ |  |
| CVE-2024-38080 | Microsoft | Windows  | 2024-07-09 | ✓ |  |
| CVE-2024-38112 | Microsoft | Windows | 2024-07-09 | ✓ |  |
| CVE-2020-13965 | Roundcube | Webmail | 2024-06-26 | ✓ |  |
| CVE-2022-2586 | Linux | Kernel | 2024-06-26 | ✓ |  |
| CVE-2024-26169 | Microsoft | Windows | 2024-06-13 | ✓ | 🦠 |
| CVE-2024-1086 | Linux | Kernel | 2024-05-30 | ✓ | 🦠 |
| CVE-2024-4978 | Justice AV Solutions | Viewer  | 2024-05-29 | ✓ |  |
| CVE-2024-5274 | Google | Chromium V8 | 2024-05-28 | ✓ |  |
| CVE-2024-4947 | Google | Chromium V8 | 2024-05-20 | ✓ |  |
| CVE-2024-4761 | Google | Chromium V8 | 2024-05-16 | ✓ |  |
| CVE-2014-100005 | D-Link | DIR-600 Router | 2024-05-16 | ✓ |  |
| CVE-2024-30051 | Microsoft | DWM Core Library | 2024-05-14 | ✓ | 🦠 |
| CVE-2024-29988 | Microsoft | SmartScreen Prompt | 2024-04-30 | ✓ |  |
| CVE-2024-20359 | Cisco | Adaptive Security Applian | 2024-04-24 | ✓ |  |
| CVE-2024-20353 | Cisco | Adaptive Security Applian | 2024-04-24 | ✓ |  |
| CVE-2023-24955 | Microsoft | SharePoint Server | 2024-03-26 | ✓ | 🦠 |
| CVE-2024-21338 | Microsoft | Windows | 2024-03-04 | ✓ | 🦠 |
| CVE-2023-29360 | Microsoft | Streaming Service | 2024-02-29 | ✓ |  |
| CVE-2024-21412 | Microsoft | Windows | 2024-02-13 | ✓ | 🦠 |
| CVE-2023-43770 | Roundcube | Webmail | 2024-02-12 | ✓ |  |
| CVE-2024-21762 | Fortinet | FortiOS | 2024-02-09 | ✓ | 🦠 |
| CVE-2023-4762 | Google | Chromium V8 | 2024-02-06 | ✓ |  |
| CVE-2018-15133 | Laravel | Laravel Framework | 2024-01-16 | ✓ |  |
| CVE-2016-20017 | D-Link | DSL-2750B Devices | 2024-01-08 | ✓ |  |
| CVE-2023-7024 | Google | Chromium WebRTC | 2024-01-02 | ✓ |  |
| CVE-2023-49897 | FXC | AE1021, AE1021PE | 2023-12-21 | ✓ |  |
| CVE-2023-36025 | Microsoft | Windows | 2023-11-14 | ✓ |  |
| CVE-2023-36846 | Juniper | Junos OS | 2023-11-13 | ✓ |  |
| CVE-2023-36847 | Juniper | Junos OS | 2023-11-13 | ✓ |  |
| CVE-2023-29552 | IETF | Service Location Protocol | 2023-11-08 | ✓ |  |
| CVE-2023-46748 | F5 | BIG-IP Configuration Util | 2023-10-31 | ✓ |  |
| CVE-2023-5631 | Roundcube | Webmail | 2023-10-26 | ✓ |  |
| CVE-2023-20273 | Cisco | Cisco IOS XE Web UI | 2023-10-23 | ✓ |  |
| CVE-2023-21608 | Adobe | Acrobat and Reader | 2023-10-10 | ✓ |  |
| CVE-2023-44487 | IETF | HTTP/2 | 2023-10-10 | ✓ |  |
| CVE-2023-28229 | Microsoft | Windows CNG Key Isolation | 2023-10-04 | ✓ |  |
| CVE-2023-5217 | Google | Chromium libvpx | 2023-10-02 | ✓ |  |
| CVE-2018-14667 | Red Hat | JBoss RichFaces Framework | 2023-09-28 | ✓ |  |
| CVE-2023-41991 | Apple | Multiple Products | 2023-09-25 | ✓ |  |
| CVE-2023-41992 | Apple | Multiple Products | 2023-09-25 | ✓ |  |
| CVE-2023-41993 | Apple | Multiple Products | 2023-09-25 | ✓ |  |
| CVE-2023-28434 | MinIO | MinIO | 2023-09-19 | ✓ |  |
| CVE-2014-8361 | Realtek | SDK | 2023-09-18 | ✓ |  |
| CVE-2017-6884 | Zyxel | EMG2926 Routers | 2023-09-18 | ✓ | 🦠 |
| CVE-2023-35674 | Android | Framework | 2023-09-13 | ✓ |  |
| CVE-2023-4863 | Google | Chromium WebP | 2023-09-13 | ✓ |  |
| CVE-2023-36802 | Microsoft | Streaming Service Proxy | 2023-09-12 | ✓ |  |
| CVE-2023-41064 | Apple | iOS, iPadOS, and macOS | 2023-09-11 | ✓ |  |
| CVE-2023-38831 | RARLAB | WinRAR | 2023-08-24 | ✓ | 🦠 |
| CVE-2023-27532 | Veeam | Backup & Replication | 2023-08-22 | ✓ | 🦠 |
| CVE-2017-18368 | Zyxel | P660HN-T1A Routers | 2023-08-07 | ✓ |  |
| CVE-2023-36884 | Microsoft | Windows | 2023-07-17 | ✓ | 🦠 |
| CVE-2023-36874 | Microsoft | Windows | 2023-07-11 | ✓ |  |
| CVE-2022-31199 | Netwrix | Auditor | 2023-07-11 | ✓ | 🦠 |
| CVE-2019-17621 | D-Link | DIR-859 Router | 2023-06-29 | ✓ |  |
| CVE-2019-20500 | D-Link | DWL-2600AP Access Point | 2023-06-29 | ✓ |  |
| CVE-2023-32434 | Apple | Multiple Products | 2023-06-23 | ✓ |  |
| CVE-2020-35730 | Roundcube | Roundcube Webmail | 2023-06-22 | ✓ |  |
| CVE-2021-44026 | Roundcube | Roundcube Webmail | 2023-06-22 | ✓ |  |
| CVE-2016-9079 | Mozilla | Firefox, Firefox ESR, and | 2023-06-22 | ✓ |  |
| CVE-2023-27997 | Fortinet | FortiOS and FortiProxy SS | 2023-06-13 | ✓ | 🦠 |
| CVE-2023-3079 | Google | Chromium V8 | 2023-06-07 | ✓ |  |
| CVE-2023-28771 | Zyxel | Multiple Firewalls | 2023-05-31 | ✓ |  |
| CVE-2023-2868 | Barracuda Networks | Email Security Gateway (E | 2023-05-26 | ✓ |  |
| CVE-2016-6415 | Cisco | IOS, IOS XR, and IOS XE | 2023-05-19 | ✓ |  |
| CVE-2021-3560 | Red Hat | Polkit | 2023-05-12 | ✓ |  |
| CVE-2014-0196 | Linux | Kernel | 2023-05-12 | ✓ |  |
| CVE-2010-3904 | Linux | Kernel | 2023-05-12 | ✓ |  |
| CVE-2023-29336 | Microsoft | Win32k | 2023-05-09 | ✓ |  |
| CVE-2023-2033 | Google | Chromium V8 | 2023-04-17 | ✓ |  |
| CVE-2023-20963 | Android | Framework | 2023-04-13 | ✓ |  |
| CVE-2023-28252 | Microsoft | Windows | 2023-04-11 | ✓ | 🦠 |
| CVE-2023-28205 | Apple | Multiple Products | 2023-04-10 | ✓ |  |
| CVE-2023-28206 | Apple | iOS, iPadOS, and macOS | 2023-04-10 | ✓ |  |
| CVE-2021-27876 | Veritas | Backup Exec Agent | 2023-04-07 | ✓ | 🦠 |
| CVE-2021-27878 | Veritas | Backup Exec Agent | 2023-04-07 | ✓ | 🦠 |
| CVE-2019-1388 | Microsoft | Windows | 2023-04-07 | ✓ | 🦠 |
| CVE-2013-3163 | Microsoft | Internet Explorer | 2023-03-30 | ✓ |  |
| CVE-2017-7494 | Samba | Samba | 2023-03-30 | ✓ | 🦠 |
| CVE-2022-39197 | Fortra | Cobalt Strike | 2023-03-30 | ✓ |  |
| CVE-2022-38181 | Arm | Mali Graphics Processing  | 2023-03-30 | ✓ |  |
| CVE-2023-0266 | Linux | Kernel | 2023-03-30 | ✓ |  |
| CVE-2022-3038 | Google | Chromium Network Service | 2023-03-30 | ✓ |  |
| CVE-2023-23397 | Microsoft | Office | 2023-03-14 | ✓ |  |
| CVE-2020-5741 | Plex | Media Server | 2023-03-10 | ✓ |  |
| CVE-2022-28810 | Zoho | ManageEngine | 2023-03-07 | ✓ |  |
| CVE-2023-21823 | Microsoft | Windows | 2023-02-14 | ✓ |  |
| CVE-2015-2291 | Intel | Ethernet Diagnostics Driv | 2023-02-10 | ✓ | 🦠 |
| CVE-2017-11357 | Telerik | User Interface (UI) for A | 2023-01-26 | ✓ | 🦠 |
| CVE-2022-41080 | Microsoft | Exchange Server | 2023-01-10 | ✓ | 🦠 |
| CVE-2023-21674 | Microsoft | Windows | 2023-01-10 | ✓ |  |
| CVE-2018-5430 | TIBCO | JasperReports | 2022-12-29 | ✓ |  |
| CVE-2022-27518 | Citrix | Application Delivery Cont | 2022-12-13 | ✓ |  |
| CVE-2022-26501 | Veeam | Backup & Replication | 2022-12-13 | ✓ | 🦠 |
| CVE-2022-4262 | Google | Chromium V8 | 2022-12-05 | ✓ |  |
| CVE-2022-4135 | Google | Chromium GPU | 2022-11-28 | ✓ |  |
| CVE-2020-3433 | Cisco | AnyConnect Secure | 2022-10-24 | ✓ | 🦠 |
| CVE-2020-3153 | Cisco | AnyConnect Secure | 2022-10-24 | ✓ | 🦠 |
| CVE-2018-19323 | GIGABYTE | Multiple Products | 2022-10-24 | ✓ | 🦠 |
| CVE-2018-19322 | GIGABYTE | Multiple Products | 2022-10-24 | ✓ | 🦠 |
| CVE-2018-19321 | GIGABYTE | Multiple Products | 2022-10-24 | ✓ | 🦠 |
| CVE-2018-19320 | GIGABYTE | Multiple Products | 2022-10-24 | ✓ | 🦠 |
| CVE-2021-3493 | Linux | Kernel | 2022-10-20 | ✓ |  |
| CVE-2022-41082 | Microsoft | Exchange Server | 2022-09-30 | ✓ | 🦠 |
| CVE-2022-41040 | Microsoft | Exchange Server | 2022-09-30 | ✓ | 🦠 |
| CVE-2013-6282 | Linux | Kernel | 2022-09-15 | ✓ |  |
| CVE-2013-2597 | Code Aurora | ACDB Audio Driver | 2022-09-15 | ✓ |  |
| CVE-2013-2596 | Linux | Kernel | 2022-09-15 | ✓ |  |
| CVE-2013-2094 | Linux | Kernel | 2022-09-15 | ✓ |  |
| CVE-2010-2568 | Microsoft | Windows | 2022-09-15 | ✓ |  |
| CVE-2022-37969 | Microsoft | Windows | 2022-09-14 | ✓ |  |
| CVE-2022-26258 | D-Link | DIR-820L | 2022-09-08 | ✓ |  |
| CVE-2020-9934 | Apple | iOS, iPadOS, and macOS | 2022-09-08 | ✓ |  |
| CVE-2018-7445 | MikroTik | RouterOS | 2022-09-08 | ✓ |  |
| CVE-2011-1823 | Android | Android OS | 2022-09-08 | ✓ |  |
| CVE-2020-28949 | PEAR | Archive_Tar | 2022-08-25 | ✓ |  |
| CVE-2022-2856 | Google | Chromium Intents | 2022-08-18 | ✓ |  |
| CVE-2022-26923 | Microsoft | Active Directory | 2022-08-18 | ✓ |  |
| CVE-2022-21971 | Microsoft | Windows | 2022-08-18 | ✓ |  |
| CVE-2022-27925 | Synacor | Zimbra Collaboration Suit | 2022-08-11 | ✓ | 🦠 |
| CVE-2022-30333 | RARLAB | UnRAR | 2022-08-09 | ✓ | 🦠 |
| CVE-2021-30533 | Google | Chromium PopupBlocker | 2022-06-27 | ✓ |  |
| CVE-2021-4034 | Red Hat | Polkit | 2022-06-27 | ✓ |  |
| CVE-2019-8605 | Apple | Multiple Products | 2022-06-27 | ✓ |  |
| CVE-2022-30190 | Microsoft | Windows | 2022-06-14 | ✓ | 🦠 |
| CVE-2021-38163 | SAP | NetWeaver | 2022-06-09 | ✓ |  |
| CVE-2016-2386 | SAP | NetWeaver | 2022-06-09 | ✓ |  |
| CVE-2016-2388 | SAP | NetWeaver | 2022-06-09 | ✓ |  |
| CVE-2019-7193 | QNAP | QTS | 2022-06-08 | ✓ | 🦠 |
| CVE-2019-5825 | Google | Chromium V8 | 2022-06-08 | ✓ |  |
| CVE-2018-6065 | Google | Chromium V8 | 2022-06-08 | ✓ |  |
| CVE-2018-17480 | Google | Chromium V8 | 2022-06-08 | ✓ |  |
| CVE-2018-17463 | Google | Chromium V8 | 2022-06-08 | ✓ |  |
| CVE-2017-5070 | Google | Chromium V8 | 2022-06-08 | ✓ |  |
| CVE-2017-5030 | Google | Chromium V8 | 2022-06-08 | ✓ |  |
| CVE-2016-5198 | Google | Chromium V8 | 2022-06-08 | ✓ |  |
| CVE-2016-1646 | Google | Chromium V8 | 2022-06-08 | ✓ |  |
| CVE-2012-5054 | Adobe | Flash Player | 2022-06-08 | ✓ |  |
| CVE-2012-4969 | Microsoft | Internet Explorer | 2022-06-08 | ✓ |  |
| CVE-2012-1889 | Microsoft | XML Core Services | 2022-06-08 | ✓ |  |
| CVE-2012-0754 | Adobe | Flash Player | 2022-06-08 | ✓ |  |
| CVE-2011-2462 | Adobe | Reader and Acrobat | 2022-06-08 | ✓ |  |
| CVE-2011-0609 | Adobe | Flash Player | 2022-06-08 | ✓ |  |
| CVE-2010-2883 | Adobe | Acrobat and Reader | 2022-06-08 | ✓ |  |
| CVE-2010-1297 | Adobe | Flash Player | 2022-06-08 | ✓ |  |
| CVE-2009-4324 | Adobe | Acrobat and Reader | 2022-06-08 | ✓ |  |
| CVE-2009-3953 | Adobe | Acrobat and Reader | 2022-06-08 | ✓ |  |
| CVE-2008-0655 | Adobe | Acrobat and Reader | 2022-06-08 | ✓ |  |
| CVE-2007-5659 | Adobe | Acrobat and Reader | 2022-06-08 | ✓ |  |
| CVE-2006-2492 | Microsoft | Word | 2022-06-08 | ✓ |  |
| CVE-2019-3010 | Oracle | Solaris | 2022-05-25 | ✓ |  |
| CVE-2016-0984 | Adobe | Flash Player and AIR | 2022-05-25 | ✓ |  |
| CVE-2015-0016 | Microsoft | Windows | 2022-05-25 | ✓ |  |
| CVE-2015-1769 | Microsoft | Windows | 2022-05-25 | ✓ |  |
| CVE-2015-4495 | Mozilla | Firefox | 2022-05-25 | ✓ |  |
| CVE-2015-8651 | Adobe | Flash Player | 2022-05-25 | ✓ |  |
| CVE-2014-3153 | Linux | Kernel | 2022-05-25 | ✓ |  |
| CVE-2013-7331 | Microsoft | Internet Explorer | 2022-05-25 | ✓ |  |
| CVE-2013-3896 | Microsoft | Silverlight | 2022-05-25 | ✓ |  |
| CVE-2013-2423 | Oracle | Java Runtime Environment  | 2022-05-25 | ✓ |  |
| CVE-2013-0431 | Oracle | Java Runtime Environment  | 2022-05-25 | ✓ | 🦠 |
| CVE-2013-0422 | Oracle | Java Runtime Environment  | 2022-05-25 | ✓ |  |
| CVE-2013-0074 | Microsoft | Silverlight | 2022-05-25 | ✓ | 🦠 |
| CVE-2010-1428 | Red Hat | JBoss | 2022-05-25 | ✓ | 🦠 |
| CVE-2010-0840 | Oracle | Java Runtime Environment  | 2022-05-25 | ✓ |  |
| CVE-2010-0738 | Red Hat | JBoss | 2022-05-25 | ✓ | 🦠 |
| CVE-2018-8611 | Microsoft | Windows | 2022-05-24 | ✓ |  |
| CVE-2017-0147 | Microsoft | SMBv1 server | 2022-05-24 | ✓ | 🦠 |
| CVE-2017-0022 | Microsoft | XML Core Services | 2022-05-24 | ✓ |  |
| CVE-2017-0005 | Microsoft | Windows | 2022-05-24 | ✓ |  |
| CVE-2017-8291 | Artifex | Ghostscript | 2022-05-24 | ✓ |  |
| CVE-2017-8543 | Microsoft | Windows | 2022-05-24 | ✓ |  |
| CVE-2016-3351 | Microsoft | Internet Explorer and Edg | 2022-05-24 | ✓ | 🦠 |
| CVE-2016-4655 | Apple | iOS | 2022-05-24 | ✓ |  |
| CVE-2016-4656 | Apple | iOS | 2022-05-24 | ✓ |  |
| CVE-2016-4657 | Apple | iOS | 2022-05-24 | ✓ |  |
| CVE-2016-6366 | Cisco | Adaptive Security Applian | 2022-05-24 | ✓ |  |
| CVE-2016-6367 | Cisco | Adaptive Security Applian | 2022-05-24 | ✓ |  |
| CVE-2021-30883 | Apple | Multiple Products | 2022-05-23 | ✓ |  |
| CVE-2020-1027 | Microsoft | Windows | 2022-05-23 | ✓ |  |
| CVE-2019-5786 | Google | Chrome Blink | 2022-05-23 | [PoC](https://crbug.com/936448) |  |
| CVE-2019-13720 | Google | Chrome WebAudio | 2022-05-23 | [PoC](http://packetstormsecurity.com/files/167066/Google-Chrome-78.0.3904.70-Remote-Code-Execution.html) |  |
| CVE-2019-11707 | Mozilla | Firefox and Thunderbird | 2022-05-23 | [PoC](https///github.com:flabbergastedbd/cve-2019-11707.git) |  |
| CVE-2019-11708 | Mozilla | Firefox and Thunderbird | 2022-05-23 | [PoC](https///gitee.com:mirrors_0vercl0k/CVE-2019-11708.git) |  |
| CVE-2019-18426 | Meta Platforms | WhatsApp | 2022-05-23 | [PoC](http://packetstormsecurity.com/files/157097/WhatsApp-Desktop-0.3.9308-Cross-Site-Scripting.html) |  |
| CVE-2014-4113 | Microsoft | Win32k | 2022-05-04 | [PoC](http://blog.trendmicro.com/trendlabs-security-intelligence/an-analysis-of-a-windows-kernel-mode-vulnerability-cve-2014-4113/) |  |
| CVE-2014-0322 | Microsoft | Internet Explorer | 2022-05-04 | [PoC](http://www.exploit-db.com/exploits/32851) |  |
| CVE-2022-26904 | Microsoft | Windows | 2022-04-25 | [PoC](https://github.com/rapid7/metasploit-framework/blob/master/modules/exploits/windows/local/cve_2022_26904_superprofile.rb) |  |
| CVE-2022-21919 | Microsoft | Windows | 2022-04-25 | [PoC](https://github.com/rapid7/metasploit-framework/blob/master/modules/exploits/windows/local/cve_2022_26904_superprofile.rb) |  |
| CVE-2022-0847 | Linux | Kernel | 2022-04-25 | [PoC](http://packetstormsecurity.com/files/166229/Dirty-Pipe-Linux-Privilege-Escalation.html) |  |
| CVE-2019-1003029 | Jenkins | Script Security Plugin | 2022-04-25 | [PoC](https://github.com/rapid7/metasploit-framework/blob/master/modules/exploits/multi/http/jenkins_metaprogramming.rb) |  |
| CVE-2022-22718 | Microsoft | Windows | 2022-04-19 | [PoC](https://github.com/ahmetfurkans/CVE-2022-22718) |  |
| CVE-2022-22960 | VMware | Multiple Products | 2022-04-15 | [PoC](http://packetstormsecurity.com/files/171918/Mware-Workspace-ONE-Remote-Code-Execution.html) |  |
| CVE-2022-1364 | Google | Chromium V8 | 2022-04-15 | [PoC](https://crbug.com/1315901) |  |
| CVE-2014-0780 | InduSoft | Web Studio | 2022-04-15 | [PoC](https://www.exploit-db.com/exploits/42699/) |  |
| CVE-2018-20753 | Kaseya | Virtual System/Server Adm | 2022-04-13 | [PoC](https://blog.huntresslabs.com/deep-dive-kaseya-vsa-mining-payload-c0ac839a0e88) | 🦠 |
| CVE-2015-5122 | Adobe | Flash Player | 2022-04-13 | [PoC](http://packetstormsecurity.com/files/132663/Adobe-Flash-opaqueBackground-Use-After-Free.html) |  |
| CVE-2015-3113 | Adobe | Flash Player | 2022-04-13 | [PoC](https://github.com/rapid7/metasploit-framework/blob/master/modules/exploits/multi/browser/adobe_flash_nellymoser_bof.rb) |  |
| CVE-2015-2502 | Microsoft | Internet Explorer | 2022-04-13 | [PoC](http://twitter.com/Laughing_Mantis/statuses/633839231840841728) |  |
| CVE-2015-0313 | Adobe | Flash Player | 2022-04-13 | [PoC](http://packetstormsecurity.com/files/131189/Adobe-Flash-Player-ByteArray-With-Workers-Use-After-Free.html) |  |
| CVE-2015-0311 | Adobe | Flash Player | 2022-04-13 | [PoC](https://github.com/rapid7/metasploit-framework/blob/master/modules/exploits/multi/browser/adobe_flash_uncompress_zlib_uaf.rb) |  |
| CVE-2021-42287 | Microsoft | Active Directory | 2022-04-11 | [PoC](https://github.com/Chrisync/CVE-Scanner) | 🦠 |
| CVE-2021-42278 | Microsoft | Active Directory | 2022-04-11 | [PoC](https///github.com:XiaoliChan/Invoke-sAMSpoofing.git) | 🦠 |
| CVE-2021-22600 | Linux | Kernel | 2022-04-11 | [PoC](https://github.com/Chinmay1743/af_packet.c) |  |
| CVE-2020-2509 | QNAP | QNAP Network-Attached Sto | 2022-04-11 | [PoC](https///github.com:jbaines-r7/overkill.git) |  |
| CVE-2017-11317 | Telerik | User Interface (UI) for A | 2022-04-11 | [PoC](http://packetstormsecurity.com/files/159653/Telerik-UI-ASP.NET-AJAX-RadAsyncUpload-Deserialization.html) |  |
| CVE-2021-31166 | Microsoft | HTTP Protocol Stack | 2022-04-06 | [PoC](https://github.com/qazbnme/CVE-2021) |  |
| CVE-2017-0148 | Microsoft | SMBv1 server | 2022-04-06 | [PoC](http://packetstormsecurity.com/files/154690/DOUBLEPULSAR-Payload-Execution-Neutralization.html) | 🦠 |
| CVE-2021-34484 | Microsoft | Windows | 2022-03-31 | [PoC](https://github.com/rapid7/metasploit-framework/blob/master/modules/exploits/windows/local/cve_2022_26904_superprofile.rb) |  |
| CVE-2021-21551 | Dell | dbutil Driver | 2022-03-31 | [PoC](http://packetstormsecurity.com/files/162604/Dell-DBUtil_2_3.sys-IOCTL-Memory-Read-Write.html) |  |
| CVE-2018-10561 | Dasan | Gigabit Passive Optical N | 2022-03-31 | [PoC](https://www.exploit-db.com/exploits/44576/) |  |
| CVE-2022-1096 | Google | Chromium V8 | 2022-03-28 | [PoC](https://github.com/Mav3r1ck0x1/Chrome-and-Edge-Version-Dumper) |  |
| CVE-2021-34486 | Microsoft | Windows | 2022-03-28 | [PoC](https://github.com/b1tg/CVE-2021-34486-exp) |  |
| CVE-2018-8440 | Microsoft | Windows | 2022-03-28 | [PoC](https://blog.0patch.com/2018/08/how-we-micropatched-publicly-dropped.html) | 🦠 |
| CVE-2017-0213 | Microsoft | Windows | 2022-03-28 | [PoC](https://www.exploit-db.com/exploits/42020/) | 🦠 |
| CVE-2017-0059 | Microsoft | Internet Explorer | 2022-03-28 | [PoC](https://www.exploit-db.com/exploits/41661/) |  |
| CVE-2017-0037 | Microsoft | Edge and Internet Explore | 2022-03-28 | [PoC](https://0patch.blogspot.si/2017/03/0patching-another-0-day-internet.html) |  |
| CVE-2016-7201 | Microsoft | Edge | 2022-03-28 | [PoC](https://github.com/theori-io/chakra-2016-11) |  |
| CVE-2016-7200 | Microsoft | Edge | 2022-03-28 | [PoC](https://github.com/theori-io/chakra-2016-11) |  |
| CVE-2016-0189 | Microsoft | Internet Explorer | 2022-03-28 | [PoC](https://www.virusbulletin.com/virusbulletin/2017/01/journey-and-evolution-god-mode-2016-cve-2016-0189/) |  |
| CVE-2016-0151 | Microsoft | Client-Server Run-time Su | 2022-03-28 | [PoC](https://www.exploit-db.com/exploits/39740/) | 🦠 |
| CVE-2016-0040 | Microsoft | Windows | 2022-03-28 | [PoC](https://www.exploit-db.com/exploits/44586/) |  |
| CVE-2015-2426 | Microsoft | Windows | 2022-03-28 | [PoC](http://blog.trendmicro.com/trendlabs-security-intelligence/a-look-at-the-open-type-font-manager-vulnerability-from-the-hacking-team-leak/) |  |
| CVE-2013-3660 | Microsoft | Win32k | 2022-03-28 | [PoC](http://twitter.com/taviso/statuses/309157606247768064) |  |
| CVE-2013-2729 | Adobe | Reader and Acrobat | 2022-03-28 | [PoC](https://github.com/feliam/CVE-2013-2729) |  |
| CVE-2013-2551 | Microsoft | Internet Explorer | 2022-03-28 | [PoC](https://github.com/rapid7/metasploit-framework/blob/master/modules/exploits/windows/browser/ms13_037_svg_dashstyle.rb) | 🦠 |
| CVE-2013-2465 | Oracle | Java SE | 2022-03-28 | [PoC](https://github.com/rapid7/metasploit-framework/blob/master/modules/exploits/multi/browser/java_storeimagearray.rb) | 🦠 |
| CVE-2013-1690 | Mozilla | Firefox and Thunderbird | 2022-03-28 | [PoC](https://github.com/rapid7/metasploit-framework/blob/master/modules/exploits/windows/browser/mozilla_firefox_onreadystatechange.rb) |  |
| CVE-2012-5076 | Oracle | Java SE | 2022-03-28 | [PoC](https://github.com/rapid7/metasploit-framework/blob/master/modules/exploits/multi/browser/java_jre17_glassfish_averagerangestatisticimpl.rb) |  |
| CVE-2011-2005 | Microsoft | Ancillary Function Driver | 2022-03-28 | [PoC](https///github.com:Ascotbe/Kernelhub.git) |  |
| CVE-2010-4398 | Microsoft | Windows | 2022-03-28 | [PoC](http://isc.sans.edu/diary.html?storyid=9988) |  |
| CVE-2022-26318 | WatchGuard | Firebox and XTM Appliance | 2022-03-25 | [PoC](https://github.com/rapid7/metasploit-framework/blob/master/modules/exploits/linux/http/watchguard_firebox_unauth_rce_cve_2022_26318.rb) |  |
| CVE-2022-21999 | Microsoft | Windows | 2022-03-25 | [PoC](https://github.com/rapid7/metasploit-framework/blob/master/modules/exploits/windows/local/cve_2022_21999_spoolfool_privesc.rb) | 🦠 |
| CVE-2021-22941 | Citrix | ShareFile | 2022-03-25 | [PoC](https://github.com/pratikjojode/citrix-cve-2021-22941-lab) | 🦠 |
| CVE-2020-9377 | D-Link | DIR-610 Devices | 2022-03-25 | [PoC](https://gist.github.com/GouveaHeitor/131557f9de7d571f118f59805df852dc) |  |
| CVE-2019-12991 | Citrix | SD-WAN and NetScaler | 2022-03-25 | [PoC](http://packetstormsecurity.com/files/153638/Citrix-SD-WAN-Appliance-10.2.2-Authentication-Bypass-Remote-Command-Execution.html) |  |
| CVE-2019-11043 | PHP | FastCGI Process Manager ( | 2022-03-25 | [PoC](https://github.com/neex/phuip-fpizdam) | 🦠 |
| CVE-2019-1003030 | Jenkins | Matrix Project Plugin | 2022-03-25 | [PoC](http://packetstormsecurity.com/files/159603/Jenkins-2.63-Sandbox-Bypass.html) |  |
| CVE-2018-8414 | Microsoft | Windows | 2022-03-25 | [PoC](https///github.com:whereisr0da/CVE-2018-8414-POC.git) |  |
| CVE-2018-6961 | VMware | SD-WAN Edge | 2022-03-25 | [PoC](https://www.exploit-db.com/exploits/44959/) |  |
| CVE-2018-14839 | LG | N1A1 NAS | 2022-03-25 | [PoC](https://medium.com/%400x616163/lg-n1a1-unauthenticated-remote-command-injection-cve-2018-14839-9d2cf760e247) |  |
| CVE-2017-6334 | NETGEAR | DGN2200 Devices | 2022-03-25 | [PoC](https://www.exploit-db.com/exploits/41459/) |  |
| CVE-2017-6316 | Citrix | NetScaler SD-WAN Enterpri | 2022-03-25 | [PoC](https://www.exploit-db.com/exploits/42345/) |  |
| CVE-2017-0146 | Microsoft | Windows | 2022-03-25 | [PoC](http://packetstormsecurity.com/files/154690/DOUBLEPULSAR-Payload-Execution-Neutralization.html) | 🦠 |
| CVE-2016-11021 | D-Link | DCS-930L Devices | 2022-03-25 | [PoC](https://www.exploit-db.com/exploits/39437) |  |
| CVE-2016-10174 | NETGEAR | WNR2000v5 Router | 2022-03-25 | [PoC](http://seclists.org/fulldisclosure/2016/Dec/72) |  |
| CVE-2016-0752 | Rails | Ruby on Rails | 2022-03-25 | [PoC](http://www.openwall.com/lists/oss-security/2016/01/25/13) |  |
| CVE-2015-1187 | D-Link and TRENDnet | Multiple Devices | 2022-03-25 | [PoC](http://packetstormsecurity.com/files/131465/D-Link-TRENDnet-NCC-Service-Command-Injection.html) |  |
| CVE-2014-6332 | Microsoft | Windows | 2022-03-25 | [PoC](http://packetstormsecurity.com/files/134053/Avant-Browser-Lite-Ultimate-Remote-Code-Execution.html) |  |
| CVE-2014-0130 | Rails | Ruby on Rails | 2022-03-25 | [PoC](https://github.com/omarkurt/cve-2014-0130) |  |
| CVE-2013-5223 | D-Link | DSL-2760U | 2022-03-25 | [PoC](http://packetstormsecurity.com/files/123976) |  |
| CVE-2013-4810 | Hewlett Packard (HP) | ProCurve Manager (PCM), P | 2022-03-25 | [PoC](https://www.exploit-db.com/exploits/28713/) |  |
| CVE-2010-4345 | Exim | Exim | 2022-03-25 | [PoC](https://github.com/rapid7/metasploit-framework/blob/master/modules/exploits/unix/smtp/exim4_string_format.rb) |  |
| CVE-2010-4344 | Exim | Exim | 2022-03-25 | [PoC](http://www.exim.org/lurker/message/20101207.215955.bb32d4f2.en.html) |  |
| CVE-2009-0927 | Adobe | Reader and Acrobat | 2022-03-25 | [PoC](https://github.com/rapid7/metasploit-framework/blob/master/modules/exploits/windows/fileformat/adobe_geticon.rb) |  |
| CVE-2005-2773 | Hewlett Packard (HP) | OpenView Network Node Man | 2022-03-25 | [PoC](http://marc.info/?l=bugtraq&m=112499121725662&w=2) |  |
| CVE-2019-1405 | Microsoft | Windows | 2022-03-15 | [PoC](https://github.com/rapid7/metasploit-framework/blob/master/modules/exploits/windows/local/comahawk.rb) | 🦠 |
| CVE-2019-1322 | Microsoft | Windows | 2022-03-15 | [PoC](http://packetstormsecurity.com/files/155723/Microsoft-UPnP-Local-Privilege-Elevation.html) | 🦠 |
| CVE-2019-1315 | Microsoft | Windows | 2022-03-15 | [PoC](https://github.com/Mayter/CVE-2019-1315) | 🦠 |
| CVE-2019-1253 | Microsoft | Windows | 2022-03-15 | [PoC](https///github.com:sgabe/CVE-2019-1253.git) | 🦠 |
| CVE-2019-1132 | Microsoft | Win32k | 2022-03-15 | [PoC](https///github.com:Ascotbe/Kernelhub.git) |  |
| CVE-2019-1069 | Microsoft | Task Scheduler | 2022-03-15 | [PoC](https://blog.0patch.com/2019/06/another-task-scheduler-0day-another.html) | 🦠 |
| CVE-2019-1064 | Microsoft | Windows | 2022-03-15 | [PoC](https///gitlab.com:gavz/CVE-2019-1064.git) | 🦠 |
| CVE-2019-0841 | Microsoft | Windows | 2022-03-15 | [PoC](http://packetstormsecurity.com/files/153642/AppXSvc-Hard-Link-Privilege-Escalation.html) | 🦠 |
| CVE-2019-0543 | Microsoft | Windows | 2022-03-15 | [PoC](https://www.exploit-db.com/exploits/46156/) | 🦠 |
| CVE-2018-8120 | Microsoft | Win32k | 2022-03-15 | [PoC](https://www.exploit-db.com/exploits/45653/) | 🦠 |
| CVE-2017-0101 | Microsoft | Windows | 2022-03-15 | [PoC](https://www.exploit-db.com/exploits/44479/) | 🦠 |
| CVE-2016-3309 | Microsoft | Windows | 2022-03-15 | [PoC](https///github.com:siberas/CVE-2016-3309_Reloaded.git) | 🦠 |
| CVE-2015-2546 | Microsoft | Win32k | 2022-03-15 | [PoC](https///github.com:Ascotbe/Kernelhub.git) | 🦠 |
| CVE-2022-26486 | Mozilla | Firefox | 2022-03-07 | [PoC](https://bugzilla.mozilla.org/show_bug.cgi?id=1758070) |  |
| CVE-2022-26485 | Mozilla | Firefox | 2022-03-07 | [PoC](https://bugzilla.mozilla.org/show_bug.cgi?id=1758062) |  |
| CVE-2020-8218 | Pulse Secure | Pulse Connect Secure | 2022-03-07 | [PoC](https://www.gosecure.net/blog/2020/11/13/forget-your-perimeter-part-2-four-vulnerabilities-in-pulse-connect-secure/) |  |
| CVE-2017-6077 | NETGEAR | Wireless Router DGN2200 | 2022-03-07 | [PoC](https://www.exploit-db.com/exploits/41394/) |  |
| CVE-2009-3960 | Adobe | BlazeDS | 2022-03-07 | [PoC](https://www.exploit-db.com/exploits/41855/) | 🦠 |
| CVE-2021-41379 | Microsoft | Windows | 2022-03-03 | [PoC](https///github.com:jbaines-r7/shakeitoff.git) | 🦠 |
| CVE-2020-11899 | Treck TCP/IP stack | IPv6 | 2022-03-03 | [PoC](https://www.jsof-tech.com/ripple20/) |  |
| CVE-2019-16928 | Exim | Exim Internet Mailer | 2022-03-03 | [PoC](http://www.openwall.com/lists/oss-security/2019/09/28/1) |  |
| CVE-2019-1652 | Cisco | Small Business RV320 and  | 2022-03-03 | [PoC](http://packetstormsecurity.com/files/152262/Cisco-RV320-Command-Injection.html) |  |
| CVE-2018-8581 | Microsoft | Exchange Server | 2022-03-03 | [PoC](https///gitee.com:mirrors_WyAtu/CVE-2018-8581.git) | 🦠 |
| CVE-2018-8298 | ChakraCore | ChakraCore scripting engi | 2022-03-03 | [PoC](https://www.exploit-db.com/exploits/45217/) |  |
| CVE-2017-8540 | Microsoft | Malware Protection Engine | 2022-03-03 | [PoC](https://www.exploit-db.com/exploits/42088/) |  |
| CVE-2017-6736 | Cisco | IOS and IOS XE Software | 2022-03-03 | [PoC](https://github.com/artkond/cisco-snmp-rce) |  |
| CVE-2017-11826 | Microsoft | Office | 2022-03-03 | [PoC](https://0patch.blogspot.com/2017/11/0patching-pretty-nasty-microsoft-word.html) |  |
| CVE-2017-0261 | Microsoft | Office | 2022-03-03 | [PoC](https///github.com:erfze/CVE-2017-0261.git) |  |
| CVE-2016-7855 | Adobe | Flash Player | 2022-03-03 | [PoC](https://github.com/swagatbora90/CheckFlashPlayerVersion) |  |
| CVE-2016-5195 | Linux | Kernel | 2022-03-03 | [PoC](http://packetstormsecurity.com/files/139277/Kernel-Live-Patch-Security-Notice-LSN-0012-1.html) |  |
| CVE-2016-4117 | Adobe | Flash Player | 2022-03-03 | [PoC](https://www.exploit-db.com/exploits/46339/) |  |
| CVE-2016-0099 | Microsoft | Windows | 2022-03-03 | [PoC](https://www.exploit-db.com/exploits/39574/) | 🦠 |
| CVE-2015-5119 | Adobe | Flash Player | 2022-03-03 | [PoC](https://packetstormsecurity.com/files/132600/Adobe-Flash-Player-ByteArray-Use-After-Free.html) |  |
| CVE-2015-3043 | Adobe | Flash Player | 2022-03-03 | [PoC](https://www.exploit-db.com/exploits/37536/) |  |
| CVE-2015-2545 | Microsoft | Office | 2022-03-03 | [PoC](http://blog.morphisec.com/exploit-bypass-emet-cve-2015-2545) |  |
| CVE-2015-2387 | Microsoft | ATM Font Driver | 2022-03-03 | [PoC](https///github.com:Ascotbe/Kernelhub.git) |  |
| CVE-2015-1701 | Microsoft | Win32k | 2022-03-03 | [PoC](https://www.exploit-db.com/exploits/37049/) | 🦠 |
| CVE-2014-4114 | Microsoft | Windows | 2022-03-03 | [PoC](http://blog.trendmicro.com/trendlabs-security-intelligence/an-analysis-of-windows-zero-day-vulnerability-cve-2014-4114-aka-sandworm/) |  |
| CVE-2013-5065 | Microsoft | Windows | 2022-03-03 | [PoC](https://www.exploit-db.com/exploits/37732/) |  |
| CVE-2013-3897 | Microsoft | Internet Explorer | 2022-03-03 | [PoC](https://github.com/rapid7/metasploit-framework/blob/master/modules/exploits/windows/browser/ms13_080_cdisplaypointer.rb) |  |
| CVE-2013-3346 | Adobe | Reader and Acrobat | 2022-03-03 | [PoC](https://github.com/rapid7/metasploit-framework/blob/master/modules/exploits/windows/fileformat/adobe_toolbutton.rb) |  |
| CVE-2013-1675 | Mozilla | Firefox | 2022-03-03 | [PoC](https://bugzilla.mozilla.org/show_bug.cgi?id=866825) |  |
| CVE-2013-1347 | Microsoft | Internet Explorer | 2022-03-03 | [PoC](http://www.exploit-db.com/exploits/25294) |  |
| CVE-2013-0632 | Adobe | ColdFusion | 2022-03-03 | [PoC](http://www.exploit-db.com/exploits/30210) |  |
| CVE-2012-4681 | Oracle | Java SE | 2022-03-03 | [PoC](http://immunityproducts.blogspot.com/2012/08/java-0day-analysis-cve-2012-4681.html) | 🦠 |
| CVE-2012-1723 | Oracle | Java SE | 2022-03-03 | [PoC](https://github.com/rapid7/metasploit-framework/blob/master/modules/exploits/multi/browser/java_verifier_field_access.rb) | 🦠 |
| CVE-2012-1535 | Adobe | Flash Player | 2022-03-03 | [PoC](https://github.com/rapid7/metasploit-framework/blob/master/modules/exploits/windows/browser/adobe_flash_otf_font.rb) |  |
| CVE-2012-0507 | Oracle | Java SE | 2022-03-03 | [PoC](http://weblog.ikvm.net/PermaLink.aspx?guid=cd48169a-9405-4f63-9087-798c4a1866d3) | 🦠 |
| CVE-2011-3544 | Oracle | Java SE JDK and JRE | 2022-03-03 | [PoC](https://github.com/rapid7/metasploit-framework/blob/master/modules/exploits/multi/browser/java_rhino.rb) |  |
| CVE-2011-0611 | Adobe | Flash Player | 2022-03-03 | [PoC](http://bugix-security.blogspot.com/2011/04/cve-2011-0611-adobe-flash-zero-day.html) |  |
| CVE-2010-3333 | Microsoft | Office | 2022-03-03 | [PoC](https://github.com/rapid7/metasploit-framework/blob/master/modules/exploits/windows/fileformat/ms10_087_rtf_pfragments_bof.rb) |  |
| CVE-2010-0232 | Microsoft | Windows | 2022-03-03 | [PoC](http://lock.cmpxchg8b.com/c0af0967d904cef2ad4db766a00bc6af/KiTrap0D.zip) |  |
| CVE-2010-0188 | Adobe | Reader and Acrobat | 2022-03-03 | [PoC](https://github.com/rapid7/metasploit-framework/blob/master/modules/exploits/windows/fileformat/adobe_libtiff.rb) | 🦠 |
| CVE-2009-3129 | Microsoft | Excel | 2022-03-03 | [PoC](http://www.exploit-db.com/exploits/14706) |  |
| CVE-2008-3431 | Oracle | VirtualBox | 2022-03-03 | [PoC](http://www.coresecurity.com/content/virtualbox-privilege-escalation-vulnerability) |  |
| CVE-2008-2992 | Adobe | Acrobat and Reader | 2022-03-03 | [PoC](http://securityreason.com/securityalert/4549) | 🦠 |
| CVE-2002-0367 | Microsoft | Windows | 2022-03-03 | [PoC](http://www.securityfocus.com/archive/1/262074) |  |
| CVE-2017-8570 | Microsoft | Office | 2022-02-25 | [PoC](https://github.com/ParsingTeam/ppsx-file-generator) |  |
| CVE-2014-6352 | Microsoft | Windows | 2022-02-25 | [PoC](https://github.com/rapid7/metasploit-framework/blob/master/modules/exploits/windows/fileformat/ms14_064_packager_python.rb) |  |
| CVE-2019-0752 | Microsoft | Internet Explorer | 2022-02-15 | [PoC](http://packetstormsecurity.com/files/153078/Microsoft-Internet-Explorer-Windows-10-1809-17763.316-Memory-Corruption.html) | 🦠 |
| CVE-2018-20250 | RARLAB | WinRAR | 2022-02-15 | [PoC](http://packetstormsecurity.com/files/152618/RARLAB-WinRAR-ACE-Format-Input-Validation-Remote-Code-Execution.html) | 🦠 |
| CVE-2018-15982 | Adobe | Flash Player | 2022-02-15 | [PoC](https://www.exploit-db.com/exploits/46051/) | 🦠 |
| CVE-2017-9841 | PHPUnit | PHPUnit | 2022-02-15 | [PoC](https://github.com/Habibullah1101/PHPUnit-GoScan) |  |
| CVE-2014-1761 | Microsoft | Word | 2022-02-15 | [PoC](https://github.com/rapid7/metasploit-framework/blob/master/modules/exploits/windows/fileformat/ms14_017_rtf.rb) |  |
| CVE-2013-3906 | Microsoft | Graphics Component | 2022-02-15 | [PoC](http://blogs.mcafee.com/mcafee-labs/mcafee-labs-detects-zero-day-exploit-targeting-microsoft-office-2) |  |
| CVE-2022-22620 | Apple | iOS, iPadOS, and macOS | 2022-02-11 | [PoC](https://github.com/bb33bb/dkjiayu.github.io) |  |
| CVE-2021-36934 | Microsoft | Windows | 2022-02-10 | [PoC](https///github.com:P1rat3R00t/Why-so-Serious-SAM.git) |  |
| CVE-2017-8464 | Microsoft | Windows | 2022-02-10 | [PoC](https://www.exploit-db.com/exploits/42382/) |  |
| CVE-2017-0263 | Microsoft | Win32k | 2022-02-10 | [PoC](https://www.exploit-db.com/exploits/44478/) |  |
| CVE-2017-0145 | Microsoft | SMBv1 | 2022-02-10 | [PoC](http://packetstormsecurity.com/files/154690/DOUBLEPULSAR-Payload-Execution-Neutralization.html) | 🦠 |
| CVE-2017-0144 | Microsoft | SMBv1 | 2022-02-10 | [PoC](http://packetstormsecurity.com/files/154690/DOUBLEPULSAR-Payload-Execution-Neutralization.html) | 🦠 |
| CVE-2015-2051 | D-Link | DIR-645 Router | 2022-02-10 | [PoC](http://securityadvisories.dlink.com/security/publication.aspx?name=SAP10051) |  |
| CVE-2015-1130 | Apple | OS X | 2022-02-10 | [PoC](http://www.securityfocus.com/bid/73982) |  |
| CVE-2014-4404 | Apple | OS X | 2022-02-10 | [PoC](https://github.com/rapid7/metasploit-framework/blob/master/modules/exploits/osx/local/iokit_keyboard_root.rb) |  |
| CVE-2022-21882 | Microsoft | Win32k | 2022-02-04 | [PoC](https://github.com/rapid7/metasploit-framework/blob/master/modules/exploits/windows/local/cve_2022_21882_win32k.rb) |  |
| CVE-2020-5722 | Grandstream | UCM6200 | 2022-01-28 | [PoC](http://packetstormsecurity.com/files/156876/UCM6202-1.0.18.13-Remote-Command-Injection.html) |  |
| CVE-2020-0787 | Microsoft | Windows | 2022-01-28 | [PoC](http://packetstormsecurity.com/files/158056/Background-Intelligent-Transfer-Service-Privilege-Escalation.html) | 🦠 |
| CVE-2014-1776 | Microsoft | Internet Explorer | 2022-01-28 | [PoC](http://www.signalsec.com/cve-2014-1776-ie-0day-analysis/) |  |
| CVE-2014-7169 | GNU | Bourne-Again Shell (Bash) | 2022-01-28 | [PoC](http://packetstormsecurity.com/files/128517/VMware-Security-Advisory-2014-0010.html) |  |
| CVE-2006-1547 | Apache | Struts 1 | 2022-01-21 | [PoC](http://struts.apache.org/struts-doc-1.2.9/userGuide/release-notes.html) |  |
| CVE-2012-0391 | Apache | Struts 2 | 2022-01-21 | [PoC](http://archives.neohapsis.com/archives/bugtraq/2012-01/0031.html) |  |
| CVE-2018-8453 | Microsoft | Win32k | 2022-01-21 | [PoC](http://packetstormsecurity.com/files/153669/Microsoft-Windows-NtUserSetWindowFNID-Win32k-User-Callback.html) | 🦠 |
| CVE-2019-1458 | Microsoft | Win32k | 2022-01-10 | [PoC](http://packetstormsecurity.com/files/156651/Microsoft-Windows-WizardOpium-Local-Privilege-Escalation.html) | 🦠 |
| CVE-2013-3900 | Microsoft | WinVerifyTrust function | 2022-01-10 | [PoC](https://github.com/oukridrig772/-WinVerifyTrust-Signature-Validation-CVE-2013-3900-Mitigation) |  |
| CVE-2018-13382 | Fortinet | FortiOS and FortiProxy | 2022-01-10 | [PoC](https///github.com:cojoben/CVE-2018-13382.git) | 🦠 |
| CVE-2019-1579 | Palo Alto Networks | PAN-OS | 2022-01-10 | [PoC](https://devco.re/blog/2019/07/17/attacking-ssl-vpn-part-1-PreAuth-RCE-on-Palo-Alto-GlobalProtect-with-Uber-as-case-study/) | 🦠 |
| CVE-2019-10149 | Exim | Mail Transfer Agent (MTA) | 2022-01-10 | [PoC](http://packetstormsecurity.com/files/153218/Exim-4.9.1-Remote-Command-Execution.html) |  |
| CVE-2021-27860 | FatPipe | WARP, IPVPN, and MPVPN so | 2022-01-10 | [PoC](https://www.ic3.gov/Media/News/2021/211117-2.pdf) |  |
| CVE-2021-43890 | Microsoft | Windows | 2021-12-15 | [PoC](https://www.microsoft.com/en-us/security/blog/2023/12/28/financially-motivated-threat-actors-misusing-app-installer/) | 🦠 |
| CVE-2019-13272 | Linux | Kernel | 2021-12-10 | [PoC](http://packetstormsecurity.com/files/154245/Kernel-Live-Patch-Security-Notice-LSN-0054-1.html) |  |
| CVE-2021-44168 | Fortinet | FortiOS | 2021-12-10 | [PoC](https///github.com:0xhaggis/CVE-2021-44168.git) |  |
| CVE-2010-1871 | Red Hat | JBoss Seam 2 | 2021-12-10 | [PoC](https://github.com/rapid7/metasploit-framework/blob/master/modules/exploits/multi/http/jboss_seam_upload_exec.rb) |  |
| CVE-2020-8816 | Pi-hole | AdminLTE | 2021-12-10 | [PoC](https://natedotred.wordpress.com/2020/03/28/cve-2020-8816-pi-hole-remote-code-execution/) |  |
| CVE-2018-14847 | MikroTik | RouterOS | 2021-12-01 | [PoC](https://github.com/BasuCert/WinboxPoC) |  |
| CVE-2021-22204 | Perl | Exiftool | 2021-11-17 | [PoC](http://packetstormsecurity.com/files/162558/ExifTool-DjVu-ANT-Perl-Injection.html) |  |
| CVE-2021-40449 | Microsoft | Windows | 2021-11-17 | [PoC](http://packetstormsecurity.com/files/164926/Win32k-NtGdiResetDC-Use-After-Free-Local-Privilege-Escalation.html) | 🦠 |
| CVE-2021-42321 | Microsoft | Exchange | 2021-11-17 | [PoC](http://packetstormsecurity.com/files/166153/Microsoft-Exchange-Server-Remote-Code-Execution.html) | 🦠 |
| CVE-2021-42292 | Microsoft | Office | 2021-11-17 | [PoC](https://github.com/corelight/CVE-2021-42292) |  |
| CVE-2021-21017 | Adobe | Acrobat and Reader | 2021-11-03 | [PoC](https///github.com:tzwlhack/CVE-2021-21017.git) |  |
| CVE-2018-4878 | Adobe | Flash Player | 2021-11-03 | [PoC](https://securingtomorrow.mcafee.com/mcafee-labs/hackers-bypassed-adobe-flash-protection-mechanism/) | 🦠 |
| CVE-2020-5735 | Amcrest | Cameras and Network Video | 2021-11-03 | [PoC](http://packetstormsecurity.com/files/157164/Amcrest-Dahua-NVR-Camera-IP2M-841-Denial-Of-Service.html) |  |
| CVE-2019-2215 | Android | Android Kernel | 2021-11-03 | [PoC](http://packetstormsecurity.com/files/154911/Android-Binder-Use-After-Free.html) |  |
| CVE-2020-0041 | Android | Android Kernel | 2021-11-03 | [PoC](https://github.com/jcalabres/root-exploit-pixel3) |  |
| CVE-2020-0069 | MediaTek | Multiple Chipsets | 2021-11-03 | [PoC](https///github.com:0xf15h/mtk_su.git) |  |
| CVE-2019-0211 | Apache | HTTP Server | 2021-11-03 | [PoC](http://packetstormsecurity.com/files/152415/Slackware-Security-Advisory-httpd-Updates.html) |  |
| CVE-2021-30858 | Apple | iOS, iPadOS, and macOS | 2021-11-03 | [PoC](https///github.com:Jeromeyoung/ps4_8.00_vuln_poc.git) |  |
| CVE-2021-30860 | Apple | Multiple Products | 2021-11-03 | [PoC](https://github.com/jeffssh/CVE-2021-30860) |  |
| CVE-2020-27930 | Apple | Multiple Products | 2021-11-03 | [PoC](https///github.com:FunPhishing/Apple-Safari-Remote-Code-Execution-CVE-2020-27930.git) |  |
| CVE-2021-30807 | Apple | Multiple Products | 2021-11-03 | [PoC](https///github.com:30440r/gex.git) |  |
| CVE-2020-27950 | Apple | Multiple Products | 2021-11-03 | [PoC](https///github.com:lyonzon2/browser-crash-tool.git) |  |
| CVE-2021-1782 | Apple | Multiple Products | 2021-11-03 | [PoC](https///github.com:synacktiv/CVE-2021-1782.git) |  |
| CVE-2021-30657 | Apple | macOS | 2021-11-03 | [PoC](https://github.com/rapid7/metasploit-framework/blob/master/modules/exploits/osx/browser/osx_gatekeeper_bypass.rb) |  |
| CVE-2021-28663 | Arm | Mali Graphics Processing  | 2021-11-03 | [PoC](https://github.com/lntrx/CVE-2021-28663) |  |
| CVE-2020-3161 | Cisco | Cisco IP Phones | 2021-11-03 | [PoC](http://packetstormsecurity.com/files/157265/Cisco-IP-Phone-11.7-Denial-Of-Service.html) |  |
| CVE-2020-8195 | Citrix | Application Delivery Cont | 2021-11-03 | [PoC](http://packetstormsecurity.com/files/160047/Citrix-ADC-NetScaler-Local-File-Inclusion.html) |  |
| CVE-2020-29557 | D-Link | DIR-825 R1 Devices | 2021-11-03 | [PoC](https://shaqed.github.io/dlink/) |  |
| CVE-2019-15752 | Docker | Desktop Community Edition | 2021-11-03 | [PoC](http://packetstormsecurity.com/files/157404/Docker-Credential-Wincred.exe-Privilege-Escalation.html) |  |
| CVE-2018-6789 | Exim | Exim | 2021-11-03 | [PoC](http://packetstormsecurity.com/files/162959/Exim-base64d-Buffer-Overflow.html) | 🦠 |
| CVE-2020-8655 | EyesOfNetwork | EyesOfNetwork | 2021-11-03 | [PoC](http://packetstormsecurity.com/files/156266/EyesOfNetwork-5.3-Remote-Code-Execution.html) |  |
| CVE-2019-5591 | Fortinet | FortiOS | 2021-11-03 | [PoC](https://github.com/ayewo/fortios-ldap-mitm-poc-CVE-2019-5591) |  |
| CVE-2020-15999 | Google | Chrome FreeType | 2021-11-03 | [PoC](https://crbug.com/1139963) |  |
| CVE-2021-37976 | Google | Chromium | 2021-11-03 | [PoC](https://crbug.com/1251787) |  |
| CVE-2020-16009 | Google | Chromium V8 | 2021-11-03 | [PoC](http://packetstormsecurity.com/files/159974/Chrome-V8-Turbofan-Type-Confusion.html) |  |
| CVE-2021-30632 | Google | Chromium V8 | 2021-11-03 | [PoC](https///github.com:paulsery/CVE-2021-30632.git) |  |
| CVE-2021-21148 | Google | Chromium V8 | 2021-11-03 | [PoC](https://github.com/Grayhaxor/CVE-2021-21148) |  |
| CVE-2021-30551 | Google | Chromium V8 | 2021-11-03 | [PoC](https://crbug.com/1216437) |  |
| CVE-2021-37975 | Google | Chromium V8 | 2021-11-03 | [PoC](https://github.com/ssaroussi/CVE-2021-37975) |  |
| CVE-2020-6418 | Google | Chromium V8 | 2021-11-03 | [PoC](http://packetstormsecurity.com/files/156632/Google-Chrome-80-JSCreate-Side-Effect-Type-Confusion.html) |  |
| CVE-2021-38000 | Google | Chromium Intents | 2021-11-03 | [PoC](https://crbug.com/1249962) |  |
| CVE-2021-38003 | Google | Chromium V8 | 2021-11-03 | [PoC](https://crbug.com/1263462) |  |
| CVE-2021-21224 | Google | Chromium V8 | 2021-11-03 | [PoC](https://crbug.com/1195777) |  |
| CVE-2021-21193 | Google | Chromium Blink | 2021-11-03 | [PoC](https://github.com/mehrzad1994/CVE-2021-21193) |  |
| CVE-2021-21220 | Google | Chromium V8 | 2021-11-03 | [PoC](http://packetstormsecurity.com/files/162437/Google-Chrome-XOR-Typer-Out-Of-Bounds-Access-Remote-Code-Execution.html) |  |
| CVE-2020-4428 | IBM | Data Risk Manager | 2021-11-03 | [PoC](https://github.com/rapid7/metasploit-framework/blob/master/modules/exploits/linux/http/ibm_drm_rce.rb) |  |
| CVE-2016-3715 | ImageMagick | ImageMagick | 2021-11-03 | [PoC](https://www.exploit-db.com/exploits/39767/) |  |
| CVE-2014-1812 | Microsoft | Windows | 2021-11-03 | [PoC](https://github.com/mauricelambert/gpp-encrypt) | 🦠 |
| CVE-2021-31955 | Microsoft | Windows | 2021-11-03 | [PoC](https://github.com/ApexPredator-InfoSec/forti_shield) |  |
| CVE-2021-1647 | Microsoft | Defender | 2021-11-03 | [PoC](https://github.com/findcool/cve-2021-1647) |  |
| CVE-2021-33739 | Microsoft | Windows | 2021-11-03 | [PoC](https///github.com:giwon9977/CVE-2021-33739_PoC_Analysis.git) |  |
| CVE-2020-0683 | Microsoft | Windows | 2021-11-03 | [PoC](https///gitee.com:mirrors_padovah4ck/CVE-2020-0683.git) |  |
| CVE-2020-17087 | Microsoft | Windows | 2021-11-03 | [PoC](https://github.com/raiden757/CVE-2020-17087) |  |
| CVE-2021-31956 | Microsoft | Windows | 2021-11-03 | [PoC](https://github.com/deletehead/Pool-Overflow-CVE-2021-31956) |  |
| CVE-2020-17144 | Microsoft | Exchange Server | 2021-11-03 | [PoC](https///gitee.com:delete_user/CVE-2020-17144-EXP.git) |  |
| CVE-2020-1020 | Microsoft | Windows | 2021-11-03 | [PoC](https///github.com:KaLendsi/CVE-2020-1020.git) |  |
| CVE-2021-34523 | Microsoft | Exchange Server | 2021-11-03 | [PoC](http://packetstormsecurity.com/files/163895/Microsoft-Exchange-ProxyShell-Remote-Code-Execution.html) | 🦠 |
| CVE-2020-0688 | Microsoft | Exchange Server | 2021-11-03 | [PoC](http://packetstormsecurity.com/files/156592/Microsoft-Exchange-2019-15.2.221.12-Remote-Code-Execution.html) | 🦠 |
| CVE-2017-0143 | Microsoft | Windows | 2021-11-03 | [PoC](http://packetstormsecurity.com/files/154690/DOUBLEPULSAR-Payload-Execution-Neutralization.html) | 🦠 |
| CVE-2016-7255 | Microsoft | Win32k | 2021-11-03 | [PoC](http://packetstormsecurity.com/files/140468/Microsoft-Windows-Kernel-win32k.sys-NtSetWindowLongPtr-Privilege-Escalation.html) |  |
| CVE-2019-0708 | Microsoft | Remote Desktop Services | 2021-11-03 | [PoC](http://packetstormsecurity.com/files/153133/Microsoft-Windows-Remote-Desktop-BlueKeep-Denial-Of-Service.html) | 🦠 |
| CVE-2020-1464 | Microsoft | Windows | 2021-11-03 | [PoC](https://medium.com/%40TalBeerySec/glueball-the-story-of-cve-2020-1464-50091a1f98bd) |  |
| CVE-2021-34527 | Microsoft | Windows | 2021-11-03 | [PoC](http://packetstormsecurity.com/files/167261/Print-Spooler-Remote-DLL-Injection.html) | 🦠 |
| CVE-2021-31207 | Microsoft | Exchange Server | 2021-11-03 | [PoC](http://packetstormsecurity.com/files/163895/Microsoft-Exchange-ProxyShell-Remote-Code-Execution.html) | 🦠 |
| CVE-2019-0803 | Microsoft | Win32k | 2021-11-03 | [PoC](https///github.com:Ascotbe/Kernelhub.git) |  |
| CVE-2021-28310 | Microsoft | Win32k | 2021-11-03 | [PoC](https://github.com/Rafael-Svechinskaya/IOC_for_CVE-2021-28310) |  |
| CVE-2020-1350 | Microsoft | Windows | 2021-11-03 | [PoC](https///gitee.com:keyboxdzd/SIGRed_RCE_PoC.git) |  |
| CVE-2021-26411 | Microsoft | Internet Explorer | 2021-11-03 | [PoC](https://github.com/CrackerCat/CVE-2021-26411) | 🦠 |
| CVE-2019-0859 | Microsoft | Win32k | 2021-11-03 | [PoC](https///github.com:Sheisback/CVE-2019-0859-1day-Exploit.git) |  |
| CVE-2021-40444 | Microsoft | MSHTML | 2021-11-03 | [PoC](http://packetstormsecurity.com/files/165214/Microsoft-Office-Word-MSHTML-Remote-Code-Execution.html) | 🦠 |
| CVE-2017-8759 | Microsoft | .NET Framework | 2021-11-03 | [PoC](https://github.com/bhdresh/CVE-2017-8759) |  |
| CVE-2021-36942 | Microsoft | Windows | 2021-11-03 | [PoC](https://www.kb.cert.org/vuls/id/405600) | 🦠 |
| CVE-2019-1215 | Microsoft | Windows | 2021-11-03 | [PoC](https///gitlab.com:gavz/CVE-2019-1215.git) | 🦠 |
| CVE-2018-0798 | Microsoft | Office | 2021-11-03 | [PoC](https://github.com/Sunqiz/CVE-2018-0798-reproduction) |  |
| CVE-2018-0802 | Microsoft | Office | 2021-11-03 | [PoC](https://github.com/rxwx/CVE-2018-0802) |  |
| CVE-2012-0158 | Microsoft | MSCOMCTL.OCX | 2021-11-03 | [PoC](https://github.com/rapid7/metasploit-framework/blob/master/modules/exploits/windows/fileformat/ms12_027_mscomctl_bof.rb) |  |
| CVE-2015-1641 | Microsoft | Office | 2021-11-03 | [PoC](https://github.com/Cyberclues/rtf_exploit_extractor) |  |
| CVE-2019-0541 | Microsoft | MSHTML | 2021-11-03 | [PoC](https://www.exploit-db.com/exploits/46536/) |  |
| CVE-2017-11882 | Microsoft | Office | 2021-11-03 | [PoC](https://github.com/0x09AL/CVE-2017-11882-metasploit) | 🦠 |
| CVE-2020-0674 | Microsoft | Internet Explorer | 2021-11-03 | [PoC](https://github.com/maxpl0it/CVE-2020-0674-Exploit) |  |
| CVE-2019-1367 | Microsoft | Internet Explorer | 2021-11-03 | [PoC](https://github.com/mandarenmanman/CVE-2019-1367) | 🦠 |
| CVE-2017-0199 | Microsoft | Office and WordPad | 2021-11-03 | [PoC](http://rewtin.blogspot.nl/2017/04/cve-2017-0199-practical-exploitation-poc.html) | 🦠 |
| CVE-2019-1429 | Microsoft | Internet Explorer | 2021-11-03 | [PoC](http://packetstormsecurity.com/files/155433/Microsoft-Internet-Explorer-Use-After-Free.html) |  |
| CVE-2017-11774 | Microsoft | Office | 2021-11-03 | [PoC](https://sensepost.com/blog/2017/outlook-home-page-another-ruler-vector/) |  |
| CVE-2020-1472 | Microsoft | Netlogon | 2021-11-03 | [PoC](http://packetstormsecurity.com/files/160127/Zerologon-Netlogon-Privilege-Escalation.html) | 🦠 |
| CVE-2021-27065 | Microsoft | Exchange Server | 2021-11-03 | [PoC](http://packetstormsecurity.com/files/161938/Microsoft-Exchange-ProxyLogon-Remote-Code-Execution.html) | 🦠 |
| CVE-2020-1054 | Microsoft | Win32k | 2021-11-03 | [PoC](http://packetstormsecurity.com/files/160515/Microsoft-Windows-DrawIconEx-Local-Privilege-Escalation.html) |  |
| CVE-2021-1675 | Microsoft | Windows | 2021-11-03 | [PoC](http://packetstormsecurity.com/files/167261/Print-Spooler-Remote-DLL-Injection.html) | 🦠 |
| CVE-2020-0601 | Microsoft | Windows | 2021-11-03 | [PoC](https///github.com:JoelBts/CVE-2020-0601_PoC.git) |  |
| CVE-2019-0808 | Microsoft | Win32k | 2021-11-03 | [PoC](http://packetstormsecurity.com/files/157616/Microsoft-Windows-NtUserMNDragOver-Local-Privilege-Escalation.html) |  |
| CVE-2021-26857 | Microsoft | Exchange Server | 2021-11-03 | [PoC](https///github.com:sirpedrotavares/Proxylogon-exploit.git) | 🦠 |
| CVE-2020-1147 | Microsoft | .NET Framework, SharePoin | 2021-11-03 | [PoC](http://packetstormsecurity.com/files/158694/SharePoint-DataSet-DataTable-Deserialization.html) |  |
| CVE-2016-3235 | Microsoft | Office | 2021-11-03 | [PoC](https://www.securify.nl/advisory/SFY20150804/microsoft_visio_multiple_dll_side_loading_vulnerabilities.html) |  |
| CVE-2021-36955 | Microsoft | Windows | 2021-11-03 | [PoC](https///github.com:JiaJinRong12138/CVE-2021-36955-EXP.git) | 🦠 |
| CVE-2021-38648 | Microsoft | Open Management Infrastru | 2021-11-03 | [PoC](http://packetstormsecurity.com/files/164925/Microsoft-OMI-Management-Interface-Authentication-Bypass.html) |  |
| CVE-2020-6819 | Mozilla | Firefox and Thunderbird | 2021-11-03 | [PoC](https://bugzilla.mozilla.org/show_bug.cgi?id=1620818) |  |
| CVE-2019-17026 | Mozilla | Firefox and Thunderbird | 2021-11-03 | [PoC](http://packetstormsecurity.com/files/162568/Firefox-72-IonMonkey-JIT-Type-Confusion.html) |  |
| CVE-2019-15949 | Nagios | Nagios XI | 2021-11-03 | [PoC](http://packetstormsecurity.com/files/156676/Nagios-XI-Authenticated-Remote-Command-Execution.html) |  |
| CVE-2019-19356 | Netis | WF2419 Devices | 2021-11-03 | [PoC](https://github.com/shadowgatt/CVE-2019-19356) |  |
| CVE-2020-2555 | Oracle | Multiple Products | 2021-11-03 | [PoC](http://packetstormsecurity.com/files/157054/Oracle-Coherence-Fusion-Middleware-Remote-Code-Execution.html) |  |
| CVE-2012-3152 | Oracle | Fusion Middleware | 2021-11-03 | [PoC](http://www.exploit-db.com/exploits/31253) |  |
| CVE-2020-14871 | Oracle | Solaris and Zettabyte Fil | 2021-11-03 | [PoC](http://packetstormsecurity.com/files/160510/Solaris-SunSSH-11.0-x86-libpam-Remote-Root.html) |  |
| CVE-2015-4852 | Oracle | WebLogic Server | 2021-11-03 | [PoC](http://foxglovesecurity.com/2015/11/06/what-do-weblogic-websphere-jboss-jenkins-opennms-and-your-application-have-in-common-this-vulnerability/) |  |
| CVE-2019-18935 | Progress | Telerik UI for ASP.NET AJ | 2021-11-03 | [PoC](https://github.com/noperator/CVE-2019-18935) | 🦠 |
| CVE-2021-22893 | Ivanti | Pulse Connect Secure | 2021-11-03 | [PoC](https://github.com/orangmuda/CVE-2021-22893) | 🦠 |
| CVE-2020-8260 | Ivanti | Pulse Connect Secure | 2021-11-03 | [PoC](http://packetstormsecurity.com/files/160619/Pulse-Secure-VPN-Remote-Code-Execution.html) |  |
| CVE-2019-11539 | Ivanti | Pulse Connect Secure and  | 2021-11-03 | [PoC](https://devco.re/blog/2019/09/02/attacking-ssl-vpn-part-3-the-golden-Pulse-Secure-ssl-vpn-rce-chain-with-Twitter-as-case-study/) | 🦠 |
| CVE-2021-1905 | Qualcomm | Multiple Chipsets | 2021-11-03 | [PoC](https://github.com/TAKIANFIF/CVE-2021-1905-CVE-2021-1906-CVE-2021-28663-CVE-2021-28664) |  |
| CVE-2020-10221 | rConfig | rConfig | 2021-11-03 | [PoC](http://packetstormsecurity.com/files/156687/rConfig-3.93-Authenticated-Remote-Code-Execution.html) |  |
| CVE-2017-16651 | Roundcube | Roundcube Webmail | 2021-11-03 | [PoC](http://packetstormsecurity.com/files/161226/Roundcube-Webmail-1.2-File-Disclosure.html) |  |
| CVE-2020-11652 | SaltStack | Salt | 2021-11-03 | [PoC](http://packetstormsecurity.com/files/157678/SaltStack-Salt-Master-Minion-Unauthenticated-Remote-Code-Execution.html) |  |
| CVE-2020-11651 | SaltStack | Salt | 2021-11-03 | [PoC](http://packetstormsecurity.com/files/157560/Saltstack-3000.1-Remote-Code-Execution.html) |  |
| CVE-2018-2380 | SAP | Customer Relationship Man | 2021-11-03 | [PoC](https://github.com/erpscanteam/CVE-2018-2380) | 🦠 |
| CVE-2016-3976 | SAP | NetWeaver | 2021-11-03 | [PoC](http://packetstormsecurity.com/files/137528/SAP-NetWeaver-AS-JAVA-7.5-Directory-Traversal.html) |  |
| CVE-2019-16256 | SIMalliance | Toolbox Browser | 2021-11-03 | [PoC](https://www.adaptivemobile.com/blog/simjacker-next-generation-spying-over-mobile) |  |
| CVE-2016-3643 | SolarWinds | Virtualization Manager | 2021-11-03 | [PoC](http://packetstormsecurity.com/files/137487/Solarwinds-Virtualization-Manager-6.3.1-Privilege-Escalation.html) |  |
| CVE-2020-12271 | Sophos | SFOS | 2021-11-03 | [PoC](https://news.sophos.com/en-us/2020/04/26/asnarok/) | 🦠 |
| CVE-2020-10181 | Sumavision | Enhanced Multimedia Route | 2021-11-03 | [PoC](http://packetstormsecurity.com/files/156746/Enhanced-Multimedia-Router-3.0.4.27-Cross-Site-Request-Forgery.html) |  |
| CVE-2019-18988 | TeamViewer | Desktop | 2021-11-03 | [PoC](https://whynotsecurity.com/blog/teamviewer/) |  |
| CVE-2017-9248 | Progress | ASP.NET AJAX and Sitefini | 2021-11-03 | [PoC](https://www.exploit-db.com/exploits/43873/) |  |
| CVE-2018-14558 | Tenda | AC7, AC9, and AC10 Router | 2021-11-03 | [PoC](https://github.com/zsjevilhex/iot/blob/master/route/tenda/tenda-01/Tenda.md) |  |
| CVE-2019-9082 | ThinkPHP | ThinkPHP | 2021-11-03 | [PoC](http://packetstormsecurity.com/files/157218/ThinkPHP-5.0.23-Remote-Code-Execution.html) |  |
| CVE-2020-5849 | Unraid | Unraid | 2021-11-03 | [PoC](http://packetstormsecurity.com/files/157275/Unraid-6.8.0-Authentication-Bypass-Arbitrary-Code-Execution.html) |  |
| CVE-2020-3992 | VMware | ESXi | 2021-11-03 | [PoC](https///github.com:ceciliaaii/CVE_2020_3992.git) | 🦠 |
| CVE-2020-3950 | VMware | Multiple Products | 2021-11-03 | [PoC](http://packetstormsecurity.com/files/156843/VMware-Fusion-11.5.2-Privilege-Escalation.html) |  |
| CVE-2019-8394 | Zoho | ManageEngine | 2021-11-03 | [PoC](https://www.exploit-db.com/exploits/46413/) |  |

*Last updated: 2025-12-19*


---
