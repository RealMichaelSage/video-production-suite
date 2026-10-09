# ⚓ ANTIGRAVITY VIDEO PRODUCTION DOCK // КОНТЕКСТНЫЙ МАНИФЕСТ ДЛЯ АГЕНТА
> **НАЗНАЧЕНИЕ:** Скопируйте этот файл целиком или отправьте путь `@[Docs/VIDEO_PRODUCTION_DOCK.md]` в любой соседний чат Antigravity. Агент мгновенно получит полный контекст, доступ ко всем локальным инструментам, готовым ассетам, путям, библиотекам и MCP-серверам для создания видео.

---

## ⚡ 1. ИНСТРУКЦИЯ ДЛЯ ПРИНИМАЮЩЕГО АГЕНТА (SYSTEM DIRECTIVE)

Ты выступаешь в роли **Lead Motion Designer & AI Video Engineer** в рабочей среде macOS Михаила Пузырёва (проектная директория: `/Users/michaelsage/Desktop/Vibes`).
В твоём распоряжении находится полностью настроенный аппаратно-ускоренный стек видеопроизводства: нейросетевые модели генерации видео, серверный Remotion, пословная транскрипция Faster-Whisper, библиотека из 13 стилей вирусных субтитров, 12 студийных звуков 48 kHz, готовый 60 FPS тактический HUD-оверлей и локальные CLI-утилиты.

При выполнении любых задач по видеомонтажу, созданию Reels/Shorts, кинетической типографике и субтитрам используй готовую инфраструктуру, описанную ниже, без повторной установки или изобретения велосипеда.

---

## 📍 2. КАТАЛОГ ГОТОВЫХ ЛОКАЛЬНЫХ АССЕТОВ (ABSOLUTE PATHS)

### 🛡️ 2.1. Тактический HUD-пак (60 FPS Sci-Fi Master)
Директория: `/Users/michaelsage/Desktop/Vibes/Assets/video_production_vault/`
* **Мастер-видеооверлей:** `Assets/video_production_vault/hud_overlays/tactical_hud_9x16_60fps.mp4`
  * Разрешение: 1080x1920, 60 FPS. Готовый прозрачный/черный оверлей (таймкод, REC, вращающийся прицел, радар, спектр аудио, координаты).
  * Наложение на любое видео через режим `blend=screen` в FFmpeg.
* **Векторы Lottie:**
  * `Assets/video_production_vault/lottie_assets/hud_radar_vector.json` (радар).
  * `Assets/video_production_vault/lottie_assets/target_lock_vector.json` (прицел).
* **Готовый консольный композитор:**
  * `Assets/video_production_vault/video_hud_compositor.py`
  * Команда: `python3 Assets/video_production_vault/video_hud_compositor.py --input <input.mp4> --output <out.mp4> --blend screen --sfx`

### 🔊 2.2. Студийные звуковые эффекты (Broadcast 48 kHz SFX)
Директория: `/Users/michaelsage/Desktop/Vibes/Assets/video_production_vault/sfx_audio/`
* **Для субтитров и кинетики:**
  * `kinetic_pop_bubble.wav` (70 мс) — поп-отскок слова при подсветке плашкой.
  * `kinetic_sub_slam.wav` (650 мс) — глубокий саб-удар на тезисе/панчлайне.
  * `kinetic_riser_tension.wav` (800 мс) — нарастающий шумовой райзер перед дропом.
  * `kinetic_marker_swoosh.wav` (180 мс) — быстрый маркерный свуш подчеркивания.
  * `kinetic_typewriter_click.wav` (35 мс) — четкий щелчок клавиатуры.
* **Для тактического HUD и свайпов:**
  * `ui_target_lock.wav` — тройной чирп захвата цели.
  * `ui_radar_ping.wav` — сонарный импульс с реверберацией.
  * `ui_data_telemetry.wav` — высокочастотный поток цифровых данных.
  * `ui_glitch_whoosh.wav` — киберпанк-переход/свайп.
  * `ui_sub_impact.wav` — кинематографичный саб-дроп.
  * `ui_scanner_hum.wav` — зацикленный гул лазерного сканера.
  * `ui_click_sharp.wav` — тактильный механический клик.

### 🎨 2.3. Библиотека стилей субтитров (Remotion Themes)
Директория: `/Users/michaelsage/Desktop/Vibes/Assets/kinetic_templates/remotion-captions-themes/`
* **13 готовых тем React/Remotion:**
  * `src/themes/kinetic-01.tsx` & `kinetic-02.tsx` — упругие прыжки, цветные маркеры.
  * `src/themes/pop.tsx` & `poppin.tsx` — классический стиль Alex Hormozi (Spring Pop).
  * `src/themes/beast.tsx` — жирный шрифт в стиле MrBeast с обводкой 4px.
  * `src/themes/hustle.tsx` — градиентная подсветка активного слова.
  * `src/themes/karaoke.tsx` — слоговое закрашивание текста под речь.
  * `src/themes/podcast.tsx` — размеренный ритм для интервью.
  * `src/themes/simple-one-word.tsx` — показ строго одного слова на экране.
  * `src/themes/soft-ai.tsx`, `gaming-stream.tsx`, `grape.tsx`, `aarit.tsx`.
* **Тестовый стенд (Vite Preview):** `test-player/` (собран и готов к запуску через `npm run dev`).

### 📑 2.4. Базы знаний и руководства
* Полная энциклопедия видеопроизводства: `Docs/video_production_arsenal.md`
* Мастер-руководство по кинетической типографике: `Docs/kinetic_typography_vault.md`
* База знаний визуальных референсов, 3D и моушн-дизайна (Three.js, WebGL, Awwwards): `Docs/DESIGN_AND_MOTION_REFERENCES.md`

---

## 🛠️ 3. СИСТЕМНЫЕ БИНАРНИКИ И CLI-ИНСТРУМЕНТЫ

1. **FFmpeg с аппаратным ускорением Apple Silicon:**
   * Путь: `/Users/michaelsage/.nvm/versions/node/v24.15.0/bin/ffmpeg`
   * Кодеки: `h264_videotoolbox`, `hevc_videotoolbox` (скорость кодирования 150+ FPS).
   * Аудио: фильтр `loudnorm` по стандарту EBU R128 (`-14 LUFS` для Reels, `-16 LUFS` для подкастов).
2. **Higgsfield AI CLI:**
   * Путь: `/Users/michaelsage/.nvm/versions/node/v24.15.0/bin/higgsfield`
   * Доступ к моделям: `veo3_1`, `kling_o3_image_reference`, `gemini_omni`, `seedance_2_5`, `minimax_h3`, `bytedance_video_upscale`, `fps_boost`.
3. **Remotion CLI:**
   * Команда: `npx remotion <render|studio|still|lambda>` (установлен v4.0.534).
4. **Python-библиотеки медиаобработки:**
   * `faster_whisper` (1.2.1) — мгновенная пословная транскрипция на CPU (`int8`).
   * `moviepy` (2.2.1) — склейка и манипуляция видеослоями.
   * `soundfile` (0.13.1) & `Pillow` (11.3.0) — генерация звука и субпиксельной графики.
5. **Lottie CLI Manager:**
   * Путь: `/Users/michaelsage/Desktop/Vibes/Scripts/lottie_manager.py` (валидация, инспекция, конвертация `.lottie` $\leftrightarrow$ `.json`).

---

## 🌐 4. ДОСТУПНЫЕ MCP-СЕРВЕРЫ (Model Context Protocol)

Принимающий агент может напрямую вызывать следующие настроенные MCP-серверы:
* **`21st`:** `video_create_project`, `video_search_blocks`, `video_apply_ops`, `video_export` — облачный таймлайн.
* **`higgsfield`:** облачный шлюз к видеомоделям, генерации аватаров и предикторам виральности.
* **`lottiefiles` (Local stdio):** `search_animations`, `get_animation_details` — поиск векторных оверлеев.
* **`lottiefiles-cloud`:** корпоративная облачная библиотека Lottie.
* **`magicui`:** `searchRegistryItems`, `getRegistryItem` — моушн-компоненты React (`retro-grid`, `animated-beam`).
* **`prompt-kit`:** компоненты Shadcn Canary для видеоинтерфейсов.
* **`figma`:** `get_image`, `get_file` — прямой экспорт векторной графики из макетов.
* **`chrome-devtools-mcp`:** `take_screenshot`, `evaluate_script` — 60 FPS покадровый захват браузерных анимаций.
* **`notebooklm`:** `notebooklm_generate_audio_overview` — синтез живого дикторского голоса 48 kHz.
* **`google-drive` & `telegram`:** бэкап исходников и отправка MP4 в Telegram Review Gate.

---

## 🧠 5. ДОСТУПНЫЕ АГЕНТСКИЕ НАВЫКИ (SKILLS)

В экосистеме активированы специализированные навыки:
* **`@kinetic-typography`** (`/Users/michaelsage/Desktop/Vibes/.agents/skills/kinetic-typography/SKILL.md`): рендеринг заголовков, пословный сплит, вариативные шрифты, пружины.
* **`@lottie-animation`** (`/Users/michaelsage/Desktop/Vibes/.agents/skills/lottie-animation/SKILL.md`): векторные анимации.
* **`@reels-ai-producer`** (`/Users/michaelsage/Desktop/Vibes/.agents/skills/reels-ai-producer/SKILL.md`): конвейер 10-секундных рилсов.
* **`@higgsfield-video-explainer`**: эксплейнеры с диктором.
* **`@podcast-factory`**: студийное аудио и Review Gate.

---

## 📐 6. ЗОЛОТЫЕ ПРАВИЛА И ФОРМУЛЫ КИНЕТИКИ

1. **Правило опережающего акцента (Anticipatory Accent):**
   Визуальное появление слова обязано стартовать на **40–60 мс раньше** звука в аудиодорожке (компенсация задержки зрительной коры мозга).
2. **Параметры пружин для вирусного отскока (Alex Hormozi Style):**
   Коэффициент затухания $\zeta \approx 0.68$, `stiffness: 180`, `damping: 12`, `mass: 0.8`.
   Анимация: $scale: 1.0 \to 1.25$ за 80 мс, затем возврат $1.25 \to 1.0$ за 100 мс.
3. **Защита от слияния с фоном:**
   `-webkit-text-stroke: 4px #000000` + двойная тень `0 4px 0 #000` и `0 8px 24px rgba(0,0,0,0.7)`.
4. **Ритм:**
   140–200 мс на слово, очистка экрана при паузах спикера $> 300$ мс.
5. **Громкость:**
   Нормализация голоса строго под `-14 LUFS` для Reels/Shorts и `-16 LUFS` для подкастов.

---

## 🚀 7. ГОТОВЫЕ РЕЦЕПТЫ И КОМАНДЫ ДЛЯ АГЕНТА

### 🔹 Рецепт А: Пословная транскрипция через Faster-Whisper
```python
from faster_whisper import WhisperModel
model = WhisperModel("tiny", device="cpu", compute_type="int8")
segments, info = model.transcribe("speech.wav", word_timestamps=True)
words = []
for segment in segments:
    for word in segment.words:
        # Сдвиг на 50 мс назад для идеальной синхронизации
        words.append({"word": word.word.strip(), "start": max(0, word.start - 0.05), "end": word.end})
```

### 🔹 Рецепт Б: Наложение тактического HUD 60 FPS
```bash
python3 /Users/michaelsage/Desktop/Vibes/Assets/video_production_vault/video_hud_compositor.py \
  --input raw_footage.mp4 \
  --output result_hud.mp4 \
  --blend screen \
  --sfx
```

### 🔹 Рецепт В: Рендер Remotion-субтитров в MP4
```bash
npx remotion render \
  Assets/kinetic_templates/remotion-captions-themes/test-player/src/index.ts \
  CaptionsComp \
  output_captions.mp4 \
  --props='{"theme":"pop","primaryColor":"#FFFFFF","secondaryColor":"#FFE600"}'
```

### 🔹 Рецепт Г: Генерация футажа через Higgsfield CLI
```bash
higgsfield video create \
  --model veo3_1 \
  --prompt "Cinematic close-up of futuristic holographic neural interface, neon teal, hyper-detailed, 8k" \
  --aspect 9:16
```

---
*Документ подготовлен для мгновенной передачи контекста в любую сессию Antigravity.*
