#!/usr/bin/env python3
"""
Ultra-Fast Dynamic Kinetic Typography & Brutalist Swiss Reel Builder.
- No bottom equalizer clutter.
- Rapid typography cuts (text changes every 0.6 - 1.2s).
- 1-3 massive screen-filling words per beat.
- No cheesy SMM spam; ends on the monumental AI Architecture Manifesto & Michael Sage signature.
"""

import os
import sys
import math
import time
import subprocess
import multiprocessing as mp
import imageio_ffmpeg
from PIL import Image, ImageDraw, ImageFont

KINETIC_DIR = '/Users/michaelsage/.gemini/antigravity/brain/c6b6eb04-2347-470d-9736-57004360b9a2/scratch_kinetic'
sys.path.insert(0, KINETIC_DIR)
import fast_kinetic_engine as fke

FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()
ARTIFACT_DIR = '/Users/michaelsage/.gemini/antigravity/brain/c6b6eb04-2347-470d-9736-57004360b9a2'
SCRATCH_DIR = os.path.join(ARTIFACT_DIR, 'scratch_kinetic_fast')
FRAMES_DIR = os.path.join(SCRATCH_DIR, 'frames')
os.makedirs(FRAMES_DIR, exist_ok=True)

FPS = 30
TOTAL_FRAMES = 1234 # 41.13 seconds
NBSP = "\u00a0"

def render_fast_frame(f):
    out_path = os.path.join(FRAMES_DIR, f"frame_{f:05d}.jpg")
    if os.path.exists(out_path) and os.path.getsize(out_path) > 10000:
        return

    # Canvas (1080 x 1920)
    img = Image.new("RGBA", (1080, 1920), fke.C_BG_DARK)
    draw = ImageDraw.Draw(img)

    # Global Minimal Swiss Frame & Corner Viewfinders
    fke.draw_clean_swiss_grid(draw, 1080, 1920, f, tag="RESPONSIBLE AI // SPEC-2026")

    # ==========================================
    # SCENE 1: HOOK & HISTORICAL BIAS (0 - 219)
    # ==========================================
    if f < 21: # 0.00 - 0.70s : "Искусственный интеллект..."
        fke.draw_running_ticker(draw, 120, "CRITICAL AUDIT /// MACHINE LEARNING /// SPEC-2026", f, speed=8, bg=fke.C_NEON_YELLOW)
        fke.draw_giant_kinetic_block(draw, 900, "ИИ", bg_color=fke.C_WHITE, text_color=fke.C_BLACK, font_key='giant_200')
        fke.draw_pill_badge(draw, 540, 1140, "ARTIFICIAL INTELLIGENCE", bg_color=fke.C_NEON_CYAN, text_color=fke.C_BLACK, font_key='din_36')

    elif f < 54: # 0.70 - 1.80s : "...не ошибается."
        fke.draw_running_ticker(draw, 120, "UNPOPULAR TRUTH /// AUDIT DETECTED /// ZERO ERROR", f, speed=8, bg=fke.C_NEON_PINK, text_col=fke.C_WHITE)
        fke.draw_giant_kinetic_block(draw, 900, "НЕ ОШИБАЕТСЯ", bg_color=fke.C_NEON_YELLOW, text_color=fke.C_BLACK, font_key='impact_130')
        draw.text((360, 1120), "> CODE: ZERO_CALC_ERRORS", font=fke.FONTS['mono_24'], fill=fke.C_NEON_GREEN)

    elif f < 84: # 1.80 - 2.80s : "Он просто обучается..."
        fke.draw_running_ticker(draw, 120, "DATA ARCHIVE INGESTION /// REAL WORLD CORPUS", f, speed=8, bg=fke.C_NEON_CYAN, text_col=fke.C_BLACK)
        fke.draw_stacked_kinetic_words(draw, 900, "ОН ПРОСТО", "ОБУЧАЕТСЯ", c1=fke.C_WHITE, c2=fke.C_NEON_CYAN, font_key='impact_130')

    elif f < 114: # 2.80 - 3.80s : "...на данных нашего реального мира."
        fke.draw_running_ticker(draw, 120, "REAL WORLD DATASETS /// HISTORICAL INGESTION", f, speed=8, bg=fke.C_WHITE, text_col=fke.C_BLACK)
        fke.draw_giant_kinetic_block(draw, 900, "НА НАШЕМ МИРЕ", bg_color=fke.C_NEON_YELLOW, text_color=fke.C_BLACK, font_key='impact_105')
        draw.text((320, 1120), "> DATASET: HUMAN_HISTORY_RAW", font=fke.FONTS['mono_24'], fill=fke.C_MUTED_GRAY)

    elif f < 144: # 3.80 - 4.80s : "А в них уже зашиты..."
        fke.draw_running_ticker(draw, 120, "WARNING /// EMBEDDED PATTERNS DETECTED", f, speed=8, bg=fke.C_NEON_YELLOW, text_col=fke.C_BLACK)
        fke.draw_stacked_kinetic_words(draw, 900, "А В НИХ", "УЖЕ ЗАШИТЫ:", c1=fke.C_MUTED_GRAY, c2=fke.C_WHITE, font_key='impact_130')

    elif f < 178: # 4.80 - 5.93s : "...все исторические стереотипы..."
        fke.draw_running_ticker(draw, 120, "BIAS CONFIRMATION /// HARDCODED PATTERNS", f, speed=9, bg=fke.C_NEON_PINK, text_col=fke.C_WHITE)
        fke.draw_giant_kinetic_block(draw, 850, "СТЕРЕОТИПЫ", bg_color=fke.C_NEON_PINK, text_color=fke.C_WHITE, font_key='impact_130')
        fke.draw_pill_badge(draw, 540, 1080, "ДИСПРОПОРЦИИ В КОДЕ", bg_color=fke.C_NEON_YELLOW, text_color=fke.C_BLACK, font_key='din_48')

    elif f < 219: # 5.93 - 7.30s : "...и неравенство."
        fke.draw_running_ticker(draw, 120, "CRITICAL ERROR /// UNFAIRNESS AT SCALE", f, speed=9, bg=fke.C_NEON_YELLOW, text_col=fke.C_BLACK)
        fke.draw_stacked_kinetic_words(draw, 880, "И НЕРАВЕНСТВО!", "В МАСШТАБЕ", c1=fke.C_WHITE, c2=fke.C_NEON_PINK, font_key='impact_130')

    # ==========================================
    # SCENE 2: ANATOMY OF ERROR & SLICES (219 - 457)
    # ==========================================
    elif f < 255: # 7.30 - 8.50s : "В исторических данных уже зашиты перекосы..."
        fke.draw_running_ticker(draw, 120, "ANATOMY OF ERROR /// MATHEMATICAL BIAS", f, speed=8, bg=fke.C_NEON_CYAN, text_col=fke.C_BLACK)
        fke.draw_stacked_kinetic_words(draw, 900, "МАТЕМАТИКА", f"БЕЗ{NBSP}ЭТИКИ", c1=fke.C_WHITE, c2=fke.C_NEON_YELLOW, font_key='impact_130')

    elif f < 290: # 8.50 - 9.67s : "...Если модель просто оптимизировать..."
        fke.draw_running_ticker(draw, 120, "OPTIMIZATION TRAP /// METRIC CORRUPTION", f, speed=8, bg=fke.C_NEON_PINK, text_col=fke.C_WHITE)
        fke.draw_giant_kinetic_block(draw, 900, "ОПАСНА!", bg_color=fke.C_NEON_PINK, text_color=fke.C_WHITE, font_key='giant_160')
        draw.text((290, 1140), "> LOSS_FUNCTION != SOCIAL_JUSTICE", font=fke.FONTS['mono_24'], fill=fke.C_NEON_GREEN)

    elif f < 335: # 9.67 - 11.17s : "...по математике..." (The Slices Trap)
        fke.draw_running_ticker(draw, 120, "THE METRIC ILLUSION /// 99% vs 54%", f, speed=8, bg=fke.C_NEON_YELLOW, text_col=fke.C_BLACK)
        # Split Swiss visual
        draw.rectangle([100, 580, 980, 840], fill=fke.C_WHITE, outline=fke.C_BLACK, width=4)
        draw.text((140, 610), "ОБЩАЯ ТОЧНОСТЬ (OVERALL):", font=fke.FONTS['bold_28'], fill=fke.C_BLACK)
        draw.text((140, 660), "99.2% [КАЖЕТСЯ НОРМОЙ]", font=fke.FONTS['impact_84'], fill=fke.C_NEON_GREEN)

        draw.rectangle([100, 900, 980, 1160], fill=(255, 240, 245), outline=fke.C_BLACK, width=4)
        draw.text((140, 930), "ТОЧНОСТЬ НА СРЕЗАХ (SLICES):", font=fke.FONTS['bold_28'], fill=fke.C_BLACK)
        draw.text((140, 980), "54.1% [КАТАСТРОФА]", font=fke.FONTS['impact_84'], fill=fke.C_NEON_PINK)

    elif f < 375: # 11.17 - 12.50s : "...она не исправит несправедливость..."
        fke.draw_running_ticker(draw, 120, "ALGORITHM FAILS TO HEAL /// REPRODUCES BIAS", f, speed=8, bg=fke.C_NEON_CYAN, text_col=fke.C_BLACK)
        fke.draw_stacked_kinetic_words(draw, 900, "НЕ ИСПРАВИТ", "НЕСПРАВЕДЛИВОСТЬ", c1=fke.C_WHITE, c2=fke.C_NEON_YELLOW, font_key='impact_105')

    elif f < 415: # 12.50 - 13.83s : "...а автоматизирует её..."
        fke.draw_running_ticker(draw, 120, "AUTOMATION SPREADS UNFAIRNESS", f, speed=9, bg=fke.C_NEON_PINK, text_col=fke.C_WHITE)
        fke.draw_giant_kinetic_block(draw, 900, "АВТОМАТИЗИРУЕТ", bg_color=fke.C_NEON_PINK, text_color=fke.C_WHITE, font_key='impact_105')

    elif f < 457: # 13.83 - 15.23s : "...в гигантском масштабе."
        fke.draw_running_ticker(draw, 120, "EXPONENTIAL SCALE /// SYSTEMIC RISK", f, speed=9, bg=fke.C_NEON_YELLOW, text_col=fke.C_BLACK)
        fke.draw_stacked_kinetic_words(draw, 880, "В ГИГАНТСКОМ", "МАСШТАБЕ!", c1=fke.C_WHITE, c2=fke.C_NEON_YELLOW, font_key='impact_130')

    # ==========================================
    # SCENE 3: GOOGLE'S 7 PRINCIPLES (457 - 720)
    # ==========================================
    elif f < 495: # 15.23 - 16.50s : "Поэтому в Google внедрили..."
        fke.draw_running_ticker(draw, 120, "GOOGLE RESPONSIBLE AI /// ETHICAL BLUEPRINT", f, speed=8, bg=fke.C_NEON_GREEN, text_col=fke.C_BLACK)
        fke.draw_stacked_kinetic_words(draw, 900, "GOOGLE", "RESPONSIBLE AI", c1=fke.C_WHITE, c2=fke.C_NEON_GREEN, font_key='impact_130')

    elif f < 525: # 16.50 - 17.50s : "...семь принципов..."
        fke.draw_running_ticker(draw, 120, "7 ETHICAL PILLARS /// SPECIFICATION 2026", f, speed=8, bg=fke.C_NEON_YELLOW, text_col=fke.C_BLACK)
        fke.draw_giant_kinetic_block(draw, 900, "7 ПРИНЦИПОВ", bg_color=fke.C_NEON_GREEN, text_color=fke.C_BLACK, font_key='giant_160')

    # Rapid Kinetic Cascade of Principles (1 principle per ~0.9s!)
    elif f < 555: # 17.50 - 18.50s : Principle 1
        fke.draw_running_ticker(draw, 120, "PRINCIPLE 01 /// SOCIAL BENEFIT", f, speed=8, bg=fke.C_WHITE, text_col=fke.C_BLACK)
        fke.draw_pill_badge(draw, 540, 700, "01 // ПРИНЦИП", bg_color=fke.C_NEON_GREEN, text_color=fke.C_BLACK, font_key='din_48')
        fke.draw_giant_kinetic_block(draw, 950, f"ПОЛЬЗА ДЛЯ{NBSP}ЛЮДЕЙ", bg_color=fke.C_WHITE, text_color=fke.C_BLACK, font_key='impact_84')

    elif f < 585: # 18.50 - 19.50s : Principle 2
        fke.draw_running_ticker(draw, 120, "PRINCIPLE 02 /// AVOID UNFAIR BIAS", f, speed=8, bg=fke.C_NEON_YELLOW, text_col=fke.C_BLACK)
        fke.draw_pill_badge(draw, 540, 700, "02 // ПРИНЦИП", bg_color=fke.C_NEON_YELLOW, text_color=fke.C_BLACK, font_key='din_48')
        fke.draw_giant_kinetic_block(draw, 950, f"ЗАЩИТА ОТ{NBSP}БАЙАСА", bg_color=fke.C_NEON_PINK, text_color=fke.C_WHITE, font_key='impact_84')

    elif f < 615: # 19.50 - 20.50s : Principle 3
        fke.draw_running_ticker(draw, 120, "PRINCIPLE 03 /// SAFETY FIRST", f, speed=8, bg=fke.C_NEON_CYAN, text_col=fke.C_BLACK)
        fke.draw_pill_badge(draw, 540, 700, "03 // ПРИНЦИП", bg_color=fke.C_NEON_CYAN, text_color=fke.C_BLACK, font_key='din_48')
        fke.draw_giant_kinetic_block(draw, 950, f"БЕЗОПАСНОСТЬ И{NBSP}ТЕСТЫ", bg_color=fke.C_WHITE, text_color=fke.C_BLACK, font_key='impact_84')

    elif f < 645: # 20.50 - 21.50s : Principle 4
        fke.draw_running_ticker(draw, 120, "PRINCIPLE 04 /// HUMAN ACCOUNTABILITY", f, speed=8, bg=fke.C_NEON_PINK, text_col=fke.C_WHITE)
        fke.draw_pill_badge(draw, 540, 700, "04 // ПРИНЦИП", bg_color=fke.C_NEON_PINK, text_color=fke.C_WHITE, font_key='din_48')
        fke.draw_giant_kinetic_block(draw, 950, "HUMAN OVERSIGHT", bg_color=fke.C_NEON_YELLOW, text_color=fke.C_BLACK, font_key='impact_84')

    elif f < 675: # 21.50 - 22.50s : Principle 5
        fke.draw_running_ticker(draw, 120, "PRINCIPLE 05 /// PRIVACY BY DESIGN", f, speed=8, bg=fke.C_NEON_GREEN, text_col=fke.C_BLACK)
        fke.draw_pill_badge(draw, 540, 700, "05 // ПРИНЦИП", bg_color=fke.C_NEON_GREEN, text_color=fke.C_BLACK, font_key='din_48')
        fke.draw_giant_kinetic_block(draw, 950, "PRIVACY BY DESIGN", bg_color=fke.C_WHITE, text_color=fke.C_BLACK, font_key='impact_84')

    elif f < 700: # 22.50 - 23.33s : Principle 6
        fke.draw_running_ticker(draw, 120, "PRINCIPLE 06 /// SCIENTIFIC RIGOR", f, speed=8, bg=fke.C_WHITE, text_col=fke.C_BLACK)
        fke.draw_pill_badge(draw, 540, 700, "06 // ПРИНЦИП", bg_color=fke.C_WHITE, text_color=fke.C_BLACK, font_key='din_48')
        fke.draw_giant_kinetic_block(draw, 950, f"НАУЧНАЯ СТРОГОСТЬ", bg_color=fke.C_NEON_CYAN, text_color=fke.C_BLACK, font_key='impact_84')

    elif f < 720: # 23.33 - 24.00s : Principle 7 (Model Cards)
        fke.draw_running_ticker(draw, 120, "PRINCIPLE 07 /// TRANSPARENCY TOOLS", f, speed=9, bg=fke.C_NEON_YELLOW, text_col=fke.C_BLACK)
        fke.draw_stacked_kinetic_words(draw, 900, "MODEL CARDS", "& DATA SLICES", c1=fke.C_NEON_CYAN, c2=fke.C_NEON_YELLOW, font_key='impact_105')

    # ==========================================
    # SCENE 4: CASE STUDY GOOGLE FLIGHTS (720 - 959)
    # ==========================================
    elif f < 760: # 24.00 - 25.33s : "Как в Google Flights..."
        fke.draw_running_ticker(draw, 120, "REAL WORLD CASE STUDY /// GOOGLE FLIGHTS", f, speed=8, bg=fke.C_NEON_CYAN, text_col=fke.C_BLACK)
        fke.draw_stacked_kinetic_words(draw, 900, "КЕЙС:", "GOOGLE FLIGHTS", c1=fke.C_MUTED_GRAY, c2=fke.C_WHITE, font_key='impact_130')

    elif f < 805: # 25.33 - 26.83s : "...алгоритм ранжирует рейсы честно..."
        fke.draw_running_ticker(draw, 120, "OBJECTIVE RANKING /// ZERO CORRUPTION", f, speed=8, bg=fke.C_NEON_YELLOW, text_col=fke.C_BLACK)
        fke.draw_stacked_kinetic_words(draw, 900, "ЧЕСТНЫЙ", "РАНЖИР", c1=fke.C_WHITE, c2=fke.C_NEON_YELLOW, font_key='impact_130')

    elif f < 850: # 26.83 - 28.33s : "...и объективно..."
        fke.draw_running_ticker(draw, 120, "OBJECTIVE ALGORITHM /// NO HIDDEN MARGINS", f, speed=8, bg=fke.C_NEON_GREEN, text_col=fke.C_BLACK)
        fke.draw_giant_kinetic_block(draw, 900, "ОБЪЕКТИВНО", bg_color=fke.C_NEON_GREEN, text_color=fke.C_BLACK, font_key='giant_160')

    elif f < 895: # 28.33 - 29.83s : "...без скрытых наценок авиакомпаний."
        fke.draw_running_ticker(draw, 120, "COMMISSION MANIPULATION REJECTED", f, speed=9, bg=fke.C_NEON_PINK, text_col=fke.C_WHITE)
        fke.draw_stacked_kinetic_words(draw, 880, "БЕЗ НАЦЕНОК", "АВИАКОМПАНИЙ", c1=fke.C_NEON_PINK, c2=fke.C_WHITE, font_key='impact_105')

    elif f < 930: # 29.83 - 31.00s : "Польза пользователя..."
        fke.draw_running_ticker(draw, 120, "ETHICAL EQUATION /// USER BENEFIT FIRST", f, speed=8, bg=fke.C_NEON_GREEN, text_col=fke.C_BLACK)
        fke.draw_giant_kinetic_block(draw, 900, f"ПОЛЬЗА ЧЕЛОВЕКА", bg_color=fke.C_NEON_GREEN, text_color=fke.C_BLACK, font_key='impact_105')

    elif f < 959: # 31.00 - 31.97s : "...всегда выше выгоды алгоритма."
        fke.draw_running_ticker(draw, 120, "USER BENEFIT > CORPORATE GREED", f, speed=9, bg=fke.C_NEON_YELLOW, text_col=fke.C_BLACK)
        fke.draw_stacked_kinetic_words(draw, 900, "> ВЫГОДЫ", "СИСТЕМЫ", c1=fke.C_NEON_YELLOW, c2=fke.C_WHITE, font_key='impact_130')

    # ==========================================
    # SCENE 5: MANIFESTO & SIGNATURE (959 - 1234)
    # ==========================================
    elif f < 1005: # 31.97 - 33.50s : "Сила архитектора сегодня..."
        fke.draw_running_ticker(draw, 120, "MANIFESTO 2026 /// PRINCIPAL AI ARCHITECT", f, speed=8, bg=fke.C_WHITE, text_col=fke.C_BLACK)
        fke.draw_stacked_kinetic_words(draw, 900, "СИЛА", "АРХИТЕКТОРА", c1=fke.C_WHITE, c2=fke.C_NEON_YELLOW, font_key='impact_130')

    elif f < 1050: # 33.50 - 35.00s : "...не в том, что его модель умеет..."
        fke.draw_running_ticker(draw, 120, "CAPABILITIES ARE CHEAP /// ETHICS IS HARD", f, speed=8, bg=fke.C_NEON_CYAN, text_col=fke.C_BLACK)
        fke.draw_stacked_kinetic_words(draw, 900, f"НЕ{NBSP}В{NBSP}ТОМ, ЧТО", "ОНА УМЕЕТ...", c1=fke.C_MUTED_GRAY, c2=fke.C_WHITE, font_key='impact_105')

    elif f < 1090: # 35.00 - 36.33s : "...а в том..."
        fke.draw_running_ticker(draw, 120, "THE TRUE MANDATE /// BOUNDARY DEFINITION", f, speed=9, bg=fke.C_NEON_YELLOW, text_col=fke.C_BLACK)
        fke.draw_stacked_kinetic_words(draw, 900, f"А{NBSP}В{NBSP}ТОМ,", "ЧЕГО ОНА...", c1=fke.C_NEON_YELLOW, c2=fke.C_NEON_CYAN, font_key='impact_130')

    elif f < 1140: # 36.33 - 38.00s : "...НИКОГДА..." (THE CLIMAX)
        fke.draw_running_ticker(draw, 120, "THE ABSOLUTE BOUNDARY /// ETHICS FIRST", f, speed=10, bg=fke.C_NEON_PINK, text_col=fke.C_WHITE)
        fke.draw_giant_kinetic_block(draw, 900, "НИКОГДА", bg_color=fke.C_NEON_PINK, text_color=fke.C_WHITE, font_key='giant_200')

    elif f < 1185: # 38.00 - 39.50s : "...себе не позволит."
        fke.draw_running_ticker(draw, 120, "RESPONSIBLE AI CORE /// FINAL MANDATE", f, speed=9, bg=fke.C_NEON_GREEN, text_col=fke.C_BLACK)
        fke.draw_stacked_kinetic_words(draw, 900, f"СЕБЕ НЕ", "ПОЗВОЛИТ!", c1=fke.C_WHITE, c2=fke.C_NEON_GREEN, font_key='impact_130')

    else: # 39.50 - 41.13s : FINAL SIGNATURE & AUTHORITY (No SMM spam!)
        fke.draw_running_ticker(draw, 120, "MICHAEL SAGE /// AI ARCHITECTURE /// A-SAGE.RU", f, speed=7, bg=fke.C_NEON_YELLOW, text_col=fke.C_BLACK)
        
        # Swiss Signature Card
        draw.rectangle([100, 680, 980, 1180], fill=fke.C_WHITE, outline=fke.C_BLACK, width=5)
        draw.rectangle([100, 680, 980, 760], fill=fke.C_BLACK)
        draw.text((130, 700), "VERIFIED AI ARCHITECT", font=fke.FONTS['mono_24'], fill=fke.C_NEON_YELLOW)

        draw.text((140, 800), "MICHAEL SAGE", font=fke.FONTS['impact_105'], fill=fke.C_BLACK)
        draw.text((140, 915), "AI ARCHITECTURE & ETHICS", font=fke.FONTS['din_48'], fill=fke.C_NEON_PINK)
        draw.text((140, 980), "Швейцарские стандарты ответственного ИИ", font=fke.FONTS['din_36'], fill=fke.C_MUTED_GRAY)

        draw.rectangle([140, 1050, 940, 1120], fill=fke.C_NEON_YELLOW, outline=fke.C_BLACK, width=2)
        draw.text((360, 1065), "a-sage.ru", font=fke.FONTS['din_48'], fill=fke.C_BLACK)

    img.convert("RGB").save(out_path, quality=94)

def run():
    print(f"=== Rendering {TOTAL_FRAMES} Ultra-Fast Kinetic Frames ===")
    t0 = time.time()
    cores = min(8, mp.cpu_count())
    print(f"Using {cores} worker cores...")
    with mp.Pool(processes=cores) as pool:
        pool.map(render_fast_frame, range(TOTAL_FRAMES))
    t_render = time.time() - t0
    print(f"All {TOTAL_FRAMES} frames rendered in {t_render:.1f}s ({TOTAL_FRAMES/t_render:.1f} FPS)!")

    # Master audio
    mixed_audio = os.path.join(ARTIFACT_DIR, 'scratch_pro', 'master_audio_sfx.wav')
    final_video = os.path.join(ARTIFACT_DIR, 'neurofam_fast_kinetic_promo.mp4')

    print("\n=== Encoding Master Ultra-Fast Kinetic Video ===")
    cmd_enc = [
        FFMPEG, '-y',
        '-framerate', str(FPS),
        '-i', os.path.join(FRAMES_DIR, 'frame_%05d.jpg'),
        '-i', mixed_audio,
        '-c:v', 'libx264',
        '-preset', 'fast',
        '-crf', '17',
        '-pix_fmt', 'yuv420p',
        '-c:a', 'aac',
        '-b:a', '192k',
        '-shortest',
        final_video
    ]
    t0 = time.time()
    subprocess.run(cmd_enc, check=True)
    print(f"Master Video encoded in {time.time()-t0:.1f}s!")
    print(f"Output path: {final_video}")
    print(f"Size: {os.path.getsize(final_video) / (1024*1024):.2f} MB")

if __name__ == '__main__':
    run()
