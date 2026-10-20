# ============================================================
# Отправляет уведомления, которые подготовил digest.py.
# Запускается последним шагом — когда сайт уже обновлён,
# поэтому по нажатию на уведомление новости уже на месте.
# ============================================================

import os
import json

import requests

PENDING_FILE = "pending_notifications.json"

if not os.path.exists(PENDING_FILE):
    print("Нет уведомлений для отправки")
    raise SystemExit(0)

with open(PENDING_FILE, encoding="utf-8") as f:
    pending = json.load(f)

for body in pending:
    try:
        requests.post("https://ntfy.sh/", json=body, timeout=30)
        print("Отправлено:", body["title"])
    except Exception as e:
        print("Не удалось отправить уведомление:", e)
