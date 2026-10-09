#!/usr/bin/env python3
"""
Kinetic Typography SFX Suite (Viral Subtitle & Motion Audio Generator)
Broadcast 48kHz audio generation for:
- kinetic_pop_bubble.wav (Word highlight pop / Submagic bounce)
- kinetic_sub_slam.wav (Hard impact for key punchlines)
- kinetic_riser_tension.wav (Pre-drop riser / whoosh build)
- kinetic_marker_swoosh.wav (Fast marker underline / sweep)
- kinetic_typewriter_click.wav (Crisp tactile character entrance)
"""

import os
import wave
import numpy as np

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR = os.path.join(BASE_DIR, "sfx_audio")
os.makedirs(OUTPUT_DIR, exist_ok=True)

SAMPLE_RATE = 48000

def save_wav(filename, samples):
    filepath = os.path.join(OUTPUT_DIR, filename)
    max_val = np.max(np.abs(samples))
    if max_val > 0:
        samples = samples / max_val * 0.90
    int_samples = np.int16(samples * 32767)
    with wave.open(filepath, 'w') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(SAMPLE_RATE)
        wf.writeframes(int_samples.tobytes())
    print(f"Generated Kinetic SFX: {filename} ({len(samples)/SAMPLE_RATE:.2f}s)")

def make_pop_bubble():
    # Rapid pitch-down sine sweep (350Hz -> 180Hz) with sharp attack (70ms)
    duration = 0.075
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), False)
    freq = np.linspace(520, 180, len(t))
    phase = 2 * np.pi * np.cumsum(freq) / SAMPLE_RATE
    env = (1 - np.cos(np.pi * t / (duration * 0.2))) / 2
    env[int(len(t)*0.2):] = np.exp(-12 * (t[int(len(t)*0.2):] - t[int(len(t)*0.2)]))
    samples = np.sin(phase) * env
    save_wav("kinetic_pop_bubble.wav", samples)

def make_sub_slam():
    # Massive sub-bass punch (80Hz -> 38Hz) with slight transient click (0.65s)
    duration = 0.65
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), False)
    freq = 78 * np.exp(-t * 3.5) + 36
    phase = 2 * np.pi * np.cumsum(freq) / SAMPLE_RATE
    sub = np.sin(phase) * np.exp(-t * 4.2)
    # transient punch
    transient = np.sin(2 * np.pi * 320 * t[:int(SAMPLE_RATE * 0.02)]) * np.exp(-t[:int(SAMPLE_RATE * 0.02)] * 200)
    sub[:len(transient)] += transient * 0.4
    save_wav("kinetic_sub_slam.wav", sub)

def make_riser_tension():
    # Tension building pitch riser (200Hz -> 850Hz) with subtle white noise (0.8s)
    duration = 0.8
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), False)
    freq = 180 + 720 * (t / duration) ** 2
    phase = 2 * np.pi * np.cumsum(freq) / SAMPLE_RATE
    env = (t / duration) ** 2
    noise = (np.random.rand(len(t)) * 2 - 1) * 0.15
    samples = (np.sin(phase) * 0.85 + noise) * env
    save_wav("kinetic_riser_tension.wav", samples)

def make_marker_swoosh():
    # Fast filtered noise whoosh for dynamic underline / pill highlight (0.18s)
    duration = 0.18
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), False)
    noise = np.random.rand(len(t)) * 2 - 1
    env = np.sin(np.pi * t / duration) ** 2
    # simple lowpass / bandpass simulation
    carrier = np.sin(2 * np.pi * 800 * t)
    samples = noise * env * 0.6 + carrier * env * 0.4
    save_wav("kinetic_marker_swoosh.wav", samples)

def make_typewriter_click():
    # Ultra-sharp mechanical keyboard tick (35ms)
    duration = 0.035
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), False)
    click = (np.sin(2 * np.pi * 2800 * t) * 0.6 + np.sin(2 * np.pi * 5200 * t) * 0.4) * np.exp(-t * 220)
    save_wav("kinetic_typewriter_click.wav", click)

if __name__ == "__main__":
    make_pop_bubble()
    make_sub_slam()
    make_riser_tension()
    make_marker_swoosh()
    make_typewriter_click()
    print("All kinetic subtitle SFX generated successfully!")
