# PoC (Proof-of-Concept) Tracking Guide

## Overview

This repository tracks the availability of **public proof-of-concept exploits** for CISA Known Exploitable Vulnerabilities (KEV) using the ProjectDiscovery API. This feature helps security teams prioritize remediation efforts based on the real-world availability of working exploits.

## Table of Contents

- [Why Track PoCs?](#why-track-pocs)
- [Data Collection](#data-collection)
- [Using PoC Data](#using-poc-data)
- [Understanding the Metrics](#understanding-the-metrics)
- [API Details](#api-details)
- [Automation](#automation)
- [Troubleshooting](#troubleshooting)

---

## Why Track PoCs?

The presence of a public proof-of-concept exploit significantly increases the risk of a vulnerability being exploited. By tracking PoC availability:

### Risk Prioritization
- Vulnerabilities with public PoCs are **actively being exploited** in the wild
- Security teams can prioritize patching based on exploit availability
- Helps with risk assessment and resource allocation

### Coverage Gap Analysis
- Identifies CVEs that have PoCs but no Nuclei scanning templates
- Highlights opportunities for community template contributions
- Shows where automated detection capabilities are missing

### Security Posture Assessment
- Understand your exposure to vulnerabilities with working exploits
- Track which vendors have the most exploitable vulnerabilities
- Measure the "exploitability coverage" of your security tooling

---

## Data Collection

### Automatic Collection (CI/CD)

The GitHub Actions workflow automatically collects PoC data daily:

```yaml
# Runs automatically on schedule
- name: Fetch PoC data from ProjectDiscovery API
  run: python scripts/fetch_poc_data.py
```

### Manual Collection

To manually fetch the latest PoC data:

```bash
# From the repository root
python scripts/fetch_poc_data.py
```

This script:
1. Reads all CVEs from `cisa-kev.csv`
2. Queries ProjectDiscovery API for each CVE
3. Collects PoC availability and metadata
4. Generates `CISA-POC-List.txt` and `poc-data.json`
5. Provides progress tracking and statistics

**Runtime:** ~15-20 minutes for all KEV CVEs (rate-limited to avoid API throttling)

### Output Files

**CISA-POC-List.txt**
- Simple text file listing CVEs with public PoCs
- One CVE per line
- Compatible with existing tooling

**poc-data.json**
- Comprehensive JSON data for all CVEs
- Includes metadata like EPSS scores, severity, etc.
- Used by analytics and visualization scripts

---

## Using PoC Data

### Query Tool (kev_query.py)

The query tool now supports PoC filtering:

**Show all CVEs with public PoCs:**
```bash
python scripts/kev_query.py --poc
```

**Show PoC-enabled CVEs with details:**
```bash
python scripts/kev_query.py --poc --details
```

**Find the testing gap (PoC but no Nuclei template):**
```bash
python scripts/kev_query.py --poc-gap
```

**Search by vendor and see PoC status:**
```bash
python scripts/kev_query.py --vendor Adobe --details
```

**Check specific CVE for PoC availability:**
```bash
python scripts/kev_query.py --cve CVE-2025-54253
```

### Icon Legend

When viewing query results:
- ✅ = Scannable with Nuclei template
- ❌ = Not scannable
- 🦠 = Ransomware-associated
- 💣 = **Public PoC available**

### Analytics Dashboard (kev_analytics.py)

Generate comprehensive visualizations including PoC coverage:

```bash
python scripts/kev_analytics.py
```

Creates a new visualization: `poc_coverage_analysis.png` with:
1. **Overall Distribution** - PoC vs Nuclei template coverage
2. **Coverage Gap Analysis** - Breakdown of PoC-only, template-only, both, neither
3. **Vendor Analysis** - PoC availability by top vendors
4. **Testing Capability** - Distribution of testable vs untestable CVEs

### Statistics Generation (generate_stats.py)

Updated statistics now include PoC metrics:

```bash
python scripts/generate_stats.py
```

Output includes:
- Total CVEs with public PoCs
- Percentage of KEV with PoCs
- CVEs with both PoC and Nuclei template
- Priority gap (PoC but no template)

---

## Understanding the Metrics

### PoC Availability Metrics

**is_poc (Boolean)**
- `true` if at least one public PoC exists
- Aggregated from multiple sources
- Updated daily

**poc_count (Integer)**
- Number of distinct PoC sources found
- Higher count = more widely available exploit
- Ranges from 0 to 20+

**EPSS Score (Float 0-1)**
- Exploit Prediction Scoring System score
- Probability of exploitation in next 30 days
- Higher = more likely to be exploited

**Severity (String)**
- `critical`, `high`, `medium`, `low`
- Based on CVSS score
- Helps prioritize remediation

**is_remote (Boolean)**
- `true` if exploitable remotely
- `false` if requires local access
- Remote exploits are higher priority

**is_auth (Boolean)**
- `true` if authentication required
- `false` if no authentication needed
- Unauthenticated exploits are higher risk

### Coverage Metrics

**Coverage Gap**
- CVEs with PoC but no Nuclei template
- These are high-priority for template development
- Represents "blind spots" in automated detection

**Full Coverage**
- CVEs with both PoC and Nuclei template
- Fully testable vulnerabilities
- Ideal state for security validation

**Template-Only**
- CVEs with Nuclei template but no known PoC
- Lower immediate risk
- Still important for proactive detection

---

## API Details

### ProjectDiscovery API

**Endpoint:** `https://api.projectdiscovery.io/v2/vulnerability/{CVE-ID}`

**Example Response:**
```json
{
  "data": {
    "cve_id": "CVE-2025-54253",
    "is_poc": true,
    "poc_count": 11,
    "epss_score": 0.48742,
    "epss_percentile": 0.97638,
    "cvss_score": 10.0,
    "severity": "critical",
    "is_remote": true,
    "is_auth": false,
    "is_template": true,
    "pocs": [
      {
        "url": "https://github.com/...",
        "source": "gh-nomi-sec",
        "added_at": "2025-08-06T10:37:01Z"
      }
    ]
  }
}
```

### Rate Limiting

The fetch script implements:
- 0.5 second delay between requests
- Checkpoint system (saves progress every 50 CVEs)
- Automatic retry with exponential backoff
- Graceful error handling

---

## Automation

### GitHub Actions Integration

The workflow automatically:

1. **Fetches CISA KEV data** from official source
2. **Matches Nuclei templates** from ProjectDiscovery repo
3. **Collects PoC data** via ProjectDiscovery API
4. **Generates statistics** including PoC metrics
5. **Updates README** with latest numbers
6. **Commits changes** back to repository
7. **Sends Slack notification** with PoC counts

### Schedule

Runs twice daily on weekdays:
- 6:00 AM UTC
- 3:00 PM UTC

Manual trigger also available via GitHub Actions UI.

---

## Troubleshooting

### PoC Data Not Available

**Symptom:** Query shows "No PoC data available"

**Solution:**
```bash
# Manually fetch PoC data
python scripts/fetch_poc_data.py

# Verify files were created
ls -lh CISA-POC-List.txt poc-data.json
```

### API Rate Limiting

**Symptom:** Script shows many timeout errors

**Solution:**
- The script has checkpoint recovery
- Just re-run it - it will resume from last checkpoint
- Rate limit is conservative to avoid throttling

### Checkpoint Recovery

**Symptom:** Script interrupted mid-execution

**Solution:**
```bash
# Script automatically creates poc-checkpoint.json
# Re-run and it will resume from where it stopped
python scripts/fetch_poc_data.py
```

### Outdated PoC Data

**Symptom:** PoC data seems stale

**Solution:**
```bash
# Delete old data and fetch fresh
rm CISA-POC-List.txt poc-data.json poc-checkpoint.json
python scripts/fetch_poc_data.py
```

---

## Best Practices

### For Security Teams

1. **Daily Review** - Check new PoC-enabled CVEs daily
2. **Prioritize Gap** - Focus on CVEs with PoC but no template
3. **Combine with EPSS** - Use EPSS scores for risk scoring
4. **Track Vendors** - Monitor which vendors have most PoC-enabled CVEs

### For Template Developers

1. **Target the Gap** - Develop templates for high-priority gap CVEs
2. **Validate with PoCs** - Use public PoCs to test template accuracy
3. **Contribute Upstream** - Submit templates to Nuclei project
4. **Document Sources** - Reference PoCs in template metadata

### For Researchers

1. **Export Data** - Use `poc-data.json` for research analysis
2. **Correlate Metrics** - Analyze PoC count vs EPSS score
3. **Vendor Analysis** - Study vendor exploit patterns
4. **Timeline Analysis** - Track PoC availability over time

---

## Examples

### Example 1: Finding Critical Gaps

```bash
# Find critical CVEs with PoC but no detection template
python scripts/kev_query.py --poc-gap --details | grep "critical"
```

### Example 2: Vendor Exploit Landscape

```bash
# Check Microsoft's PoC coverage
python scripts/kev_query.py --vendor Microsoft --poc --details
```

### Example 3: Recent Exploitable Additions

```bash
# CVEs added in last 7 days with PoCs
python scripts/kev_query.py --recent 7 --details | grep "💣"
```

### Example 4: High-Risk Combinations

```bash
# Ransomware-associated CVEs with public PoCs
python scripts/kev_query.py --ransomware --details | grep "💣"
```

---

## Contributing

Help improve PoC tracking:

1. **Report Issues** - If PoC detection seems incorrect
2. **Suggest Features** - Additional PoC-related metrics
3. **Contribute Templates** - For gap CVEs
4. **Share Analysis** - Interesting findings from the data

---

## Resources

- [ProjectDiscovery API Documentation](https://docs.projectdiscovery.io/)
- [CISA KEV Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
- [Nuclei Templates Repository](https://github.com/projectdiscovery/nuclei-templates)
- [EPSS Calculator](https://www.first.org/epss/)

---

## License

This documentation is part of the CISA-KEV repository and follows the same license.
