# Ethereum Wallet Tracker Telegram Bot

A simple **Telegram bot** that tracks **Ethereum wallet transactions** using the **Etherscan API**. Send an Ethereum address to the bot, and it will reply with the latest transaction details.

## 🚀 Features
- ✅ Track the **latest transaction** of any Ethereum wallet.
- ✅ Converts **wei** to **ETH** for easy reading.
- ✅ Displays human-readable **timestamps**.
- ✅ Validates Ethereum wallet addresses.
- ✅ Handles API and network errors gracefully.

---

## 📦 Requirements
- Python 3.7+
- Telegram Bot Token (Open Telegram and search for @BotFather)
- Etherscan API Key

### Install Dependencies
```bash
pip install python-telegram-bot requests
```

---

## ⚙️ Setup

1. **Clone the repository:**
```bash
git clone https://github.com/fd2013/wallet-tracker-telegram-bot.git
cd wallet-tracker-telegram-bot
```

2. **Configure Environment Variables:**
Create a `.env` file (or set environment variables directly):
```bash
TELEGRAM_TOKEN=your_telegram_bot_token
ETHERSCAN_API_KEY=your_etherscan_api_key
```

3. **Run the bot:**
```bash
python wallet-tracker-telegram-bot.py
```

---

## 💬 Usage
- Start the bot on Telegram with `/start`.
- Send an Ethereum wallet address (e.g., `0x742d35Cc6634C0532925a3b844Bc454e4438f44e`).
- Receive the latest transaction details:
  - **Hash**
  - **Value** (in ETH)
  - **Date** (formatted timestamp)

---

## 🛡️ Security Notes
- **Never hardcode API keys**. Use environment variables.
- Handle rate limits responsibly when making API calls.

---

## 🧩 Contributing
1. Fork the repository
2. Create a new branch (`git checkout -b feature-xyz`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature-xyz`)
5. Open a pull request 🚀

---

## 📜 License
[MIT License](LICENSE)

---

## 🌐 Acknowledgements
- [Telegram Bot API](https://core.telegram.org/bots/api)
- [Etherscan API](https://docs.etherscan.io/)

---

**Happy Tracking! 🚀**

