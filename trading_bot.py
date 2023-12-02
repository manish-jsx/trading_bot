import ccxt
import pandas as pd
import numpy as np
import time

# Initialize Binance exchange object
exchange = ccxt.binance({
    'apiKey': 'YOUR_API_KEY',
    'secret': 'YOUR_SECRET_KEY',
})

# Set trading parameters
symbol = 'BTC/USDT'
timeframe = '1h'
fast_ma_period = 10
slow_ma_period = 30
quantity = 0.001  # Number of coins to buy/sell

# Function to get historical OHLCV data
def fetch_ohlcv(symbol, timeframe, limit=100):
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe, limit=limit)
    df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df.set_index('timestamp', inplace=True)
    return df

# Function to calculate moving averages
def calculate_moving_averages(df, fast_period, slow_period):
    df['fast_ma'] = df['close'].rolling(window=fast_period, min_periods=1).mean()
    df['slow_ma'] = df['close'].rolling(window=slow_period, min_periods=1).mean()

# Function to execute buy order
def execute_buy_order(symbol, quantity):
    print(f'Executing BUY order for {quantity} {symbol}')
    order = exchange.create_market_buy_order(symbol, quantity)

# Function to execute sell order
def execute_sell_order(symbol, quantity):
    print(f'Executing SELL order for {quantity} {symbol}')
    order = exchange.create_market_sell_order(symbol, quantity)

# Main trading loop
while True:
    try:
        # Fetch historical data
        historical_data = fetch_ohlcv(symbol, timeframe, limit=100)

        # Calculate moving averages
        calculate_moving_averages(historical_data, fast_ma_period, slow_ma_period)

        # Get the last row of data
        last_row = historical_data.iloc[-1]

        # Buy signal: Fast MA crosses above Slow MA
        if last_row['fast_ma'] > last_row['slow_ma']:
            execute_buy_order(symbol, quantity)

        # Sell signal: Fast MA crosses below Slow MA
        elif last_row['fast_ma'] < last_row['slow_ma']:
            execute_sell_order(symbol, quantity)

        # Pause for a while before the next iteration
        time.sleep(600)  # Pause for 10 minutes

    except Exception as e:
        print(f'Error: {e}')
        time.sleep(60)  # Pause for 1 minute in case of an error
