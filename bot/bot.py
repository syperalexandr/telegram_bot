# -*- coding: utf-8 -*-
import time
import config
import telebot

bot = telebot.TeleBot(config.token)

@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_msg(message):
    bot.send_message(message.chat.id, message.text)
if __name__ == '__main__':
    bot.polling(none_stop=True)


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
     bot.polling(none_stop=True)

@bot.message_handler (content_types=['document','audio'])
def handle_docs_audio(message):
    or file in os.listdir('music/'):
        if file.split('.')[-1] == 'ogg':
            f = open('music/'+file, 'rb')
            msg = bot.send_voice(message.chat.id, f, None)
            # А теперь отправим вслед за файлом его file_id
            bot.send_message(message.chat.id, msg.voice.file_id, reply_to_message_id=msg.message_id)
        time.sleep(3)

# # Обработчик команд /start  и /help 
# @bot.message_handler (commands=['start','help'])
# def handle_start_help(message):
#     pass

# # Обработчик документов и аудиофайлов
# @bot.message_handler (content_types=['document','audio'])
# def handle_docs_audio(message):
#     pass

# # Обработчик сообщений, подходящих под указанное регулярное выражение 
# @bot.message_handler (regexp=["SOME_REGEXP"])
# def handle_start_help(message):
#     pass

# # Обработчик сообщений, содержащих документ с mine_type 'text/plain' (обычный текст)  
# @bot.message_handler (func=lambda message: message.document.mime_type == 'text/plain', content_types=['document'])

# def handle_text_doc(message):
#     pass