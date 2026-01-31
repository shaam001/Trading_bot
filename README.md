# Binance Futures Trading Bot

# Installation & Setup
## Prerequisites
- Python 3.12 or higher installed on your system.

- A Binance Futures Testnet account. Get free API keys from: https://testnet.binancefuture.com/

## Step 1: Clone or Download
- Download this project folder to your local machine from `https://github.com/shaam001/Trading_bot/tree/main`.

## Step 2: Install Dependencies
- Open your terminal, navigate to the project folder, and run:

   ```Bash
   pip install -r requirements.txt
   ```

## Step 3: Configure API Keys
- Create a new file in the root folder named .env.

- Open it with a text editor and add your Testnet keys:
   ```
   BINANCE_API_KEY=your_actual_api_key_here
   BINANCE_SECRET=your_actual_secret_key_here
   ```

## How to Run
- Run the bot using the python cli.py command followed by your order details.

### 1. Market Order

- Syntax: python cli.py [SYMBOL] [SIDE] MARKET [QUANTITY]
- Example: Buy 0.002 BTC immediately.

   ```Bash
   python cli.py BTCUSDT BUY MARKET 0.002
   ```

### 2. Limit Order

- Syntax: python cli.py [SYMBOL] [SIDE] LIMIT [QUANTITY] --price [PRICE]

- Example: Sell 0.002 BTC if the price hits $95,000.

   ```Bash
   python cli.py BTCUSDT SELL LIMIT 0.002 --price 95000
   ```

### 3. TWAP Strategy

- Syntax: python cli.py [SYMBOL] [SIDE] TWAP [TOTAL_QTY] --duration [MINUTES] --splits [COUNT]

- Example: Buy 0.01 BTC total, split into 4 orders over 2 minutes.

   ```Bash
   python cli.py BTCUSDT BUY TWAP 0.01 --duration 2 --splits 4
   ```