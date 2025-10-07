#!/usr/bin/env python3
"""
CISA KEV Scanning Capabilities Trend Visualizer

This script analyzes the git history to track:
- Total CVEs in KEV over time
- Scanning capabilities over time
- Coverage percentage over time
"""

import subprocess
import re
from datetime import datetime
from collections import defaultdict
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from pathlib import Path

def get_git_commits():
    """Get all commits that modified README.md with their dates."""
    try:
        result = subprocess.run(
            ['git', 'log', '--pretty=format:%H|%ci', '--', 'README.md'],
            capture_output=True,
            text=True,
            check=True
        )
        commits = []
        for line in result.stdout.strip().split('\n'):
            if '|' in line:
                commit_hash, date_str = line.split('|', 1)
                # Parse date: "2025-10-07 10:30:45 +0000"
                date = datetime.strptime(date_str[:19], '%Y-%m-%d %H:%M:%S')
                commits.append((commit_hash, date))
        return commits
    except subprocess.CalledProcessError as e:
        print(f"Error getting git commits: {e}")
        return []

def extract_stats_from_readme(commit_hash):
    """Extract stats from README.md at a specific commit."""
    try:
        result = subprocess.run(
            ['git', 'show', f'{commit_hash}:README.md'],
            capture_output=True,
            text=True,
            check=True
        )
        content = result.stdout
        
        # Extract Total CVEs
        total_match = re.search(r'\*\*Total CVEs in the KEV\*\*:\s*(\d+)', content)
        # Extract Scanning capabilities
        scanning_match = re.search(r'\*\*Scanning capabilities\*\*:\s*(\d+)', content)
        
        if total_match and scanning_match:
            total = int(total_match.group(1))
            scanning = int(scanning_match.group(1))
            percentage = (scanning / total * 100) if total > 0 else 0
            return {
                'total': total,
                'scanning': scanning,
                'percentage': percentage
            }
    except (subprocess.CalledProcessError, AttributeError) as e:
        pass
    
    return None

def collect_historical_data():
    """Collect all historical data points from git history."""
    commits = get_git_commits()
    print(f"Found {len(commits)} commits that modified README.md")
    
    data_points = []
    prev_stats = None
    
    for commit_hash, date in reversed(commits):  # Process oldest to newest
        stats = extract_stats_from_readme(commit_hash)
        if stats and stats != prev_stats:  # Only include if stats changed
            data_points.append({
                'date': date,
                'total': stats['total'],
                'scanning': stats['scanning'],
                'percentage': stats['percentage']
            })
            prev_stats = stats
            print(f"  {date.strftime('%Y-%m-%d')}: Total={stats['total']}, Scanning={stats['scanning']} ({stats['percentage']:.1f}%)")
    
    return data_points

def plot_trends(data_points):
    """Create a comprehensive visualization of the trends."""
    if not data_points:
        print("No data points found to plot.")
        return
    
    dates = [dp['date'] for dp in data_points]
    totals = [dp['total'] for dp in data_points]
    scanning = [dp['scanning'] for dp in data_points]
    percentages = [dp['percentage'] for dp in data_points]
    
    # Create figure with 3 subplots
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(14, 12))
    fig.suptitle('CISA KEV Scanning Capabilities Over Time', fontsize=16, fontweight='bold')
    
    # Plot 1: Total CVEs and Scanning Capabilities
    ax1.plot(dates, totals, marker='o', linewidth=2, color='#e74c3c', label='Total CVEs in KEV', markersize=5)
    ax1.plot(dates, scanning, marker='s', linewidth=2, color='#27ae60', label='Scanning Capabilities', markersize=5)
    ax1.fill_between(dates, totals, alpha=0.1, color='#e74c3c')
    ax1.fill_between(dates, scanning, alpha=0.1, color='#27ae60')
    ax1.set_ylabel('Number of CVEs', fontsize=12, fontweight='bold')
    ax1.set_title('Total CVEs vs Scannable CVEs', fontsize=13, pad=10)
    ax1.legend(loc='upper left', fontsize=10)
    ax1.grid(True, alpha=0.3, linestyle='--')
    ax1.set_axisbelow(True)
    
    # Plot 2: Coverage Percentage
    ax2.plot(dates, percentages, marker='D', linewidth=2.5, color='#3498db', label='Coverage %', markersize=5)
    ax2.fill_between(dates, percentages, alpha=0.2, color='#3498db')
    ax2.set_ylabel('Coverage (%)', fontsize=12, fontweight='bold')
    ax2.set_title('Scanning Coverage Percentage', fontsize=13, pad=10)
    ax2.legend(loc='upper left', fontsize=10)
    ax2.grid(True, alpha=0.3, linestyle='--')
    ax2.set_axisbelow(True)
    ax2.axhline(y=25, color='orange', linestyle='--', alpha=0.5, label='25% threshold')
    
    # Plot 3: Gap Analysis (Unscannable CVEs)
    gap = [t - s for t, s in zip(totals, scanning)]
    ax3.fill_between(dates, gap, alpha=0.3, color='#e67e22', label='Unscannable CVEs')
    ax3.plot(dates, gap, marker='v', linewidth=2, color='#d35400', markersize=5)
    ax3.set_ylabel('Number of CVEs', fontsize=12, fontweight='bold')
    ax3.set_xlabel('Date', fontsize=12, fontweight='bold')
    ax3.set_title('Gap: CVEs Without Scanning Capabilities', fontsize=13, pad=10)
    ax3.legend(loc='upper left', fontsize=10)
    ax3.grid(True, alpha=0.3, linestyle='--')
    ax3.set_axisbelow(True)
    
    # Format x-axis for all plots
    for ax in [ax1, ax2, ax3]:
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        ax.xaxis.set_major_locator(mdates.AutoDateLocator())
        plt.setp(ax.xaxis.get_majorticklabels(), rotation=45, ha='right')
    
    plt.tight_layout()
    
    # Save the plot
    output_path = Path('outputs/graphs/kev_trends.png')
    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"\n✅ Graph saved as: {output_path.absolute()}")
    
    # Show the plot
    plt.show()

def generate_summary_stats(data_points):
    """Generate summary statistics."""
    if len(data_points) < 2:
        print("Not enough data points for analysis.")
        return
    
    first = data_points[0]
    last = data_points[-1]
    
    print("\n" + "="*60)
    print("📊 SUMMARY STATISTICS")
    print("="*60)
    print(f"First recorded: {first['date'].strftime('%Y-%m-%d')}")
    print(f"  Total CVEs: {first['total']}")
    print(f"  Scannable: {first['scanning']} ({first['percentage']:.1f}%)")
    print()
    print(f"Latest update: {last['date'].strftime('%Y-%m-%d')}")
    print(f"  Total CVEs: {last['total']}")
    print(f"  Scannable: {last['scanning']} ({last['percentage']:.1f}%)")
    print()
    print(f"📈 Growth:")
    print(f"  Total CVEs increased by: {last['total'] - first['total']} (+{((last['total'] - first['total']) / first['total'] * 100):.1f}%)")
    print(f"  Scannable CVEs increased by: {last['scanning'] - first['scanning']} (+{((last['scanning'] - first['scanning']) / first['scanning'] * 100):.1f}%)")
    print(f"  Coverage change: {last['percentage'] - first['percentage']:.2f} percentage points")
    print("="*60)

def main():
    print("🔍 Analyzing CISA KEV Scanning Capabilities Trends...")
    print("="*60)
    
    # Check if we're in a git repository
    if not Path('.git').exists():
        print("❌ Error: Not in a git repository!")
        return
    
    # Collect historical data
    data_points = collect_historical_data()
    
    if not data_points:
        print("\n❌ No historical data found in git commits.")
        print("💡 Make sure you have commits with stats in README.md")
        return
    
    print(f"\n✅ Collected {len(data_points)} unique data points")
    
    # Generate summary statistics
    generate_summary_stats(data_points)
    
    # Create visualizations
    print("\n📊 Generating visualizations...")
    plot_trends(data_points)

if __name__ == '__main__':
    main()
