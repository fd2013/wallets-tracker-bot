import os
import requests
import re
from datetime import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Load tokens from environment variables for better security
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
ETHERSCAN_API_KEY = os.getenv('ETHERSCAN_API_KEY')

# Regex for basic Ethereum address validation
ETH_ADDRESS_REGEX = re.compile(r"^0x[a-fA-F0-9]{40}$")

# Function to validate Ethereum address
def is_valid_eth_address(address):
    return ETH_ADDRESS_REGEX.match(address) is not None

# Function to get the latest transaction for a given Ethereum wallet address
def get_latest_transaction(wallet_address):
    url = (
        f'https://api.etherscan.io/api?module=account&action=txlist&address={wallet_address}'
        f'&sort=desc&apikey={ETHERSCAN_API_KEY}'
    )
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        if data.get('status') == '0':
            return f"Error: {data.get('message', 'Unknown error')}"
        elif not data.get('result'):
            return 'No transactions found for this address.'
        else:
            latest_tx = data['result'][0]
            tx_hash = latest_tx.get('hash', 'N/A')
            value = int(latest_tx.get('value', 0)) / 1e18  # Convert wei to ETH
            timestamp = datetime.fromtimestamp(int(latest_tx.get('timeStamp', 0))).strftime('%Y-%m-%d %H:%M:%S')

            return (
                f"Latest Transaction:\n"
                f"Hash: {tx_hash}\n"
                f"Value: {value:.6f} ETH\n"
                f"Date: {timestamp}"
            )
    except requests.RequestException as e:
        return f"Network error: {e}"

# Handle the /start command
def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=(
            "Hi! I'm a bot that tracks Ethereum wallet transactions via Etherscan.\n"
            "Send me a valid Ethereum wallet address to get the latest transaction details."
        )
    )

# Handle incoming text messages
def handle_message(update, context):
    wallet_address = update.message.text.strip()

    if not is_valid_eth_address(wallet_address):
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Invalid Ethereum address. Please send a valid address."
        )
        return

    latest_tx = get_latest_transaction(wallet_address)
    context.bot.send_message(chat_id=update.effective_chat.id, text=latest_tx)

# Initialize the Telegram bot
updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Add command and message handlers
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

# Start the bot
updater.start_polling()
updater.idle()
