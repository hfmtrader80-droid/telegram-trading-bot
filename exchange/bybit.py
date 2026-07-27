import ccxt
from config import BYBIT_API_KEY, BYBIT_API_SECRET


class BybitClient:
    def __init__(self):
        self.exchange = ccxt.bybit({
            "apiKey": BYBIT_API_KEY,
            "secret": BYBIT_API_SECRET,
            "enableRateLimit": True,
            "options": {
                "defaultType": "linear"
            }
        })

    def balance(self):
        return self.exchange.fetch_balance()

    def ticker(self, symbol):
        return self.exchange.fetch_ticker(symbol)

    def candles(self, symbol, timeframe="15m", limit=200):
        return self.exchange.fetch_ohlcv(symbol, timeframe, limit=limit)

    def buy(self, symbol, amount):
        return self.exchange.create_market_buy_order(symbol, amount)

    def sell(self, symbol, amount):
        return self.exchange.create_market_sell_order(symbol, amount)
