import telebot

# 🔑 Replace with your bot token
BOT_TOKEN = "7600634437:AAFvGomJfy-r758y4Dn7vjXrUBUrEfVNu_o"
bot = telebot.TeleBot(BOT_TOKEN)

# 🎬 Content database (edit this to add movies/series links)
content_db = {
    "inception": "https://example.com/inception",
    "avatar": "https://example.com/avatar",
    "money heist": "https://example.com/money-heist"
}

# 🟢 /start command
@bot.message_handler(commands=['start'])
def start(message):
    welcome_text = (
        "🎬 *Welcome to Cine Stream Bot!*\n\n"
        "Use `/search <movie/series>` to find content.\n"
        "Example: `/search avatar`\n\n"
        "❗ Accurate match & keyword match both supported."
    )
    bot.send_message(message.chat.id, welcome_text, parse_mode="Markdown")

# 🔎 /search command
@bot.message_handler(commands=['search'])
def search(message):
    query = message.text.replace("/search", "").strip().lower()

    if not query:
        bot.reply_to(message, "⚠️ Please provide a search term.\nExample: `/search inception`", parse_mode="Markdown")
        return

    # First check for exact match
    if query in content_db:
        bot.send_message(
            message.chat.id,
            f"✅ Found: *{query.title()}*\n🔗 {content_db[query]}",
            parse_mode="Markdown"
        )
        return

    # Then check for keyword match
    for key, link in content_db.items():
        if query in key or key in query:
            bot.send_message(
                message.chat.id,
                f"✅ Found: *{key.title()}*\n🔗 {link}",
                parse_mode="Markdown"
            )
            return

    # If nothing found
    bot.send_message(message.chat.id, "❌ No content found for your search.")

# 🚀 Run the bot
print("🤖 Bot is running...")
bot.infinity_polling()