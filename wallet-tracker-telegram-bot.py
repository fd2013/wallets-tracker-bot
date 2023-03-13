import os
import requests
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Insert your Telegram bot token and Etherscan API key here
TELEGRAM_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
ETHERSCAN_API_KEY = 'YOUR_ETHERSCAN_API_KEY'

# Define a function to get the latest transaction for a given Ethereum wallet address
def get_latest_transaction(wallet_address):
    url = f'https://api.etherscan.io/api?module=account&action=txlist&address={wallet_address}&sort=desc&apikey={ETHERSCAN_API_KEY}'
    response = requests.get(url)
    data = response.json()
    if data['status'] == '0':
        return 'Error: ' + data['message']
    elif len(data['result']) == 0:
        return 'No transactions found for this address'
    else:
        latest_tx = data['result'][0]
        return f"Latest transaction:\n{latest_tx['hash']}\n{latest_tx['value']} wei\n{latest_tx['timeStamp']}"

# Define a function to handle the /start command
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hi! I'm a bot that can track Ethereum wallets and their transactions on Etherscan. To get started, send me a wallet address.")

# Define a function to handle text messages
def echo(update, context):
    wallet_address = update.message.text
    latest_tx = get_latest_transaction(wallet_address)
    context.bot.send_message(chat_id=update.effective_chat.id, text=latest_tx)

# Create a Telegram bot and add handlers
updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(MessageHandler(Filters.text, echo))

# Start the bot
updater.start_polling()
updater.idle()
