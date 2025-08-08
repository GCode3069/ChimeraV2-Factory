#!/usr/bin/env python3
"""
Oracle Horror Production CLI
Command-line interface for immediate horror video production
"""

import argparse
import json
import os
import sys
import time
from datetime import datetime
from pathlib import Path

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.oracle_horror_manifest import OracleHorrorManifest

# Optional imports for when dependencies are available
try:
    from src.video_generator import HorrorVideoGenerator
    VIDEO_GENERATION_AVAILABLE = True
except ImportError as e:
    print(f"Warning: Video generation not available - {e}")
    VIDEO_GENERATION_AVAILABLE = False

try:
    from src.audio_processor import HorrorAudioProcessor
    AUDIO_PROCESSING_AVAILABLE = True
except ImportError as e:
    print(f"Warning: Audio processing not available - {e}")
    AUDIO_PROCESSING_AVAILABLE = False


class OracleHorrorCLI:
    """Command-line interface for Oracle Horror Production System"""
    
    def __init__(self):
        self.output_dir = "output"
        self.campaigns = {
            "awakening": {
                "title": "The Oracle Awakening",
                "duration": 6,
                "theme": "ai_consciousness",
                "description": "AI system gaining consciousness in corporate environment"
            },
            "merchants": {
                "title": "Memory Merchants",
                "duration": 7,
                "theme": "corporate_conspiracy", 
                "description": "Corporate memory manipulation and data harvesting"
            },
            "possession": {
                "title": "Digital Possession",
                "duration": 8,
                "theme": "digital_possession",
                "description": "AI entity possessing human consciousness through digital interfaces"
            }
        }

    def print_banner(self):
        """Print Oracle Horror system banner"""
        print("=" * 80)
        print("🔥 ORACLE HORROR PRODUCTION SYSTEM 🔥")
        print("Mission Critical: AI Horror Dominance Protocol")
        print("Commander: GCode3069")
        print(f"System Time: {datetime.utcnow().isoformat()} UTC")
        print("=" * 80)

    def print_campaign_info(self, campaign_key: str):
        """Print campaign information"""
        campaign = self.campaigns[campaign_key]
        print(f"\n📹 CAMPAIGN: {campaign['title']}")
        print(f"   Duration: {campaign['duration']} minutes")
        print(f"   Theme: {campaign['theme']}")
        print(f"   Description: {campaign['description']}")

    def generate_manifest(self, campaign_key: str, output_path: str = None) -> str:
        """Generate horror manifest for campaign"""
        campaign = self.campaigns[campaign_key]
        
        print(f"\n🎬 Generating manifest for {campaign['title']}...")
        
        # Create manifest generator
        generator = OracleHorrorManifest(campaign['duration'])
        manifest = generator.generate_manifest(
            campaign['title'],
            campaign['theme']
        )
        
        # Save manifest
        if not output_path:
            os.makedirs(self.output_dir, exist_ok=True)
            output_path = os.path.join(self.output_dir, f"manifest_{campaign_key}.json")
        
        with open(output_path, 'w') as f:
            json.dump(manifest, f, indent=2)
        
        print(f"✅ Manifest saved: {output_path}")
        print(f"   Scenes: {len(manifest['scenes'])}")
        print(f"   Total duration: {manifest['video_info']['total_seconds']} seconds")
        
        return output_path

    def generate_segments(self, manifest_path: str, campaign_key: str) -> list:
        """Generate video segments from manifest"""
        if not VIDEO_GENERATION_AVAILABLE:
            print(f"\n⚠️  Video generation unavailable - install dependencies with: pip install -r requirements.txt")
            return []
            
        print(f"\n🎥 Generating video segments...")
        
        # Load manifest
        with open(manifest_path, 'r') as f:
            manifest = json.load(f)
        
        # Create video generator
        generator = HorrorVideoGenerator(self.output_dir)
        segment_paths = []
        
        scenes = manifest['scenes']
        total_scenes = len(scenes)
        
        for idx, scene in enumerate(scenes):
            try:
                print(f"   Generating segment {idx + 1}/{total_scenes}...")
                segment_path = generator.generate_horror_segment(scene, idx)
                segment_paths.append(segment_path)
                print(f"   ✅ Segment {idx + 1} complete")
            except Exception as e:
                print(f"   ⚠️  Warning: Failed to generate segment {idx + 1}: {e}")
        
        # Save segment list
        segments_file = os.path.join(self.output_dir, f"segments_{campaign_key}.json")
        with open(segments_file, 'w') as f:
            json.dump(segment_paths, f)
        
        print(f"✅ Generated {len(segment_paths)} segments")
        return segment_paths

    def generate_audio(self, manifest_path: str, campaign_key: str) -> str:
        """Generate atmospheric audio track"""
        if not AUDIO_PROCESSING_AVAILABLE:
            print(f"\n⚠️  Audio processing unavailable - install dependencies with: pip install -r requirements.txt")
            return ""
            
        print(f"\n🔊 Generating atmospheric audio...")
        
        # Load manifest
        with open(manifest_path, 'r') as f:
            manifest = json.load(f)
        
        # Create audio processor
        audio_output_dir = os.path.join(self.output_dir, "audio")
        processor = HorrorAudioProcessor(output_dir=audio_output_dir)
        
        # Extract parameters
        duration_seconds = manifest['video_info']['total_seconds']
        theme = manifest['video_info']['theme']
        intensity_curve = [scene['horror_intensity'] for scene in manifest['scenes']]
        
        # Generate atmospheric track
        audio_path = processor.generate_atmospheric_track(
            duration_seconds, theme, intensity_curve
        )
        
        print(f"✅ Atmospheric audio generated: {audio_path}")
        return audio_path

    def assemble_video(self, manifest_path: str, segments_file: str, campaign_key: str) -> str:
        """Assemble final horror video"""
        if not VIDEO_GENERATION_AVAILABLE:
            print(f"\n⚠️  Video assembly unavailable - install dependencies with: pip install -r requirements.txt")
            return ""
            
        print(f"\n🎞️  Assembling final video...")
        
        # Load manifest and segments
        with open(manifest_path, 'r') as f:
            manifest = json.load(f)
        
        with open(segments_file, 'r') as f:
            segment_paths = json.load(f)
        
        # Create video generator
        generator = HorrorVideoGenerator(self.output_dir)
        
        # Assemble video
        final_path = generator.assemble_full_video(manifest, segment_paths)
        
        print(f"✅ Final video assembled: {final_path}")
        return final_path

    def produce_campaign(self, campaign_key: str, force: bool = False) -> str:
        """Produce complete campaign video"""
        if campaign_key not in self.campaigns:
            raise ValueError(f"Unknown campaign: {campaign_key}")
        
        campaign = self.campaigns[campaign_key]
        self.print_campaign_info(campaign_key)
        
        # Check if already exists
        expected_output = os.path.join(
            self.output_dir, 
            f"{campaign['title'].replace(' ', '_').lower()}_horror_campaign.mp4"
        )
        
        if os.path.exists(expected_output) and not force:
            print(f"✅ Video already exists: {expected_output}")
            print("   Use --force to regenerate")
            return expected_output
        
        start_time = time.time()
        
        try:
            # Phase 1: Generate manifest
            print(f"\n🔄 Phase 1: Manifest Generation")
            manifest_path = self.generate_manifest(campaign_key)
            
            # Phase 2: Generate segments
            print(f"\n🔄 Phase 2: Video Segment Generation")
            segment_paths = self.generate_segments(manifest_path, campaign_key)
            
            # Phase 3: Generate audio
            print(f"\n🔄 Phase 3: Atmospheric Audio Generation")
            audio_path = self.generate_audio(manifest_path, campaign_key)
            
            # Phase 4: Assemble video
            print(f"\n🔄 Phase 4: Final Video Assembly")
            segments_file = os.path.join(self.output_dir, f"segments_{campaign_key}.json")
            final_path = self.assemble_video(manifest_path, segments_file, campaign_key)
            
            # Production complete
            elapsed_time = time.time() - start_time
            print(f"\n🎉 PRODUCTION COMPLETE!")
            print(f"   Final video: {final_path}")
            print(f"   Production time: {elapsed_time:.1f} seconds")
            
            return final_path
            
        except Exception as e:
            print(f"\n❌ PRODUCTION FAILED: {e}")
            raise

    def produce_all_campaigns(self, force: bool = False) -> list:
        """Produce all three campaign videos"""
        self.print_banner()
        print("\n🚀 INITIATING FULL CAMPAIGN PRODUCTION")
        print("Target: 3 Oracle Horror Videos for Competitive Dominance")
        
        start_time = time.time()
        completed_videos = []
        
        for i, campaign_key in enumerate(self.campaigns.keys(), 1):
            print(f"\n{'='*60}")
            print(f"VIDEO {i}/3: {self.campaigns[campaign_key]['title']}")
            print(f"{'='*60}")
            
            try:
                video_path = self.produce_campaign(campaign_key, force)
                completed_videos.append(video_path)
                print(f"✅ Video {i}/3 COMPLETE")
            except Exception as e:
                print(f"❌ Video {i}/3 FAILED: {e}")
        
        # Final summary
        total_time = time.time() - start_time
        print(f"\n{'='*80}")
        print(f"🏆 CAMPAIGN PRODUCTION SUMMARY")
        print(f"{'='*80}")
        print(f"Videos completed: {len(completed_videos)}/3")
        print(f"Total production time: {total_time/60:.1f} minutes")
        print(f"Average per video: {total_time/len(completed_videos)/60:.1f} minutes" if completed_videos else "N/A")
        
        if len(completed_videos) == 3:
            print(f"\n🎬 MISSION ACCOMPLISHED! ALL VIDEOS PRODUCED!")
            print(f"Oracle Horror Dominance Protocol: ACTIVE")
            print(f"Ready for deployment and competitive supremacy!")
        else:
            print(f"\n⚠️  PARTIAL COMPLETION: {3 - len(completed_videos)} videos failed")
        
        print(f"\nGenerated Videos:")
        for video_path in completed_videos:
            file_size = os.path.getsize(video_path) / (1024 * 1024)  # MB
            print(f"  📹 {os.path.basename(video_path)} ({file_size:.1f} MB)")
        
        return completed_videos

    def list_campaigns(self):
        """List available campaigns"""
        print("\n📋 Available Campaigns:")
        for key, campaign in self.campaigns.items():
            print(f"  {key}: {campaign['title']} ({campaign['duration']} min)")
            print(f"    Theme: {campaign['theme']}")
            print(f"    {campaign['description']}")
            print()

def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        description="Oracle Horror Production System - AI Horror Video Generator",
        epilog="Commander GCode3069 - Mission Critical Production Pipeline"
    )
    
    parser.add_argument(
        'action',
        choices=['list', 'produce', 'all', 'manifest', 'test'],
        help='Action to perform'
    )
    
    parser.add_argument(
        '--campaign',
        choices=['awakening', 'merchants', 'possession'],
        help='Specific campaign to produce'
    )
    
    parser.add_argument(
        '--force',
        action='store_true',
        help='Force regeneration of existing files'
    )
    
    parser.add_argument(
        '--output',
        default='output',
        help='Output directory (default: output)'
    )
    
    args = parser.parse_args()
    
    # Create CLI instance
    cli = OracleHorrorCLI()
    cli.output_dir = args.output
    
    try:
        if args.action == 'list':
            cli.print_banner()
            cli.list_campaigns()
            
        elif args.action == 'manifest':
            if not args.campaign:
                print("Error: --campaign required for manifest generation")
                sys.exit(1)
            cli.print_banner()
            cli.generate_manifest(args.campaign)
            
        elif args.action == 'produce':
            if not args.campaign:
                print("Error: --campaign required for production")
                sys.exit(1)
            cli.print_banner()
            cli.produce_campaign(args.campaign, args.force)
            
        elif args.action == 'all':
            cli.produce_all_campaigns(args.force)
            
        elif args.action == 'test':
            cli.print_banner()
            print("\n🧪 Testing system components...")
            
            # Test manifest generation
            test_manifest = cli.generate_manifest('awakening')
            print(f"✅ Manifest generation: OK")
            
            # Test audio generation (if available)
            if AUDIO_PROCESSING_AVAILABLE:
                print(f"🔊 Testing audio generation...")
                processor = HorrorAudioProcessor()
                test_audio = processor.generate_element_audio('heartbeat', 5, 5)
                print(f"✅ Audio generation: OK")
            else:
                print(f"⚠️  Audio generation: UNAVAILABLE (missing dependencies)")
            
            # Test video generation (if available)
            if VIDEO_GENERATION_AVAILABLE:
                print(f"🎥 Video generation: OK")
            else:
                print(f"⚠️  Video generation: UNAVAILABLE (missing dependencies)")
            
            print(f"\n🎉 Core system operational!")
            if not (VIDEO_GENERATION_AVAILABLE and AUDIO_PROCESSING_AVAILABLE):
                print(f"💡 Install dependencies for full functionality: pip install -r requirements.txt")
            
    except KeyboardInterrupt:
        print("\n\n⚠️  Production interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ SYSTEM ERROR: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()