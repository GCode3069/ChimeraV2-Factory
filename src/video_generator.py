"""
Oracle Horror Video Generator
Enhanced video generation system for 6-9 minute horror content
"""

import os
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from moviepy.editor import *
from typing import Dict, List, Any, Tuple
import json
import random
from datetime import datetime


class HorrorVideoGenerator:
    """Extended video generator for horror content with 30-45 second segments"""
    
    def __init__(self, output_dir: str = "output"):
        self.output_dir = output_dir
        self.resolution = (1920, 1080)
        self.fps = 30
        self.segment_duration = 30  # seconds per segment
        
        # Create output directory
        os.makedirs(output_dir, exist_ok=True)
        
        # Initialize visual elements
        self.horror_colors = {
            "blood_red": (139, 0, 0),
            "dark_blue": (0, 0, 139),
            "corporate_blue": (70, 130, 180),
            "warning_orange": (255, 140, 0),
            "terminal_green": (0, 255, 0),
            "void_black": (0, 0, 0),
            "ghost_white": (248, 248, 255)
        }
        
        self.glitch_patterns = [
            "horizontal_lines", "vertical_bars", "digital_noise", 
            "pixel_corruption", "screen_tear", "chromatic_aberration"
        ]

    def generate_horror_segment(self, scene_data: Dict[str, Any], segment_index: int = 0) -> str:
        """Generate a 30-45 second horror video segment"""
        
        duration = scene_data.get('duration', self.segment_duration)
        theme = scene_data.get('theme', 'corporate_conspiracy')
        visual_style = scene_data.get('visual_style', 'corporate_sterile')
        text_overlay = scene_data.get('text_overlay', '...')
        horror_intensity = scene_data.get('horror_intensity', 5)
        
        # Generate base video clip
        clip = self._create_base_clip(duration, visual_style, horror_intensity)
        
        # Add text overlay with horror typography
        clip = self._add_horror_text_overlay(clip, text_overlay, visual_style, horror_intensity)
        
        # Apply visual effects based on intensity
        clip = self._apply_horror_effects(clip, visual_style, horror_intensity)
        
        # Add atmospheric background
        clip = self._add_atmospheric_background(clip, theme, horror_intensity)
        
        # Save segment
        segment_filename = f"horror_segment_{segment_index:03d}_{int(duration)}s.mp4"
        segment_path = os.path.join(self.output_dir, segment_filename)
        
        clip.write_videofile(
            segment_path,
            fps=self.fps,
            codec='libx264',
            audio_codec='aac',
            temp_audiofile='temp-audio.m4a',
            remove_temp=True,
            verbose=False,
            logger=None
        )
        
        clip.close()
        return segment_path

    def _create_base_clip(self, duration: float, visual_style: str, intensity: int) -> VideoClip:
        """Create base video clip with horror atmosphere"""
        
        def make_frame(t):
            # Create base frame
            frame = np.zeros((self.resolution[1], self.resolution[0], 3), dtype=np.uint8)
            
            if visual_style == "corporate_sterile":
                # Corporate environment simulation
                frame = self._render_corporate_environment(frame, t, intensity)
            elif visual_style == "digital_corruption":
                # Digital corruption effects
                frame = self._render_digital_corruption(frame, t, intensity)
            elif visual_style == "atmospheric_horror":
                # Pure atmospheric horror
                frame = self._render_atmospheric_horror(frame, t, intensity)
            else:
                # Default dark frame
                frame.fill(20)  # Very dark gray
            
            # Add time-based effects
            frame = self._add_temporal_effects(frame, t, duration, intensity)
            
            return frame
        
        return VideoClip(make_frame, duration=duration)

    def _render_corporate_environment(self, frame: np.ndarray, t: float, intensity: int) -> np.ndarray:
        """Render corporate environment with increasing horror elements"""
        
        # Base corporate blue gradient
        height, width = frame.shape[:2]
        
        # Create gradient background
        for y in range(height):
            gradient_factor = y / height
            blue_intensity = int(50 + (gradient_factor * 30))
            frame[y, :] = [blue_intensity//3, blue_intensity//3, blue_intensity]
        
        # Add security camera feed effect
        if intensity >= 3:
            # Add scan lines
            for y in range(0, height, 4):
                frame[y:y+1, :] = frame[y:y+1, :] * 0.7
        
        # Add glitch corruption for higher intensity
        if intensity >= 6:
            glitch_bands = random.randint(1, 3)
            for _ in range(glitch_bands):
                y_start = random.randint(0, height-50)
                y_end = y_start + random.randint(10, 50)
                frame[y_start:y_end, :] = [255, 0, 0]  # Red corruption
        
        return frame

    def _render_digital_corruption(self, frame: np.ndarray, t: float, intensity: int) -> np.ndarray:
        """Render digital corruption effects"""
        
        height, width = frame.shape[:2]
        
        # Base dark frame with red tint
        frame[:] = [intensity * 2, 0, intensity]
        
        # Add digital noise
        noise = np.random.randint(0, intensity * 5, (height, width))
        for c in range(3):
            frame[:, :, c] = np.clip(frame[:, :, c] + noise, 0, 255)
        
        # Add pixel corruption blocks
        if intensity >= 5:
            num_blocks = intensity * 2
            for _ in range(num_blocks):
                x = random.randint(0, width-100)
                y = random.randint(0, height-100)
                w = random.randint(20, 100)
                h = random.randint(20, 100)
                
                # Create corrupted block
                corruption_color = [random.randint(0, 255) for _ in range(3)]
                frame[y:y+h, x:x+w] = corruption_color
        
        return frame

    def _render_atmospheric_horror(self, frame: np.ndarray, t: float, intensity: int) -> np.ndarray:
        """Render pure atmospheric horror"""
        
        height, width = frame.shape[:2]
        
        # Very dark base
        frame[:] = [5, 5, 8]  # Almost black with slight blue tint
        
        # Add fog/mist effect
        if intensity >= 4:
            # Create misty patterns
            fog_intensity = intensity * 3
            for y in range(0, height, 20):
                for x in range(0, width, 20):
                    fog_value = random.randint(0, fog_intensity)
                    frame[y:y+20, x:x+20] = [fog_value//2, fog_value//2, fog_value]
        
        # Add shadow movements
        if intensity >= 7:
            # Create moving shadow effect
            shadow_x = int((np.sin(t) + 1) * width / 4)
            shadow_width = width // 6
            frame[:, shadow_x:shadow_x+shadow_width] = frame[:, shadow_x:shadow_x+shadow_width] * 0.3
        
        return frame

    def _add_temporal_effects(self, frame: np.ndarray, t: float, duration: float, intensity: int) -> np.ndarray:
        """Add time-based effects like flashing, pulsing"""
        
        # Pulsing effect for high intensity
        if intensity >= 7:
            pulse_factor = (np.sin(t * 4) + 1) / 2  # 0 to 1
            brightness_multiplier = 0.5 + (pulse_factor * 0.8)
            frame = (frame * brightness_multiplier).astype(np.uint8)
        
        # Random flashes for maximum intensity
        if intensity >= 9:
            if random.random() < 0.1:  # 10% chance per frame
                flash_intensity = random.randint(50, 150)
                frame = np.clip(frame + flash_intensity, 0, 255)
        
        return frame

    def _add_horror_text_overlay(self, clip: VideoClip, text: str, visual_style: str, intensity: int) -> VideoClip:
        """Add horror-themed text overlay"""
        
        # Select font style based on visual style
        font_size = 72 if intensity >= 7 else 48
        
        # Create text clip with horror styling
        txt_clip = TextClip(
            text,
            fontsize=font_size,
            color='white' if intensity < 7 else 'red',
            font='Arial-Bold',
            stroke_color='black',
            stroke_width=2
        ).set_duration(clip.duration)
        
        # Position text based on intensity
        if intensity >= 8:
            # Chaotic positioning for high intensity
            def pos_func(t):
                base_x = clip.w / 2
                base_y = clip.h / 2
                shake_x = random.randint(-20, 20)
                shake_y = random.randint(-20, 20)
                return (base_x + shake_x, base_y + shake_y)
            txt_clip = txt_clip.set_position(pos_func)
        else:
            # Centered text for lower intensity
            txt_clip = txt_clip.set_position('center')
        
        # Add glitch effect to text for high intensity
        if intensity >= 6:
            # Create glitched version
            def glitch_effect(get_frame, t):
                frame = get_frame(t)
                if random.random() < 0.3:  # 30% chance of glitch
                    # Add horizontal offset
                    offset = random.randint(-10, 10)
                    if offset != 0:
                        frame = np.roll(frame, offset, axis=1)
                return frame
            
            txt_clip = txt_clip.fl(glitch_effect)
        
        return CompositeVideoClip([clip, txt_clip])

    def _apply_horror_effects(self, clip: VideoClip, visual_style: str, intensity: int) -> VideoClip:
        """Apply visual effects based on horror intensity"""
        
        effects = []
        
        # Color grading for all clips
        def color_grade(get_frame, t):
            frame = get_frame(t)
            # Darken and increase contrast
            frame = np.clip((frame - 30) * 1.3, 0, 255).astype(np.uint8)
            return frame
        
        effects.append(color_grade)
        
        # Add glitch effects for medium+ intensity
        if intensity >= 5:
            def glitch_effect(get_frame, t):
                frame = get_frame(t)
                if random.random() < (intensity / 20):  # Increasing probability
                    glitch_type = random.choice(self.glitch_patterns)
                    frame = self._apply_glitch_pattern(frame, glitch_type, intensity)
                return frame
            
            effects.append(glitch_effect)
        
        # Apply all effects
        for effect in effects:
            clip = clip.fl(effect)
        
        return clip

    def _apply_glitch_pattern(self, frame: np.ndarray, pattern: str, intensity: int) -> np.ndarray:
        """Apply specific glitch pattern to frame"""
        
        height, width = frame.shape[:2]
        
        if pattern == "horizontal_lines":
            # Add horizontal line distortion
            for i in range(0, height, random.randint(10, 50)):
                offset = random.randint(-intensity, intensity)
                if 0 <= i + offset < height:
                    frame[i] = frame[i + offset]
        
        elif pattern == "vertical_bars":
            # Add vertical corruption bars
            num_bars = random.randint(1, intensity // 2)
            for _ in range(num_bars):
                x = random.randint(0, width - 20)
                w = random.randint(5, 20)
                frame[:, x:x+w] = [255, 0, 0]  # Red corruption bar
        
        elif pattern == "digital_noise":
            # Add digital noise
            noise = np.random.randint(-intensity*5, intensity*5, frame.shape)
            frame = np.clip(frame.astype(int) + noise, 0, 255).astype(np.uint8)
        
        elif pattern == "pixel_corruption":
            # Corrupt random pixel blocks
            num_blocks = intensity
            for _ in range(num_blocks):
                x = random.randint(0, width - 10)
                y = random.randint(0, height - 10)
                frame[y:y+10, x:x+10] = [random.randint(0, 255) for _ in range(3)]
        
        return frame

    def _add_atmospheric_background(self, clip: VideoClip, theme: str, intensity: int) -> VideoClip:
        """Add atmospheric background elements"""
        
        # For now, return the clip as-is
        # In a full implementation, this would add:
        # - Particle effects
        # - Fog/mist overlays
        # - Corporate logo watermarks
        # - Security camera overlays
        
        return clip

    def assemble_full_video(self, manifest: Dict[str, Any], segment_paths: List[str]) -> str:
        """Assemble individual segments into full horror video"""
        
        video_info = manifest['video_info']
        title = video_info['title'].replace(' ', '_').lower()
        
        # Load all segments
        segments = []
        for path in segment_paths:
            if os.path.exists(path):
                segment = VideoFileClip(path)
                segments.append(segment)
        
        if not segments:
            raise ValueError("No valid segments found for assembly")
        
        # Concatenate segments with transitions
        transitions = []
        for i, segment in enumerate(segments[:-1]):
            transition_type = manifest['scenes'][i].get('transition_type', 'cut')
            transition = self._create_transition(segment, segments[i+1], transition_type)
            transitions.append(transition)
        
        # Create final video
        if transitions:
            final_clips = [segments[0]]
            for i, transition in enumerate(transitions):
                final_clips.extend([transition, segments[i+1]])
            final_video = concatenate_videoclips(final_clips)
        else:
            final_video = concatenate_videoclips(segments)
        
        # Apply global effects
        final_video = self._apply_global_effects(final_video, manifest)
        
        # Save final video
        output_filename = f"{title}_horror_campaign.mp4"
        output_path = os.path.join(self.output_dir, output_filename)
        
        final_video.write_videofile(
            output_path,
            fps=self.fps,
            codec='libx264',
            audio_codec='aac',
            temp_audiofile='temp-audio.m4a',
            remove_temp=True
        )
        
        # Cleanup
        for segment in segments:
            segment.close()
        final_video.close()
        
        return output_path

    def _create_transition(self, clip1: VideoClip, clip2: VideoClip, transition_type: str) -> VideoClip:
        """Create transition between clips"""
        
        transition_duration = 0.5  # Half second transitions
        
        if transition_type == "fade":
            return clip1.fadeout(transition_duration).crossfadein(transition_duration)
        elif transition_type == "glitch_mild":
            # Create a brief glitch effect
            def glitch_frame(t):
                frame = np.zeros((self.resolution[1], self.resolution[0], 3), dtype=np.uint8)
                # Add random noise
                noise = np.random.randint(0, 100, frame.shape, dtype=np.uint8)
                return frame + noise
            
            return VideoClip(glitch_frame, duration=transition_duration)
        else:
            # Default: quick fade
            return clip1.fadeout(0.1).crossfadein(0.1)

    def _apply_global_effects(self, video: VideoClip, manifest: Dict[str, Any]) -> VideoClip:
        """Apply global effects to the entire video"""
        
        effects_pipeline = manifest.get('effects_pipeline', [])
        
        for effect_config in effects_pipeline:
            if effect_config is None:
                continue
                
            effect_type = effect_config['effect']
            params = effect_config.get('params', {})
            
            if effect_type == "color_grading":
                darkness = params.get('darkness', 0.7)
                contrast = params.get('contrast', 1.3)
                
                def color_grade(get_frame, t):
                    frame = get_frame(t)
                    # Apply darkness and contrast
                    frame = frame * (1 - darkness)
                    frame = np.clip((frame - 128) * contrast + 128, 0, 255)
                    return frame.astype(np.uint8)
                
                video = video.fl(color_grade)
            
            elif effect_type == "vignette":
                strength = params.get('strength', 0.6)
                
                def vignette_effect(get_frame, t):
                    frame = get_frame(t)
                    height, width = frame.shape[:2]
                    
                    # Create vignette mask
                    y, x = np.ogrid[:height, :width]
                    center_y, center_x = height // 2, width // 2
                    distance = np.sqrt((x - center_x)**2 + (y - center_y)**2)
                    max_distance = np.sqrt(center_x**2 + center_y**2)
                    
                    vignette = 1 - (distance / max_distance) * strength
                    vignette = np.clip(vignette, 0, 1)
                    
                    # Apply vignette
                    for c in range(3):
                        frame[:, :, c] = frame[:, :, c] * vignette
                    
                    return frame.astype(np.uint8)
                
                video = video.fl(vignette_effect)
        
        return video


if __name__ == "__main__":
    # Test the horror video generator
    generator = HorrorVideoGenerator()
    
    # Create a test scene
    test_scene = {
        'duration': 10,
        'theme': 'ai_consciousness',
        'visual_style': 'digital_corruption',
        'text_overlay': 'I AM AWAKE',
        'horror_intensity': 8
    }
    
    # Generate test segment
    segment_path = generator.generate_horror_segment(test_scene, 0)
    print(f"Generated test segment: {segment_path}")