from telegram.ext import Updater, CommandHandler
import requests


def get_url():
     r=requests.get('http://aws.random.cat/meow').json()
     return r['file']


def drop(bot, update):
    url = get_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)


def main():
    updater = Updater('782286279:AAG2hy2CZ8SxPBhP8bccuxZhF9h6sBZ3H_E')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('cat', drop))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()