#!/usr/bin/env python3
"""
Procedural 60 FPS Tactical HUD Video Generator (9:16 & 16:9)
Renders ultra-crisp, broadcast-grade Sci-Fi HUD overlays on black background
ready for 1-command blend='screen' compositing in FFmpeg.
"""

import os
import sys
import math
import subprocess
import numpy as np
from PIL import Image, ImageDraw, ImageFont

WIDTH = 1080
HEIGHT = 1920
FPS = 60
DURATION_SEC = 5.0
TOTAL_FRAMES = int(FPS * DURATION_SEC)
OUTPUT_DIR = "/Users/michaelsage/Desktop/Vibes/Assets/video_production_vault/hud_overlays"
os.makedirs(OUTPUT_DIR, exist_ok=True)
OUTPUT_VIDEO = os.path.join(OUTPUT_DIR, "tactical_hud_9x16_60fps.mp4")

# Color Palette (High-Contrast Cyber Cyan / Neon Emerald / Warning Amber)
COLOR_CYAN = (0, 245, 255)
COLOR_EMERALD = (0, 255, 157)
COLOR_AMBER = (255, 184, 0)
COLOR_RED = (255, 59, 48)
COLOR_DIM = (0, 110, 128)
COLOR_GRID = (0, 45, 55)

def draw_hud_frame(frame_idx):
    # Create black canvas
    img = Image.new("RGB", (WIDTH, HEIGHT), (0, 0, 0))
    draw = ImageDraw.Draw(img)
    t = frame_idx / FPS
    progress = frame_idx / TOTAL_FRAMES

    # --- 1. Subtle Background Grid (50px) ---
    grid_step = 60
    for x in range(grid_step, WIDTH, grid_step * 2):
        draw.line([(x, 100), (x, HEIGHT - 100)], fill=(0, 25, 30), width=1)
    for y in range(160, HEIGHT - 160, grid_step * 2):
        draw.line([(60, y), (WIDTH - 60, y)], fill=(0, 25, 30), width=1)

    # --- 2. Four Corner Tactical Brackets ---
    pad = 50
    blen = 90
    bw = 3
    # Top-Left
    draw.line([(pad, pad), (pad + blen, pad)], fill=COLOR_CYAN, width=bw)
    draw.line([(pad, pad), (pad, pad + blen)], fill=COLOR_CYAN, width=bw)
    draw.rectangle([pad + 6, pad + 6, pad + 14, pad + 14], fill=COLOR_CYAN)
    
    # Top-Right
    draw.line([(WIDTH - pad - blen, pad), (WIDTH - pad, pad)], fill=COLOR_CYAN, width=bw)
    draw.line([(WIDTH - pad, pad), (WIDTH - pad, pad + blen)], fill=COLOR_CYAN, width=bw)
    draw.rectangle([WIDTH - pad - 14, pad + 6, WIDTH - pad - 6, pad + 14], fill=COLOR_CYAN)

    # Bottom-Left
    draw.line([(pad, HEIGHT - pad), (pad + blen, HEIGHT - pad)], fill=COLOR_CYAN, width=bw)
    draw.line([(pad, HEIGHT - pad - blen), (pad, HEIGHT - pad)], fill=COLOR_CYAN, width=bw)

    # Bottom-Right
    draw.line([(WIDTH - pad - blen, HEIGHT - pad), (WIDTH - pad, HEIGHT - pad)], fill=COLOR_CYAN, width=bw)
    draw.line([(WIDTH - pad, HEIGHT - pad - blen), (WIDTH - pad, HEIGHT - pad)], fill=COLOR_CYAN, width=bw)

    # --- 3. Top Header Bar (Telemetry, Timecode, Status) ---
    rec_blink = (int(t * 2) % 2) == 0
    if rec_blink:
        draw.ellipse([pad + 30, pad + 12, pad + 46, pad + 28], fill=COLOR_RED)
    draw.text((pad + 56, pad + 10), "REC  [RAW 4K 60FPS]", fill=(240, 240, 240))
    
    # Live Simulated Timecode
    sec = int(t) % 60
    msec = int((t - int(t)) * 100)
    tc_str = f"TC 00:04:{sec:02d}:{msec:02d}"
    draw.text((WIDTH // 2 - 80, pad + 10), tc_str, fill=COLOR_AMBER)

    draw.text((WIDTH - pad - 260, pad + 10), "SYS: ARMED // NET: SECURE", fill=COLOR_EMERALD)
    draw.line([(pad, pad + 38), (WIDTH - pad, pad + 38)], fill=COLOR_DIM, width=1)

    # Coordinates ticker
    coord_str = f"LAT 55°45'21.4\"N  |  LON 37°37'04.1\"E  |  ALT 418.2M  |  HEADING 084°"
    draw.text((pad + 30, pad + 46), coord_str, fill=COLOR_DIM)

    # --- 4. Center Tactical Reticle (Crosshair & Rotating Ring) ---
    cx, cy = WIDTH // 2, HEIGHT // 2 - 40
    r_outer = 180
    r_inner = 130
    
    # Rotating outer tick ring
    angle_offset = t * 45.0  # 45 deg per sec
    draw.ellipse([cx - r_outer, cy - r_outer, cx + r_outer, cy + r_outer], outline=COLOR_DIM, width=1)
    for a in range(0, 360, 15):
        rad = math.radians(a + angle_offset)
        x1 = cx + (r_outer - 8) * math.cos(rad)
        y1 = cy + (r_outer - 8) * math.sin(rad)
        x2 = cx + r_outer * math.cos(rad)
        y2 = cy + r_outer * math.sin(rad)
        col = COLOR_CYAN if (a % 45 == 0) else COLOR_DIM
        draw.line([(x1, y1), (x2, y2)], fill=col, width=2 if (a % 45 == 0) else 1)

    # Inner targeting brackets
    pulse = 1.0 + 0.05 * math.sin(t * 8.0)
    b_size = int(65 * pulse)
    bracket_col = COLOR_EMERALD if (int(t * 1.5) % 2 == 0) else COLOR_CYAN
    draw.line([(cx - b_size, cy - b_size), (cx - b_size + 24, cy - b_size)], fill=bracket_col, width=2)
    draw.line([(cx - b_size, cy - b_size), (cx - b_size, cy - b_size + 24)], fill=bracket_col, width=2)
    draw.line([(cx + b_size, cy - b_size), (cx + b_size - 24, cy - b_size)], fill=bracket_col, width=2)
    draw.line([(cx + b_size, cy - b_size), (cx + b_size, cy - b_size + 24)], fill=bracket_col, width=2)
    draw.line([(cx - b_size, cy + b_size), (cx - b_size + 24, cy + b_size)], fill=bracket_col, width=2)
    draw.line([(cx - b_size, cy + b_size), (cx - b_size, cy + b_size - 24)], fill=bracket_col, width=2)
    draw.line([(cx + b_size, cy + b_size), (cx + b_size - 24, cy + b_size)], fill=bracket_col, width=2)
    draw.line([(cx + b_size, cy + b_size), (cx + b_size, cy + b_size - 24)], fill=bracket_col, width=2)

    # Center Crosshair with micro-gap
    gap = 8
    draw.line([(cx - 24, cy), (cx - gap, cy)], fill=COLOR_CYAN, width=2)
    draw.line([(cx + gap, cy), (cx + 24, cy)], fill=COLOR_CYAN, width=2)
    draw.line([(cx, cy - 24), (cx, cy - gap)], fill=COLOR_CYAN, width=2)
    draw.line([(cx, cy + gap), (cx, cy + 24)], fill=COLOR_CYAN, width=2)

    # Target Lock Status
    dist_val = 42.8 + 1.2 * math.sin(t * 3.0)
    draw.text((cx - 55, cy + b_size + 14), f"LOCK  {dist_val:.1f}M", fill=bracket_col)

    # --- 5. Bottom Left Radar Scanner ---
    rx, ry = 220, HEIGHT - 340
    radar_r = 140
    draw.ellipse([rx - radar_r, ry - radar_r, rx + radar_r, ry + radar_r], outline=COLOR_DIM, width=1)
    draw.ellipse([rx - radar_r // 2, ry - radar_r // 2, rx + radar_r // 2, ry + radar_r // 2], outline=COLOR_GRID, width=1)
    draw.line([(rx - radar_r, ry), (rx + radar_r, ry)], fill=COLOR_GRID, width=1)
    draw.line([(rx, ry - radar_r), (rx, ry + radar_r)], fill=COLOR_GRID, width=1)
    
    # Rotating Radar Sweep line
    sweep_rad = (t * 2.0 * math.pi) % (2.0 * math.pi)
    sx = rx + radar_r * math.cos(sweep_rad)
    sy = ry + radar_r * math.sin(sweep_rad)
    draw.line([(rx, ry), (sx, sy)], fill=COLOR_EMERALD, width=2)

    # Radar Blips (Targets)
    blips = [
        (rx + 45, ry - 60, 0.2),
        (rx - 70, ry + 30, 0.7),
        (rx + 80, ry + 50, 1.4)
    ]
    for bx, by, phase in blips:
        blip_intensity = math.exp(-((t - phase) % 1.0) * 3.5)
        if blip_intensity > 0.15:
            b_alpha = int(255 * blip_intensity)
            draw.ellipse([bx - 4, by - 4, bx + 4, by + 4], fill=(0, b_alpha, int(b_alpha * 0.6)))
            draw.text((bx + 8, by - 6), "TGT_01", fill=(0, b_alpha, b_alpha))

    draw.text((rx - 45, ry + radar_r + 14), "RADAR 360° // 5KM", fill=COLOR_DIM)

    # --- 6. Bottom Right Audio Spectrum / Hex Telemetry ---
    spec_x = WIDTH - 420
    spec_y = HEIGHT - 380
    draw.text((spec_x, spec_y), "AUDIO FREQ SPECTRUM // CH 1-2", fill=COLOR_CYAN)
    
    num_bars = 20
    bar_w = 12
    bar_gap = 6
    for i in range(num_bars):
        bx = spec_x + i * (bar_w + bar_gap)
        bar_h = int(12 + 65 * math.sin(t * 7.0 + i * 0.4) ** 2)
        draw.rectangle([bx, spec_y + 110 - bar_h, bx + bar_w, spec_y + 110], fill=COLOR_CYAN if i < 15 else COLOR_AMBER)

    # Hex stream
    hex_vals = [
        f"0x{int(t * 100 + i * 17) % 0xFFFF:04X}" for i in range(4)
    ]
    draw.text((spec_x, spec_y + 124), "HEX: " + " ".join(hex_vals), fill=COLOR_DIM)
    draw.text((spec_x, spec_y + 146), "BUFFER: 100% [SYNC_OK]", fill=COLOR_EMERALD)

    # --- 7. Bottom Global Bar ---
    draw.line([(pad, HEIGHT - pad - 40), (WIDTH - pad, HEIGHT - pad - 40)], fill=COLOR_DIM, width=1)
    draw.text((pad + 20, HEIGHT - pad - 28), "ANTIGRAVITY HUD PROTOCOL 4.0  //  PROMPT: MISSION_CRITICAL", fill=COLOR_DIM)
    draw.text((WIDTH - pad - 230, HEIGHT - pad - 28), "STATUS: NORMAL", fill=COLOR_EMERALD)

    return img

def render_video():
    print(f"Rendering 60 FPS Tactical HUD ({WIDTH}x{HEIGHT}, {DURATION_SEC}s, {TOTAL_FRAMES} frames)...")
    ffmpeg_cmd = [
        "ffmpeg",
        "-y",
        "-f", "rawvideo",
        "-vcodec", "rawvideo",
        "-s", f"{WIDTH}x{HEIGHT}",
        "-pix_fmt", "rgb24",
        "-r", str(FPS),
        "-i", "-",
        "-c:v", "libx264",
        "-preset", "fast",
        "-crf", "16",
        "-pix_fmt", "yuv420p",
        OUTPUT_VIDEO
    ]
    
    proc = subprocess.Popen(ffmpeg_cmd, stdin=subprocess.PIPE)
    for i in range(TOTAL_FRAMES):
        frame_img = draw_hud_frame(i)
        proc.stdin.write(frame_img.tobytes())
        if i % 30 == 0:
            print(f"Rendered frame {i}/{TOTAL_FRAMES} ({(i/TOTAL_FRAMES)*100:.1f}%)")
            
    proc.stdin.close()
    proc.wait()
    print(f"HUD Master Video Rendered successfully: {OUTPUT_VIDEO}")

if __name__ == "__main__":
    render_video()
