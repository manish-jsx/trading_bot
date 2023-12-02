import pytest
import pandas as pd
from trading_bot import run_trading_strategy

@pytest.mark.parametrize("symbol, timeframe, fast_ma_period, slow_ma_period, quantity", [
    ("BTC/USDT", "1h", 10, 30, 0.001),
    # Add more test cases as needed
])
def test_trading_strategy(symbol, timeframe, fast_ma_period, slow_ma_period, quantity):
    # You might want to mock the ccxt library for testing purposes
    # For simplicity, let's assume fetch_ohlcv always returns the same data
    def mock_fetch_ohlcv(symbol, timeframe, limit=100):
        return pd.DataFrame({
            'timestamp': [pd.Timestamp.now()] * limit,
            'open': [1.0] * limit,
            'high': [2.0] * limit,
            'low': [0.5] * limit,
            'close': [1.5] * limit,
            'volume': [100.0] * limit
        })

    # Override the fetch_ohlcv function with our mock
    with monkeypatch.context() as m:
        m.setattr("trading_bot.fetch_ohlcv", mock_fetch_ohlcv)

        # Run the trading strategy
        run_trading_strategy(symbol, timeframe, fast_ma_period, slow_ma_period, quantity)
