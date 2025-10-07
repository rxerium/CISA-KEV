# CISA-KEV Scanning Capabilities

[![CISA KEV](https://github.com/rxerium/CISA-KEV/actions/workflows/CISA.yaml/badge.svg)](https://github.com/rxerium/CISA-KEV/actions/workflows/CISA.yaml)

A repository that automatically tracks and cross-references CISA's Known Exploitable Vulnerabilities (KEV) list with available Nuclei templates for vulnerability scanning.

## Stats

- **Total CVEs in the KEV**: 1434
- **Scanning capabilities**: 361

## Overview

This project maintains an up-to-date copy of CISA's KEV catalog and identifies which vulnerabilities can be scanned using [Project Discovery's Nuclei](https://github.com/projectdiscovery/nuclei-templates) templates.

## Features

- **Automated Updates**: Runs twice daily (6 AM and 3 PM UTC) on weekdays to fetch the latest CISA KEV data
- **Nuclei Template Matching**: Cross-references CISA KEV entries with available Nuclei scanning templates
- **Slack Notifications**: Sends alerts when new vulnerabilities are added to the KEV list
- **Scannable CVE List**: Generates `CISA-Scannable-List.txt` containing KEV entries that have corresponding Nuclei templates

## Files

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

## Contact

If you have any questions feel free to reach out to me on [Signal](https://signal.me/#eu/0Qd68U1ivXNdWCF4hf70UYFo7tB0w-GQqFpYcyV6-yr4exn2SclB6bFeP7wTAxQw) or via email: rishi@rxerium.com.
