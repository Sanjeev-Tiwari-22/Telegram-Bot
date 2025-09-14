import telebot
from yt_dlp import YoutubeDL
import os

TOKEN = '7600634437:AAFvGomJfy-r758y4Dn7vjXrUBUrEfVNu_o'
bot = telebot.TeleBot(TOKEN)

# Configure yt-dlp
ydl_opts = {
    'outtmpl': 'downloads/%(title)s.%(ext)s',
    'format': 'best',
}

if not os.path.exists('downloads'):
    os.makedirs('downloads')

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Send me a YouTube link and I'll download the video for you.")

@bot.message_handler(func=lambda message: True)
def download_video(message):
    url = message.text.strip()
    bot.send_message(message.chat.id, "Processing your link...")
    try:
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            file_path = ydl.prepare_filename(info)
            with open(file_path, 'rb') as f:
                bot.send_video(message.chat.id, f)
        os.remove(file_path)
    except Exception as e:
        bot.send_message(message.chat.id, f"Failed to download: {str(e)}")

bot.polling()
