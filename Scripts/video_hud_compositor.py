#!/usr/bin/env python3
"""
Master Video HUD Compositor (Vibes Ecosystem)
Merges any input video with HUD overlays (using screen blend mode)
and mixes in high-tech HUD sound effects (target lock, radar ping, telemetry chatter).
"""

import os
import sys
import argparse
import subprocess

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
VAULT_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, "..", "Vault"))
DEFAULT_HUD = os.path.join(VAULT_DIR, "hud_overlays/tactical_hud_9x16_60fps.mp4")
SFX_DIR = os.path.join(VAULT_DIR, "sfx_audio")


def composite_video(input_video, output_video, hud_overlay=DEFAULT_HUD, add_sfx=True, opacity=1.0):
    if not os.path.exists(input_video):
        print(f"Error: input video not found: {input_video}")
        sys.exit(1)
        
    if not os.path.exists(hud_overlay):
        print(f"Error: HUD overlay not found: {hud_overlay}")
        sys.exit(1)
        
    print(f"Compositing video...")
    print(f"  Base Video: {input_video}")
    print(f"  HUD Layer : {hud_overlay}")
    print(f"  Add SFX   : {add_sfx}")
    
    # Complex filter:
    # 1. Scale HUD to match base video dimensions
    # 2. Loop HUD stream so it covers any video length
    # 3. Blend using 'screen' mode so pure black becomes 100% transparent
    filter_complex = (
        f"[1:v]loop=loop=-1:size=300:start=0,format=rgba[hud_loop];"
        f"[hud_loop][0:v]scale2ref=w=iw:h=ih[hud_scaled][base];"
        f"[base][hud_scaled]blend=all_mode='screen':all_opacity={opacity}:shortest=1[v_out]"
    )
    
    cmd = [
        "ffmpeg", "-y",
        "-i", input_video,
        "-i", hud_overlay,
    ]
    
    if add_sfx:
        # Load sound effects from vault
        sfx_lock = os.path.join(SFX_DIR, "ui_target_lock.wav")
        sfx_radar = os.path.join(SFX_DIR, "ui_radar_ping.wav")
        sfx_telemetry = os.path.join(SFX_DIR, "ui_data_telemetry.wav")
        
        cmd.extend([
            "-i", sfx_lock,
            "-i", sfx_radar,
            "-i", sfx_telemetry,
            "-filter_complex", 
            f"{filter_complex};"
            f"[2:a]adelay=600|600,volume=0.45[a_lock];"
            f"[3:a]adelay=1800|1800,volume=0.35[a_radar];"
            f"[4:a]adelay=100|100,volume=0.25[a_telem];"
            f"[0:a][a_lock][a_radar][a_telem]amix=inputs=4:duration=first:dropout_transition=2[a_out]",
            "-map", "[v_out]",
            "-map", "[a_out]"
        ])
    else:
        cmd.extend([
            "-filter_complex", filter_complex,
            "-map", "[v_out]",
            "-map", "0:a?",
        ])
        
    cmd.extend([
        "-c:v", "libx264",
        "-preset", "fast",
        "-crf", "18",
        "-c:a", "aac",
        "-b:a", "192k",
        "-pix_fmt", "yuv420p",
        output_video
    ])
    
    subprocess.run(cmd, check=True)
    print(f"\n Master Composited Video Created Successfully: {output_video}")

def main():
    parser = argparse.ArgumentParser(description="Master Video HUD Compositor")
    parser.add_argument("input", help="Path to input video footage")
    parser.add_argument("-o", "--output", default="output_hud_composited.mp4", help="Output video path")
    parser.add_argument("--hud", default=DEFAULT_HUD, help="Path to HUD overlay video")
    parser.add_argument("--no-sfx", action="store_true", help="Do not add HUD sound effects")
    parser.add_argument("--opacity", type=float, default=1.0, help="HUD opacity (0.1 to 1.0)")
    
    args = parser.parse_args()
    composite_video(
        input_video=args.input,
        output_video=args.output,
        hud_overlay=args.hud,
        add_sfx=not args.no_sfx,
        opacity=args.opacity
    )

if __name__ == "__main__":
    main()
