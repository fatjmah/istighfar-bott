from telegram import Bot
import asyncio
import logging
from flask import Flask
from threading import Thread

TOKEN = "7411219135:AAEJvTp1Gopb4eoYCYHgiJ52MreJyr8DbHk"
CHANNEL_ID = "@O4istghfar"

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Bot is alive"

def run_flask():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run_flask)
    t.start()

istighfar_messages = [
    "أسْتَغْفِرُ اللهَ الْعَظِيمِ وَأتُوبُ إلَيْهِ",
]

async def send_loop():
    bot = Bot(token=TOKEN)
    i = 0
    while True:
        try:
            msg = istighfar_messages[i % len(istighfar_messages)]
            await bot.send_message(chat_id=CHANNEL_ID, text=msg)
            logging.info(f"✅ Sent: {msg}")
            i += 1
            await asyncio.sleep(300)  # كل 5 دقائق
        except Exception as e:
            logging.error(f"❌ Error: {e}")
            await asyncio.sleep(60)

if __name__ == '__main__':
    keep_alive()
    asyncio.get_event_loop().run_until_complete(send_loop())
