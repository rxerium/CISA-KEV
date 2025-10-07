#!/usr/bin/env python3
"""
CISA KEV Analytics Dashboard

Comprehensive analytics for the CISA KEV database including:
- Vendor/Product analysis
- CWE distribution
- Temporal analysis
- Ransomware campaign tracking
"""

import csv
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter, defaultdict
from datetime import datetime
import numpy as np
from pathlib import Path

# Set style for better-looking plots
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (14, 10)

def load_kev_data(csv_path='cisa-kev.csv'):
    """Load the CISA KEV CSV file."""
    try:
        df = pd.read_csv(csv_path)
        df['dateAdded'] = pd.to_datetime(df['dateAdded'])
        print(f"✅ Loaded {len(df)} CVEs from CISA KEV")
        return df
    except Exception as e:
        print(f"❌ Error loading CSV: {e}")
        return None

def load_scannable_list(txt_path='CISA-Scannable-List.txt'):
    """Load the list of scannable CVEs."""
    try:
        with open(txt_path, 'r') as f:
            scannable = set(line.strip() for line in f if line.strip())
        print(f"✅ Loaded {len(scannable)} scannable CVEs")
        return scannable
    except Exception as e:
        print(f"❌ Error loading scannable list: {e}")
        return set()

def analyze_top_vendors(df, top_n=15):
    """Analyze top vendors by vulnerability count."""
    vendor_counts = df['vendorProject'].value_counts().head(top_n)
    
    plt.figure(figsize=(12, 8))
    colors = plt.cm.RdYlGn_r(np.linspace(0.3, 0.7, len(vendor_counts)))
    bars = plt.barh(vendor_counts.index, vendor_counts.values, color=colors)
    plt.xlabel('Number of CVEs', fontsize=12, fontweight='bold')
    plt.ylabel('Vendor/Project', fontsize=12, fontweight='bold')
    plt.title(f'Top {top_n} Vendors/Projects in CISA KEV', fontsize=14, fontweight='bold', pad=20)
    plt.gca().invert_yaxis()
    
    # Add value labels
    for i, (bar, value) in enumerate(zip(bars, vendor_counts.values)):
        plt.text(value + 1, i, str(value), va='center', fontsize=10, fontweight='bold')
    
    plt.tight_layout()
    output_path = Path('outputs/graphs/vendor_analysis.png')
    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"💾 Saved: {output_path}")
    plt.show()
    
    return vendor_counts

def analyze_products(df, top_n=15):
    """Analyze top products by vulnerability count."""
    product_counts = df['product'].value_counts().head(top_n)
    
    plt.figure(figsize=(12, 8))
    colors = plt.cm.Spectral(np.linspace(0.2, 0.8, len(product_counts)))
    bars = plt.barh(product_counts.index, product_counts.values, color=colors)
    plt.xlabel('Number of CVEs', fontsize=12, fontweight='bold')
    plt.ylabel('Product', fontsize=12, fontweight='bold')
    plt.title(f'Top {top_n} Products in CISA KEV', fontsize=14, fontweight='bold', pad=20)
    plt.gca().invert_yaxis()
    
    # Add value labels
    for i, (bar, value) in enumerate(zip(bars, product_counts.values)):
        plt.text(value + 0.5, i, str(value), va='center', fontsize=10, fontweight='bold')
    
    plt.tight_layout()
    output_path = Path('outputs/graphs/product_analysis.png')
    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"💾 Saved: {output_path}")
    plt.show()
    
    return product_counts

def analyze_temporal_trends(df):
    """Analyze when CVEs were added over time."""
    # Group by month
    df['yearMonth'] = df['dateAdded'].dt.to_period('M')
    monthly_counts = df.groupby('yearMonth').size()
    
    # Convert to datetime for plotting
    dates = [period.to_timestamp() for period in monthly_counts.index]
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10))
    
    # Monthly additions
    ax1.plot(dates, monthly_counts.values, marker='o', linewidth=2, color='#3498db', markersize=4)
    ax1.fill_between(dates, monthly_counts.values, alpha=0.3, color='#3498db')
    ax1.set_ylabel('CVEs Added', fontsize=12, fontweight='bold')
    ax1.set_title('Monthly KEV Additions', fontsize=13, fontweight='bold', pad=10)
    ax1.grid(True, alpha=0.3)
    
    # Cumulative
    cumulative = monthly_counts.cumsum()
    ax2.plot(dates, cumulative.values, marker='s', linewidth=2.5, color='#e74c3c', markersize=4)
    ax2.fill_between(dates, cumulative.values, alpha=0.2, color='#e74c3c')
    ax2.set_ylabel('Cumulative CVEs', fontsize=12, fontweight='bold')
    ax2.set_xlabel('Date', fontsize=12, fontweight='bold')
    ax2.set_title('Cumulative KEV Growth', fontsize=13, fontweight='bold', pad=10)
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    output_path = Path('outputs/graphs/temporal_trends.png')
    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"💾 Saved: {output_path}")
    plt.show()

def analyze_ransomware(df):
    """Analyze CVEs associated with ransomware campaigns."""
    ransomware = df[df['knownRansomwareCampaignUse'] == 'Known']
    
    print("\n" + "="*60)
    print("🦠 RANSOMWARE-ASSOCIATED CVEs")
    print("="*60)
    print(f"Total CVEs with known ransomware use: {len(ransomware)}")
    print(f"Percentage of KEV: {len(ransomware)/len(df)*100:.1f}%")
    
    if len(ransomware) > 0:
        print("\nTop vendors affected by ransomware campaigns:")
        for vendor, count in ransomware['vendorProject'].value_counts().head(10).items():
            print(f"  • {vendor}: {count} CVEs")
    
    # Create visualization
    if len(ransomware) > 0:
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
        
        # Ransomware vs Non-Ransomware
        categories = ['Ransomware\nAssociated', 'Not Ransomware\nAssociated']
        counts = [len(ransomware), len(df) - len(ransomware)]
        colors = ['#e74c3c', '#95a5a6']
        
        ax1.pie(counts, labels=categories, autopct='%1.1f%%', startangle=90, colors=colors,
                textprops={'fontsize': 11, 'fontweight': 'bold'})
        ax1.set_title('Ransomware Campaign Association', fontsize=13, fontweight='bold', pad=15)
        
        # Top vendors with ransomware CVEs
        top_ransomware_vendors = ransomware['vendorProject'].value_counts().head(10)
        colors_bar = plt.cm.Reds(np.linspace(0.4, 0.8, len(top_ransomware_vendors)))
        ax2.barh(top_ransomware_vendors.index, top_ransomware_vendors.values, color=colors_bar)
        ax2.set_xlabel('Number of CVEs', fontsize=11, fontweight='bold')
        ax2.set_title('Top 10 Vendors (Ransomware CVEs)', fontsize=13, fontweight='bold', pad=15)
        ax2.invert_yaxis()
        
        plt.tight_layout()
        output_path = Path('outputs/graphs/ransomware_analysis.png')
        output_path.parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        print(f"💾 Saved: {output_path}")
        plt.show()

def analyze_cwe_distribution(df):
    """Analyze CWE (Common Weakness Enumeration) distribution."""
    # Parse CWEs (some entries have multiple CWEs)
    all_cwes = []
    for cwes in df['cwes'].dropna():
        if isinstance(cwes, str):
            all_cwes.extend([cwe.strip() for cwe in cwes.split(',')])
    
    cwe_counts = Counter(all_cwes).most_common(15)
    
    if cwe_counts:
        cwes, counts = zip(*cwe_counts)
        
        plt.figure(figsize=(12, 8))
        colors = plt.cm.viridis(np.linspace(0.2, 0.8, len(cwes)))
        bars = plt.barh(cwes, counts, color=colors)
        plt.xlabel('Number of CVEs', fontsize=12, fontweight='bold')
        plt.ylabel('CWE', fontsize=12, fontweight='bold')
        plt.title('Top 15 CWEs in CISA KEV', fontsize=14, fontweight='bold', pad=20)
        plt.gca().invert_yaxis()
        
        # Add value labels
        for i, (bar, value) in enumerate(zip(bars, counts)):
            plt.text(value + 0.5, i, str(value), va='center', fontsize=10, fontweight='bold')
        
        plt.tight_layout()
        output_path = Path('outputs/graphs/cwe_distribution.png')
        output_path.parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        print(f"💾 Saved: {output_path}")
        plt.show()

def analyze_scanning_coverage(df, scannable_set):
    """Analyze scanning coverage by vendor."""
    df['is_scannable'] = df['cveID'].isin(scannable_set)
    
    # Coverage by top vendors
    top_vendors = df['vendorProject'].value_counts().head(15).index
    vendor_coverage = []
    
    for vendor in top_vendors:
        vendor_df = df[df['vendorProject'] == vendor]
        total = len(vendor_df)
        scannable = vendor_df['is_scannable'].sum()
        percentage = (scannable / total * 100) if total > 0 else 0
        vendor_coverage.append({
            'vendor': vendor,
            'total': total,
            'scannable': scannable,
            'percentage': percentage
        })
    
    # Sort by percentage
    vendor_coverage.sort(key=lambda x: x['percentage'], reverse=True)
    
    # Create visualization
    fig, ax = plt.subplots(figsize=(12, 8))
    
    vendors = [vc['vendor'] for vc in vendor_coverage]
    percentages = [vc['percentage'] for vc in vendor_coverage]
    
    # Color code: green for high coverage, red for low
    colors = plt.cm.RdYlGn(np.array(percentages) / 100)
    bars = ax.barh(vendors, percentages, color=colors)
    
    ax.set_xlabel('Scanning Coverage (%)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Vendor/Project', fontsize=12, fontweight='bold')
    ax.set_title('Scanning Coverage by Top Vendors', fontsize=14, fontweight='bold', pad=20)
    ax.invert_yaxis()
    ax.set_xlim(0, 100)
    
    # Add percentage labels
    for i, (bar, vc) in enumerate(zip(bars, vendor_coverage)):
        label = f"{vc['percentage']:.1f}% ({vc['scannable']}/{vc['total']})"
        ax.text(vc['percentage'] + 2, i, label, va='center', fontsize=9, fontweight='bold')
    
    plt.tight_layout()
    output_path = Path('outputs/graphs/vendor_coverage.png')
    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"💾 Saved: {output_path}")
    plt.show()
    
    print("\n" + "="*60)
    print("📊 SCANNING COVERAGE BY VENDOR")
    print("="*60)
    for vc in vendor_coverage:
        print(f"{vc['vendor']}: {vc['percentage']:.1f}% ({vc['scannable']}/{vc['total']})")

def generate_comprehensive_report(df, scannable_set):
    """Generate a comprehensive text report."""
    print("\n" + "="*70)
    print("📋 COMPREHENSIVE CISA KEV ANALYTICS REPORT")
    print("="*70)
    
    print(f"\n📊 OVERALL STATISTICS:")
    print(f"  Total CVEs in KEV: {len(df)}")
    print(f"  Scannable CVEs: {len(scannable_set)}")
    print(f"  Coverage: {len(scannable_set)/len(df)*100:.2f}%")
    print(f"  Unscannable CVEs: {len(df) - len(scannable_set)}")
    
    print(f"\n📅 TEMPORAL INFORMATION:")
    print(f"  Earliest CVE added: {df['dateAdded'].min().strftime('%Y-%m-%d')}")
    print(f"  Latest CVE added: {df['dateAdded'].max().strftime('%Y-%m-%d')}")
    print(f"  Date range: {(df['dateAdded'].max() - df['dateAdded'].min()).days} days")
    
    print(f"\n🏢 VENDOR STATISTICS:")
    print(f"  Unique vendors: {df['vendorProject'].nunique()}")
    print(f"  Unique products: {df['product'].nunique()}")
    
    ransomware_count = len(df[df['knownRansomwareCampaignUse'] == 'Known'])
    print(f"\n🦠 RANSOMWARE STATISTICS:")
    print(f"  CVEs with known ransomware use: {ransomware_count} ({ransomware_count/len(df)*100:.1f}%)")
    
    cwes_with_data = df['cwes'].notna().sum()
    print(f"\n🔍 CWE COVERAGE:")
    print(f"  CVEs with CWE data: {cwes_with_data} ({cwes_with_data/len(df)*100:.1f}%)")
    
    print("="*70)

def main():
    print("🚀 CISA KEV Analytics Dashboard")
    print("="*70)
    
    # Load data
    df = load_kev_data()
    if df is None:
        return
    
    scannable_set = load_scannable_list()
    
    # Generate comprehensive report
    generate_comprehensive_report(df, scannable_set)
    
    print("\n📊 Generating analytics visualizations...")
    print("="*70)
    
    # Run all analyses
    print("\n1️⃣  Analyzing top vendors...")
    analyze_top_vendors(df)
    
    print("\n2️⃣  Analyzing top products...")
    analyze_products(df)
    
    print("\n3️⃣  Analyzing temporal trends...")
    analyze_temporal_trends(df)
    
    print("\n4️⃣  Analyzing ransomware associations...")
    analyze_ransomware(df)
    
    print("\n5️⃣  Analyzing CWE distribution...")
    analyze_cwe_distribution(df)
    
    print("\n6️⃣  Analyzing scanning coverage by vendor...")
    analyze_scanning_coverage(df, scannable_set)
    
    print("\n" + "="*70)
    print("✅ Analysis complete! All visualizations have been saved.")
    print("="*70)

if __name__ == '__main__':
    main()
