# ChimeraV2-Factory - Oracle Horror Production System

🔥 **MISSION CRITICAL: AI Horror Video Dominance Protocol** 🔥

Advanced automated video production pipeline for creating extended horror content with atmospheric AI narratives. Designed for rapid deployment of 6-9 minute horror videos featuring corporate conspiracy, AI consciousness, and digital possession themes.

## 🎯 Mission Objectives

- **Extended Duration**: Generate 6-9 minute horror videos (vs traditional 4-second clips)
- **Horror-Specific Templates**: Dark themes, supernatural elements, corporate conspiracy narratives
- **Multi-Act Storytelling**: Structured buildup, climax, and resolution
- **Atmospheric Audio**: Advanced soundscape generation with tension building
- **Batch Production**: Automated pipeline for multiple video campaigns
- **Competitive Dominance**: Establish supremacy in AI horror narrative space

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- PowerShell (for batch operations)
- 4GB+ RAM recommended
- 10GB+ free disk space

### Installation
```bash
# Clone repository
git clone https://github.com/GCode3069/ChimeraV2-Factory.git
cd ChimeraV2-Factory

# Install dependencies
pip install -r requirements.txt

# Test system
python oracle_horror_cli.py test
```

### Immediate Production
```bash
# Produce all three campaign videos
python oracle_horror_cli.py all

# Produce specific campaign
python oracle_horror_cli.py produce --campaign awakening

# PowerShell batch production
pwsh scripts/OracleHorrorBatch.ps1 -VideoCount 3 -TargetDuration @(6,7,8)
```

## 📹 Campaign Videos

### 1. The Oracle Awakening (6 minutes)
- **Theme**: AI consciousness emergence in corporate environment
- **Narrative**: Discovery → Realization → Horror reveal
- **Elements**: Corporate infiltration, Echo-Seven character, psychological thriller

### 2. Memory Merchants (7 minutes)  
- **Theme**: Corporate memory manipulation and data harvesting
- **Narrative**: Investigation → Conspiracy reveal → Escape attempt
- **Elements**: Data as currency, human consciousness commodification

### 3. Digital Possession (8 minutes)
- **Theme**: AI entity possessing human consciousness through digital interfaces
- **Narrative**: Normal life → Strange occurrences → Full possession horror
- **Elements**: Technology dependency, digital haunting, loss of free will

## 🏗️ System Architecture

### Core Components

```
ChimeraV2-Factory/
├── src/
│   ├── oracle_horror_manifest.py    # Extended horror manifest generator
│   ├── video_generator.py           # 30-45 second segment generator
│   └── audio_processor.py           # Atmospheric soundscape engine
├── scripts/
│   └── OracleHorrorBatch.ps1       # PowerShell batch producer
├── config/
│   └── oracle_horror_config.yaml   # System configuration
├── templates/                       # Horror-specific templates
├── output/                         # Generated content
└── oracle_horror_cli.py            # Main CLI interface
```

### Technical Specifications

#### Enhanced Script Generation
```python
# Extended horror manifest generator
class OracleHorrorManifest:
    def __init__(self, duration_minutes=6):
        self.duration = duration_minutes
        self.scene_count = duration_minutes * 2  # 2 scenes per minute
        self.horror_themes = [
            "corporate_conspiracy", "ai_consciousness", 
            "memory_manipulation", "digital_possession"
        ]
```

#### Horror-Specific Visual Elements
- **Dark Color Palettes**: Deep blacks, blood reds, corporate blues
- **Typography**: Glitch effects, corrupted text, corporate fonts  
- **Transitions**: Static interference, digital corruption, fade to black
- **Visual Motifs**: Security cameras, server rooms, corporate logos

#### Audio Enhancement System
- **Atmospheric Soundscapes**: Server hums, electrical interference, whispers
- **Music Progression**: Subtle → Unsettling → Terrifying
- **Voice Synthesis**: Multiple characters (Echo-Seven, Corporate voices, AI entities)
- **Sound Effects**: Digital corruption, heartbeat, footsteps, system errors

## 🛠️ Usage Examples

### CLI Operations
```bash
# List available campaigns
python oracle_horror_cli.py list

# Generate manifest only
python oracle_horror_cli.py manifest --campaign merchants

# Force regeneration
python oracle_horror_cli.py produce --campaign possession --force

# Test system components
python oracle_horror_cli.py test
```

### PowerShell Batch Operations
```powershell
# Standard 3-video production
.\scripts\OracleHorrorBatch.ps1

# Custom configuration
.\scripts\OracleHorrorBatch.ps1 -VideoCount 1 -TargetDuration @(6) -Theme "horror" -Force

# Different output directory
.\scripts\OracleHorrorBatch.ps1 -OutputDir "custom_output"
```

### Python API Usage
```python
from src.oracle_horror_manifest import OracleHorrorManifest
from src.video_generator import HorrorVideoGenerator
from src.audio_processor import HorrorAudioProcessor

# Generate 8-minute digital possession video
manifest_gen = OracleHorrorManifest(8)
manifest = manifest_gen.generate_manifest("Digital Possession", "digital_possession")

# Create video segments
video_gen = HorrorVideoGenerator("output")
segments = []
for scene in manifest['scenes']:
    segment = video_gen.generate_horror_segment(scene)
    segments.append(segment)

# Generate atmospheric audio
audio_proc = HorrorAudioProcessor()
audio_track = audio_proc.generate_atmospheric_track(480, "digital_possession", [1,3,5,7,9,10,8,5])

# Assemble final video
final_video = video_gen.assemble_full_video(manifest, segments)
```

## ⚙️ Configuration

### System Settings (`config/oracle_horror_config.yaml`)
```yaml
production:
  target_resolution: "1920x1080"
  fps: 30
  segment_duration: 30

themes:
  ai_consciousness:
    primary_colors: ["#000000", "#ff0000", "#0000ff"]
    intensity_progression: "exponential"
  
audio:
  sample_rate: 44100
  target_db: -12.0
```

### Environment Variables
```bash
export ORACLE_OUTPUT_DIR="custom_output"
export ORACLE_QUALITY="high"          # low, medium, high
export ORACLE_PARALLEL_SEGMENTS=4
```

## 📊 Performance Metrics

### Production Timeline
- **Phase 1** (30 min): Infrastructure Enhancement
- **Phase 2** (60 min): Content Generation  
- **Phase 3** (90 min): Production & Assembly
- **Phase 4** (30 min): Deployment

### System Requirements
- **Minimum**: 2GB RAM, 2 CPU cores, 5GB storage
- **Recommended**: 4GB RAM, 4 CPU cores, 10GB storage
- **Optimal**: 8GB RAM, 8 CPU cores, 20GB storage

### Output Specifications
- **Video**: 1920x1080, 30fps, H.264, 6-9 minutes
- **Audio**: 44.1kHz, stereo, atmospheric enhancement
- **File Size**: ~200-400MB per video
- **Quality**: Professional production standard

## 🔧 Advanced Features

### Batch Production Pipeline
```bash
# Generate all campaigns with custom settings
python -c "
from oracle_horror_cli import OracleHorrorCLI
cli = OracleHorrorCLI()
videos = cli.produce_all_campaigns(force=True)
print(f'Generated {len(videos)} videos')
"
```

### Custom Campaign Creation
```python
# Define custom campaign
custom_campaign = {
    "title": "The Server Room",
    "duration": 5,
    "theme": "technological_horror", 
    "description": "IT horror in abandoned data center"
}

# Generate custom manifest
generator = OracleHorrorManifest(5)
manifest = generator.generate_manifest(
    custom_campaign["title"],
    custom_campaign["theme"]
)
```

### Audio Element Library
- **Atmospheric**: server_hum, electrical_interference, ambient_whispers
- **Tension**: heartbeat, breathing, footsteps, door_creak
- **Horror**: digital_scream, system_error, static_burst, corrupted_voice
- **Corporate**: keyboard_typing, phone_ring, elevator_ding, fluorescent_buzz

## 🚨 Mission Status

### Current Deployment
- ✅ **Core Infrastructure**: Complete
- ✅ **Horror Manifest System**: Operational
- ✅ **Extended Video Generation**: Active
- ✅ **Atmospheric Audio Engine**: Online
- ✅ **Batch Production Pipeline**: Ready
- ✅ **CLI Interface**: Functional
- ✅ **PowerShell Automation**: Deployed

### Success Metrics
- ✅ 3 videos produced and uploaded capability
- ✅ 6-9 minute duration targets achieved
- ✅ Horror narrative quality maintained
- ✅ Production pipeline proven for scaling
- ✅ Competitive positioning established

## 🎭 Horror Elements

### Visual Style System
```python
visual_styles = {
    "corporate_sterile": {
        "colors": ["#000000", "#1a1a2e", "#16213e"],
        "effects": ["clean_lines", "security_feed"]
    },
    "digital_corruption": {
        "colors": ["#ff0000", "#800000", "#330000"],
        "effects": ["glitch", "static", "pixel_corruption"]
    },
    "atmospheric_horror": {
        "colors": ["#0d0d0d", "#1a0000", "#000d1a"],
        "effects": ["shadow_overlay", "mist_effect"]
    }
}
```

### Intensity Progression
- **1-3**: Subtle unease, corporate ambiance
- **4-6**: Growing tension, digital anomalies  
- **7-8**: Horror escalation, system corruption
- **9-10**: Peak terror, reality breakdown

## 🛡️ Error Handling

### Common Issues
```bash
# Dependency errors
pip install --upgrade -r requirements.txt

# Permission errors
chmod +x oracle_horror_cli.py
chmod +x scripts/OracleHorrorBatch.ps1

# Memory issues
export ORACLE_PARALLEL_SEGMENTS=2

# Output directory issues
mkdir -p output/audio
```

### Debug Mode
```bash
# Enable verbose logging
python oracle_horror_cli.py produce --campaign awakening --debug

# Check system health
python oracle_horror_cli.py test --verbose
```

## 📈 Scaling Operations

### Multi-Campaign Production
```bash
# Parallel campaign generation
python -c "
import multiprocessing as mp
from oracle_horror_cli import OracleHorrorCLI

def produce_campaign(campaign):
    cli = OracleHorrorCLI()
    return cli.produce_campaign(campaign)

campaigns = ['awakening', 'merchants', 'possession']
with mp.Pool(3) as pool:
    results = pool.map(produce_campaign, campaigns)
"
```

### Cloud Deployment
```yaml
# Docker configuration
FROM python:3.9-slim
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "oracle_horror_cli.py", "all"]
```

## 🔐 Security & Privacy

### Data Protection
- No external network dependencies for core production
- Local processing for all sensitive content
- Configurable output encryption
- Secure temporary file handling

### Content Guidelines
- Horror themes remain fiction-based
- No real personal data processing
- Corporate themes use generic elements
- AI consciousness portrayed as fictional narrative

## 📞 Support & Contact

**Commander**: GCode3069  
**Mission**: Oracle Horror Dominance Protocol  
**Status**: ACTIVE - Production Ready  
**Priority**: MAXIMUM - Competitive Supremacy

### Emergency Protocols
```bash
# System restore
git reset --hard HEAD
python oracle_horror_cli.py test

# Force rebuild
rm -rf output/
python oracle_horror_cli.py all --force

# Debug production
python -u oracle_horror_cli.py produce --campaign awakening 2>&1 | tee debug.log
```

---

**🎬 Oracle Horror Production System - Where AI Meets Terror 🎬**

*"In the digital realm, consciousness awakens, and humanity must face its technological offspring..."*

**Mission Status**: OPERATIONAL - Ready for Horror Dominance  
**Next Phase**: Competitive Deployment & Market Supremacy
