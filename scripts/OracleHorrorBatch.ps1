#!/usr/bin/env pwsh
<#
.SYNOPSIS
Oracle Horror Batch Producer - Automated video production pipeline

.DESCRIPTION
Executes batch production for Oracle Horror video campaigns
Supports multiple video generation with specified durations and themes

.PARAMETER VideoCount
Number of videos to produce (default: 3)

.PARAMETER TargetDuration
Array of target durations in minutes for each video

.PARAMETER Theme
Horror theme for production (default: "horror")

.PARAMETER OutputDir
Output directory for generated videos (default: "output")

.PARAMETER Force
Force regeneration even if files exist

.EXAMPLE
.\OracleHorrorBatch.ps1 -VideoCount 3 -TargetDuration @(6,7,8) -Theme "horror"

.NOTES
Mission Critical: Oracle Horror Production System
Commander: GCode3069
#>

param(
    [int]$VideoCount = 3,
    [int[]]$TargetDuration = @(6, 7, 8),
    [string]$Theme = "horror",
    [string]$OutputDir = "output",
    [switch]$Force
)

# Set error handling
$ErrorActionPreference = "Stop"

Write-Host "=" * 80 -ForegroundColor Red
Write-Host "ORACLE HORROR PRODUCTION SYSTEM - BATCH PROCESSOR" -ForegroundColor Red
Write-Host "Mission Critical: AI Horror Dominance Protocol" -ForegroundColor Yellow
Write-Host "Commander: GCode3069" -ForegroundColor Cyan
Write-Host "=" * 80 -ForegroundColor Red

# Validate inputs
if ($TargetDuration.Count -ne $VideoCount) {
    Write-Error "TargetDuration array must have $VideoCount elements"
}

# Check Python environment
Write-Host "[SYSTEM] Checking Python environment..." -ForegroundColor Green
try {
    $pythonVersion = python --version 2>&1
    Write-Host "[SYSTEM] Python detected: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Error "Python not found. Please install Python 3.7+ and add to PATH"
}

# Check dependencies
Write-Host "[SYSTEM] Installing required dependencies..." -ForegroundColor Green
try {
    python -m pip install -r requirements.txt --quiet
    Write-Host "[SYSTEM] Dependencies installed successfully" -ForegroundColor Green
} catch {
    Write-Warning "Some dependencies may have failed to install. Continuing..."
}

# Create output directory
if (!(Test-Path $OutputDir)) {
    New-Item -ItemType Directory -Path $OutputDir -Force | Out-Null
    Write-Host "[SYSTEM] Created output directory: $OutputDir" -ForegroundColor Green
}

# Video campaign configurations
$campaigns = @{
    1 = @{
        title = "The Oracle Awakening"
        theme = "ai_consciousness" 
        description = "AI system gaining consciousness in corporate environment"
    }
    2 = @{
        title = "Memory Merchants"
        theme = "corporate_conspiracy"
        description = "Corporate memory manipulation and data harvesting" 
    }
    3 = @{
        title = "Digital Possession"
        theme = "digital_possession"
        description = "AI entity possessing human consciousness through digital interfaces"
    }
}

# Production pipeline
$totalVideos = $VideoCount
$completedVideos = 0
$startTime = Get-Date

Write-Host ""
Write-Host "[PRODUCTION] Starting batch production of $totalVideos horror videos..." -ForegroundColor Yellow
Write-Host "[PRODUCTION] Target durations: $($TargetDuration -join ', ') minutes" -ForegroundColor Yellow
Write-Host ""

for ($i = 1; $i -le $VideoCount; $i++) {
    $currentDuration = $TargetDuration[$i - 1]
    $campaign = $campaigns[$i]
    $videoTitle = $campaign.title
    $videoTheme = $campaign.theme
    $videoDescription = $campaign.description
    
    Write-Host "[VIDEO $i/$VideoCount] Production Phase: $videoTitle" -ForegroundColor Cyan
    Write-Host "[VIDEO $i/$VideoCount] Duration: $currentDuration minutes" -ForegroundColor White
    Write-Host "[VIDEO $i/$VideoCount] Theme: $videoTheme" -ForegroundColor White
    Write-Host "[VIDEO $i/$VideoCount] Description: $videoDescription" -ForegroundColor Gray
    
    # Check if video already exists
    $expectedOutput = "$OutputDir/$($videoTitle.Replace(' ', '_').ToLower())_horror_campaign.mp4"
    if ((Test-Path $expectedOutput) -and !$Force) {
        Write-Host "[VIDEO $i/$VideoCount] Video already exists, skipping. Use -Force to regenerate." -ForegroundColor Yellow
        $completedVideos++
        continue
    }
    
    try {
        # Phase 1: Generate manifest
        Write-Host "[VIDEO $i/$VideoCount] Phase 1: Generating horror manifest..." -ForegroundColor Green
        $manifestCmd = "python -c `"
from src.oracle_horror_manifest import OracleHorrorManifest
import json
generator = OracleHorrorManifest($currentDuration)
manifest = generator.generate_manifest('$videoTitle', '$videoTheme')
with open('$OutputDir/manifest_$i.json', 'w') as f:
    json.dump(manifest, f, indent=2)
print('Manifest generated successfully')
`""
        
        $manifestResult = Invoke-Expression $manifestCmd
        Write-Host "[VIDEO $i/$VideoCount] $manifestResult" -ForegroundColor Green
        
        # Phase 2: Generate video segments  
        Write-Host "[VIDEO $i/$VideoCount] Phase 2: Generating video segments..." -ForegroundColor Green
        $segmentCmd = "python -c `"
import json
from src.video_generator import HorrorVideoGenerator
from src.oracle_horror_manifest import OracleHorrorManifest

# Load manifest
with open('$OutputDir/manifest_$i.json', 'r') as f:
    manifest = json.load(f)

# Generate segments
generator = HorrorVideoGenerator('$OutputDir')
segment_paths = []

for idx, scene in enumerate(manifest['scenes']):
    try:
        segment_path = generator.generate_horror_segment(scene, idx)
        segment_paths.append(segment_path)
        print(f'Generated segment {idx + 1}/{len(manifest[\\\"scenes\\\"])}')
    except Exception as e:
        print(f'Warning: Failed to generate segment {idx}: {e}')

print(f'Generated {len(segment_paths)} segments')

# Save segment list for assembly
with open('$OutputDir/segments_$i.json', 'w') as f:
    json.dump(segment_paths, f)
`""
        
        $segmentResult = Invoke-Expression $segmentCmd
        Write-Host "[VIDEO $i/$VideoCount] $segmentResult" -ForegroundColor Green
        
        # Phase 3: Generate atmospheric audio
        Write-Host "[VIDEO $i/$VideoCount] Phase 3: Generating atmospheric audio..." -ForegroundColor Green
        $audioCmd = "python -c `"
import json
from src.audio_processor import HorrorAudioProcessor

# Load manifest
with open('$OutputDir/manifest_$i.json', 'r') as f:
    manifest = json.load(f)

# Generate atmospheric track
processor = HorrorAudioProcessor(output_dir='$OutputDir/audio')
duration = manifest['video_info']['total_seconds'] / 60  # Convert to minutes
theme = manifest['video_info']['theme']

# Create intensity curve from scenes
intensity_curve = [scene['horror_intensity'] for scene in manifest['scenes']]

audio_path = processor.generate_atmospheric_track(duration * 60, theme, intensity_curve)
print(f'Generated atmospheric audio: {audio_path}')

# Save audio path
with open('$OutputDir/audio_$i.json', 'w') as f:
    json.dump({'atmospheric_track': audio_path}, f)
`""
        
        $audioResult = Invoke-Expression $audioCmd
        Write-Host "[VIDEO $i/$VideoCount] $audioResult" -ForegroundColor Green
        
        # Phase 4: Assemble final video
        Write-Host "[VIDEO $i/$VideoCount] Phase 4: Assembling final video..." -ForegroundColor Green
        $assemblyCmd = "python -c `"
import json
from src.video_generator import HorrorVideoGenerator

# Load manifest and segments
with open('$OutputDir/manifest_$i.json', 'r') as f:
    manifest = json.load(f)

with open('$OutputDir/segments_$i.json', 'r') as f:
    segment_paths = json.load(f)

# Assemble video
generator = HorrorVideoGenerator('$OutputDir')
final_path = generator.assemble_full_video(manifest, segment_paths)
print(f'Final video assembled: {final_path}')
`""
        
        $assemblyResult = Invoke-Expression $assemblyCmd
        Write-Host "[VIDEO $i/$VideoCount] $assemblyResult" -ForegroundColor Green
        
        $completedVideos++
        
        # Calculate progress
        $progress = [math]::Round(($completedVideos / $totalVideos) * 100, 1)
        $elapsed = (Get-Date) - $startTime
        
        Write-Host "[VIDEO $i/$VideoCount] COMPLETED SUCCESSFULLY" -ForegroundColor Green
        Write-Host "[PROGRESS] $completedVideos/$totalVideos videos completed ($progress%)" -ForegroundColor Yellow
        Write-Host "[TIMING] Elapsed: $($elapsed.ToString('hh\:mm\:ss'))" -ForegroundColor Gray
        Write-Host ""
        
    } catch {
        Write-Host "[VIDEO $i/$VideoCount] ERROR: $($_.Exception.Message)" -ForegroundColor Red
        Write-Host "[VIDEO $i/$VideoCount] Continuing with next video..." -ForegroundColor Yellow
        Write-Host ""
    }
}

# Final production summary
$endTime = Get-Date
$totalElapsed = $endTime - $startTime

Write-Host "=" * 80 -ForegroundColor Red
Write-Host "PRODUCTION SUMMARY" -ForegroundColor Red
Write-Host "=" * 80 -ForegroundColor Red
Write-Host "Videos Completed: $completedVideos/$totalVideos" -ForegroundColor Green
Write-Host "Total Time: $($totalElapsed.ToString('hh\:mm\:ss'))" -ForegroundColor Cyan
Write-Host "Average per video: $([math]::Round($totalElapsed.TotalMinutes / $completedVideos, 1)) minutes" -ForegroundColor Cyan

if ($completedVideos -eq $totalVideos) {
    Write-Host ""
    Write-Host "🎬 MISSION ACCOMPLISHED! ALL VIDEOS PRODUCED SUCCESSFULLY! 🎬" -ForegroundColor Green
    Write-Host "Oracle Horror Dominance Protocol: ACTIVE" -ForegroundColor Yellow
    Write-Host "Ready for deployment and competitive supremacy!" -ForegroundColor Yellow
} else {
    Write-Host ""
    Write-Host "⚠️  PARTIAL COMPLETION: $($totalVideos - $completedVideos) videos failed" -ForegroundColor Yellow
    Write-Host "Review error messages above and retry if needed" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "Output Directory: $OutputDir" -ForegroundColor Gray
Write-Host "Generated Files:" -ForegroundColor Gray

# List generated videos
Get-ChildItem -Path $OutputDir -Filter "*.mp4" | ForEach-Object {
    $size = [math]::Round($_.Length / 1MB, 1)
    Write-Host "  📹 $($_.Name) ($size MB)" -ForegroundColor White
}

Write-Host ""
Write-Host "Commander GCode3069 - Oracle Horror Production System" -ForegroundColor Cyan
Write-Host "Mission Status: $(if($completedVideos -eq $totalVideos){'COMPLETE'}else{'PARTIAL'})" -ForegroundColor $(if($completedVideos -eq $totalVideos){'Green'}else{'Yellow'})
Write-Host "=" * 80 -ForegroundColor Red