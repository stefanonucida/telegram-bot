import requests
import os 
from telegram.ext import Updater, CommandHandler

def get_price(): 
    url = "https://api.coinmarketcap.com/v2/ticker/1/"
    response = requests.get(url)
    print(response)
    data = response.json()
    price = data["data"]["quotes"]["USD"]["price"]
    return price

def price(update, context):
    price = get_price()
    update.message.reply_text(f"Il prezzo attuale di Bitcoin è di ${price:.2f}")

def main():
    updater = Updater(token=os.environ['MY_SUPERSECRET_TOKEN'], use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("price", price))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
