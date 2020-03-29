import telebot
# import urllib, requests
# url = 'https://api.telegram.org/bot%s/sendMessage?chat_id=%s&text=%s' % (
#     '<token>', '<chat_id>', urllib.quote_plus('<message>'))
# _ = requests.get(url, timeout=10)
bot = telebot.TeleBot("")

# handles incoming /start and /help commands
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

# echoes all incoming text messages back to the sender. 
# It uses a lambda function to test a message. 
# If the lambda returns True, the message is handled by the decorated function.
@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()


import requests

def telegram_bot_sendtext(bot_message):
    
    bot_token = ''
    bot_chatID = ''
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()
    

datetime = "Thursday, 26/3/2020, 10:30am"
clinic = "test clinic"
link = "www.google.com"
test = telegram_bot_sendtext(f"You have an appointment on {datetime} at {clinic}. Please refer to the link for more details, {link}")
print(test)
# import telebot

# TOKEN = '<token_string>'
# tb = telebot.TeleBot(TOKEN)	#create a new Telegram Bot object

# # Upon calling this function, TeleBot starts polling the Telegram servers for new messages.
# # - none_stop: True/False (default False) - Don't stop polling when receiving an error from the Telegram servers
# # - interval: True/False (default False) - The interval between polling requests
# #           Note: Editing this parameter harms the bot's response time
# # - timeout: integer (default 20) - Timeout in seconds for long polling.
# tb.polling(none_stop=False, interval=0, timeout=20)

# # getMe
# user = tb.get_me()

# # setWebhook
# tb.set_webhook(url="http://example.com", certificate=open('mycert.pem'))
# # unset webhook
# tb.remove_webhook()

# # getUpdates
# updates = tb.get_updates()
# updates = tb.get_updates(1234,100,20) #get_Updates(offset, limit, timeout):

# # sendMessage
# tb.send_message(chat_id, text)

# # forwardMessage
# tb.forward_message(to_chat_id, from_chat_id, message_id)

# # All send_xyz functions which can take a file as an argument, can also take a file_id instead of a file.
# # sendPhoto
# photo = open('/tmp/photo.png', 'rb')
# tb.send_photo(chat_id, photo)
# tb.send_photo(chat_id, "FILEID")

# # sendAudio
# audio = open('/tmp/audio.mp3', 'rb')
# tb.send_audio(chat_id, audio)
# tb.send_audio(chat_id, "FILEID")

# ## sendAudio with duration, performer and title.
# tb.send_audio(CHAT_ID, file_data, 1, 'eternnoir', 'pyTelegram')

# # sendVoice
# voice = open('/tmp/voice.ogg', 'rb')
# tb.send_voice(chat_id, voice)
# tb.send_voice(chat_id, "FILEID")

# # sendDocument
# doc = open('/tmp/file.txt', 'rb')
# tb.send_document(chat_id, doc)
# tb.send_document(chat_id, "FILEID")

# # sendSticker
# sti = open('/tmp/sti.webp', 'rb')
# tb.send_sticker(chat_id, sti)
# tb.send_sticker(chat_id, "FILEID")

# # sendVideo
# video = open('/tmp/video.mp4', 'rb')
# tb.send_video(chat_id, video)
# tb.send_video(chat_id, "FILEID")

# # sendVideoNote
# videonote = open('/tmp/videonote.mp4', 'rb')
# tb.send_video_note(chat_id, videonote)
# tb.send_video_note(chat_id, "FILEID")

# # sendLocation
# tb.send_location(chat_id, lat, lon)

# # sendChatAction
# # action_string can be one of the following strings: 'typing', 'upload_photo', 'record_video', 'upload_video',
# # 'record_audio', 'upload_audio', 'upload_document' or 'find_location'.
# tb.send_chat_action(chat_id, action_string)

# # getFile
# # Downloading a file is straightforward
# # Returns a File object
# import requests
# file_info = tb.get_file(file_id)

# file = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(API_TOKEN, file_info.file_path))