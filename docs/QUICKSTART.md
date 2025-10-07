# CISA KEV Analytics Tools - Quick Start Guide

## 🚀 What's New?

Your CISA KEV repository now has powerful analytics capabilities! Here's what you can do:

## 📋 Available Tools

### 1. **KEV Query Tool** (`kev_query.py`)
   - Search by vendor, product, or CVE ID
   - Filter by scannable/unscannable
   - Find recent additions
   - Track ransomware-associated CVEs
   - Get detailed statistics

### 2. **Trend Visualizer** (`visualize_trends.py`)
   - Track scanning capabilities over time
   - Generate beautiful line graphs
   - Analyze historical growth
   - Calculate coverage trends
   - Shows gap between total KEV and scannable CVEs

### 3. **Comprehensive Analytics** (`kev_analytics.py`)
   - Top vendors and products analysis
   - Temporal trends (monthly/cumulative)
   - Ransomware campaign tracking
   - CWE distribution charts
   - Vendor-specific scanning coverage
   - Generates multiple high-quality visualizations

## 🎯 Creating a Line Graph of Scanning Capabilities Over Time

This is what you asked for! Here's exactly how to do it:

```bash
# Step 1: Setup (one-time only)
./setup.sh

# Step 2: Activate the virtual environment
source venv/bin/activate

# Step 3: Run the trend visualizer
python visualize_trends.py
```

**What you'll get:**
- A comprehensive 3-panel visualization showing:
  1. Total CVEs vs Scannable CVEs over time
  2. Coverage percentage trend
  3. Gap analysis (unscannable CVEs)
- Summary statistics printed to console
- High-resolution PNG saved as `kev_trends.png`

**How it works:**
- Analyzes your git history to extract stats from README.md
- Tracks changes over time
- Creates professional visualizations with matplotlib

## 💡 Interesting Things You Can Do

### Quick Examples:

```bash
# Activate environment first
source venv/bin/activate

# Search for all Microsoft CVEs
python kev_query.py --vendor Microsoft

# Find CVEs added today/this week
python kev_query.py --recent 7

# Show only scannable CVEs with details
python kev_query.py --scannable --details

# Look up a specific CVE
python kev_query.py --cve CVE-2024-12345

# Find all ransomware-related vulnerabilities
python kev_query.py --ransomware

# Get comprehensive statistics
python kev_query.py --stats

# Generate all analytics visualizations
python kev_analytics.py
```

## 📊 Output Files

After running the analytics tools, you'll have:

- `kev_trends.png` - Time series of scanning capabilities
- `vendor_analysis.png` - Top vendors by CVE count
- `product_analysis.png` - Most vulnerable products
- `temporal_trends.png` - Monthly and cumulative additions
- `ransomware_analysis.png` - Ransomware-associated CVEs
- `cwe_distribution.png` - Common weakness types
- `vendor_coverage.png` - Scanning coverage by vendor

All saved in high resolution (300 DPI) for presentations/reports!

## 🎨 Visualization Features

All graphs include:
- ✅ Professional color schemes
- ✅ Clear labels and legends
- ✅ Grid lines for readability
- ✅ High-resolution output
- ✅ Interactive display (zoom, pan)
- ✅ Automatic date formatting

## 🔧 Customization

Want to modify the visualizations? Each script is well-commented and easy to customize:

- **Colors**: Change color schemes in the plot functions
- **Time ranges**: Modify date filters
- **Chart types**: Switch between bar, line, pie charts
- **Data points**: Add/remove metrics
- **Export formats**: Change from PNG to SVG, PDF, etc.

## 📈 Example: Tracking Your Scanning Coverage

To create a line graph specifically for scanning coverage over time:

```python
# This is already built into visualize_trends.py!
# Just run it:
python visualize_trends.py
```

The second panel shows **scanning coverage percentage** as a line graph over time, exactly what you wanted!

## 🎯 Next Steps

Check out `IDEAS.md` for 100+ additional features you could implement, including:

- Interactive web dashboards
- Email/Discord notifications
- Machine learning predictions
- REST API
- Mobile apps
- And much more!

## 💬 Questions?

The tools are designed to be self-explanatory, but if you need help:

```bash
# All tools support --help
python kev_query.py --help
```

## 🎉 Have Fun Exploring!

These tools turn your KEV database into actionable intelligence. Mix and match queries, create custom reports, and track trends over time!

---

**Pro Tip**: Run `kev_analytics.py` after each update to automatically generate a complete analytics snapshot! 📸
