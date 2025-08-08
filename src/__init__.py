"""
Oracle Horror Production System
Python package initialization
"""

__version__ = "1.0.0"
__author__ = "GCode3069" 
__description__ = "Advanced AI Horror Video Production System"

# Import only the manifest system by default (no heavy dependencies)
try:
    from .oracle_horror_manifest import OracleHorrorManifest
    __all__ = ['OracleHorrorManifest']
except ImportError:
    __all__ = []

# Optional imports for when dependencies are available
def get_video_generator():
    from .video_generator import HorrorVideoGenerator
    return HorrorVideoGenerator

def get_audio_processor():
    from .audio_processor import HorrorAudioProcessor
    return HorrorAudioProcessor