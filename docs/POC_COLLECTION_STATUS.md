# PoC Data Collection Status

## 🚀 Initial Collection - IN PROGRESS

**Status:** Running (Started: 2025-12-17)
**Progress:** ~155/1478 CVEs processed (10%)
**Estimated Completion:** ~15-20 minutes total
**Log File:** `poc_collection.log`

### Monitor Progress

```bash
# Watch real-time progress
tail -f poc_collection.log

# Count completed CVEs
grep -c '✅' poc_collection.log

# See checkpoint status
grep 'Checkpoint' poc_collection.log
```

## 📊 Expected Output Files

Once collection completes, you'll have:

1. **CISA-POC-List.txt** - Simple list of CVEs with public PoCs
   ```
   CVE-2018-4063
   CVE-2022-37055
   CVE-2025-6218
   ...
   ```

2. **poc-data.json** - Detailed metadata for all CVEs
   ```json
   {
     "CVE-2025-6218": {
       "cve_id": "CVE-2025-6218",
       "is_poc": true,
       "poc_count": 16,
       "epss_score": 0.07167,
       "status": "success"
     }
   }
   ```

## 🔄 Automated Daily Updates

The GitHub Actions workflow will automatically:

### Schedule
- **Runs:** Twice daily on weekdays
- **Times:** 6:00 AM UTC & 3:00 PM UTC
- **File:** `.github/workflows/CISA.yaml`

### What It Does
1. ✅ Fetches latest CISA KEV data
2. ✅ Matches Nuclei templates
3. ✅ **Collects PoC data from ProjectDiscovery API**
4. ✅ Updates statistics with PoC metrics
5. ✅ Generates visualizations
6. ✅ Commits changes to repo
7. ✅ Sends Slack notification with PoC count

### Workflow Configuration

```yaml
- name: Fetch PoC data from ProjectDiscovery API
  run: |
       echo "🔍 Fetching PoC availability data from ProjectDiscovery API..."
       python scripts/fetch_poc_data.py || echo "⚠️  PoC data fetch failed, continuing without PoC data"
```

The workflow includes graceful error handling - if PoC collection fails, the workflow continues without it.

## 💣 PoC Gap Analysis

### What is the PoC Gap?

The "PoC Gap" shows **high-priority CVEs that have public exploits but NO Nuclei templates** for automated scanning.

This identifies:
- ✅ Vulnerabilities actively being exploited (has PoC)
- ❌ Missing automated detection (no Nuclei template)
- 🎯 **Priority opportunities for template development**

### Using the PoC Gap Query

Once data collection completes, run:

```bash
# Show all CVEs with PoC but no Nuclei template
python3 scripts/kev_query.py --poc-gap

# Show with detailed information
python3 scripts/kev_query.py --poc-gap --details
```

### Example Output

```
🔓 Found 234 CVEs with PoC but no Nuclei template (priority testing gap):

❌   💣 CVE-2024-1234 - Microsoft Windows
❌   💣 CVE-2024-5678 - Adobe Flash Player
❌   💣 CVE-2023-9012 - Oracle WebLogic
...
```

**Icon Legend:**
- ❌ = Not scannable (no Nuclei template)
- 💣 = Public PoC available
- 🦠 = Ransomware-associated

### Detailed View

```bash
python3 scripts/kev_query.py --poc-gap --details
```

Shows for each CVE:
- Vulnerability name
- Date added to KEV
- Short description
- CWE classification
- PoC availability status

## 📈 Other Useful Queries

### Show All CVEs with PoCs

```bash
python3 scripts/kev_query.py --poc
```

### Filter by Vendor with PoC Status

```bash
python3 scripts/kev_query.py --vendor Microsoft --details
python3 scripts/kev_query.py --vendor Adobe --poc
```

### Check Specific CVE

```bash
python3 scripts/kev_query.py --cve CVE-2025-54253
```

Output includes:
- Scannable: ✅/❌
- Ransomware: 🦠
- **Public PoC: 💣 Yes/No**

### Statistics with PoC Metrics

```bash
python3 scripts/kev_query.py --stats
```

Shows:
- Total CVEs with public PoCs
- CVEs with PoC + Nuclei template (fully testable)
- **Testing gap (PoC but no template)**

## 📊 Visualizations

Generate comprehensive analytics including PoC coverage:

```bash
python3 scripts/kev_analytics.py
```

Creates: `outputs/graphs/poc_coverage_analysis.png`

Shows:
1. PoC vs Nuclei template distribution
2. Coverage gap breakdown
3. PoC availability by vendor
4. Testing capability distribution

## 🔍 Current Test Results

From initial test (first 10 CVEs):
- **90% had public PoCs** (9 out of 10)
- Average 6.5 PoC sources per CVE
- CVE-2025-6218 had 16 different PoC sources

This suggests **high PoC availability** across the KEV catalog, making gap analysis even more valuable.

## 📝 Next Steps

1. **Wait for collection to complete** (~10 more minutes)
2. **Run PoC gap query** to find priority CVEs:
   ```bash
   python3 scripts/kev_query.py --poc-gap > poc-gaps.txt
   ```
3. **Generate visualizations**:
   ```bash
   python3 scripts/kev_analytics.py
   ```
4. **Update README stats**:
   ```bash
   python3 scripts/generate_stats.py
   ```
5. **Commit and push** to trigger automated workflow

## 🐛 Troubleshooting

### If Collection Gets Interrupted

The script has checkpoint recovery:
```bash
# Just re-run, it will resume from checkpoint
python3 scripts/fetch_poc_data.py
```

### Check Checkpoint Status

```bash
# View checkpoint file
cat poc-checkpoint.json | jq '. | length'
```

### Clean Start

```bash
# Remove old data and start fresh
rm CISA-POC-List.txt poc-data.json poc-checkpoint.json
python3 scripts/fetch_poc_data.py
```

## 📚 Documentation

- [README.md](README.md) - Overview and usage
- [docs/POC_TRACKING.md](docs/POC_TRACKING.md) - Comprehensive guide
- [scripts/README.md](scripts/README.md) - Script documentation

---

**Last Updated:** 2025-12-17
**Collection Status:** In Progress (10% complete)
