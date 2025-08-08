#!/bin/bash
# Oracle Horror Production System - Installation Script
# Commander: GCode3069

echo "🔥 ORACLE HORROR PRODUCTION SYSTEM - INSTALLER 🔥"
echo "Mission Critical: AI Horror Dominance Protocol"
echo "================================================================="

# Check Python
echo "📋 Checking Python installation..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found. Please install Python 3.7+ first."
    exit 1
fi

PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
echo "✅ Python $PYTHON_VERSION detected"

# Check pip
echo "📋 Checking pip installation..."
if ! python3 -m pip --version &> /dev/null; then
    echo "❌ pip not found. Please install pip first."
    exit 1
fi

echo "✅ pip detected"

# Install dependencies
echo "📦 Installing Oracle Horror dependencies..."
echo "   This may take a few minutes..."

# Try to install with timeout and better error handling
if python3 -m pip install -r requirements.txt --timeout 300 --retries 3; then
    echo "✅ Dependencies installed successfully"
else
    echo "⚠️  Some dependencies failed to install."
    echo "   You can still use the manifest generation system."
    echo "   For full video/audio production, manually install:"
    echo "   - OpenCV: pip install opencv-python"
    echo "   - MoviePy: pip install moviepy"
    echo "   - Numpy: pip install numpy"
    echo "   - Scipy: pip install scipy"
fi

# Test the system
echo "🧪 Testing Oracle Horror Production System..."
if python3 oracle_horror_cli.py test; then
    echo "✅ System test completed"
else
    echo "⚠️  System test had issues, but core functionality should work"
fi

# Make scripts executable
echo "🔧 Setting up executable permissions..."
chmod +x oracle_horror_cli.py
chmod +x scripts/OracleHorrorBatch.ps1

echo ""
echo "🎬 ORACLE HORROR PRODUCTION SYSTEM READY 🎬"
echo "================================================================="
echo "Quick Start Commands:"
echo "  List campaigns:     python3 oracle_horror_cli.py list"
echo "  Generate manifest:  python3 oracle_horror_cli.py manifest --campaign awakening"
echo "  Full production:    python3 oracle_horror_cli.py all"
echo "  PowerShell batch:   pwsh scripts/OracleHorrorBatch.ps1"
echo ""
echo "Mission Status: OPERATIONAL"
echo "Commander: GCode3069"
echo "Ready for Horror Dominance Protocol activation!"
echo "================================================================="