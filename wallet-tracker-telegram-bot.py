import os
import requests
import re
from datetime import datetime
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Load tokens from environment variables
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
ETHERSCAN_API_KEY = os.getenv("ETHERSCAN_API_KEY")

# Regex for basic Ethereum address validation
ETH_ADDRESS_REGEX = re.compile(r"^0x[a-fA-F0-9]{40}$")

# Function to validate Ethereum address
def is_valid_eth_address(address):
    return ETH_ADDRESS_REGEX.match(address) is not None

# Function to get the latest transaction for a given Ethereum wallet address
def get_latest_transaction(wallet_address):
    url = (
        f"https://api.etherscan.io/api?module=account&action=txlist&address={wallet_address}"
        f"&sort=desc&apikey={ETHERSCAN_API_KEY}"
    )
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        if data.get("status") == "0":
            return f"Error: {data.get('message', 'Unknown error')}"
        elif not data.get("result"):
            return "No transactions found for this address."
        else:
            latest_tx = data["result"][0]
            tx_hash = latest_tx.get("hash", "N/A")
            value = int(latest_tx.get("value", 0)) / 1e18  # Convert wei to ETH
            timestamp = datetime.fromtimestamp(int(latest_tx.get("timeStamp", 0))).strftime("%Y-%m-%d %H:%M:%S")

            return (
                f"📌 Latest Transaction:\n"
                f"🔗 Hash: {tx_hash}\n"
                f"💰 Value: {value:.6f} ETH\n"
                f"📅 Date: {timestamp}"
            )
    except requests.RequestException as e:
        return f"⚠️ Network error: {e}"

# Handle the /start command
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "👋 Hi! I'm an Ethereum wallet tracker bot.\n"
        "📡 Send me a valid Ethereum address to get the latest transaction details."
    )

# Handle Ethereum address messages
async def handle_message(update: Update, context: CallbackContext):
    wallet_address = update.message.text.strip()

    if not is_valid_eth_address(wallet_address):
        await update.message.reply_text("❌ Invalid Ethereum address. Please send a valid address.")
        return

    latest_tx = get_latest_transaction(wallet_address)
    await update.message.reply_text(latest_tx)

# Main function to start the bot
def main():
    app = Application.builder().token(TELEGRAM_TOKEN).build()

    # Add command and message handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Run the bot
    print("🚀 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
