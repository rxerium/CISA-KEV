#!/bin/bash

# Setup script for CISA KEV Analytics tools

echo "🚀 Setting up CISA KEV Analytics environment..."
echo "================================================"

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.7 or higher."
    exit 1
fi

echo "✅ Python 3 found: $(python3 --version)"

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
else
    echo "✅ Virtual environment already exists"
fi

# Activate virtual environment
echo "🔌 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📥 Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo ""
echo "================================================"
echo "✅ Setup complete!"
echo ""
echo "To use the analytics tools:"
echo "  1. Activate the environment: source venv/bin/activate"
echo "  2. Run full analytics: python scripts/kev_analytics.py"
echo "  3. Query the database: python scripts/kev_query.py --stats"
echo "  4. Or use Make: make analytics"
echo "  5. Deactivate when done: deactivate"
echo "================================================"
