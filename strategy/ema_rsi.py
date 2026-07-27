import pandas as pd
import ta


def calculate_signal(candles, ema_fast=20, ema_slow=50, rsi_period=14):
    df = pd.DataFrame(
        candles,
        columns=["time", "open", "high", "low", "close", "volume"]
    )

    df["EMA_FAST"] = ta.trend.ema_indicator(
        df["close"],
        window=ema_fast
    )

    df["EMA_SLOW"] = ta.trend.ema_indicator(
        df["close"],
        window=ema_slow
    )

    df["RSI"] = ta.momentum.rsi(
        df["close"],
        window=rsi_period
    )

    last = df.iloc[-1]

    if (
        last["EMA_FAST"] > last["EMA_SLOW"]
        and last["RSI"] < 30
    ):
        return "BUY"

    if (
        last["EMA_FAST"] < last["EMA_SLOW"]
        and last["RSI"] > 70
    ):
        return "SELL"

    return "HOLD"
