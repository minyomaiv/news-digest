# ============================================================
# Запускается ОДИН раз (на ноутбуке или в Google Colab).
# Печатает "строку сессии" — её нужно положить в секрет TG_SESSION на GitHub.
# ВНИМАНИЕ: строка сессии = полный доступ к вашему Telegram. Никому её не показывайте.
#
# В Google Colab:
#   1) в первой ячейке:  !pip install telethon
#   2) во второй ячейке вставьте этот код и запустите
# ============================================================

from telethon.sync import TelegramClient
from telethon.sessions import StringSession

api_id = int(input("api_id: "))
api_hash = input("api_hash: ")

# Telethon спросит номер телефона и код, который придёт в приложение Telegram
with TelegramClient(StringSession(), api_id, api_hash) as client:
    print("\nВход выполнен. Ваша строка сессии (скопируйте целиком):\n")
    print(client.session.save())
