# 🚀 Video Production Vault & HUD Engine (Vibes Ecosystem)
**Локальная библиотека и автоматизированный конвейер производства видеороликов с HUD-интерфейсами, Lottie-анимациями и саунд-дизайном**

---

## 📂 Структура хранилища (`Assets/video_production_vault/`)

```
Assets/video_production_vault/
├── hud_overlays/             # Готовые 60 FPS HUD-видео (1080x1920) на чёрном фоне
│   └── tactical_hud_9x16_60fps.mp4
├── sfx_audio/                # Студийные 48kHz звуковые эффекты для интерфейсов
│   ├── ui_target_lock.wav    # Тройной тактический чирп захвата цели
│   ├── ui_radar_ping.wav     # Глубокий резонансный сонарный пинг радара
│   ├── ui_glitch_whoosh.wav  # Цифровой глитч-переход
│   ├── ui_data_telemetry.wav # Поток быстрых вычислений / бегущие данные
│   ├── ui_sub_impact.wav     # Кинематографичный саб-бас дроп (удар)
│   ├── ui_scanner_hum.wav    # Фоновый лазерный LFO-гул сканера
│   └── ui_click_sharp.wav    # Механический микро-клик
├── lottie_assets/            # Векторные Lottie-анимации для веба и видео
│   ├── hud_radar_vector.json # Вращающийся радар со сканирующим лучом
│   └── target_lock_vector.json # Пульсирующий прицел захвата цели
├── generators/               # Процедурные генераторы ассетов
│   ├── render_tactical_hud_overlay.py # Генератор 60 FPS HUD-видео любого разрешения
│   ├── generate_hud_sfx.py            # Синтезатор звуковых эффектов
│   └── generate_core_lottie_assets.py # Генератор Lottie JSON
├── rendered_vault/           # Готовые скомпонованные видеоролики
│   └── demo_hud_neurofam.mp4 # Демо-ролик с наложенным HUD и саунд-дизайном
└── video_hud_compositor.py   # МАСТЕР-КОМПОУЗЕР (FFmpeg Pipeline в 1 клик)
```

---

## ⚡ Как наложить HUD и звук на любое видео за 1 секунду

Запусти скрипт компоузера:
```bash
python3 Assets/video_production_vault/video_hud_compositor.py \
  /путь/к/исходному_видео.mp4 \
  -o /путь/к/итоговому_видео.mp4 \
  --opacity 0.85
```

### Что делает компоузер автоматически:
1. Подгоняет разрешение HUD-слоя под разрешение твоего видео.
2. Бесшовно зацикливает HUD на любую длительность исходника.
3. Через алгоритм `blend=screen` растворяет чёрный фон — неоновая графика чисто ложится поверх людей, фона или текста.
4. Вшивает синхронные звуковые эффекты в аудиодорожку:
   * 0.1s — поток телеметрии (`ui_data_telemetry`);
   * 0.6s — звук захвата цели (`ui_target_lock`);
   * 1.8s — сонарный пинг радара (`ui_radar_ping`).
5. Рендерит видео с аппаратным ускорением Apple Silicon в `yuv420p` для гарантированного воспроизведения в Telegram, Instagram Reels и на смартфонах.

---

## 🎨 Как сгенерировать новый кастомный HUD
Если нужно изменить элементы, цвета или надписи HUD:
1. Открой `generators/render_tactical_hud_overlay.py`.
2. Измени палитру (`COLOR_CYAN`, `COLOR_EMERALD`, `COLOR_AMBER`) или тексты телеметрии (`LAT/LON`, `REC`, статус).
3. Запусти генерацию:
   ```bash
   python3 Assets/video_production_vault/generators/render_tactical_hud_overlay.py
   ```
   *(5 секунд — и новый 60 FPS master-слой готов)*.
