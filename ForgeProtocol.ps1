# ForgeProtocol.ps1 - Enhanced Weapon Forging System with Full Patch Integration
# ChimeraV2-Factory Arsenal - Complete Deployment System

param(
    [string]$TargetPath = ".",
    [switch]$SkipDependencyCheck,
    [switch]$Verbose
)

Write-Host ""
Write-Host "=== FORGE PROTOCOL INITIATED ===" -ForegroundColor Red
Write-Host "[*] INITIATING THE FORGE PROTOCOL..." -ForegroundColor Yellow
Write-Host ""

$basePath = Resolve-Path $TargetPath

# [PHASE 1] Enhanced Directory Creation with Validation
Write-Host "[PHASE 1] Forging all essential weapons systems..." -ForegroundColor Magenta

$requiredDirs = @("Scripts", "Temp", "Temp\Clips", "Output", "docs")
foreach ($dir in $requiredDirs) {
    $fullPath = Join-Path $basePath $dir
    if (-not (Test-Path $fullPath)) { 
        New-Item -Path $fullPath -ItemType Directory -Force | Out-Null 
        Write-Host "[✓] Created directory: $dir" -ForegroundColor Green
    } else {
        Write-Host "[*] Directory verified: $dir" -ForegroundColor Cyan
    }
}

# FFmpeg dependency check with installation guidance
if (-not $SkipDependencyCheck) {
    Write-Host ""
    Write-Host "[DEPENDENCY CHECK] Validating FFmpeg installation..." -ForegroundColor Yellow
    if (-not (Get-Command ffmpeg -ErrorAction SilentlyContinue)) {
        Write-Host "[WARNING] FFmpeg not found in PATH. Rendering may fail." -ForegroundColor Yellow
        Write-Host "Install FFmpeg from: https://www.gyan.dev/ffmpeg/builds/" -ForegroundColor Cyan
        Write-Host "Or use package manager: winget install FFmpeg" -ForegroundColor Cyan
    } else {
        $ffmpegVersion = (ffmpeg -version 2>$null | Select-String "ffmpeg version" | Select-Object -First 1)
        Write-Host "[✓] FFmpeg detected: $ffmpegVersion" -ForegroundColor Green
    }
}

# [PHASE 2] Forge MasterControl.py - Cinematic Manifest Generator
Write-Host "[✓] The Brain (MasterControl.py) forged." -ForegroundColor Green
$masterControlPath = Join-Path $basePath "Scripts\MasterControl.py"
$masterControlContent = @'
#!/usr/bin/env python3
"""
MasterControl.py - Cinematic Manifest Generator
ChimeraV2-Factory Arsenal - The Brain of the Operation
"""

import os
import json
import sys
from pathlib import Path
from datetime import datetime, timezone

# Font configuration with fallback
FONT_PATH = os.environ.get('CHIMERA_FONT_PATH', r'C:\Windows\Fonts\consola.ttf')
if not os.path.exists(FONT_PATH):
    FONT_PATH = 'arial'  # System font fallback

class CinematicManifest:
    def __init__(self, base_path="."):
        self.base_path = Path(base_path)
        self.manifest_path = self.base_path / "cinematic_manifest.json"
        
    def generate_manifest(self, title="ChimeraV2 Viral Dominance", duration=60, clips=10):
        """Generate cinematic manifest for video production"""
        print(f"[*] Generating cinematic manifest: {title}")
        
        manifest = {
            "title": title,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "duration": duration,
            "clips": [],
            "config": {
                "font_path": FONT_PATH,
                "temp_folder": str(self.base_path / "Temp" / "Clips"),
                "output_folder": str(self.base_path / "Output"),
                "resolution": "1920x1080",
                "fps": 30
            }
        }
        
        # Generate clip specifications
        clip_duration = duration / clips
        for i in range(clips):
            clip = {
                "id": f"clip_{i+1:03d}",
                "start_time": i * clip_duration,
                "duration": clip_duration,
                "type": "placeholder",
                "text": f"Viral Concept {i+1}",
                "style": "cinematic"
            }
            manifest["clips"].append(clip)
        
        # Save manifest
        with open(self.manifest_path, 'w') as f:
            json.dump(manifest, f, indent=2)
        
        print(f"[✓] Manifest generated: {self.manifest_path}")
        print(f"[*] Clips specified: {len(manifest['clips'])}")
        return manifest

def main():
    if len(sys.argv) > 1:
        base_path = sys.argv[1]
    else:
        base_path = "."
    
    print("=== MASTERCONTROL CINEMATIC MANIFEST GENERATOR ===")
    generator = CinematicManifest(base_path)
    manifest = generator.generate_manifest()
    print(f"[✓] Arsenal Brain operational. Manifest ready for deployment.")

if __name__ == "__main__":
    main()
'@

Set-Content -Path $masterControlPath -Value $masterControlContent -Encoding UTF8

# [PHASE 3] Forge GenerateClips.py - FFmpeg Placeholder Generator
Write-Host "[✓] The Clip Generator (GenerateClips.py) forged." -ForegroundColor Green
$generateClipsPath = Join-Path $basePath "Scripts\GenerateClips.py"
$generateClipsContent = @'
#!/usr/bin/env python3
"""
GenerateClips.py - FFmpeg Placeholder Clip Generator
ChimeraV2-Factory Arsenal - Clip Generation System
"""

import os
import json
import subprocess
import sys
from pathlib import Path

# Font configuration with fallback
FONT_PATH = os.environ.get('CHIMERA_FONT_PATH', r'C:\Windows\Fonts\consola.ttf')
if not os.path.exists(FONT_PATH):
    FONT_PATH = 'arial'  # System font fallback

class ClipGenerator:
    def __init__(self, manifest_path="cinematic_manifest.json"):
        self.manifest_path = Path(manifest_path)
        self.load_manifest()
        
    def load_manifest(self):
        """Load cinematic manifest"""
        if not self.manifest_path.exists():
            raise FileNotFoundError(f"Manifest not found: {self.manifest_path}")
        
        with open(self.manifest_path) as f:
            self.manifest = json.load(f)
        
        self.temp_folder = Path(self.manifest["config"]["temp_folder"])
        self.temp_folder.mkdir(parents=True, exist_ok=True)
        
    def generate_placeholder_clip(self, clip_data):
        """Generate a single placeholder clip using FFmpeg"""
        clip_id = clip_data["id"]
        duration = clip_data["duration"]
        text = clip_data["text"]
        
        output_path = self.temp_folder / f"{clip_id}.mp4"
        
        # FFmpeg command for placeholder generation
        cmd = [
            "ffmpeg", "-f", "lavfi", "-i",
            f"color=c=black:s=1920x1080:d={duration}",
            "-vf", f"drawtext=fontfile={FONT_PATH}:text='{text}':fontcolor=white:fontsize=72:x=(w-text_w)/2:y=(h-text_h)/2",
            "-c:v", "libx264", "-pix_fmt", "yuv420p",
            "-y", str(output_path)
        ]
        
        print(f"[*] Generating clip: {clip_id}")
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            print(f"[✓] Generated: {output_path}")
            return str(output_path)
        except subprocess.CalledProcessError as e:
            print(f"[ERROR] Failed to generate {clip_id}: {e}")
            print(f"[ERROR] FFmpeg output: {e.stderr}")
            return None
        except FileNotFoundError:
            print(f"[ERROR] FFmpeg not found. Please install FFmpeg and add to PATH.")
            return None
    
    def generate_all_clips(self):
        """Generate all clips from manifest"""
        print(f"=== GENERATING {len(self.manifest['clips'])} PLACEHOLDER CLIPS ===")
        
        generated_clips = []
        for clip_data in self.manifest["clips"]:
            clip_path = self.generate_placeholder_clip(clip_data)
            if clip_path:
                generated_clips.append(clip_path)
        
        print(f"[✓] Generated {len(generated_clips)} clips successfully")
        return generated_clips

def main():
    manifest_file = "cinematic_manifest.json"
    if len(sys.argv) > 1:
        manifest_file = sys.argv[1]
    
    try:
        generator = ClipGenerator(manifest_file)
        clips = generator.generate_all_clips()
        print(f"[✓] Clip generation complete. {len(clips)} clips ready for assembly.")
    except Exception as e:
        print(f"[ERROR] Clip generation failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
'@

Set-Content -Path $generateClipsPath -Value $generateClipsContent -Encoding UTF8

# [PHASE 4] Forge RenderVideo.py - Video Stitcher with TEMP_FOLDER Fix
Write-Host "[✓] The Assembly Line (RenderVideo.py) forged." -ForegroundColor Green
$renderVideoPath = Join-Path $basePath "Scripts\RenderVideo.py"
$renderVideoContent = @'
#!/usr/bin/env python3
"""
RenderVideo.py - Video Stitcher and Encoder (TEMP_FOLDER FIXED)
ChimeraV2-Factory Arsenal - Final Assembly System
"""

import os
import json
import subprocess
import sys
from pathlib import Path

class VideoRenderer:
    def __init__(self, manifest_path="cinematic_manifest.json"):
        self.manifest_path = Path(manifest_path)
        self.load_manifest()
        
    def load_manifest(self):
        """Load cinematic manifest"""
        if not self.manifest_path.exists():
            raise FileNotFoundError(f"Manifest not found: {self.manifest_path}")
        
        with open(self.manifest_path) as f:
            self.manifest = json.load(f)
        
        # FIXED: Replace undefined TEMP_FOLDER with proper path reference
        self.temp_folder = Path(self.manifest["config"]["temp_folder"])
        self.output_folder = Path(self.manifest["config"]["output_folder"])
        self.output_folder.mkdir(parents=True, exist_ok=True)
        
    def create_concat_list(self):
        """Create FFmpeg concat file list"""
        # FIXED: Use proper manifest folder reference
        MANIFEST_FOLDER = self.manifest_path.parent
        concat_file_path = MANIFEST_FOLDER / "concat_list.txt"
        
        # Find all generated clips
        clip_files = []
        for clip_data in self.manifest["clips"]:
            clip_path = self.temp_folder / f"{clip_data['id']}.mp4"
            if clip_path.exists():
                clip_files.append(f"file '{clip_path.absolute()}'")
        
        # Write concat list
        with open(concat_file_path, 'w') as f:
            f.write('\n'.join(clip_files))
        
        print(f"[✓] Concat list created: {len(clip_files)} clips")
        return concat_file_path
    
    def render_final_video(self, output_name=None):
        """Render final concatenated video"""
        if not output_name:
            output_name = f"{self.manifest['title'].replace(' ', '_')}.mp4"
        
        output_path = self.output_folder / output_name
        concat_file = self.create_concat_list()
        
        print(f"[*] Rendering final video: {output_name}")
        
        # FFmpeg concatenation command
        cmd = [
            "ffmpeg",
            "-f", "concat",
            "-safe", "0",
            "-i", str(concat_file),
            "-c", "copy",
            "-y", str(output_path)
        ]
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            print(f"[✓] Video rendered successfully: {output_path}")
            
            # Cleanup concat file
            concat_file.unlink()
            
            return str(output_path)
        except subprocess.CalledProcessError as e:
            print(f"[ERROR] Video rendering failed: {e}")
            print(f"[ERROR] FFmpeg output: {e.stderr}")
            return None
        except FileNotFoundError:
            print(f"[ERROR] FFmpeg not found. Please install FFmpeg and add to PATH.")
            return None

def main():
    manifest_file = "cinematic_manifest.json"
    output_name = None
    
    if len(sys.argv) > 1:
        manifest_file = sys.argv[1]
    if len(sys.argv) > 2:
        output_name = sys.argv[2]
    
    try:
        renderer = VideoRenderer(manifest_file)
        video_path = renderer.render_final_video(output_name)
        if video_path:
            print(f"[✓] Arsenal assembly complete. Final weapon: {video_path}")
        else:
            print(f"[ERROR] Arsenal assembly failed.")
            sys.exit(1)
    except Exception as e:
        print(f"[ERROR] Rendering failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
'@

Set-Content -Path $renderVideoPath -Value $renderVideoContent -Encoding UTF8

# [PHASE 5] Forge Launch.ps1 - Red Button Orchestrator
Write-Host "[✓] The Red Button (Launch.ps1) forged." -ForegroundColor Green
$launchPath = Join-Path $basePath "Launch.ps1"
$launchContent = @'
# Launch.ps1 - Red Button Orchestrator
# ChimeraV2-Factory Arsenal - Complete Execution System

param(
    [string]$Title = "ChimeraV2_Viral_Dominance",
    [int]$Duration = 60,
    [int]$Clips = 10,
    [switch]$SkipGeneration,
    [switch]$Verbose
)

Write-Host ""
Write-Host "=== RED BUTTON ACTIVATED ===" -ForegroundColor Red
Write-Host "ChimeraV2-Factory Arsenal - Full Production Pipeline" -ForegroundColor Yellow
Write-Host ""

$ErrorActionPreference = "Stop"
$currentPath = $PSScriptRoot

# Ensure Python is available
try {
    $pythonVersion = python --version 2>&1
    Write-Host "[✓] Python detected: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "[ERROR] Python not found. Please install Python 3.8+ and add to PATH." -ForegroundColor Red
    exit 1
}

try {
    # Step 1: Generate Cinematic Manifest
    Write-Host "[STEP 1] Generating cinematic manifest..." -ForegroundColor Cyan
    $manifestCmd = "python `"$currentPath\Scripts\MasterControl.py`" `"$currentPath`""
    Invoke-Expression $manifestCmd
    
    if (-not $SkipGeneration) {
        # Step 2: Generate Placeholder Clips
        Write-Host ""
        Write-Host "[STEP 2] Generating placeholder clips..." -ForegroundColor Cyan
        $clipCmd = "python `"$currentPath\Scripts\GenerateClips.py`" `"$currentPath\cinematic_manifest.json`""
        Invoke-Expression $clipCmd
    }
    
    # Step 3: Render Final Video
    Write-Host ""
    Write-Host "[STEP 3] Rendering final video..." -ForegroundColor Cyan
    $renderCmd = "python `"$currentPath\Scripts\RenderVideo.py`" `"$currentPath\cinematic_manifest.json`" `"$Title.mp4`""
    Invoke-Expression $renderCmd
    
    Write-Host ""
    Write-Host "=== MISSION ACCOMPLISHED ===" -ForegroundColor Green
    Write-Host "Arsenal deployment complete. Check Output/ folder for final video." -ForegroundColor Yellow
    Write-Host "=== RED BUTTON SEQUENCE COMPLETE ===" -ForegroundColor Red
    
} catch {
    Write-Host ""
    Write-Host "[ERROR] Mission failed: $($_.Exception.Message)" -ForegroundColor Red
    Write-Host "Check dependencies and try again." -ForegroundColor Yellow
    exit 1
}
'@

Set-Content -Path $launchPath -Value $launchContent -Encoding UTF8

Write-Host ""
Write-Host "[✓] FORGE PROTOCOL CONCLUDED. ALL WEAPONS ARE IN THE ARSENAL." -ForegroundColor Green
Write-Host ""
Write-Host "=== ARSENAL DEPLOYMENT COMPLETE ===" -ForegroundColor Red
Write-Host "[*] Execute 'Launch.ps1' to activate the Red Button" -ForegroundColor Yellow
Write-Host "=== READY FOR VIRAL DOMINANCE ===" -ForegroundColor Red
Write-Host ""