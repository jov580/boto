import os
import validators
import telebot
import requests
import yt_dlp
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['hi', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Hello")

@bot.message_handler(commands=['image', 'photo'])
def check_url(message):
    if validators.url(message.text[7:]):
        bot.reply_to(message, "It is valid link.")
        img_data = requests.get(message.text[7:]).content
        with open('image_name.jpg', 'wb') as handler:
            handler.write(img_data)
        bot.send_photo(message.chat.id, img_data)        
    else:
        bot.reply_to(message, "It is not a valid link.")

@bot.message_handler(commands=['video'])
def check_url_video(message):
    if validators.url(message.text[7:]):
        bot.reply_to(message, "It is valid link.")
        options = {'outtmpl' : 'video.%(ext)s', 'format' : 'mp4'}
        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([message.text[7:]])
        bot.send_video(message.chat.id, open('video.mp4', 'rb'))        
    else:
        bot.reply_to(message, "It is not a valid link.")

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()