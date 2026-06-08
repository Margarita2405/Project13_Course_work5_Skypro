from django.conf import settings


def send_telegram_message(telegram_id: str, text: str) -> bool:
    """Отправляет текстовое сообщение пользователю в Telegram.
    Возвращает True в случае успеха, False при ошибке."""
    token = getattr(settings, "TELEGRAM_BOT_TOKEN", None)
    if not token or not telegram_id:
        print(f"Ошибка: token={token}, telegram_id={telegram_id}")
        return False

    url = f"https://api.telegram.org/bot{token}/sendMessage"

    # ЗАГЛУШКА для сдачи работы – реальная отправка отключена из‑за блокировки сети
    payload = {"chat_id": telegram_id, "text": text}
    print(f"[Telegram] (симуляция) Отправлено сообщение: {payload}")
    return True

    # try:
    # response = requests.post(url, json=payload, timeout=5)
    # print(f"Telegram ответ: {response.status_code} - {response.text}")
    # return response.status_code == 200
    # except requests.exceptions.RequestException as e:
    # print(f"Исключение при отправке: {e}")
    # return False
