def check_signal(df):
    latest = df.iloc[-1]
    previous = df.iloc[-2]

    rsi = latest["RSI"]
    price = latest["Close"]
    sma = latest["SMA"]
    atr = latest["ATR"]

    # Cálculo básico de SL y TP
    sl_multiplier = 1.5
    tp_multiplier = 2.0

    stop_loss = round(price - sl_multiplier * atr, 2)
    take_profit = round(price + tp_multiplier * atr, 2)

    if previous["RSI"] < 30 and rsi >= 30 and price > sma:
        return f"🟢 [Compra] {latest.name} | Precio: {price:.2f} | RSI: {rsi:.2f} | SL: {stop_loss} | TP: {take_profit}"

    elif previous["RSI"] > 70 and rsi <= 70 and price < sma:
        return f"🔴 [Venta] {latest.name} | Precio: {price:.2f} | RSI: {rsi:.2f} | SL: {stop_loss} | TP: {take_profit}"

    else:
        return None