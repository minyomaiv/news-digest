# news-digest

Личный агрегатор новостей из Telegram-каналов: нейросеть (Gemini) раскладывает новости по темам, пишет короткие сводки, убирает дубли. Несколько раз в день приходит уведомление в ntfy, а все новости открываются на веб-странице.

## Файлы

| Файл | Что делает |
|---|---|
| `config.py` | каналы, темы и подтемы, настройки |
| `login.py` | разовый вход в Telegram, выдаёт строку сессии |
| `digest.py` | главный скрипт: Telegram → Gemini → сохранение → уведомление |
| `docs/index.html` | веб-приложение |
| `docs/news.json`, `docs/topics.json` | данные для приложения (создаются автоматически) |
| `data/state.json` | какие сообщения уже прочитаны (создаётся автоматически) |
| `.github/workflows/run.yml` | расписание запуска |

## Настройка

1. **Загрузить файлы** в репозиторий (Add file → Upload files), сохранив папки.
2. **Получить строку сессии Telegram**: открыть colab.research.google.com, в первой ячейке `!pip install telethon`, во второй — код из `login.py`. Ввести api_id, api_hash, номер телефона и код из Telegram. Скопировать напечатанную строку.
3. **Добавить секреты**: Settings → Secrets and variables → Actions → New repository secret:
   - `TG_API_ID` — api_id
   - `TG_API_HASH` — api_hash
   - `TG_SESSION` — строка сессии из шага 2
   - `GEMINI_API_KEY` — ключ из Google AI Studio
   - `NTFY_TOPIC` — имя темы в ntfy
4. **Включить страницу**: Settings → Pages → Source: Deploy from a branch → Branch: `main`, папка `/docs` → Save.
5. **Первый запуск вручную**: Actions → news-digest → Run workflow.

Страница будет по адресу `https://<логин>.github.io/news-digest/`. На телефоне откройте её в браузере и выберите «Добавить на главный экран».

## Если что-то сломалось

- В Actions запуск красный → откройте его и посмотрите текст ошибки.
- «Сессия Telegram недействительна» → повторите шаг 2 и обновите секрет `TG_SESSION`.
- Ошибка про модель → замените `MODEL` в `config.py` на актуальное название из Google AI Studio.
