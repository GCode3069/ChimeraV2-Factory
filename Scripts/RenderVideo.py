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