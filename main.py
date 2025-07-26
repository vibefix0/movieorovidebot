from pyrogram import Client, filters

API_ID = 26840557
API_HASH = "cad0724aa97f65e118bf3599d8ba9c50"
BOT_TOKEN = "8160041262:AAH18KC3LCAFPJxZn1vPBXD4TJjz3O6F9VM"

app = Client("movieorovidebot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
def start(client, message):
    message.reply_text("🎬 Welcome to MovieVerse HD Bot!\nType /movie <name> to search.")

@app.on_message(filters.command("movie"))
def movie(client, message):
    if len(message.command) < 2:
        message.reply_text("❗ Usage: /movie <movie name>")
        return

    query = " ".join(message.command[1:])
    message.reply_text(f"🔍 Searching Telegram for: {query} ... (feature coming soon)")

app.run()
