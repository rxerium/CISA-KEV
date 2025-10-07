# Scripts Directory

This directory contains all analytics and query tools for the CISA KEV database.

## 📊 Available Scripts

### 1. `kev_analytics.py`
**Purpose**: Comprehensive analytics dashboard with multiple visualizations

**Features**:
- Top 15 vendors by CVE count
- Top 15 vulnerable products
- Monthly and cumulative temporal trends
- Ransomware campaign analysis
- CWE (weakness) distribution
- Scanning coverage by vendor
- Generates 6 high-resolution visualizations
- All outputs saved to `outputs/graphs/`

**Usage**:
```bash
python scripts/kev_analytics.py
# or
make analytics
```

**Outputs**:
- `vendor_analysis.png`
- `product_analysis.png`
- `temporal_trends.png`
- `ransomware_analysis.png`
- `cwe_distribution.png`
- `vendor_coverage.png`

---

### 2. `kev_query.py`
**Purpose**: CLI search and query tool for the KEV database

**Features**:
- Search by vendor, product, or CVE ID
- Filter scannable/unscannable CVEs
- Show recent additions
- Track ransomware-associated CVEs
- Comprehensive statistics
- Detailed or summary output modes

**Usage Examples**:
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
python scripts/kev_query.py --scannable --details

# Show statistics
python scripts/kev_query.py --stats

# Or use Make shortcuts
make stats
make query-vendor VENDOR="Microsoft"
make recent DAYS=30
make ransomware
```

**Icon Legend**:
- ✅ = Scannable with Nuclei
- ❌ = Not scannable
- 🦠 = Associated with ransomware campaigns

---

### 3. `generate_stats.py`
**Purpose**: Generate comprehensive statistics for README.md

**Features**:
- Analyzes entire KEV database
- Calculates vendor/product statistics
- Tracks ransomware associations
- Shows recent activity (last 30 days)
- Generates markdown-formatted output
- CWE distribution analysis

**Usage**:
```bash
python scripts/generate_stats.py
# or
make show-stats

# To update README stats
make update-readme-stats
```

**Output**: Formatted markdown statistics ready for README

---

## 🚀 Quick Commands

```bash
# Generate all visualizations
make all

# Generate comprehensive analytics
make analytics

# Show database statistics
make stats

# Show comprehensive formatted stats
make show-stats

# Update README statistics
make update-readme-stats

# List all generated outputs
make show-outputs

# Clean generated files
make clean
```

## 📦 Dependencies

All scripts require:
- Python 3.7+
- matplotlib
- pandas
- seaborn
- numpy

Install with:
```bash
make setup
# or
pip install -r requirements.txt
```

## 📁 Output Locations

All generated files are saved to organized directories:
- **Graphs**: `outputs/graphs/*.png`
- **Data exports** (future): `outputs/data/`

## 🔧 Configuration

Scripts automatically:
- Create output directories if needed
- Use relative paths from project root
- Save high-resolution (300 DPI) outputs
- Display interactive plots when run

## 💡 Tips

1. **Run from project root**: Always execute from the repository root directory
2. **Use Make**: The Makefile provides convenient shortcuts
3. **Check outputs**: Use `make show-outputs` to see generated files
4. **Virtual environment**: Activate with `source venv/bin/activate`

## 📚 Documentation

For more details, see:
- `docs/QUICKSTART.md` - Quick start guide
- `docs/ORGANIZATION.md` - Project structure and M-o-M analysis details
- `docs/IDEAS.md` - Future enhancement ideas
- Main `README.md` - Complete documentation

## 🐛 Troubleshooting

**Script not found?**
```bash
# Make sure you're in the project root
cd /path/to/CISA-KEV-Scanning-Capabilities
```

**Import errors?**
```bash
# Install dependencies
make setup
```

**No output?**
```bash
# Check if outputs directory exists
ls -la outputs/graphs/
```

---

Happy analyzing! 🎉
