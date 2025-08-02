from telethon import TelegramClient, events
from keep_alive import keep_alive
import os

api_id = int(os.environ.get("29914850"))
api_hash = os.environ.get("de7b0ee6f49fff7b4a5f0e5c015972ce")
bot_token = os.environ.get("7880874056:AAHj9ZmU28tIortiYxZjt-oxyVcQXrKNa2Q")

client = TelegramClient("bot", api_id, api_hash).start(bot_token=bot_token)

@client.on(events.NewMessage(pattern='/start'))
async def start_handler(event):
    user_id = event.sender_id
    await event.respond(f"👤 حسابك:\nID: `{user_id}`", parse_mode="md")

keep_alive()  # لتشغيل السيرفر الصغير
print("✅ البوت شغال على Railway")
client.run_until_disconnected()
