#!/usr/bin/env python3
"""
Oracle Horror Production System - Example Usage
Demonstrates manifest generation and campaign creation
"""

import json
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.oracle_horror_manifest import OracleHorrorManifest


def demo_manifest_generation():
    """Demonstrate manifest generation capabilities"""
    print("🎬 ORACLE HORROR MANIFEST GENERATION DEMO")
    print("=" * 60)
    
    # Create generator for 6-minute video
    print("\n📝 Creating 6-minute AI consciousness horror video...")
    generator = OracleHorrorManifest(duration_minutes=6)
    
    # Generate manifest
    manifest = generator.generate_manifest(
        video_title="The Oracle Awakening",
        theme="ai_consciousness"
    )
    
    # Display key information
    print(f"✅ Generated manifest for: {manifest['video_info']['title']}")
    print(f"   Duration: {manifest['video_info']['duration_minutes']} minutes")
    print(f"   Scenes: {manifest['video_info']['scene_count']}")
    print(f"   Theme: {manifest['video_info']['theme']}")
    print(f"   Resolution: {manifest['production_specs']['target_resolution']}")
    
    # Show some scenes
    print(f"\n🎞️  Scene Breakdown:")
    for i, scene in enumerate(manifest['scenes'][:3]):  # Show first 3 scenes
        print(f"   Scene {scene['scene_id']}: {scene['narrative_beat']}")
        print(f"     Duration: {scene['duration']}s")
        print(f"     Intensity: {scene['horror_intensity']}/10") 
        print(f"     Text: '{scene['text_overlay']}'")
        print(f"     Style: {scene['visual_style']}")
        print()
    
    if len(manifest['scenes']) > 3:
        print(f"   ... and {len(manifest['scenes']) - 3} more scenes")
    
    return manifest


def demo_campaign_generation():
    """Demonstrate full campaign generation"""
    print("\n🚀 ORACLE HORROR CAMPAIGN GENERATION DEMO") 
    print("=" * 60)
    
    generator = OracleHorrorManifest()
    campaigns = generator.generate_campaign_manifests()
    
    print(f"✅ Generated {len(campaigns)} campaign manifests:")
    
    for campaign_id, manifest in campaigns.items():
        video_info = manifest['video_info']
        print(f"\n📹 {video_info['title']}")
        print(f"   Duration: {video_info['duration_minutes']} minutes")
        print(f"   Theme: {video_info['theme']}")
        print(f"   Scenes: {video_info['scene_count']}")
        
        # Show intensity progression
        intensities = [scene['horror_intensity'] for scene in manifest['scenes']]
        print(f"   Intensity curve: {intensities[:5]}...{intensities[-3:]} (1-10 scale)")
    
    return campaigns


def demo_horror_elements():
    """Demonstrate horror element generation"""
    print("\n👻 HORROR ELEMENTS DEMONSTRATION")
    print("=" * 60)
    
    generator = OracleHorrorManifest(duration_minutes=8)
    
    # Show themes
    print(f"\n🎭 Available Horror Themes:")
    for theme in generator.horror_themes:
        print(f"   • {theme}")
    
    # Show visual styles
    print(f"\n🎨 Visual Styles:")
    for style, config in generator.visual_styles.items():
        print(f"   • {style}:")
        print(f"     Colors: {config['colors'][:2]}...")
        print(f"     Effects: {config['effects'][:2]}...")
    
    # Show audio elements
    print(f"\n🔊 Audio Element Categories:")
    for category, elements in generator.audio_elements.items():
        print(f"   • {category}: {elements[:3]}...")
    
    # Generate sample scene for each intensity level
    print(f"\n📈 Horror Intensity Progression (1-10):")
    sample_manifest = generator.generate_manifest("Sample Horror", "digital_possession")
    
    # Group scenes by intensity
    intensity_examples = {}
    for scene in sample_manifest['scenes']:
        intensity = scene['horror_intensity']
        if intensity not in intensity_examples:
            intensity_examples[intensity] = scene
    
    for intensity in sorted(intensity_examples.keys()):
        scene = intensity_examples[intensity]
        print(f"   Level {intensity}: {scene['visual_style']} - '{scene['text_overlay']}'")


def save_example_manifests():
    """Save example manifests for reference"""
    print("\n💾 SAVING EXAMPLE MANIFESTS")
    print("=" * 60)
    
    # Create output directory
    os.makedirs("examples", exist_ok=True)
    
    # Generate and save each campaign
    generator = OracleHorrorManifest()
    campaigns = generator.generate_campaign_manifests()
    
    for campaign_id, manifest in campaigns.items():
        filename = f"examples/{campaign_id}_manifest.json"
        with open(filename, 'w') as f:
            json.dump(manifest, f, indent=2)
        print(f"✅ Saved: {filename}")
    
    # Create a simple manifest for quick reference
    simple_manifest = generator.generate_manifest("Quick Demo", "ai_consciousness")
    with open("examples/quick_demo_manifest.json", 'w') as f:
        json.dump(simple_manifest, f, indent=2)
    print(f"✅ Saved: examples/quick_demo_manifest.json")
    
    print(f"\n📁 Example manifests saved in 'examples/' directory")


def main():
    """Run all demonstrations"""
    print("🔥 ORACLE HORROR PRODUCTION SYSTEM - DEMO 🔥")
    print("Mission Critical: AI Horror Dominance Protocol")
    print("Commander: GCode3069")
    print("=" * 80)
    
    try:
        # Run demonstrations
        demo_manifest_generation()
        demo_campaign_generation() 
        demo_horror_elements()
        save_example_manifests()
        
        print("\n🎉 DEMONSTRATION COMPLETE")
        print("=" * 80)
        print("Next Steps:")
        print("  1. Run 'python oracle_horror_cli.py list' to see available campaigns")
        print("  2. Run 'python oracle_horror_cli.py manifest --campaign awakening' to generate a manifest")
        print("  3. Install full dependencies with './install.sh' for video production")
        print("  4. Run 'python oracle_horror_cli.py all' for full campaign production")
        print("")
        print("🎬 Oracle Horror Production System: OPERATIONAL")
        print("Ready for competitive dominance in AI horror space!")
        
    except Exception as e:
        print(f"\n❌ Demo failed: {e}")
        print("This might indicate missing dependencies or system issues.")
        print("Try running: python oracle_horror_cli.py test")


if __name__ == "__main__":
    main()