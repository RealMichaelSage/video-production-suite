#!/usr/bin/env python3
"""
HUD & Sci-Fi SFX Generator (Procedural Audio Synthesis)
Generates studio-grade sound effects for UI, HUD elements, transitions, and video motion.
"""

import os
import wave
import struct
import numpy as np

OUTPUT_DIR = "/Users/michaelsage/Desktop/Vibes/Assets/video_production_vault/sfx_audio"
os.makedirs(OUTPUT_DIR, exist_ok=True)
SAMPLE_RATE = 48000  # Broadcast standard 48kHz

def save_wav(filename, samples):
    filepath = os.path.join(OUTPUT_DIR, filename)
    # Normalize to -1 dB to prevent clipping
    max_val = np.max(np.abs(samples))
    if max_val > 0:
        samples = samples / max_val * 0.89
    
    # Convert to 16-bit PCM
    int_samples = np.int16(samples * 32767)
    with wave.open(filepath, 'w') as wf:
        wf.setnchannels(1)  # Mono for precise positioning
        wf.setsampwidth(2)  # 16-bit
        wf.setframerate(SAMPLE_RATE)
        wf.writeframes(int_samples.tobytes())
    print(f"Generated SFX: {filename} ({len(samples)/SAMPLE_RATE:.2f}s)")

def make_ui_click():
    # Crisp mechanical UI click (50ms)
    t = np.linspace(0, 0.05, int(SAMPLE_RATE * 0.05), False)
    decay = np.exp(-t * 120)
    wave_data = np.sin(2 * np.pi * 1800 * t) * decay + np.sin(2 * np.pi * 3200 * t) * decay * 0.5
    save_wav("ui_click_sharp.wav", wave_data)

def make_target_lock():
    # 3 rapid tactical chirps ascending in pitch (150ms total)
    total_len = int(SAMPLE_RATE * 0.28)
    out = np.zeros(total_len)
    freqs = [1200, 1600, 2400]
    chirp_dur = int(SAMPLE_RATE * 0.06)
    
    for i, f in enumerate(freqs):
        offset = int(i * SAMPLE_RATE * 0.08)
        t = np.linspace(0, 0.06, chirp_dur, False)
        env = np.sin(np.pi * t / 0.06) ** 2
        chirp = np.sin(2 * np.pi * f * t) * env
        out[offset:offset+chirp_dur] += chirp
        
    save_wav("ui_target_lock.wav", out)

def make_radar_ping():
    # Resonant submarine/tactical radar sonar ping with harmonic reverb tail (1.2s)
    t = np.linspace(0, 1.2, int(SAMPLE_RATE * 1.2), False)
    decay = np.exp(-t * 4.5)
    f0 = 950
    ping = (np.sin(2 * np.pi * f0 * t) + 
            0.4 * np.sin(2 * np.pi * (f0 * 2) * t) + 
            0.2 * np.sin(2 * np.pi * (f0 * 3) * t)) * decay
    save_wav("ui_radar_ping.wav", ping)

def make_glitch_whoosh():
    # Dynamic transition whoosh with digital white noise sweep (0.4s)
    dur = 0.4
    t = np.linspace(0, dur, int(SAMPLE_RATE * dur), False)
    noise = np.random.uniform(-1, 1, len(t))
    # Frequency sweep filter simulation
    sweep = np.sin(2 * np.pi * (150 + 800 * (t / dur) ** 2) * t)
    env = np.sin(np.pi * t / dur) ** 1.8
    out = (noise * 0.6 + sweep * 0.4) * env
    save_wav("ui_glitch_whoosh.wav", out)

def make_data_telemetry_chatter():
    # Rapid digital data calculation stream (0.8s)
    dur = 0.8
    total_len = int(SAMPLE_RATE * dur)
    out = np.zeros(total_len)
    np.random.seed(42)
    
    num_blips = 32
    for _ in range(num_blips):
        idx = int(np.random.uniform(0, total_len - 1000))
        freq = np.random.choice([1400, 1750, 2100, 2600, 3100])
        blip_t = np.linspace(0, 0.015, int(SAMPLE_RATE * 0.015), False)
        blip = np.sin(2 * np.pi * freq * blip_t) * np.exp(-blip_t * 300)
        out[idx:idx+len(blip)] += blip * 0.4
        
    save_wav("ui_data_telemetry.wav", out)

def make_sub_impact():
    # Cinematic sub-bass drop / impact hit for chapter titles or dramatic reveal (1.0s)
    dur = 1.0
    t = np.linspace(0, dur, int(SAMPLE_RATE * dur), False)
    freq = 120 * np.exp(-t * 5.0) + 38  # Glides from 158Hz down to 38Hz
    env = np.exp(-t * 3.2)
    punch = np.sin(2 * np.pi * freq * t) * env
    save_wav("ui_sub_impact.wav", punch)

def make_scanner_hum():
    # Looping sci-fi scanner / laser beam LFO hum (2.0s)
    dur = 2.0
    t = np.linspace(0, dur, int(SAMPLE_RATE * dur), False)
    lfo = 1.0 + 0.3 * np.sin(2 * np.pi * 5.0 * t)  # 5Hz modulation
    carrier = np.sin(2 * np.pi * 320 * t) * lfo
    harm = 0.3 * np.sin(2 * np.pi * 640 * t)
    out = (carrier + harm) * 0.5
    save_wav("ui_scanner_hum.wav", out)

if __name__ == "__main__":
    print(f"Synthesizing HUD SFX suite into {OUTPUT_DIR}...")
    make_ui_click()
    make_target_lock()
    make_radar_ping()
    make_glitch_whoosh()
    make_data_telemetry_chatter()
    make_sub_impact()
    make_scanner_hum()
    print("All HUD SFX generated successfully!")
