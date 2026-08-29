# Binance Futures Trading Bot

## 1. Project Overview
- A CLI-based trading bot for the Binance Futures Testnet. It supports Market and Limit orders and implements an algorithmic TWAP strategy. All actions are logged to trading_bot.log for auditing.

## 2. Usage Guide
### A. Market Order
- Executes immediately at current market price.

    ``` Bash
    python cli.py BTCUSDT BUY MARKET 0.001
    ```

### B. Limit Order
- Executes only when the market reaches a specific price.

    ``` Bash
    python cli.py BTCUSDT SELL LIMIT 0.001 --price 95000
    ```

### C. TWAP Strategy
- Splits a large order into smaller chunks over time.

    ```Bash
    python cli.py BTCUSDT BUY TWAP 0.01 --duration 5 --splits 10
    ```
- Logic: Buys 0.01 BTC total by placing 10 smaller orders over 5 minutes.

## 3. Order Strategies Explained
### A. Market Order
- Concept: A request to buy or sell immediately at the best available current price.

- Priority: Speed. The order is guaranteed to execute instantly.

### B. Limit Order
- Concept: A request to buy or sell only at a specific price (or better).

- Priority: Price Control. You are guaranteed not to pay more than your set price.


### C. TWAP Strategy (Time-Weighted Average Price)
- Concept: An algorithmic strategy that slices one large order into multiple smaller orders and executes them at regular time intervals.

#### Why use it?

- Reduces Market Impact: Buying a massive amount at once can artificially spike the price against you.

- Smooths Volatility: By buying over time, you get an "average" price rather than risking buying everything at a momentary peak.

## 4. Technical Architecture
### The data flow follows a strict 4-layer separation of concerns:

- Interface (cli.py): Uses argparse to capture user input.

- Guard (bot/validators.py): Blocks invalid inputs (e.g., negative quantities, invalid symbols) before execution.

- Logic (bot/orders.py): The OrderManager class determines the strategy. For TWAP, it manages the timing loop; for standard orders, it formats the payload.

- Connector (bot/client.py): The BinanceClientWrapper handles authentication via .env and executes the final API call using python-binance.
