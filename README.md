# wallet-tracker
A Python script that uses the Python-Telegram-Bot library to create a Telegram bot that can track Ethereum wallets and their transactions on Etherscan

To use this script, you'll need to install the Python-Telegram-Bot library with:

$ pip install python-telegram-bot

Replace the YOUR_TELEGRAM_BOT_TOKEN and YOUR_ETHERSCAN_API_KEY placeholders with your own Telegram bot token and Etherscan API key, respectively.

You can obtain a telegram bot token by contacting @BotFather, issuing the /newbot command and following the steps until you're given a new token.

You can obtain the etherscan api key easily by creating an account, go to progile and check API Keys, click to Add or just follow this link: 

https://etherscan.io/myapikey

Before running the script do install these requirements

$ python -m pip install requests

$ pip install python-telegram-bot --upgrade

Once you've done that, you can run the script and start chatting with your bot on Telegram.

When you send the bot a message with an Ethereum wallet address, it will use the Etherscan API to look up the latest transaction for that address and send you a message with the transaction hash, value, and timestamp.
