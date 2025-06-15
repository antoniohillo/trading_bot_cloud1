import telegram

bot = None

def init_telegram():
    global bot
    from config1 import TELEGRAM_BOT_TOKEN
    bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)

def send_telegram_message(message):
    from config1 import ADMIN_CHAT_ID
    try:
        bot.send_message(chat_id=ADMIN_CHAT_ID, text=message)
    except Exception as e:
        print(f"❌ Error enviando mensaje por Telegram: {e}")