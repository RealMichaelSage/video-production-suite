# 🎬 VIDEO PRODUCTION SUITE // ЭКОСИСТЕМА ВИДЕОПРОИЗВОДСТВА МИХАИЛА ПУЗЫРЁВА

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Node.js](https://img.shields.io/badge/Node.js-v18%2B-green.svg)](https://nodejs.org/)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://python.org/)
[![FFmpeg](https://img.shields.io/badge/FFmpeg-Apple_Silicon_%26_NVENC-orange.svg)](https://ffmpeg.org/)
[![Remotion](https://img.shields.io/badge/Remotion-v4.0.534-purple.svg)](https://remotion.dev/)

> **Автономный комплекс для производства видеороликов, динамических Reels/Shorts/TikTok, вирусных субтитров, кинетической типографики, тактического киберпанк HUD и AI-монтажа с аппаратным ускорением.**

---

## 📑 Содержание

1. [Что это такое и зачем нужно](#-1-что-это-такое-и-зачем-нужно)
2. [Быстрая установка в 1 клик (Quick Start)](#-2-быстрая-установка-в-1-клик)
3. [Ручная пошаговая установка (Manual Setup)](#-3-ручная-пошаговая-установка)
4. [Карта структуры репозитория](#-4-карта-структуры-репозитория)
5. [5 главных сценариев использования (Workflows)](#-5-главных-сценариев-использования)
   * [Сценарий 1: Вирусные субтитры (13 стилей Remotion)](#сценарий-1-вирусные-субтитры-13-стилей-remotion)
   * [Сценарий 2: Тактический HUD 60 FPS и саунд-дизайн](#сценарий-2-тактический-hud-60-fps-и-саунд-дизайн)
   * [Сценарий 3: Пословная AI-транскрипция (Faster-Whisper)](#сценарий-3-пословная-ai-транскрипция-faster-whisper)
   * [Сценарий 4: Генерация видео через нейросети (Higgsfield)](#сценарий-4-генерация-видео-через-нейросети-higgsfield)
   * [Сценарий 5: Сверхбыстрый Python-рендер (120+ FPS)](#сценарий-5-сверхбыстрый-python-рендер-120-fps)
6. [Звуковой арсенал (12 звуков 48 kHz SFX)](#-6-звуковой-арсенал-12-звуков-48-khz-sfx)
7. [Математика пружин и золотые правила монтажа](#-7-математика-пружин-и-правила-монтажа)
8. [Передача контекста в ИИ-агенты (Antigravity DOCK)](#-8-передача-контекста-в-ии-агенты-antigravity-dock)
9. [Частые вопросы и устранение неполадок (FAQ & Troubleshooting)](#-9-частые-вопросы-и-troubleshooting)

---

## 💡 1. Что это такое и зачем нужно

Этот репозиторий решает главную проблему видеопроизводства: **рутинный, медленный ручной монтаж**.
Вместо часов работы в Premiere Pro или After Effects здесь собрана **программная фабрика контента**:

* **Авто-субтитры уровня Submagic / Opus Clip / Alex Hormozi:** 13 готовых дизайн-тем с упругим пружинным отскоком (`scale: 1.0 -> 1.25 -> 1.0`), цветными инверсными плашками и опережением звука на 50 мс.
* **Тактический HUD-оверлей 60 FPS:** 1080x1920 мастер-луп интерфейса будущего (прицел, радар, таймкод, REC, спектрограмма) с консольным автокомпозитором.
* **Студийный саунд-дизайн:** 12 эфирных 48 kHz звуковых эффектов (поп-отскоки, саб-удары, свуши, механические клики).
* **Флагманские нейросети:** доступ к генерации видео Google Veo 3.1, Kling 3.0, Gemini Omni и 4K-апскейлерам через CLI.
* **Аппаратное ускорение:** рендеринг видео на максимальной скорости чипов Apple Silicon (`h264_videotoolbox`) или Nvidia GPU (`h264_nvenc`).

---

## ⚡ 2. Быстрая установка в 1 клик

Для macOS и Linux (включая Ubuntu и WSL2 на Windows) достаточно запустить один скрипт:

```bash
git clone <URL_РЕПОЗИТОРИЯ> video-production
cd video-production
bash setup.sh
```

**Что автоматически сделает `setup.sh`:**
1. Проверит версии Node.js (18+), Python (3.9+) и наличие FFmpeg.
2. Установит все Python-зависимости (`faster-whisper`, `moviepy`, `soundfile`, `pillow`, `numpy`, `scipy`).
3. Настроит NPM-модули и интерактивный плеер Remotion.
4. Проверит наличие и целостность всех аудио- и видео-ассетов (при необходимости автоматически сгенерирует недостающие звуки).
5. Сделает все служебные скрипты исполняемыми.

---

## 🛠️ 3. Ручная пошаговая установка

Если вы предпочитаете настраивать систему вручную или у вас специфическое окружение:

### Шаг 1: Системные требования
* **Node.js:** v18.0.0 или новее.
* **Python:** v3.9 или новее.
* **FFmpeg:** с поддержкой H.264/AAC.

#### macOS:
```bash
# Установка через Homebrew
brew install node python ffmpeg
```

#### Ubuntu / Debian / WSL2:
```bash
sudo apt update
sudo apt install -y nodejs npm python3 python3-pip ffmpeg
```

### Шаг 2: Установка Python-библиотек
```bash
pip3 install -r requirements.txt
```

### Шаг 3: Установка зависимостей субтитров Remotion
```bash
npm install --prefix Templates/remotion-captions-themes
npm install --prefix Templates/remotion-captions-themes/test-player
```

---

## 🗂️ 4. Карта структуры репозитория

```
VideoProduction/
├── 📄 README.md                      # Данное руководство
├── ⚓ DOCK.md                        # Контекстный файл для ИИ-ассистентов (Antigravity/Claude)
├── 📦 package.json                   # NPM-шорткаты (npm run preview:captions и др.)
├── 🐍 requirements.txt               # Список Python-зависимостей
├── ⚙️ setup.sh                       # Автоматический установщик
│
├── 📑 Docs/                          # Документация и базы знаний
│   ├── VIDEO_PRODUCTION_DOCK.md     # Манифест быстрого старта для ИИ
│   ├── video_production_arsenal.md  # 10-категорийная энциклопедия инструментов
│   └── kinetic_typography_vault.md  # Математика пружин, сплайны Безье и вирусный монтаж
│
├── 🛡️ Vault/                         # Мастер-ассеты, HUD и звуки
│   ├── VAULT_MANUAL.md              # Документация хранилища
│   ├── hud_overlays/
│   │   └── tactical_hud_9x16_60fps.mp4 # 1080x1920 60 FPS мастер-оверлей
│   ├── sfx_audio/                   # 12 студийных звуков 48 kHz
│   ├── lottie_assets/               # Векторные радары и прицелы (.json)
│   ├── generators/                  # Генераторы процедурного звука и HUD
│   ├── rendered_vault/              # Примеры готовых смонтированных роликов
│   └── video_hud_compositor.py      # Автономный CLI-композитор HUD
│
├── 🎨 Templates/                     # Готовые моушн-компоненты
│   ├── remotion-captions-themes/    # 13 стилей субтитров (Remotion/React)
│   └── kinetic-typography-skills/   # Витрина GSAP (showcase.html) и скрипты снапшотов
│
└── 🛠️ Scripts/                       # Консольные скрипты автоматизации
    ├── video_hud_compositor.py      # Наложение тактического HUD
    ├── lottie_manager.py            # Инспекция и конвертация Lottie
    └── build_ultra_fast_kinetic_reel.py # Сверхбыстрый Python In-Memory рендер (120+ FPS)
```

---

## 🚀 5. Главных сценариев использования

### Сценарий 1: Вирусные субтитры (13 стилей Remotion)

В каталоге `Templates/remotion-captions-themes/` собрано 13 стилей анимированных субтитров:
* **`pop` & `poppin`:** классический пружинный отскок Alex Hormozi.
* **`beast`:** ультражирный шрифт MrBeast с массивной обводкой.
* **`kinetic-01` & `kinetic-02`:** упругие прыжки со швейцарскими рамками и цветными плашками.
* **`hustle`:** неоновая подсветка активного слова градиентом.
* **`karaoke`:** слоговое заполнение цветом в такт голосу.
* **`simple-one-word`:** строго одно ключевое слово на экране.
* **`podcast`, `soft-ai`, `gaming-stream`, `grape`, `aarit`.**

#### Запуск визуального предпросмотра:
```bash
npm run preview:captions
```
Откройте браузер по адресу `http://localhost:5173`. Вы сможете на лету переключать темы, менять основной и акцентный цвета, шрифт и размер кегля.

#### Рендеринг субтитров в видео (Remotion CLI):
```bash
npx remotion render \
  Templates/remotion-captions-themes/test-player/src/index.ts \
  CaptionsComp \
  output_subtitles.mp4 \
  --props='{"theme":"pop","primaryColor":"#FFFFFF","secondaryColor":"#FFE600"}'
```

---

### Сценарий 2: Тактический HUD 60 FPS и саунд-дизайн

Если вам нужно стилизовать видео под интерфейс искусственного интеллекта, киберпанк или военную телеметрию:

```bash
python3 Scripts/video_hud_compositor.py \
  --input /path/to/my_footage.mp4 \
  --output /path/to/result_hud.mp4 \
  --blend screen \
  --sfx
```

* **Флаг `--blend screen`:** накладывает элементы HUD поверх видеоряда без потери яркости и контраста.
* **Флаг `--sfx`:** автоматически подмешивает звуковые эффекты захвата цели (`ui_target_lock.wav`) и радара (`ui_radar_ping.wav`) в нужные таймкоды.

---

### Сценарий 3: Пословная AI-транскрипция (Faster-Whisper)

Для получения точных таймкодов каждого слова (до 10–20 мс) используется локальный движок `faster-whisper`:

```python
from faster_whisper import WhisperModel

# Запуск квантованной модели (работает мгновенно на любом CPU)
model = WhisperModel("tiny", device="cpu", compute_type="int8")
segments, info = model.transcribe("speech.wav", word_timestamps=True)

words_timeline = []
for segment in segments:
    for word in segment.words:
        # Золотое правило: сдвиг на 50 мс назад для идеальной синхронизации с глазом
        words_timeline.append({
            "word": word.word.strip(),
            "start": max(0, word.start - 0.05),
            "end": word.end
        })

print(f"Распознано {len(words_timeline)} слов!")
```

---

### Сценарий 4: Генерация видео через нейросети (Higgsfield)

В систему интегрирован локальный CLI-клиент Higgsfield:

```bash
# Генерация голливудского видеоряда через Google Veo 3.1 (формат 9:16)
higgsfield video create \
  --model veo3_1 \
  --prompt "Cinematic close-up of futuristic cybernetic eye scanning code, neon cyan, 8k" \
  --aspect 9:16

# AI-апскейл до 4K
higgsfield postprocess upscale --input input.mp4 --model bytedance_video_upscale

# Генерация Slow-Mo 60/120 FPS
higgsfield postprocess fps_boost --input input.mp4 --fps 60
```

---

### Сценарий 5: Сверхбыстрый Python-рендер (120+ FPS)

Для создания динамичных манифестов и промо-роликов без браузера используется прямой рендер из оперативной памяти в пайп FFmpeg:

```bash
python3 Scripts/build_ultra_fast_kinetic_reel.py
```
Скрипт рисует кадры в Pillow и транслирует несжатые байты RGBA прямо в `stdin` FFmpeg через `pipe:0`. Скорость генерации превышает **120–180 кадров в секунду**.

---

## 🔊 6. Звуковой арсенал (12 звуков 48 kHz SFX)

Все файлы расположены в `Vault/sfx_audio/` и подготовлены в формате **48 000 Hz, 16-bit PCM Mono**:

| Файл | Длительность | Назначение |
| :--- | :--- | :--- |
| `kinetic_pop_bubble.wav` | 70 мс | Мягкий поп-отскок при всплытии плашки слова |
| `kinetic_sub_slam.wav` | 650 мс | Глубокий саб-удар на кульминации или панчлайне |
| `kinetic_riser_tension.wav` | 800 мс | Нарастающий шум перед переходом сцены |
| `kinetic_marker_swoosh.wav` | 180 мс | Свист маркера при рисовании подчеркивания |
| `kinetic_typewriter_click.wav` | 35 мс | Четкий механический щелчок терминала |
| `ui_target_lock.wav` | 280 мс | Тройной тактический сигнал захвата объекта |
| `ui_radar_ping.wav` | 1.2 с | Глубокий импульс сонара с эхо-хвостом |
| `ui_data_telemetry.wav` | 800 мс | Высокочастотный поток цифровых данных |
| `ui_glitch_whoosh.wav` | 400 мс | Киберпанк-свайп при резкой смене плана |
| `ui_sub_impact.wav` | 1.0 с | Кинематографичный низкочастотный дроп |
| `ui_scanner_hum.wav` | 2.0 с | Фоновый гул работающего лазера |
| `ui_click_sharp.wav` | 50 мс | Тактильный клик переключателя |

*Скрипты перегенерации звуков:* `npm run generate:sfx`.

---

## 📐 7. Математика пружин и правила монтажа

### 7.1. Формула упругого отскока (Spring Bounce)
Линейные анимации (`linear`) запрещены. Вся кинетика рассчитывается по дифференциальному уравнению затухающих колебаний:

$$m \frac{d^2 x}{dt^2} + c \frac{dx}{dt} + k x = 0$$

* Для вирусного отскока Submagic/Hormozi используется субкритическое затухание $\zeta \approx 0.68$:
  `mass: 0.8`, `damping: 12`, `stiffness: 180`.
* Слово увеличивается до `1.25x` за 80 мс, затем за 100 мс пружинит к нормальному размеру `1.0x`.

### 7.2. Опережающий визуальный акцент (Anticipatory Accent)
* **Правило:** Визуальное начало анимации слова обязано стартовать на **40–60 мс раньше** фактического звука в аудио.
* **Причина:** Зрительная кора головного мозга человека обрабатывает сигнал на 30–50 мс медленнее слуховой. Опережение компенсирует задержку и создает идеальную синестезию звука и картинки.

### 7.3. Контраст и читаемость на любом фоне
* Черный контур толщиной 4px: `-webkit-text-stroke: 4px #000; paint-order: stroke fill;`.
* Тройная тень: `0px 4px 0px #000` (жесткая подложка) + `0px 8px 24px rgba(0,0,0,0.75)` (мягкое рассеивание).
* Нормализация звука: строго под **`-14 LUFS`** (интегрированная громкость EBU R128).

---

## 🧠 8. Передача контекста в ИИ-агенты (Antigravity DOCK)

В корне репозитория подготовлен специальный файл-манифест: **`DOCK.md`**.

Если вы работаете с ИИ-ассистентом (Google Antigravity, Claude Code, Cursor, OpenCode):
1. Просто отправьте ссылку на файл: `@[DOCK.md]`
2. Или скопируйте его содержимое в первое сообщение диалога.
3. Агент мгновенно получит полное знание всех локальных путей, установленных утилит, MCP-серверов и готовых ассетов, и сможет писать рабочий код без уточняющих вопросов.

---

## ❓ 9. Частые вопросы и Troubleshooting

#### 1. «Команда ffmpeg не найдена»
Убедитесь, что FFmpeg установлен в вашей системе:
* На macOS: `brew install ffmpeg`
* На Linux: `sudo apt install -y ffmpeg`
* На Windows: скачайте сборку с gyan.dev и добавьте в системный PATH.

#### 2. «Порт 5173 уже занят при запуске превью субтитров»
Vite автоматически предложит следующий свободный порт (например, 5174). Если нужно освободить порт:
```bash
npx kill-port 5173
```

#### 3. «Ошибка сборки faster-whisper»
`faster-whisper` работает на предкомпилированных бинарниках CTranslate2 и не требует CUDA на процессорах Apple Silicon / Intel / AMD. Если возникает ошибка `libomp`, на macOS выполните: `brew install libomp`.

---

## 📜 Лицензия и авторство
* **Автор архитектуры:** Михаил Пузырёв (Michael Sage)
* **Email:** `i@michaelpuzyrev.ru` | **Сайт:** `https://a-sage.ru`
* **Лицензия:** MIT License. Свободно для коммерческого и персонального использования.
