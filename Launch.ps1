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