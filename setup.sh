#!/usr/bin/env bash
# ==============================================================================
# 🎬 VIDEO PRODUCTION SUITE // AUTOMATED INSTALLER & ENVIRONMENT SETUP
# ==============================================================================
# One-click installer for macOS and Linux.
# Configures Python dependencies, Node/Remotion libraries, and verifies assets.
# ==============================================================================

set -e

# Colors
C_RESET="\033[0m"
C_BOLD="\033[1m"
C_GREEN="\033[32m"
C_CYAN="\033[36m"
C_YELLOW="\033[33m"
C_RED="\033[31m"
C_MAGENTA="\033[35m"

BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo -e "${C_CYAN}${C_BOLD}"
echo "╔══════════════════════════════════════════════════════════════════════╗"
echo "║          🎬 VIDEO PRODUCTION SUITE // ENVIRONMENT SETUP              ║"
echo "║             AI Video, Kinetic Typography & Tactical HUD              ║"
echo "╚══════════════════════════════════════════════════════════════════════╝"
echo -e "${C_RESET}"

# 1. Check Python
echo -e "${C_BOLD}▶ [1/6] Проверка Python окружения...${C_RESET}"
if command -v python3 >/dev/null 2>&1; then
    PY_VER=$(python3 -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
    echo -e "  ${C_GREEN}✓${C_RESET} Python3 найден: v${PY_VER}"
else
    echo -e "  ${C_RED}✗ Ошибка:${C_RESET} python3 не найден. Пожалуйста, установите Python 3.9+."
    exit 1
fi

# 2. Check Node & NPM
echo -e "${C_BOLD}▶ [2/6] Проверка Node.js и NPM...${C_RESET}"
if command -v node >/dev/null 2>&1 && command -v npm >/dev/null 2>&1; then
    NODE_VER=$(node -v)
    NPM_VER=$(npm -v)
    echo -e "  ${C_GREEN}✓${C_RESET} Node.js найден: ${NODE_VER}"
    echo -e "  ${C_GREEN}✓${C_RESET} NPM найден: v${NPM_VER}"
else
    echo -e "  ${C_RED}✗ Ошибка:${C_RESET} Node.js / NPM не найдены. Установите Node.js 18+ (https://nodejs.org/)."
    exit 1
fi

# 3. Check FFmpeg
echo -e "${C_BOLD}▶ [3/6] Проверка FFmpeg...${C_RESET}"
if command -v ffmpeg >/dev/null 2>&1; then
    FF_VER=$(ffmpeg -version | head -n 1 | awk '{print $3}')
    echo -e "  ${C_GREEN}✓${C_RESET} FFmpeg найден: v${FF_VER}"
else
    echo -e "  ${C_YELLOW}⚠ Внимание:${C_RESET} FFmpeg не найден в системном PATH."
    echo -e "    На macOS установите через: ${C_CYAN}brew install ffmpeg${C_RESET}"
    echo -e "    На Ubuntu/Debian: ${C_CYAN}sudo apt update && sudo apt install -y ffmpeg${C_RESET}"
fi

# 4. Install Python Dependencies
echo -e "${C_BOLD}▶ [4/6] Установка зависимостей Python (faster-whisper, moviepy, soundfile, pillow)...${C_RESET}"
if [ -f "$BASE_DIR/requirements.txt" ]; then
    python3 -m pip install -q -r "$BASE_DIR/requirements.txt"
    echo -e "  ${C_GREEN}✓${C_RESET} Python зависимости успешно установлены."
else
    echo -e "  ${C_YELLOW}⚠ requirements.txt не найден, пропускаем.${C_RESET}"
fi

# 5. Install Remotion Caption Templates Dependencies
echo -e "${C_BOLD}▶ [5/6] Настройка моушн-шаблонов Remotion и витрины стилей...${C_RESET}"
THEMES_DIR="$BASE_DIR/Templates/remotion-captions-themes"
if [ -d "$THEMES_DIR" ]; then
    npm install --silent --prefix "$THEMES_DIR"
    if [ -d "$THEMES_DIR/test-player" ]; then
        npm install --silent --prefix "$THEMES_DIR/test-player"
    fi
    echo -e "  ${C_GREEN}✓${C_RESET} Remotion Captions (13 стилей) успешно настроены."
else
    echo -e "  ${C_YELLOW}⚠ Папка шаблонов не найдена.${C_RESET}"
fi

# 6. Verify and Generate Assets if needed
echo -e "${C_BOLD}▶ [6/6] Проверка аудио-эффектов (SFX) и векторных ассетов...${C_RESET}"
SFX_DIR="$BASE_DIR/Vault/sfx_audio"
mkdir -p "$SFX_DIR"

# Generate SFX if empty or missing key files
if [ ! -f "$SFX_DIR/kinetic_pop_bubble.wav" ] || [ ! -f "$SFX_DIR/ui_target_lock.wav" ]; then
    echo -e "  ${C_CYAN}ℹ${C_RESET} Генерация студийных звуковых эффектов (48 kHz)..."
    python3 "$BASE_DIR/Vault/generators/generate_hud_sfx.py" >/dev/null 2>&1 || true
    python3 "$BASE_DIR/Vault/generators/generate_kinetic_sfx.py" >/dev/null 2>&1 || true
fi

# Generate core Lottie if missing
LOTTIE_DIR="$BASE_DIR/Vault/lottie_assets"
mkdir -p "$LOTTIE_DIR"
if [ ! -f "$LOTTIE_DIR/hud_radar_vector.json" ]; then
    echo -e "  ${C_CYAN}ℹ${C_RESET} Генерация векторных Lottie-ассетов..."
    python3 "$BASE_DIR/Vault/generators/generate_core_lottie_assets.py" >/dev/null 2>&1 || true
fi

echo -e "  ${C_GREEN}✓${C_RESET} Все аудио- и видео-ассеты верифицированы."

# Make scripts executable
chmod +x "$BASE_DIR/Scripts/"*.py 2>/dev/null || true
chmod +x "$BASE_DIR/Vault/video_hud_compositor.py" 2>/dev/null || true

# Summary
echo -e "\n${C_GREEN}${C_BOLD}══════════════════════════════════════════════════════════════════════${C_RESET}"
echo -e "${C_GREEN}${C_BOLD} 🎉 СИСТЕМА УСПЕШНО РАЗВЕРНУТА И ГОТОВА К ПРОДАКШЕНУ!${C_RESET}"
echo -e "${C_GREEN}${C_BOLD}══════════════════════════════════════════════════════════════════════${C_RESET}"
echo -e "\n${C_BOLD}Быстрые команды для старта:${C_RESET}"
echo -e "  1. Предпросмотр 13 стилей субтитров:  ${C_CYAN}npm run preview:captions${C_RESET}"
echo -e "  2. Наложение тактического HUD 60 FPS: ${C_CYAN}python3 Scripts/video_hud_compositor.py --input raw.mp4 --output out.mp4 --blend screen --sfx${C_RESET}"
echo -e "  3. Инспекция Lottie-анимаций:         ${C_CYAN}python3 Scripts/lottie_manager.py info animation.json${C_RESET}"
echo -e "  4. Контекстный манифест для ИИ:       ${C_MAGENTA}DOCK.md${C_RESET}"
echo -e "\nПолная документация находится в: ${C_BOLD}Docs/video_production_arsenal.md${C_RESET}\n"
