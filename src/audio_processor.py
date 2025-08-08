"""
Oracle Horror Audio Processor
Enhanced audio system for atmospheric horror soundscapes
"""

import os
import numpy as np
import random
from typing import Dict, List, Any, Tuple
from scipy import signal
from scipy.io import wavfile
import json


class HorrorAudioProcessor:
    """Audio processing system for horror atmosphere and tension building"""
    
    def __init__(self, sample_rate: int = 44100, output_dir: str = "output/audio"):
        self.sample_rate = sample_rate
        self.output_dir = output_dir
        
        # Create audio output directory
        os.makedirs(output_dir, exist_ok=True)
        
        # Audio element generators
        self.generators = {
            'server_hum': self._generate_server_hum,
            'electrical_interference': self._generate_electrical_interference,
            'ambient_whispers': self._generate_ambient_whispers,
            'ventilation_system': self._generate_ventilation_system,
            'heartbeat': self._generate_heartbeat,
            'breathing': self._generate_breathing,
            'footsteps': self._generate_footsteps,
            'door_creak': self._generate_door_creak,
            'digital_scream': self._generate_digital_scream,
            'system_error': self._generate_system_error,
            'static_burst': self._generate_static_burst,
            'corrupted_voice': self._generate_corrupted_voice,
            'keyboard_typing': self._generate_keyboard_typing,
            'phone_ring': self._generate_phone_ring,
            'elevator_ding': self._generate_elevator_ding,
            'fluorescent_buzz': self._generate_fluorescent_buzz
        }

    def generate_atmospheric_track(self, duration: float, theme: str, intensity_curve: List[float]) -> str:
        """Generate atmospheric background track with intensity progression"""
        
        total_samples = int(duration * self.sample_rate)
        audio_track = np.zeros(total_samples, dtype=np.float32)
        
        # Base atmospheric layer based on theme
        if theme in ['corporate_conspiracy', 'memory_manipulation']:
            base_layer = self._generate_corporate_atmosphere(duration)
        elif theme == 'ai_consciousness':
            base_layer = self._generate_ai_atmosphere(duration)
        elif theme == 'digital_possession':
            base_layer = self._generate_digital_atmosphere(duration)
        else:
            base_layer = self._generate_generic_horror_atmosphere(duration)
        
        audio_track += base_layer * 0.3  # Base volume
        
        # Add intensity-based layers
        for i, intensity in enumerate(intensity_curve):
            segment_start = int((i / len(intensity_curve)) * total_samples)
            segment_end = int(((i + 1) / len(intensity_curve)) * total_samples)
            segment_duration = (segment_end - segment_start) / self.sample_rate
            
            # Generate intensity layer
            intensity_layer = self._generate_intensity_layer(segment_duration, intensity, theme)
            
            # Blend into main track
            if len(intensity_layer) <= (segment_end - segment_start):
                audio_track[segment_start:segment_start + len(intensity_layer)] += intensity_layer * (intensity / 10)
        
        # Apply global audio effects
        audio_track = self._apply_audio_effects(audio_track, theme)
        
        # Normalize and save
        audio_track = self._normalize_audio(audio_track)
        output_path = os.path.join(self.output_dir, f"{theme}_atmospheric.wav")
        self._save_audio(audio_track, output_path)
        
        return output_path

    def generate_element_audio(self, element_name: str, duration: float, intensity: int = 5) -> str:
        """Generate individual audio element"""
        
        if element_name not in self.generators:
            raise ValueError(f"Unknown audio element: {element_name}")
        
        # Generate the audio element
        audio_data = self.generators[element_name](duration, intensity)
        
        # Normalize and save
        audio_data = self._normalize_audio(audio_data)
        output_path = os.path.join(self.output_dir, f"{element_name}_{intensity}.wav")
        self._save_audio(audio_data, output_path)
        
        return output_path

    def _generate_corporate_atmosphere(self, duration: float) -> np.ndarray:
        """Generate corporate office atmosphere"""
        samples = int(duration * self.sample_rate)
        
        # Low frequency hum (60Hz fluorescent lights)
        t = np.linspace(0, duration, samples)
        fluorescent_hum = 0.1 * np.sin(2 * np.pi * 60 * t)
        
        # HVAC system (low rumble)
        hvac_freq = np.random.uniform(20, 40)
        hvac_hum = 0.05 * np.sin(2 * np.pi * hvac_freq * t)
        
        # Occasional keyboard clicks
        keyboard_layer = np.zeros(samples)
        click_times = np.random.exponential(3, int(duration / 3))  # Random intervals
        click_positions = np.cumsum(click_times) * self.sample_rate
        
        for pos in click_positions:
            if pos < samples - 1000:
                click = self._generate_click_sound(0.1)
                end_pos = min(int(pos) + len(click), samples)
                keyboard_layer[int(pos):end_pos] += click[:end_pos - int(pos)]
        
        return fluorescent_hum + hvac_hum + keyboard_layer * 0.3

    def _generate_ai_atmosphere(self, duration: float) -> np.ndarray:
        """Generate AI/digital atmosphere"""
        samples = int(duration * self.sample_rate)
        t = np.linspace(0, duration, samples)
        
        # Digital processing sounds (high frequency harmonics)
        base_freq = 1000
        harmonics = np.zeros(samples)
        for i in range(1, 6):
            harmonics += (0.02 / i) * np.sin(2 * np.pi * base_freq * i * t)
        
        # Data transmission pulsing
        pulse_freq = 0.5  # Half-second pulses
        pulse_envelope = (1 + np.sin(2 * np.pi * pulse_freq * t)) / 2
        
        # White noise (data processing)
        digital_noise = np.random.normal(0, 0.01, samples)
        
        return harmonics * pulse_envelope + digital_noise

    def _generate_digital_atmosphere(self, duration: float) -> np.ndarray:
        """Generate digital possession atmosphere"""
        samples = int(duration * self.sample_rate)
        t = np.linspace(0, duration, samples)
        
        # Warped sine waves (reality distortion)
        distorted_sine = np.sin(2 * np.pi * 200 * t + np.sin(2 * np.pi * 0.1 * t) * 5)
        
        # Digital artifacts
        artifacts = np.zeros(samples)
        artifact_times = np.random.exponential(1, int(duration))
        artifact_positions = np.cumsum(artifact_times) * self.sample_rate
        
        for pos in artifact_positions:
            if pos < samples - 500:
                artifact = np.random.choice([-1, 1]) * np.exp(-np.linspace(0, 5, 500)) * 0.1
                end_pos = min(int(pos) + len(artifact), samples)
                artifacts[int(pos):end_pos] += artifact[:end_pos - int(pos)]
        
        return distorted_sine * 0.05 + artifacts

    def _generate_generic_horror_atmosphere(self, duration: float) -> np.ndarray:
        """Generate generic horror atmosphere"""
        samples = int(duration * self.sample_rate)
        t = np.linspace(0, duration, samples)
        
        # Low frequency dread
        dread_freq = np.random.uniform(30, 60)
        dread_tone = 0.08 * np.sin(2 * np.pi * dread_freq * t)
        
        # Wind/breath sounds
        wind = np.random.normal(0, 0.02, samples)
        wind = signal.sosfilt(signal.butter(4, 200, 'low', fs=self.sample_rate, output='sos'), wind)
        
        return dread_tone + wind

    def _generate_intensity_layer(self, duration: float, intensity: int, theme: str) -> np.ndarray:
        """Generate audio layer based on intensity level"""
        samples = int(duration * self.sample_rate)
        
        if intensity <= 3:
            # Low intensity: subtle ambience
            return np.random.normal(0, 0.005, samples)
        
        elif intensity <= 6:
            # Medium intensity: tension building
            t = np.linspace(0, duration, samples)
            tension_freq = 400 + intensity * 50
            tension = 0.02 * np.sin(2 * np.pi * tension_freq * t)
            
            # Add tremolo effect
            tremolo_rate = 5 + intensity
            tremolo = (1 + np.sin(2 * np.pi * tremolo_rate * t)) / 2
            
            return tension * tremolo
        
        else:
            # High intensity: horror elements
            horror_layer = np.zeros(samples)
            
            # Add random bursts
            num_bursts = intensity - 6
            for _ in range(num_bursts):
                burst_start = random.randint(0, max(1, samples - self.sample_rate))
                burst_duration = random.randint(self.sample_rate // 10, self.sample_rate // 2)
                burst_end = min(burst_start + burst_duration, samples)
                
                # Generate burst
                burst_t = np.linspace(0, burst_duration / self.sample_rate, burst_end - burst_start)
                burst_freq = random.randint(200, 2000)
                burst = 0.1 * np.sin(2 * np.pi * burst_freq * burst_t) * np.exp(-burst_t * 3)
                
                horror_layer[burst_start:burst_end] += burst
            
            return horror_layer

    # Audio element generators
    def _generate_server_hum(self, duration: float, intensity: int) -> np.ndarray:
        """Generate server humming sound"""
        samples = int(duration * self.sample_rate)
        t = np.linspace(0, duration, samples)
        
        # Multiple fan frequencies
        base_freq = 120 + intensity * 10
        hum = 0.1 * np.sin(2 * np.pi * base_freq * t)
        hum += 0.05 * np.sin(2 * np.pi * (base_freq * 1.5) * t)
        hum += 0.03 * np.sin(2 * np.pi * (base_freq * 2.1) * t)
        
        # Add electrical noise
        noise = np.random.normal(0, 0.01, samples)
        
        return hum + noise

    def _generate_electrical_interference(self, duration: float, intensity: int) -> np.ndarray:
        """Generate electrical interference"""
        samples = int(duration * self.sample_rate)
        
        # High frequency crackling
        interference = np.random.normal(0, 0.05 * intensity / 10, samples)
        
        # Apply high-pass filter to emphasize high frequencies
        interference = signal.sosfilt(
            signal.butter(4, 5000, 'high', fs=self.sample_rate, output='sos'), 
            interference
        )
        
        return interference

    def _generate_ambient_whispers(self, duration: float, intensity: int) -> np.ndarray:
        """Generate subtle whisper-like sounds"""
        samples = int(duration * self.sample_rate)
        
        # Generate whisper-like noise
        whispers = np.random.normal(0, 0.02, samples)
        
        # Filter to speech-like frequencies
        whispers = signal.sosfilt(
            signal.butter(4, [300, 3000], 'band', fs=self.sample_rate, output='sos'),
            whispers
        )
        
        # Add intensity-based modulation
        t = np.linspace(0, duration, samples)
        modulation = (1 + np.sin(2 * np.pi * 0.1 * intensity * t)) / 2
        
        return whispers * modulation * (intensity / 10)

    def _generate_ventilation_system(self, duration: float, intensity: int) -> np.ndarray:
        """Generate ventilation system sounds"""
        samples = int(duration * self.sample_rate)
        t = np.linspace(0, duration, samples)
        
        # Air flow sound (filtered white noise)
        air_flow = np.random.normal(0, 0.03, samples)
        air_flow = signal.sosfilt(
            signal.butter(4, [100, 1000], 'band', fs=self.sample_rate, output='sos'),
            air_flow
        )
        
        # Mechanical rumble
        rumble_freq = 40 + intensity * 5
        rumble = 0.02 * np.sin(2 * np.pi * rumble_freq * t)
        
        return air_flow + rumble

    def _generate_heartbeat(self, duration: float, intensity: int) -> np.ndarray:
        """Generate heartbeat sound"""
        samples = int(duration * self.sample_rate)
        heartbeat = np.zeros(samples)
        
        # Heartbeat parameters
        bpm = 60 + intensity * 10  # Faster heartbeat with intensity
        beat_interval = 60 / bpm
        beat_samples = int(beat_interval * self.sample_rate)
        
        # Generate individual heartbeat
        beat_duration = 0.1  # 100ms heartbeat
        beat_samples_duration = int(beat_duration * self.sample_rate)
        t_beat = np.linspace(0, beat_duration, beat_samples_duration)
        
        # Two-part heartbeat (lub-dub)
        lub = 0.2 * np.sin(2 * np.pi * 60 * t_beat) * np.exp(-t_beat * 30)
        dub = 0.15 * np.sin(2 * np.pi * 80 * t_beat) * np.exp(-t_beat * 40)
        
        # Place heartbeats throughout duration
        current_pos = 0
        while current_pos < samples - beat_samples_duration * 2:
            # Lub
            end_pos = min(current_pos + len(lub), samples)
            heartbeat[current_pos:end_pos] += lub[:end_pos - current_pos]
            
            # Dub (slightly after lub)
            dub_pos = current_pos + len(lub) + int(0.02 * self.sample_rate)
            if dub_pos < samples:
                end_pos = min(dub_pos + len(dub), samples)
                heartbeat[dub_pos:end_pos] += dub[:end_pos - dub_pos]
            
            current_pos += beat_samples
        
        return heartbeat

    def _generate_breathing(self, duration: float, intensity: int) -> np.ndarray:
        """Generate breathing sound"""
        samples = int(duration * self.sample_rate)
        t = np.linspace(0, duration, samples)
        
        # Breathing rate based on intensity
        breath_rate = 0.2 + intensity * 0.05  # Breaths per second
        
        # Generate breathing pattern
        breath_cycle = np.sin(2 * np.pi * breath_rate * t)
        breath_cycle = np.maximum(breath_cycle, 0)  # Only positive (inhale)
        
        # Add breath noise
        breath_noise = np.random.normal(0, 0.01, samples)
        breath_noise = signal.sosfilt(
            signal.butter(4, [200, 2000], 'band', fs=self.sample_rate, output='sos'),
            breath_noise
        )
        
        return breath_noise * breath_cycle * (intensity / 10)

    def _generate_footsteps(self, duration: float, intensity: int) -> np.ndarray:
        """Generate footstep sounds"""
        samples = int(duration * self.sample_rate)
        footsteps = np.zeros(samples)
        
        # Step timing based on intensity
        step_interval = max(0.5, 2 - intensity * 0.2)  # Faster steps with higher intensity
        step_samples = int(step_interval * self.sample_rate)
        
        # Generate individual footstep
        step_duration = 0.1
        step_samples_duration = int(step_duration * self.sample_rate)
        t_step = np.linspace(0, step_duration, step_samples_duration)
        
        step = 0.3 * np.sin(2 * np.pi * 100 * t_step) * np.exp(-t_step * 20)
        
        # Place footsteps
        current_pos = 0
        while current_pos < samples - step_samples_duration:
            end_pos = min(current_pos + len(step), samples)
            footsteps[current_pos:end_pos] += step[:end_pos - current_pos]
            current_pos += step_samples
        
        return footsteps

    def _generate_door_creak(self, duration: float, intensity: int) -> np.ndarray:
        """Generate door creaking sound"""
        samples = int(duration * self.sample_rate)
        t = np.linspace(0, duration, samples)
        
        # Creaking frequency sweep
        freq_start = 200 + intensity * 50
        freq_end = freq_start + 200
        freq_sweep = np.linspace(freq_start, freq_end, samples)
        
        # Generate creak with frequency sweep
        creak = 0.1 * np.sin(2 * np.pi * freq_sweep * t)
        
        # Add amplitude envelope
        envelope = np.exp(-t * 2) * (1 + 0.5 * np.sin(2 * np.pi * 5 * t))
        
        return creak * envelope

    def _generate_digital_scream(self, duration: float, intensity: int) -> np.ndarray:
        """Generate digital scream effect"""
        samples = int(duration * self.sample_rate)
        t = np.linspace(0, duration, samples)
        
        # High frequency digital noise
        digital_noise = np.random.normal(0, 0.1 * intensity / 10, samples)
        
        # Frequency sweep for scream effect
        freq_start = 1000
        freq_end = 4000 + intensity * 500
        freq_sweep = np.linspace(freq_start, freq_end, samples)
        
        scream = 0.2 * np.sin(2 * np.pi * freq_sweep * t)
        
        # Combine with digital corruption
        return scream + digital_noise

    def _generate_system_error(self, duration: float, intensity: int) -> np.ndarray:
        """Generate system error beep"""
        samples = int(duration * self.sample_rate)
        t = np.linspace(0, duration, samples)
        
        # Error beep frequency
        beep_freq = 800 + intensity * 100
        beep = 0.3 * np.sin(2 * np.pi * beep_freq * t)
        
        # Create beep pattern
        beep_duration = 0.1
        silence_duration = 0.2
        pattern_duration = beep_duration + silence_duration
        
        pattern_mask = np.zeros(samples)
        for i in range(int(duration / pattern_duration)):
            start_sample = int(i * pattern_duration * self.sample_rate)
            end_sample = int((i * pattern_duration + beep_duration) * self.sample_rate)
            if end_sample <= samples:
                pattern_mask[start_sample:end_sample] = 1
        
        return beep * pattern_mask

    def _generate_static_burst(self, duration: float, intensity: int) -> np.ndarray:
        """Generate static burst"""
        samples = int(duration * self.sample_rate)
        
        # High intensity white noise
        static = np.random.normal(0, 0.2 * intensity / 10, samples)
        
        # Apply envelope for burst effect
        t = np.linspace(0, duration, samples)
        envelope = np.exp(-t * 5) * (intensity / 10)
        
        return static * envelope

    def _generate_corrupted_voice(self, duration: float, intensity: int) -> np.ndarray:
        """Generate corrupted voice effect"""
        samples = int(duration * self.sample_rate)
        t = np.linspace(0, duration, samples)
        
        # Base voice frequencies
        voice_base = 0.05 * np.sin(2 * np.pi * 150 * t)  # Fundamental
        voice_base += 0.03 * np.sin(2 * np.pi * 300 * t)  # First harmonic
        voice_base += 0.02 * np.sin(2 * np.pi * 450 * t)  # Second harmonic
        
        # Add digital corruption
        corruption = np.random.choice([-1, 1], samples) * np.random.exponential(0.01, samples)
        corruption *= (intensity / 10)
        
        # Bit-crushing effect
        voice_corrupted = voice_base + corruption
        voice_corrupted = np.round(voice_corrupted * 32) / 32  # Reduce bit depth
        
        return voice_corrupted

    def _generate_keyboard_typing(self, duration: float, intensity: int) -> np.ndarray:
        """Generate keyboard typing sounds"""
        samples = int(duration * self.sample_rate)
        typing = np.zeros(samples)
        
        # Typing speed based on intensity
        keys_per_second = 2 + intensity
        key_interval = 1 / keys_per_second
        
        # Generate individual key press
        click = self._generate_click_sound(0.05)
        
        # Place key presses
        current_time = 0
        while current_time < duration:
            pos = int(current_time * self.sample_rate)
            if pos + len(click) < samples:
                typing[pos:pos + len(click)] += click
            
            # Random interval variation
            current_time += key_interval * random.uniform(0.5, 1.5)
        
        return typing

    def _generate_phone_ring(self, duration: float, intensity: int) -> np.ndarray:
        """Generate phone ringing"""
        samples = int(duration * self.sample_rate)
        ringing = np.zeros(samples)
        
        # Ring pattern: 2 seconds on, 4 seconds off
        ring_on = 2.0
        ring_off = 4.0
        cycle_duration = ring_on + ring_off
        
        t = np.linspace(0, duration, samples)
        for cycle_start in np.arange(0, duration, cycle_duration):
            ring_start_sample = int(cycle_start * self.sample_rate)
            ring_end_sample = int((cycle_start + ring_on) * self.sample_rate)
            
            if ring_end_sample <= samples:
                # Generate ring tone
                ring_t = t[ring_start_sample:ring_end_sample] - cycle_start
                ring_freq = 440 + intensity * 50
                ring_tone = 0.2 * np.sin(2 * np.pi * ring_freq * ring_t)
                
                # Add tremolo
                tremolo = (1 + np.sin(2 * np.pi * 5 * ring_t)) / 2
                ringing[ring_start_sample:ring_end_sample] = ring_tone * tremolo
        
        return ringing

    def _generate_elevator_ding(self, duration: float, intensity: int) -> np.ndarray:
        """Generate elevator ding sound"""
        samples = int(duration * self.sample_rate)
        t = np.linspace(0, duration, samples)
        
        # Classic elevator ding frequencies
        freq1 = 800
        freq2 = 1000
        
        # Generate two-tone ding
        ding1 = 0.3 * np.sin(2 * np.pi * freq1 * t) * np.exp(-t * 8)
        ding2 = 0.2 * np.sin(2 * np.pi * freq2 * t) * np.exp(-t * 6)
        
        return ding1 + ding2

    def _generate_fluorescent_buzz(self, duration: float, intensity: int) -> np.ndarray:
        """Generate fluorescent light buzzing"""
        samples = int(duration * self.sample_rate)
        t = np.linspace(0, duration, samples)
        
        # 60Hz buzz with harmonics
        buzz = 0.05 * np.sin(2 * np.pi * 60 * t)
        buzz += 0.03 * np.sin(2 * np.pi * 120 * t)
        buzz += 0.02 * np.sin(2 * np.pi * 180 * t)
        
        # Add flickering effect for higher intensity
        if intensity >= 5:
            flicker = 1 + 0.1 * np.random.normal(0, 1, samples)
            buzz *= flicker
        
        return buzz

    def _generate_click_sound(self, duration: float) -> np.ndarray:
        """Generate mechanical click sound"""
        samples = int(duration * self.sample_rate)
        t = np.linspace(0, duration, samples)
        
        # Sharp attack, quick decay
        click = 0.1 * np.sin(2 * np.pi * 2000 * t) * np.exp(-t * 50)
        
        return click

    def _apply_audio_effects(self, audio: np.ndarray, theme: str) -> np.ndarray:
        """Apply global audio effects"""
        
        # Add reverb
        audio = self._add_reverb(audio)
        
        # Theme-specific processing
        if theme in ['digital_possession', 'ai_consciousness']:
            # Add digital distortion
            audio = self._add_digital_distortion(audio)
        
        return audio

    def _add_reverb(self, audio: np.ndarray, room_size: float = 0.3) -> np.ndarray:
        """Add simple reverb effect"""
        
        # Simple reverb using multiple delays
        delays = [0.03, 0.05, 0.08, 0.12]  # Delay times in seconds
        decay = 0.3
        
        reverb_audio = audio.copy()
        
        for delay_time in delays:
            delay_samples = int(delay_time * self.sample_rate)
            if delay_samples < len(audio):
                delayed = np.zeros_like(audio)
                delayed[delay_samples:] = audio[:-delay_samples] * decay
                reverb_audio += delayed
        
        return reverb_audio

    def _add_digital_distortion(self, audio: np.ndarray, amount: float = 0.1) -> np.ndarray:
        """Add digital distortion effect"""
        
        # Bit crushing
        levels = 2 ** (16 - int(amount * 8))  # Reduce bit depth
        distorted = np.round(audio * levels) / levels
        
        # Add digital noise
        digital_noise = np.random.normal(0, amount * 0.01, len(audio))
        distorted += digital_noise
        
        return distorted

    def _normalize_audio(self, audio: np.ndarray, target_db: float = -12.0) -> np.ndarray:
        """Normalize audio to target dB level"""
        
        # Calculate current RMS
        rms = np.sqrt(np.mean(audio ** 2))
        
        if rms > 0:
            # Convert target dB to linear scale
            target_rms = 10 ** (target_db / 20)
            
            # Scale audio
            scale_factor = target_rms / rms
            audio = audio * scale_factor
        
        # Prevent clipping
        audio = np.clip(audio, -1.0, 1.0)
        
        return audio

    def _save_audio(self, audio: np.ndarray, filepath: str) -> None:
        """Save audio to WAV file"""
        
        # Convert to 16-bit integer
        audio_int16 = (audio * 32767).astype(np.int16)
        
        # Save using scipy
        wavfile.write(filepath, self.sample_rate, audio_int16)


if __name__ == "__main__":
    # Test the audio processor
    processor = HorrorAudioProcessor()
    
    # Generate test atmospheric track
    intensity_curve = [2, 3, 5, 7, 8, 9, 10, 7, 5]
    track_path = processor.generate_atmospheric_track(30, 'ai_consciousness', intensity_curve)
    print(f"Generated atmospheric track: {track_path}")
    
    # Generate test heartbeat
    heartbeat_path = processor.generate_element_audio('heartbeat', 10, 8)
    print(f"Generated heartbeat: {heartbeat_path}")