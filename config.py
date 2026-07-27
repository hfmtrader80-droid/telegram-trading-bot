import os
from dotenv import load_dotenv

load_dotenv()

BYBIT_API_KEY = os.getenv("BYBIT_API_KEY")
BYBIT_API_SECRET = os.getenv("BYBIT_API_SECRET")

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

SYMBOL = os.getenv("SYMBOL", "BTC/USDT")
TIMEFRAME = os.getenv("TIMEFRAME", "15m")

EMA_FAST = int(os.getenv("EMA_FAST", 20))
EMA_SLOW = int(os.getenv("EMA_SLOW", 50))
RSI_PERIOD = int(os.getenv("RSI_PERIOD", 14))

STOP_LOSS = float(os.getenv("STOP_LOSS", 2))
TAKE_PROFIT = float(os.getenv("TAKE_PROFIT", 5))

TRADE_AMOUNT = float(os.getenv("TRADE_AMOUNT", 20))
