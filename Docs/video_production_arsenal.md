# 🎬 Полная энциклопедия и арсенал видеопроизводства (Master Video Production Arsenal 2024–2026)
**Единый исчерпывающий каталог MCP-серверов, нейросетевых видеомоделей, открытых движков моушна, библиотек субтитров, звуковых эффектов, CLI-утилит и математических стандартов в экосистеме Михаила Пузырёва**

---

## 📑 Содержание по категориям

1. [Категория 1: Программный стек и MCP-серверы (Model Context Protocol)](#категория-1-программный-стек-и-mcp-серверы)
2. [Категория 2: Флагманские нейросетевые видеомодели и CLI-генераторы (Higgsfield Suite)](#категория-2-нейросетевые-видеомодели-и-cli)
3. [Категория 3: Движки кинетической типографики и программного видео (Code-to-Video)](#категория-3-движки-кинетической-типографики)
4. [Категория 4: Готовые библиотеки стилей, шаблоны субтитров и репозитории](#категория-4-библиотеки-стилей-и-шаблоны)
5. [Категория 5: Специализированные навыки агента (Antigravity Skills)](#категория-5-специализированные-навыки)
6. [Категория 6: Звуковой арсенал и библиотека шумов (Broadcast 48 kHz SFX Vault)](#категория-6-звуковой-арсенал-и-sfx)
7. [Категория 7: Готовые видеооверлеи, HUD и Lottie-ассеты (Production Vault)](#категория-7-видеооверлеи-и-hud)
8. [Категория 8: Системный рантайм, кодеки и AI-транскрипция (Local Stack)](#категория-8-системный-рантайм-и-кодеки)
9. [Категория 9: Математика пружин, психоакустика и алгоритмы вирусных субтитров](#категория-9-математика-пружин-и-алгоритмы)
10. [Категория 10: Архитектура сквозного конвейера (От сценария до публикации)](#категория-10-архитектура-сквозного-конвейера)

---

## Категория 1: Программный стек и MCP-серверы

В системе подключена распределенная сеть MCP-серверов, охватывающая все фазы видеопроизводства — от генерации сценария до монтажа и релиза:

```
┌────────────────────────────────────────────────────────────────────────┐
│                   ЭКОСИСТЕМА MCP ДЛЯ ВИДЕОПРОИЗВОДСТВА                 │
├─────────────────────┬─────────────────────┬────────────────────────────┤
│ СБОРКА И ТАЙМЛАЙН   │ ВЕКТОР И АНИМАЦИЯ   │ КОМПОНЕНТЫ И РЕГИСТРЫ      │
│ • 21st (Timeline)   │ • lottiefiles       │ • magicui                  │
│ • higgsfield        │ • lottiefiles-cloud │ • prompt-kit               │
├─────────────────────┼─────────────────────┼────────────────────────────┤
│ ДИЗАЙН И ВЕКТОРЫ    │ HEADLESS ЗАХВАТ     │ ГОЛОС И ДИКТОРЫ            │
│ • figma             │ • chrome-devtools   │ • notebooklm               │
├─────────────────────┼─────────────────────┼────────────────────────────┤
│ OPEN-SOURCE ИИ      │ ХРАНИЛИЩЕ МЕДИА     │ REVIEW GATE & ДИСТРИБУЦИЯ  │
│ • huggingface       │ • google-drive      │ • telegram                 │
└─────────────────────┴─────────────────────┴────────────────────────────┘
```

### 1.1. `21st` (21st.dev Video Studio Engine)
* **Эндпоинт:** `https://21st.dev/api/mcp`
* **Назначение:** Полноценный облачный JSON-based движок для сборки и рендера моушн-роликов из готовых блоков, компонентов и типографики.
* **Доступный инструментарий:**
  * `video_create_project`: создание проекта с заданным соотношением сторон (9:16, 16:9, 1:1) и FPS.
  * `video_search_blocks` / `video_list_blocks`: семантический поиск анимированных блоков (титры, плашки, переходы).
  * `video_apply_ops`: точечные атомарные операции на таймлайне (слои, маски, длительности, аудиодорожки).
  * `video_propose_variants`: генерация нескольких дизайн-вариантов сцены.
  * `video_upload_asset` / `video_finalize_asset`: загрузка пользовательских футажей в облачный пайплайн.
  * `video_snapshot`: мгновенный рендер кадра-превью на любой миллисекунде.
  * `video_export` / `video_export_status`: компиляция финального MP4 в высоком разрешении.

### 1.2. `higgsfield` (Higgsfield Video AI Engine)
* **Эндпоинт:** `https://mcp.higgsfield.ai/mcp`
* **Назначение:** Облачный интерфейс к флагманским мировым генеративным видеомоделям, цифровым аватарам (Soul ID) и предикторам виральности.
* **Возможности:** Текстовая и покадровая генерация динамичных сцен, управление сохранением лиц, аудит виральности видеоряда.

### 1.3. `lottiefiles` (Local High-Speed Vector Engine)
* **Конфигурация:** Локальный stdio-сервер `/Users/michaelsage/.nvm/versions/node/v24.15.0/bin/mcp-server-lottiefiles`
* **Назначение:** Мгновенный поиск, парсинг и локальная выгрузка векторных Lottie- и dotLottie v2-анимаций.
* **Инструментарий:**
  * `search_animations`: поиск по миллионам моушн-ассетов (радары, прицелы, маркеры, стрелки, спиннеры).
  * `get_animation_details`: получение полного JSON-дерева анимации с возможностью программного изменения цветов и скорости.
  * `get_popular_animations`: мониторинг трендовых визуальных эффектов.

### 1.4. `lottiefiles-cloud` (LottieFiles Enterprise Cloud)
* **Эндпоинт:** `https://mcp.lottiefiles.com/mcp` (SSE / Streamable)
* **Назначение:** Доступ к приватным библиотекам Lottie, командным проектам и облачной конвертации `.lottie` ↔ `.json`.

### 1.5. `magicui` (@magicuidesign/mcp)
* **Конфигурация:** `npx -y @magicuidesign/mcp@latest`
* **Назначение:** Каталог анимированных компонентов для видео-эксплейнеров и демонстрации интерфейсов:
  * Компоненты: `retro-grid` (ретро-сетка), `animated-beam` (движущиеся лучи), `terminal` (кинематический набор кода), `particles` (интерактивные частицы), `shimmer-button`, `neon-gradient-card`.
  * Применение: импорт в сцены Remotion или захват в 60 FPS через headless-браузер.
* **Инструментарий:** `searchRegistryItems`, `getRegistryItem`, `listRegistryItems`.

### 1.6. `prompt-kit` (Shadcn Canary Motion Registry)
* **Конфигурация:** `npx -y shadcn@canary mcp` с реестром `https://www.prompt-kit.com/c/registry.json`
* **Назначение:** Каталог интерфейсных примитивов, диалоговых анимаций и блоков чата для создания реалистичных роликов об искусственном интеллекте.
* **Инструментарий:** `search_items_in_registries`, `view_items_in_registries`, `list_items_in_registries`.

### 1.7. `figma` (Figma REST API Studio)
* **Конфигурация:** `Desktop/Vibes/MCP/MSP Figma/dist/index.js` с авторизованным токеном
* **Назначение:** Прямой экспорт графических элементов, логотипов, векторных иконок, масок и раскадровок прямо из макетов дизайнеров.
* **Инструментарий:**
  * `get_image`: экспорт выделенных слоев и фреймов в SVG, PNG (1x, 2x, 4x), WebP для использования в видеомонтаже.
  * `get_file_nodes` / `get_file`: чтение геометрии, векторных кривых и цветовых токенов.

### 1.8. `chrome-devtools-mcp` (Headless Browser & Canvas Recording)
* **Конфигурация:** `npx -y chrome-devtools-mcp@latest --headless`
* **Назначение:** Запуск изолированного Chromium для покадрового рендера сложных веб-анимаций (Three.js, Canvas 2D, GSAP, CSS Scroll):
  * `evaluate_script`: покадровая перемотка таймлайна (`window.tl.seek(t)`).
  * `take_screenshot`: сохранение несжатых PNG-кадров для последующей склейки в 60 FPS ProRes/H.264 через FFmpeg.

### 1.9. `notebooklm` (NotebookLM Studio Engine)
* **Конфигурация:** `Desktop/Vibes/MCP/notebooklm-mcp/dist/index.js` (headless-сессия)
* **Назначение:**
  * `notebooklm_generate_audio_overview`: генерация живых подкаст-диалогов и дикторских дорожек с ультрареалистичной интонацией и темпом речи.
  * `notebooklm_query_notebook`: извлечение фактов и инсайтов из лонгридов для подготовки сценариев видеороликов.

### 1.10. `huggingface` (Hugging Face Hub & Spaces)
* **Эндпоинт:** `https://hf.co/mcp`
* **Назначение:** Доступ к открытым моделям видеогенерации (Wan 2.1, HunyuanVideo, CogVideoX, AnimateDiff) и Spaces для генерации турбо-ключевых кадров (`gr1_z_image_turbo_generate`).

### 1.11. `google-drive` & `telegram`
* **`google-drive`:** автоматическая синхронизация сырых футажей, бэкап готовых роликов в мастер-папки проектов на Google Диске.
* **`telegram`:** отправка готовых видеороликов лично Михаилу в Telegram на согласование (`send_video`, `send_animation`) в рамках протокола Review Gate.

---

## Категория 2: Нейросетевые видеомодели и CLI

Локально установленный консольный инструмент:
`/Users/michaelsage/.nvm/versions/node/v24.15.0/bin/higgsfield`

### 🎥 2.1. Модели генерации видео (Text-to-Video / Image-to-Video)
1. **Google Veo 3.1 & Veo 3.1 Lite (`veo3_1`, `veo3_1_lite`, `veo3`):**
   * Кинематографичное видео голливудского уровня, идеальная физика света, глубокая перспектива.
2. **Kling 3.0 Omni & Kling 3.0 Turbo (`kling_o3_image_reference`, `kling3_0_turbo`, `kling2_6`):**
   * Топовая модель для фотореалистичных движений людей, динамичных экшен-сцен и анимации с сохранением референса лица.
3. **Gemini Omni Flash & 1.1 (`gemini_omni`, `gemini_omni_flash_1_1`):**
   * Сверхбыстрая генерация сочных видеоклипов под динамичные Reels и короткие форматы.
4. **Seedance 2.5 (`seedance_2_5`):**
   * Модель по умолчанию для плавных органических переходов и пластики движений.
5. **MiniMax H3 & Hailuo (`minimax_h3`, `minimax_h3_max`, `minimax_hailuo`):**
   * Невероятная детализация текстур, кинематографичные крупные планы и микромимика.
6. **FLUX 3 Video & FLUX 3 Edit (`flux_3_video`, `flux_3_video_edit`):**
   * Генерация видео на базе архитектуры Flux с возможностью точечного видео-редактирования по маске.
7. **Grok Video 1.5 (`grok_video_v15`, `grok_video_v15_lite`):**
   * Модель генерации видео от xAI.

### 🪄 2.2. Пост-процессинг и видео-обработка (AI Post-Processing)
* **ByteDance Video Upscale (`bytedance_video_upscale`):** апскейл и очистка видео до 4K с ультра-резкостью.
* **FPS Boost (`fps_boost`):** нейросетевая интерполяция кадров для создания сверхплавного Slow-Mo (из 24/30 FPS в 60/120 FPS).
* **Genjutsu Motion Control (`hf_mult_motion_control`):** точечный перенос траектории движения с одного видео на другой объект.
* **SAM 3 Video Background Removal (`sam_3_video`):** сегментация и удаление фона на лету в динамичном видео без хромакея.
* **Marketing Studio (`ad_multiplier`, `clipify`):** генерация рекламных креативов и адаптация хуков.

---

## Категория 3: Движки кинетической типографики

### 3.1. Remotion Suite (React-to-Video)
Глобально установлен: `remotion` v4.0.534 (`@remotion/cli`, `@remotion/captions`, `@remotion/layout-utils`, `@remotion/paths`).
* **Команды CLI:**
  * `npx remotion studio`: запуск интерактивной веб-студии с визуальным таймлайном.
  * `npx remotion render <entry> <comp> <out>`: компиляция видео в MP4/ProRes с аппаратным ускорением.
  * `npx remotion still`: экспорт статичного постера/обложки.
  * `npx remotion lambda`: параллельный распределенный рендеринг в облаке AWS.
* **Ключевые модули:**
  * `@remotion/captions`: пословная нарезка с авто-группировкой слов в чанки (`createTikTokStyleCaptions`).
  * `@remotion/layout-utils`: серверное измерение ширины слова (`measureText`) без рендера в DOM, предотвращающее сдвиг фоновых плашек.
  * `@remotion/paths`: векторная анимация SVG-контуров букв.

### 3.2. Motion Canvas (Процедурный векторный движок)
* **Стек:** TypeScript + HTML5 Canvas (`motioncanvas.io`).
* **Особенность:** Анимация описывается генераторами `function* () { yield* all(...); }`.
* **Применение:** Высокоточная типографика, плавные графики, математические визуализации, экспорт через `@motion-canvas/ffmpeg`.

### 3.3. GSAP 3 & Split-Type (DOM & Headless Animation)
Установлены в системе: `gsap`, `split-type`.
* **Функционал:** Разделение любого заголовка на массивы элементов `.lines`, `.words`, `.chars`.
* **Механика:** Каскадный вылет букв со сдвигом `stagger: 0.03s`, пружинное сглаживание `ease: "back.out(2)"`, интерполяция положения слов при переносе строк (`GSAP Flip Plugin`).

### 3.4. Three.js & WebGL 3D Typography
* **Официальный портал и база референсов:** [threejs.org](https://threejs.org/) | [threejs.org/examples](https://threejs.org/examples/)
* **Галерея мировых 3D-проектов:** интерактивная витрина Featured Projects на главной странице [threejs.org](https://threejs.org/) (бенчмарки уровня Bruno Simon, Merci-Michel, Apple, Shopify).
* **Troika-three-text (`protectwise/troika`):** Генерация Signed Distance Fields (SDF) на лету в Web Worker из обычных файлов TTF/WOFF. Идеальный антиалиасинг под любыми ракурсами камеры и зумом.
* **GLSL Shaders & Post-Processing:** Кастомные шейдеры объема (Raymarching), неоновое свечение (UnrealBloomPass), глубина резкости (Bokeh/DoF), деформация текста волновым шумом Перлина и симуляции частиц (GPU Particles).
* **Полный реестр 3D и моушн-референсов:** подробный каталог эталонных платформ вынесен в отдельный документ: [`Docs/DESIGN_AND_MOTION_REFERENCES.md`](file:///Users/michaelsage/Desktop/Vibes/VideoProduction/Docs/DESIGN_AND_MOTION_REFERENCES.md).

### 3.5. Fast Python Low-Level Engine (Наш движок)
Скрипт: [`scratch_kinetic_fast/build_ultra_fast_kinetic_reel.py`](file:///Users/michaelsage/.gemini/antigravity/brain/c6b6eb04-2347-470d-9736-57004360b9a2/scratch_kinetic_fast/build_ultra_fast_kinetic_reel.py)
* **Принцип:** Отрисовка кадров в Pillow (`ImageDraw`) с бруталистскими плашками и тикерами, передача несжатых байт RGBA напрямую в stdin FFmpeg через `pipe:0`.
* **Скорость:** Свыше **120–180 кадров в секунду** на процессоре Apple Silicon.

---

## Категория 4: Библиотеки стилей и шаблоны

Каталог в проекте: [`Assets/kinetic_templates/`](file:///Users/michaelsage/Desktop/Vibes/Assets/kinetic_templates/)

### 4.1. Репозиторий `remotion-captions-themes`
Путь: [`Assets/kinetic_templates/remotion-captions-themes/`](file:///Users/michaelsage/Desktop/Vibes/Assets/kinetic_templates/remotion-captions-themes/)
Зависимости установлены, тестовый плеер собран на Vite (`dist/` скомпилирован).

**Реестр 13 стилей субтитров:**
1. **`kinetic-01` (`src/themes/kinetic-01.tsx`):** Упругий пружинный отскок активного слова с неоновой плашкой и швейцарскими рамками.
2. **`kinetic-02` (`src/themes/kinetic-02.tsx`):** Альтернативная динамическая кинетика с акцентными цветными маркерами.
3. **`pop` (`src/themes/pop.tsx`):** Классический упругий Zoom-Pop в стиле вирусных рилсов Alex Hormozi.
4. **`poppin` (`src/themes/poppin.tsx`):** Динамичный упругий вылет с масштабированием `scale: 1.0 -> 1.25 -> 1.0`.
5. **`beast` (`src/themes/beast.tsx`):** Крупный контрастный шрифт в стиле MrBeast с массивной черной обводкой 4px.
6. **`hustle` (`src/themes/hustle.tsx`):** Подсветка активного слова ярким градиентом с мягким свечением.
7. **`karaoke` (`src/themes/karaoke.tsx`):** Слоговая заливка текста цветом синхронно со звуком речи.
8. **`podcast` (`src/themes/podcast.tsx`):** Спокойный эстетичный ритм для экспертных интервью и подкастов.
9. **`gaming-stream` (`src/themes/gaming-stream.tsx`):** Киберспортивный неоновый стиль с глитч-эффектами.
10. **`grape` (`src/themes/grape.tsx`):** Фиолетовый акцентный стиль для креативных роликов.
11. **`aarit` (`src/themes/aarit.tsx`):** Минималистичная швейцарская типографика без лишнего визуального шума.
12. **`soft-ai` (`src/themes/soft-ai.tsx`):** Мягкий полупрозрачный нео-гротеск для презентаций ИИ-продуктов.
13. **`simple-one-word` (`src/themes/simple-one-word.tsx`):** Фокусировка внимания: показ строго одного ключевого слова на экране в каждый момент времени.

**Тестовый стенд:**
* Запуск интерактивного плеера для предпросмотра тем:
  `cd Assets/kinetic_templates/remotion-captions-themes/test-player && npm run dev`

### 4.2. Репозиторий `kinetic-typography-skills`
Путь: [`Assets/kinetic_templates/kinetic-typography-skills/`](file:///Users/michaelsage/Desktop/Vibes/Assets/kinetic_templates/kinetic-typography-skills/)
* **[`showcase.html`](file:///Users/michaelsage/Desktop/Vibes/Assets/kinetic_templates/kinetic-typography-skills/showcase.html):** Интерактивная витрина кинетической типографики на GSAP (Anton, Archivo Black, Fraunces, Inter).
* **Скрипты снапшотов:**
  * `scripts/seek-shot.sh`: покадровая заморозка и скриншоты анимации по заданным таймкодам.
  * `scripts/contact-sheet.sh`: склейка кадров в контактный лист для быстрой проверки раскадровки.
  * `scripts/probe-mp4.sh`: технический аудит метаданных видеофайлов.

---

## Категория 5: Специализированные навыки

В системе настроены специализированные Antigravity-навыки, автоматизирующие производство контента:

1. **[`kinetic-typography`](file:///Users/michaelsage/Desktop/Vibes/.agents/skills/kinetic-typography/SKILL.md):**
   * Проектирование заголовков, титров, лирик-видео, вариативных шрифтов и пружинных анимаций. Установлен глобально в `~/.gemini/config/skills/kinetic-typography/` и локально в проекте.
2. **[`lottie-animation`](file:///Users/michaelsage/Desktop/Vibes/.agents/skills/lottie-animation/SKILL.md):**
   * Поиск через MCP `lottiefiles`, валидация JSON-схем, CLI-конвертер `lottie_manager.py`, наложение оверлеев и оптимизация под Remotion.
3. **[`reels-ai-producer`](file:///Users/michaelsage/Desktop/Vibes/.agents/skills/reels-ai-producer/SKILL.md):**
   * Автономный 7-стадийный конвейер для ежедневного создания зацикленных рилсов (10s Seamless Loop) через Omni Video Engine, выравнивание аудио под `-14 LUFS` и автопостинг.
4. **[`higgsfield-video-explainer`](file:///Users/michaelsage/Desktop/Vibes/.agents/skills/higgsfield-video-explainer/SKILL.md):**
   * Сборка 10-секундных модульных видео-эксплейнеров со связкой диктора (Seed Audio) и видеоряда (Gemini Omni).
5. **[`higgsfield-youtube-thumbnail`](file:///Users/michaelsage/Desktop/Vibes/.agents/skills/higgsfield-youtube-thumbnail/SKILL.md) & [`higgsfield-soul-id`](file:///Users/michaelsage/Desktop/Vibes/.agents/skills/higgsfield-soul-id/SKILL.md):**
   * Обучение персонального цифрового двойника лица (Soul) для генерации превью и видео с лицом Михаила.
6. **[`aimkt-video-clip-pipeline`](file:///Users/michaelsage/Desktop/Vibes/.agents/skills/aimkt-video-clip-pipeline/SKILL.md) & [`aimkt-short-form-pipeline`](file:///Users/michaelsage/Desktop/Vibes/.agents/skills/aimkt-short-form-pipeline/SKILL.md):**
   * Автоматическая нарезка длинных видео/подкастов на вирусные вертикальные клипы с оценкой виральности.
7. **[`aimkt-video-caption-generator`](file:///Users/michaelsage/Desktop/Vibes/.agents/skills/aimkt-video-caption-generator/SKILL.md):**
   * Транскрибация видео из Google Drive, генерация привлекающих внимание субтитров и заголовков.
8. **[`podcast-factory`](file:///Users/michaelsage/.gemini/config/skills/podcast-factory/SKILL.md):**
   * Студийное аудиопроизводство, мастеринг (-16 LUFS, VAD, джинглы), Telegram Review Gate и авторелиз.
9. **[`blender-automation`](file:///Users/michaelsage/.gemini/config/skills/blender-automation/SKILL.md):**
   * Автоматизация 3D-анимации и рендера трехмерных сцен через Python-скрипты в Blender.
10. **[`threejs-animation`](file:///Users/michaelsage/.gemini/config/skills/threejs-animation/SKILL.md) & [`animejs-animation`](file:///Users/michaelsage/.gemini/config/skills/animejs-animation/SKILL.md):**
    * Программные анимации частиц, 3D-сцен и кинетических объектов для экранных записей.

---

## Категория 6: Звуковой арсенал и SFX

Директория: [`Assets/video_production_vault/sfx_audio/`](file:///Users/michaelsage/Desktop/Vibes/Assets/video_production_vault/sfx_audio/)
Все файлы синтезированы в вещательном стандарте **48 kHz 16-bit PCM Mono**:

### 🎵 6.1. Звуковые эффекты для субтитров и кинетики
1. **`kinetic_pop_bubble.wav` (70 мс):** Быстрый свип (520 Гц $\to$ 180 Гц) с мягкой атакой. Используется в момент всплытия фоновой плашки ключевого слова.
2. **`kinetic_sub_slam.wav` (650 мс):** Мощный саб-басовый удар (78 Гц $\to$ 36 Гц) с резким транзиентом. Ставится на панчлайнах и главных выводах.
3. **`kinetic_riser_tension.wav` (800 мс):** Нарастающий частотный свип (180 Гц $\to$ 900 Гц) с примесью белого шума для нагнетания перед кульминацией.
4. **`kinetic_marker_swoosh.wav` (180 мс):** Свист маркера/кисти при рисовании подчеркивания или обводки слова.
5. **`kinetic_typewriter_click.wav` (35 мс):** Сверхчеткий тактильный щелчок механической клавиатуры при посимвольном наборе.

### 🎛️ 6.2. Звуковые эффекты для тактического HUD и переходов
6. **`ui_target_lock.wav` (280 мс):** Тройной тактический чирп с повышением тона при захвате объекта.
7. **`ui_radar_ping.wav` (1.2 с):** Глубокий гидроакустический сонар с затухающим гармоническим шлейфом.
8. **`ui_data_telemetry.wav` (800 мс):** Высокочастотный поток цифровых данных и радиопередачи.
9. **`ui_glitch_whoosh.wav` (400 мс):** Плотный киберпанк-свайп при резкой смене кадра.
10. **`ui_sub_impact.wav` (1.0 с):** Низкочастотный кинематографичный дроп (65 Гц $\to$ 28 Гц).
11. **`ui_scanner_hum.wav` (2.0 с):** Зацикленный гул работающего лазерного сканера.
12. **`ui_click_sharp.wav` (50 мс):** Резкий щелчок тумблера/переключателя.

**Генераторы аудио:**
* [`Assets/video_production_vault/generators/generate_hud_sfx.py`](file:///Users/michaelsage/Desktop/Vibes/Assets/video_production_vault/generators/generate_hud_sfx.py)
* [`Assets/video_production_vault/generators/generate_kinetic_sfx.py`](file:///Users/michaelsage/Desktop/Vibes/Assets/video_production_vault/generators/generate_kinetic_sfx.py)

---

## Категория 7: Видеооверлеи и HUD

Директория: [`Assets/video_production_vault/`](file:///Users/michaelsage/Desktop/Vibes/Assets/video_production_vault/)

* **Мастер-оверлей:** [`hud_overlays/tactical_hud_9x16_60fps.mp4`](file:///Users/michaelsage/Desktop/Vibes/Assets/video_production_vault/hud_overlays/tactical_hud_9x16_60fps.mp4)
  * Разрешение: 1080x1920, частота кадров: **60 FPS**.
  * Элементы: динамический таймкод, индикатор REC, вращающийся видоискатель с прицелом, радарное сканирование, звуковая волна, телеметрия координат, швейцарские маркеры углов.
* **Векторные исходники:**
  * `lottie_assets/hud_radar_vector.json`: векторный радар со стрелкой сканирования.
  * `lottie_assets/target_lock_vector.json`: тактический прицел захвата цели.
* **Автономный консольный композитор:**
  * [`video_hud_compositor.py`](file:///Users/michaelsage/Desktop/Vibes/Assets/video_production_vault/video_hud_compositor.py)
  * Команда запуска:
    `python3 video_hud_compositor.py --input raw_video.mp4 --output final.mp4 --blend screen --sfx`
  * Автоматически накладывает 60 FPS HUD через режим `blend=screen` и подмешивает синхронизированные аудиоэффекты.
* **Проверенный готовый рендер:** [`rendered_vault/demo_hud_neurofam.mp4`](file:///Users/michaelsage/Desktop/Vibes/Assets/video_production_vault/rendered_vault/demo_hud_neurofam.mp4).

---

## Категория 8: Системный рантайм и кодеки

### 8.1. Системные бинарники и кодеки
* **FFmpeg:** `/Users/michaelsage/.nvm/versions/node/v24.15.0/bin/ffmpeg`
  * Аппаратное ускорение Apple Silicon: кодеки `h264_videotoolbox` и `hevc_videotoolbox`.
  * Аудио-нормализация: фильтр `loudnorm` по стандарту EBU R128 (`-14 LUFS` для Reels/Shorts, `-16 LUFS` для подкастов).
  * Видео-фильтры: `blend=screen`, `xfade` (плавные кроссфейды), `drawtext` / `ass` (вжигание субтитров).

### 8.2. AI-распознавание речи (ASR & Forced Alignment)
* **`faster-whisper` (v1.2.1):**
  * Запуск на движке CTranslate2 с квантованием `int8`.
  * Пословные таймкоды (`word-level timestamps`) с точностью до 10–20 мс без дрейфа и галлюцинаций.
* **`moviepy` (v2.2.1):**
  * Автоматизированная склейка клипов, манипуляция слоями и микширование звуковых дорожек.
* **`soundfile` (v0.13.1):**
  * Чтение и запись высокоточного аудио без артефактов компрессии.

### 8.3. CLI-инструменты управления Lottie
* Скрипт [`Scripts/lottie_manager.py`](file:///Users/michaelsage/Desktop/Vibes/Scripts/lottie_manager.py):
  * Команды: `info` (инспекция кадров, слоев, FPS), `validate` (проверка схемы Lottie), `convert` (конвертация `.lottie` $\leftrightarrow$ `.json`), `extract` (распаковка ассетов).

---

## Категория 9: Математика пружин и алгоритмы

### 9.1. Физика пружин (Spring Physics)
Линейная интерполяция (`linear`) категорически запрещена. Движение описывается физикой упругих колебаний:

$$m \frac{d^2 x}{dt^2} + c \frac{dx}{dt} + k x = 0$$

где $m$ — масса (`mass`), $c$ — демпфирование (`damping`), $k$ — жесткость (`stiffness`).

**Коэффициент затухания:**
$$\zeta = \frac{c}{2 \sqrt{k \cdot m}}$$

* **Вирусный отскок слова (Alex Hormozi / Submagic):**
  Субкритическое затухание $\zeta \approx 0.65 - 0.72$ (`stiffness: 180`, `damping: 12`, `mass: 0.8`).
  Слово вылетает за 80 мс с увеличением масштаба до `1.25x`, затем за 100 мс пружинит к нормальному размеру `1.0x`.
* **Плавный подъем (Editorial):**
  Критическое затухание $\zeta = 1.0$ (`stiffness: 120`, `damping: 24`, `mass: 1.0`, `overshootClamping: true`).

### 9.2. Психоакустика и опережающий акцент (Anticipatory Accent 40–60 мс)
* **Железное правило монтажа:** Визуальное появление слова обязано начинаться на **40–60 мс раньше** фактического звука в аудиодорожке.
* **Причина:** Зрительная кора головного мозга человека обрабатывает зрительный стимул на 30–50 мс медленнее, чем слуховая кора обрабатывает звук. Запуск с опережением создает ощущение абсолютной синхронности («звук бьет по слову»).

### 9.3. Защита от слияния с фоном (Multi-layer Stroke & Shadow)
* Обводка: `-webkit-text-stroke: 4px #000000; paint-order: stroke fill;`.
* Тройная тень: `0px 4px 0px #000000` (жесткая контрастная подложка) + `0px 8px 24px rgba(0, 0, 0, 0.75)` (мягкое отделение от фона).
* Инверсная фоновая плашка: цвет плашки — флуоресцентный лайм (`#D4FF00`), желтый (`#FFE600`) или электро-циан (`#00E5FF`), цвет текста внутри — абсолютно черный (`#000000`).

---

## Категория 10: Архитектура сквозного конвейера

```
┌────────────────────────────────────────────────────────────────────────┐
│             СКВОЗНОЙ КОНВЕЙЕР ПРОИЗВОДСТВА ВИДЕОРОЛИКОВ                │
└──────────────────────────────────┬─────────────────────────────────────┘
                                   │
                                   ▼
          ┌─────────────────────────────────────────────────┐
          │ 1. СЦЕНАРИЙ И ФАКТУРА                           │
          │    • MCP NotebookLM / Claude                    │
          │    • Генерация хука, тезисов и панчлайна        │
          └────────────────────────┬────────────────────────┘
                                   │
                                   ▼
          ┌─────────────────────────────────────────────────┐
          │ 2. СИНТЕЗ ГОЛОСА И ДИКТОРА                      │
          │    • MCP NotebookLM (Deep Dive Audio)           │
          │    • Экспорт мастер-звука 48 kHz                │
          └────────────────────────┬────────────────────────┘
                                   │
                                   ▼
          ┌─────────────────────────────────────────────────┐
          │ 3. ASR & FORCED ALIGNMENT                       │
          │    • faster-whisper (CTranslate2 INT8)          │
          │    • Вычисление таймкодов каждого слова (мс)    │
          │    • Сдвиг на опережение: -50 мс                │
          └────────────────────────┬────────────────────────┘
                                   │
                                   ▼
          ┌─────────────────────────────────────────────────┐
          │ 4. СЕМАНТИЧЕСКАЯ РАЗМЕТКА И МОУШН               │
          │    • Выделение ударных слов и пауз > 300 мс     │
          │    • Назначение стилей субтитров (Remotion)     │
          │    • Расстановка звуковых эффектов (SFX Vault)  │
          └────────────────────────┬────────────────────────┘
                                   │
                                   ▼
          ┌─────────────────────────────────────────────────┐
          │ 5. ВИДЕОГЕНЕРАЦИЯ И КОМПОЗИТИНГ                 │
          │    • Генерация футажей (Higgsfield Veo/Kling)   │
          │    • Наложение 60 FPS тактического HUD          │
          │    • Аппаратный рендер FFmpeg (Apple Silicon)   │
          │    • Нормализация звука: -14 LUFS               │
          └────────────────────────┬────────────────────────┘
                                   │
                                   ▼
          ┌─────────────────────────────────────────────────┐
          │ 6. TELEGRAM REVIEW GATE BOT                     │
          │    Мгновенная отправка MP4 Михаилу на ревью     │
          └─────────────────────────────────────────────────┘
```

---
*Документ является официальным эталонным стандартом видеопроизводства экосистемы Михаила Пузырёва.*
