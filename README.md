
# Cryptocurrency Trading Bot with Moving Average Crossover Strategy

This Python script implements a basic cryptocurrency trading bot that uses a simple moving average crossover strategy. The bot connects to the Binance exchange, fetches historical price data, calculates moving averages, and executes buy/sell orders based on the crossover signals.

## Prerequisites

Before running the script, make sure you have the following:

- Python installed (version 3.x recommended)
- Required Python libraries installed. You can install them using the following command:

  ```bash
  pip install ccxt pandas numpy
  ```

- Binance API key and secret. Obtain them by creating a Binance account and generating API keys in your account settings.

## Setup

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/manish-jsx/trading_bot.git
   ```

2. Navigate to the project directory:

   ```bash
   cd cryptobot
   ```



3. Install required packages:

   ```bash
   pip install -r requirements.txt
   ```



4. Open the `trading_bot.py` file in a text editor and replace the placeholder values with your Binance API key and secret.

   ```python
   'apiKey': 'YOUR_API_KEY',
   'secret': 'YOUR_SECRET_KEY',
   ```

## Usage

Run the trading bot script using the following command:

```bash
python trading_bot.py
```

The bot will start executing buy and sell orders based on the moving average crossover strategy. Make sure to monitor the bot's behavior and adjust parameters as needed.

## Customization

Feel free to customize the script according to your trading strategy, risk management, and other preferences. You can modify parameters such as the trading symbol, timeframe, moving average periods, and quantity.

## Disclaimer

- **Use at your own risk:** Trading cryptocurrencies involves risks, and the provided script is for educational purposes only. Be cautious when using real money for trading.
- **Security:** Keep your API keys secure and do not share them publicly. Use only the necessary permissions required for trading.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
