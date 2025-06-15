import yfinance as yf
import pandas as pd
from indicators1 import calculate_sma, calculate_rsi, calculate_atr
from signals1 import check_signal
from telegram1 import send_telegram_message

def scan_stock(symbol):
    try:
        df = yf.download(symbol, period="6mo", interval="1h")
        df = calculate_sma(df)
        df = calculate_rsi(df)
        df = calculate_atr(df)
        signal = check_signal(df)

        if signal:
            print(signal)
            send_telegram_message(signal)
        else:
            print(f"🟡 [{symbol}] Sin señal clara")

    except Exception as e:
        print(f"❌ Error procesando {symbol}: {e}")

def scan_all_stocks(stocks=None):
    stocks = stocks or ["AAPL", "TSLA", "MSFT", "AMZN", "GOOG"]
    for symbol in stocks:
        scan_stock(symbol)