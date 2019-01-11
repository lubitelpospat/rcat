from telegram.ext import Updater, CommandHandler
import requests
# dogs library: https://dog.ceo/api/breeds/image/random

def get_cat_url():
     r = requests.get('http://aws.random.cat/meow').json()
     return r['file']

def get_dog_url():
     r = requests.get('https://random.dog/woof.json').json()
     return r['message']

def drop_cat(bot, update):
    url = get_cat_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)

def drop_dog(bot, update):
    url = get_dog_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
def main():
    updater = Updater('782286279:AAG2hy2CZ8SxPBhP8bccuxZhF9h6sBZ3H_E')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('cat', drop_cat))
    dp.add_handler(CommandHandler('dog', drop_dog))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
