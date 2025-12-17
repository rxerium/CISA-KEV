# Changes Summary - PoC Tracking Enhancements

## ✅ Changes Completed

### 1. Weekly PoC Collection Schedule

**Changed:** PoC data collection from daily to **weekly**

**Workflow Schedule:**
```yaml
schedule:
  - cron: '0 6,15 * * 1,2,3,4,5'  # KEV updates: Twice daily on weekdays
  - cron: '0 3 * * 0'              # PoC data: Weekly on Sunday at 3 AM UTC
```

**Why Weekly?**
- PoC availability changes slowly compared to KEV updates
- Reduces API load and execution time
- Still provides timely updates
- Manual trigger available via `workflow_dispatch`

**Location:** `.github/workflows/CISA.yaml:6-7`

---

### 2. Show ALL Gap CVEs (Not Just Top 50)

**Changed:** Priority gap table from 50 CVEs to **ALL gap CVEs**

**Before:**
```
Showing 50 of 800 total gap CVEs
```

**After:**
```
All 800 gap CVEs listed below
```

**Impact:** Complete visibility into all vulnerabilities with PoC but no template

**Location:** `scripts/generate_stats.py:193`

---

### 3. Added PoC Links to Table

**Added:** Clickable PoC links in the gap table

**New Column:** `PoC` with direct links to exploit code

**Table Structure:**
```markdown
| CVE ID | Vendor | Product | Date Added | PoC | Ransomware |
|--------|--------|---------|------------|-----|------------|
| CVE-2025-XXXXX | Microsoft | Windows | 2025-12-15 | [PoC](https://...) | 🦠 |
```

**PoC Link Logic:**
- If PoC URL available → Clickable `[PoC](url)` link
- If no URL but has PoC → Checkmark `✓`
- Links to first available PoC from ProjectDiscovery API

**Locations:**
- `scripts/fetch_poc_data.py:54-56` - Captures PoC URLs
- `scripts/generate_stats.py:206-214` - Generates markdown links

---

### 4. Enhanced PoC Data Collection

**Added:** PoC URL capture to data collection

**New Field:** `poc_url` in poc-data.json

**Example:**
```json
{
  "CVE-2025-6218": {
    "cve_id": "CVE-2025-6218",
    "is_poc": true,
    "poc_count": 16,
    "poc_url": "https://foresiet.com/blog/...",
    "epss_score": 0.07167,
    "severity": "critical"
  }
}
```

**Location:** `scripts/fetch_poc_data.py:54-62`

---

## 📊 Expected Results

### Gap Table Size

Based on current collection (40% complete):
- **PoC Rate:** 60% (359 of 595 CVEs have PoCs)
- **Estimated Total PoCs:** ~890 CVEs
- **Expected Gap Size:** ~750-850 CVEs (assuming 28% scanning coverage)

### Table Format Example

```markdown
### 🔓 Priority Gap: CVEs with Public PoCs but No Nuclei Template

**Total Gap CVEs:** 823 vulnerabilities have public exploits but lack automated detection templates.

**All 823 gap CVEs** listed below (sorted by date added to KEV, most recent first):

| CVE ID | Vendor | Product | Date Added | PoC | Ransomware |
|--------|--------|---------|------------|-----|------------|
| CVE-2025-59718 | Fortinet | Multiple Products | 2025-12-16 | [PoC](https://fortiguard.fortinet.com/...) | |
| CVE-2025-14611 | Gladinet | CentreStack and Triofox | 2025-12-15 | [PoC](https://www.centrestack.com/...) | |
| CVE-2025-43529 | Apple | Multiple Products | 2025-12-15 | [PoC](https://support.apple.com/...) | 🦠 |
...
(823 total rows)
```

---

## 🔄 Workflow Behavior

### Daily Runs (Weekdays)
**Runs:** 6 AM & 3 PM UTC, Mon-Fri
**Actions:**
1. ✅ Fetch CISA KEV data
2. ✅ Match Nuclei templates
3. ❌ Skip PoC collection (uses existing data)
4. ✅ Generate stats with existing PoC data
5. ✅ Update README
6. ✅ Commit changes

**PoC Table:** Uses cached data from last Sunday

---

### Weekly Run (Sunday)
**Runs:** 3 AM UTC, Sunday
**Actions:**
1. ✅ Fetch CISA KEV data
2. ✅ Match Nuclei templates
3. ✅ **Collect fresh PoC data (~15-20 min)**
4. ✅ Generate stats with new PoC data
5. ✅ Update README with ALL gap CVEs
6. ✅ Commit changes

**PoC Table:** Fresh data with updated links

---

### Manual Trigger
**Available:** Via GitHub Actions UI
**Actions:** Same as weekly run (includes PoC collection)
**Use Case:** On-demand PoC data refresh

---

## 📁 Files Modified

### 1. `.github/workflows/CISA.yaml`
- Added weekly schedule for PoC collection
- Conditional PoC fetch (Sundays only or manual)
- Maintained daily KEV updates

### 2. `scripts/fetch_poc_data.py`
- Enhanced to capture PoC URLs
- Saves first available PoC link
- Includes in poc-data.json output

### 3. `scripts/generate_stats.py`
- Removed 50-CVE limit
- Shows ALL gap CVEs
- Added PoC link column
- Links to exploit code when available

---

## 🎯 Usage Examples

### View the Gap Table in README

Once collection completes and stats generate:
```bash
cat README.md | grep -A 1000 "Priority Gap"
```

### Query Specific Gap CVEs

```bash
# All gap CVEs
python3 scripts/kev_query.py --poc-gap

# With details including PoC URLs
python3 scripts/kev_query.py --poc-gap --details

# Filter by vendor
python3 scripts/kev_query.py --vendor Microsoft --poc-gap

# Ransomware-associated gaps only
python3 scripts/kev_query.py --poc-gap --details | grep "🦠"
```

### Access PoC URLs Programmatically

```bash
# Get PoC URL for specific CVE
cat poc-data.json | jq '.["CVE-2025-6218"].poc_url'

# List all CVEs with PoC URLs
cat poc-data.json | jq -r 'to_entries[] | select(.value.poc_url != "") | "\(.key): \(.value.poc_url)"'

# Count CVEs with PoC links
cat poc-data.json | jq -r '[.[] | select(.poc_url != "")] | length'
```

---

## 📈 Benefits

### 1. Complete Visibility
- **Before:** Only saw 50 of 800+ gap CVEs
- **After:** See ALL gap CVEs in one table

### 2. Direct Access to Exploits
- **Before:** Had to manually search for PoC code
- **After:** One-click access to exploit code

### 3. Optimized Workflow
- **Before:** Daily PoC collection (slow, unnecessary)
- **After:** Weekly updates (efficient, sufficient)

### 4. Better Prioritization
- See entire landscape of exploitable vulnerabilities
- Click through to understand exploit mechanics
- Focus template development on highest-impact gaps

---

## 🔍 Current Status

**PoC Collection Progress:** 595/1478 (40%)
**PoCs Found:** 359 CVEs
**PoC Rate:** 60% of scanned CVEs
**ETA:** ~8 more minutes

**Next Steps:**
1. ✅ Wait for collection to complete
2. ✅ Run `python3 scripts/generate_stats.py`
3. ✅ Review full gap table in README
4. ✅ Commit and push changes
5. ✅ Weekly automation handles updates

---

## 🎓 Key Points

1. **Weekly PoC Updates:** Runs every Sunday at 3 AM UTC
2. **ALL Gap CVEs:** No more 50-item limit
3. **PoC Links:** Direct access to exploit code
4. **Efficient:** Daily updates use cached PoC data
5. **Manual Trigger:** Available for on-demand updates

---

**Last Updated:** 2025-12-17
**Collection Status:** 595/1478 (40%) - In Progress
**Changes Status:** Complete ✅
