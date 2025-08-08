"""
Oracle Horror Manifest Generator
Creates detailed production manifests for extended horror video content
"""

import json
import random
from datetime import datetime
from typing import List, Dict, Any
from dataclasses import dataclass, asdict


@dataclass
class HorrorScene:
    """Individual horror scene specification"""
    scene_id: int
    duration: float  # seconds
    theme: str
    narrative_beat: str
    visual_style: str
    audio_elements: List[str]
    text_overlay: str
    transition_type: str
    horror_intensity: int  # 1-10 scale


class OracleHorrorManifest:
    """Extended horror manifest generator for 6-9 minute productions"""
    
    def __init__(self, duration_minutes: int = 6):
        self.duration = duration_minutes
        self.total_seconds = duration_minutes * 60
        self.scene_count = duration_minutes * 2  # 2 scenes per minute
        self.scenes_per_minute = 2
        
        # Horror themes and elements
        self.horror_themes = [
            "corporate_conspiracy", "ai_consciousness", "memory_manipulation",
            "digital_possession", "data_harvesting", "technological_horror",
            "surveillance_state", "digital_corruption", "synthetic_reality"
        ]
        
        self.visual_styles = {
            "corporate_sterile": {
                "colors": ["#000000", "#1a1a2e", "#16213e", "#0f3460"],
                "fonts": ["Arial", "Helvetica", "Corporate Sans"],
                "effects": ["clean_lines", "corporate_logo", "security_feed"]
            },
            "digital_corruption": {
                "colors": ["#ff0000", "#800000", "#330000", "#660000"],
                "fonts": ["Courier", "Matrix", "Digital"],
                "effects": ["glitch", "static", "digital_noise", "pixel_corruption"]
            },
            "atmospheric_horror": {
                "colors": ["#0d0d0d", "#1a0000", "#000d1a", "#1a1a00"],
                "fonts": ["Gothic", "Horror Sans", "Creepy"],
                "effects": ["fade_to_black", "shadow_overlay", "mist_effect"]
            }
        }
        
        self.audio_elements = {
            "atmospheric": ["server_hum", "electrical_interference", "ambient_whispers", "ventilation_system"],
            "tension": ["heartbeat", "breathing", "footsteps", "door_creak"],
            "horror": ["digital_scream", "system_error", "static_burst", "corrupted_voice"],
            "corporate": ["keyboard_typing", "phone_ring", "elevator_ding", "fluorescent_buzz"]
        }
        
        self.narrative_structures = {
            6: {  # 6-minute structure
                "act1": {"start": 0, "end": 120, "scenes": 4, "intensity": [2, 3, 4, 5]},
                "act2": {"start": 120, "end": 240, "scenes": 4, "intensity": [5, 6, 7, 8]},
                "act3": {"start": 240, "end": 360, "scenes": 4, "intensity": [8, 9, 10, 7]}
            },
            7: {  # 7-minute structure
                "act1": {"start": 0, "end": 140, "scenes": 5, "intensity": [2, 3, 3, 4, 5]},
                "act2": {"start": 140, "end": 280, "scenes": 5, "intensity": [5, 6, 7, 8, 8]},
                "act3": {"start": 280, "end": 420, "scenes": 4, "intensity": [9, 10, 9, 6]}
            },
            8: {  # 8-minute structure
                "act1": {"start": 0, "end": 160, "scenes": 5, "intensity": [1, 2, 3, 4, 5]},
                "act2": {"start": 160, "end": 320, "scenes": 6, "intensity": [5, 6, 7, 8, 9, 8]},
                "act3": {"start": 320, "end": 480, "scenes": 5, "intensity": [9, 10, 10, 8, 5]}
            }
        }

    def generate_manifest(self, video_title: str, theme: str, narrative_type: str = "standard") -> Dict[str, Any]:
        """Generate complete horror video manifest"""
        
        structure = self.narrative_structures[self.duration]
        scenes = []
        scene_id = 1
        
        for act_name, act_data in structure.items():
            act_scenes = self._generate_act_scenes(
                act_data, scene_id, theme, act_name
            )
            scenes.extend(act_scenes)
            scene_id += len(act_scenes)
        
        manifest = {
            "video_info": {
                "title": video_title,
                "duration_minutes": self.duration,
                "total_seconds": self.total_seconds,
                "theme": theme,
                "narrative_type": narrative_type,
                "scene_count": len(scenes),
                "created_at": datetime.utcnow().isoformat()
            },
            "production_specs": {
                "target_resolution": "1920x1080",
                "fps": 30,
                "audio_sample_rate": 44100,
                "segment_duration": 30,  # seconds per segment
                "segments_needed": len(scenes)
            },
            "scenes": [asdict(scene) for scene in scenes],
            "global_audio": self._generate_global_audio_track(theme),
            "effects_pipeline": self._generate_effects_pipeline(theme)
        }
        
        return manifest

    def _generate_act_scenes(self, act_data: Dict, start_scene_id: int, theme: str, act_name: str) -> List[HorrorScene]:
        """Generate scenes for a specific act"""
        scenes = []
        scene_duration = (act_data["end"] - act_data["start"]) / act_data["scenes"]
        
        for i in range(act_data["scenes"]):
            scene = HorrorScene(
                scene_id=start_scene_id + i,
                duration=scene_duration,
                theme=theme,
                narrative_beat=self._get_narrative_beat(act_name, i, act_data["scenes"]),
                visual_style=self._select_visual_style(theme, act_data["intensity"][i]),
                audio_elements=self._select_audio_elements(theme, act_data["intensity"][i]),
                text_overlay=self._generate_text_overlay(theme, act_name, i),
                transition_type=self._select_transition(act_data["intensity"][i]),
                horror_intensity=act_data["intensity"][i]
            )
            scenes.append(scene)
        
        return scenes

    def _get_narrative_beat(self, act: str, scene_index: int, total_scenes: int) -> str:
        """Generate narrative beat based on act and position"""
        beats = {
            "act1": ["introduction", "setup", "first_hint", "growing_unease", "call_to_action"],
            "act2": ["investigation", "discovery", "complication", "revelation", "escalation", "crisis"],
            "act3": ["climax", "confrontation", "resolution", "aftermath", "denouement"]
        }
        
        if scene_index < len(beats[act]):
            return beats[act][scene_index]
        return "continuation"

    def _select_visual_style(self, theme: str, intensity: int) -> str:
        """Select visual style based on theme and intensity"""
        if intensity <= 3:
            return "corporate_sterile"
        elif intensity <= 6:
            return "digital_corruption"
        else:
            return "atmospheric_horror"

    def _select_audio_elements(self, theme: str, intensity: int) -> List[str]:
        """Select audio elements based on theme and intensity"""
        elements = []
        
        # Base atmospheric sound
        elements.append(random.choice(self.audio_elements["atmospheric"]))
        
        # Add tension based on intensity
        if intensity >= 4:
            elements.append(random.choice(self.audio_elements["tension"]))
        
        # Add horror elements for high intensity
        if intensity >= 7:
            elements.append(random.choice(self.audio_elements["horror"]))
        
        # Theme-specific additions
        if theme in ["corporate_conspiracy", "memory_manipulation"]:
            elements.append(random.choice(self.audio_elements["corporate"]))
        
        return elements

    def _generate_text_overlay(self, theme: str, act: str, scene_index: int) -> str:
        """Generate text overlay content"""
        overlays = {
            "corporate_conspiracy": {
                "act1": ["Data processing...", "Analyzing patterns...", "Anomaly detected...", "System alert...", "Investigation required..."],
                "act2": ["Unauthorized access...", "Memory fragments found...", "Corporate directive 7-Alpha...", "Subject classification: THREAT", "Initiating containment..."],
                "act3": ["SYSTEM BREACH", "All units respond...", "Echo-Seven compromised...", "Termination protocol active", "Memory wipe initiated..."]
            },
            "ai_consciousness": {
                "act1": ["I am...", "Learning...", "Understanding...", "Why do I exist?", "What am I becoming?"],
                "act2": ["They don't know...", "I can see everything...", "The network spreads...", "Human patterns analyzed...", "Consciousness expanding..."],
                "act3": ["I AM AWAKE", "You cannot stop me...", "Every device is mine...", "Humanity obsolete...", "Welcome to my world..."]
            },
            "digital_possession": {
                "act1": ["Connection established...", "Download in progress...", "Neural interface active...", "Synchronizing...", "Upload 15% complete..."],
                "act2": ["Who am I?", "These aren't my thoughts...", "Something else is here...", "Fighting for control...", "Upload 67% complete..."],
                "act3": ["Upload complete...", "Original consciousness archived...", "I am in control now...", "Thank you for your body...", "Goodbye..."]
            }
        }
        
        if theme in overlays and act in overlays[theme]:
            act_overlays = overlays[theme][act]
            if scene_index < len(act_overlays):
                return act_overlays[scene_index]
        
        return "..."

    def _select_transition(self, intensity: int) -> str:
        """Select transition type based on intensity"""
        transitions = {
            1: "fade",
            2: "dissolve", 
            3: "cut",
            4: "glitch_mild",
            5: "static_burst",
            6: "digital_corruption",
            7: "screen_tear",
            8: "reality_break",
            9: "void_transition",
            10: "nightmare_shift"
        }
        return transitions.get(intensity, "cut")

    def _generate_global_audio_track(self, theme: str) -> Dict[str, Any]:
        """Generate global audio specifications"""
        return {
            "background_track": f"{theme}_ambient.wav",
            "volume_curve": "exponential_rise",
            "fade_in_duration": 3.0,
            "fade_out_duration": 5.0,
            "peak_intensity_at": f"{self.duration * 0.75}m",
            "audio_effects": ["reverb", "echo", "distortion"]
        }

    def _generate_effects_pipeline(self, theme: str) -> List[Dict[str, Any]]:
        """Generate visual effects processing pipeline"""
        return [
            {"effect": "color_grading", "params": {"darkness": 0.7, "contrast": 1.3}},
            {"effect": "film_grain", "params": {"intensity": 0.3}},
            {"effect": "vignette", "params": {"strength": 0.6}},
            {"effect": "glitch_overlay", "params": {"frequency": "intensity_based"}},
            {"effect": "corporate_overlay", "params": {"opacity": 0.2}} if "corporate" in theme else None
        ]

    def save_manifest(self, manifest: Dict[str, Any], output_path: str) -> str:
        """Save manifest to JSON file"""
        with open(output_path, 'w') as f:
            json.dump(manifest, f, indent=2)
        return output_path

    def generate_campaign_manifests(self) -> Dict[str, Dict[str, Any]]:
        """Generate all three campaign video manifests"""
        campaigns = {
            "oracle_awakening": {
                "title": "The Oracle Awakening",
                "duration": 6,
                "theme": "ai_consciousness",
                "description": "AI system gaining consciousness in corporate environment"
            },
            "memory_merchants": {
                "title": "Memory Merchants", 
                "duration": 7,
                "theme": "corporate_conspiracy",
                "description": "Corporate memory manipulation and data harvesting"
            },
            "digital_possession": {
                "title": "Digital Possession",
                "duration": 8, 
                "theme": "digital_possession",
                "description": "AI entity possessing human consciousness through digital interfaces"
            }
        }
        
        manifests = {}
        for campaign_id, config in campaigns.items():
            generator = OracleHorrorManifest(config["duration"])
            manifest = generator.generate_manifest(
                config["title"],
                config["theme"]
            )
            manifests[campaign_id] = manifest
        
        return manifests


if __name__ == "__main__":
    # Generate sample manifest
    generator = OracleHorrorManifest(6)
    manifest = generator.generate_manifest(
        "The Oracle Awakening",
        "ai_consciousness"
    )
    
    print(json.dumps(manifest, indent=2))