# ChimeraV2-Factory – Operation Viral Dominance

[![Arsenal Status](https://img.shields.io/badge/Arsenal-FULLY_DEPLOYED-red.svg)](https://github.com/GCode3069/ChimeraV2-Factory)
[![Mission Status](https://img.shields.io/badge/Mission-VIRAL_DOMINANCE-gold.svg)](https://github.com/GCode3069/ChimeraV2-Factory)
[![Protocol](https://img.shields.io/badge/Protocol-CHIMERA_V2-green.svg)](https://github.com/GCode3069/ChimeraV2-Factory)

**Commander**: GCode3069  
**Mission**: Complete AI video content pipeline for viral shorts production  
**Status**: ALL SYSTEMS NOMINAL - FORGE IS LIT

## 🏭 Architecture Overview

The ChimeraV2-Factory is a complete automated video production arsenal designed for rapid viral content generation. The system employs a modular weapon architecture with PowerShell orchestration and Python execution cores.

### 🔧 Weapon System Specifications

```
ChimeraV2-Factory/
├── PhoenixProtocol.ps1              # Archives old factory, forges Chimera_v2
├── ForgeProtocol.ps1                # Enhanced weapon deployment system
├── Launch.ps1                       # Red Button orchestrator
├── Scripts/
│   ├── MasterControl.py             # Cinematic manifest generator (The Brain)
│   ├── GenerateClips.py             # FFmpeg placeholder clip generator
│   └── RenderVideo.py               # Video stitcher and encoder (TEMP_FOLDER FIXED)
├── Output/                          # Final .mp4s output destination
├── Temp/Clips/                      # Temporary FFmpeg processing
├── .gitignore                       # Excludes Output/, Temp/, *.pyc, etc.
└── docs/
    └── pipeline_overview.md         # Technical walkthrough, future API hooks
```

## 🚀 Usage Instructions

### Quick Deployment (Red Button)
```powershell
# Execute complete arsenal deployment
.\Launch.ps1

# Custom parameters
.\Launch.ps1 -Title "MyViralContent" -Duration 30 -Clips 5
```

### Manual Deployment Sequence
```powershell
# Phase 1: Initialize factory structure
.\PhoenixProtocol.ps1

# Phase 2: Deploy weapon systems
.\ForgeProtocol.ps1

# Phase 3: Execute production pipeline
.\Launch.ps1
```

### Advanced Operations
```powershell
# Skip clip generation (use existing clips)
.\Launch.ps1 -SkipGeneration

# Verbose logging
.\Launch.ps1 -Verbose

# Custom font path
$env:CHIMERA_FONT_PATH = "C:\Fonts\MyCustomFont.ttf"
.\Launch.ps1
```

## 🔥 Forge Protocol Execution Report

```
### 🔥 Forge Protocol Execution Report  

[*] INITIATING THE FORGE PROTOCOL...

[PHASE 1] Forging all essential weapons systems...
[✓] The Brain (MasterControl.py) forged.
[✓] The Clip Generator (GenerateClips.py) forged.
[✓] The Assembly Line (RenderVideo.py) forged.
[✓] The Red Button (Launch.ps1) forged.

[✓] FORGE PROTOCOL CONCLUDED. ALL WEAPONS ARE IN THE ARSENAL.
```

## 📋 Requirements

### Core Dependencies
- **Python 3.8+** - Arsenal brain and execution cores
- **PowerShell 5.0+** - Orchestration and deployment systems
- **FFmpeg** - Video processing and rendering engine

### Installation Commands
```bash
# Windows (PowerShell)
winget install Python.Python.3
winget install FFmpeg

# Verify installations
python --version
ffmpeg -version
```

## ⚠️ Critical System Patches Applied

### 1. Path Correction in RenderVideo.py
- **Issue**: Undefined `TEMP_FOLDER` variable causing rendering failures
- **Fix**: Proper path reference using `MANIFEST_FOLDER` resolution
- **Impact**: Eliminates concatenation errors and ensures reliable video output

### 2. Robust Folder Creation in ForgeProtocol.ps1
- **Enhancement**: Directory existence validation with creation confirmation
- **Features**: Comprehensive error handling and status reporting
- **Benefit**: Prevents deployment failures due to missing directories

### 3. FFmpeg Presence Check with Installation Guidance
- **Validation**: Automatic FFmpeg detection in system PATH
- **Guidance**: Clear installation instructions and download links
- **Fallback**: Graceful handling when FFmpeg unavailable

### 4. Flexible Font Fallback System
- **Configuration**: Environment variable font path (`CHIMERA_FONT_PATH`)
- **Fallback**: Automatic system font detection (Arial backup)
- **Compatibility**: Cross-platform font resolution

## 🛠️ Troubleshooting

### Common Issues

#### FFmpeg Not Found
```
[WARNING] FFmpeg not found in PATH. Rendering may fail.
```
**Solution**: Install FFmpeg from https://www.gyan.dev/ffmpeg/builds/ or use `winget install FFmpeg`

#### Python Import Errors
```
[ERROR] Python not found. Please install Python 3.8+ and add to PATH.
```
**Solution**: Install Python 3.8+ and ensure it's added to system PATH

#### Font Rendering Issues
```
[WARNING] Font not found, using system fallback
```
**Solution**: Set custom font path: `$env:CHIMERA_FONT_PATH = "path\to\font.ttf"`

### Dependency Verification
```powershell
# Check all dependencies
.\ForgeProtocol.ps1 -Verbose

# Skip dependency checks (testing only)
.\ForgeProtocol.ps1 -SkipDependencyCheck
```

## 🎯 Strategic Advantages

### Oracle Series Competitive Positioning
- **Oracle EP001**: Post-deadline analysis and completion capabilities
- **Oracle EP002**: 24-hour tactical deployment window optimization
- **Viral Pipeline**: AI $100K concept integration ready
- **ARG Community**: Primed for immediate activation and scaling

### Production Workflow Benefits
- **Automated Manifest Generation**: Zero manual configuration required
- **Batch Processing**: Efficient multi-clip generation and assembly
- **Error Recovery**: Robust fallback systems and detailed logging
- **Scalability**: Modular architecture enables rapid feature expansion

### Technical Excellence
- **Cross-Platform Compatibility**: Windows/Linux font and path handling
- **Professional Logging**: Comprehensive status reporting and error tracking
- **Clean Architecture**: Separation of concerns with clear module boundaries
- **Future-Proof Design**: API integration hooks and extensibility points

## 📊 Success Metrics

- ✅ **Flawless Deployment**: Zero-configuration factory initialization
- ✅ **Resilient Operation**: Comprehensive error handling and recovery
- ✅ **Shareable Codebase**: Professional documentation and onboarding
- ✅ **Contributor Ready**: Clear architecture and extension points
- ✅ **Battle-Tested**: Production pipeline validation and optimization

## 🔗 Documentation

- [Technical Pipeline Overview](docs/pipeline_overview.md) - Detailed architecture and API hooks
- [Forge Protocol Report](#-forge-protocol-execution-report) - Deployment verification
- [Troubleshooting Guide](#-troubleshooting) - Common issues and solutions

---

**Authorization**: GCode3069  
**Mission Priority**: CRITICAL - ARSENAL DEPLOYMENT  
**Status**: ALL SYSTEMS NOMINAL - FORGE IS LIT  
**Ready for**: Contributors, collaborators, and viral dominance
