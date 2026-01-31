import argparse
from bot.logging_config import setup_logging
from bot.validators import validate_order_input
from bot.orders import OrderManager

def main():
    # Setup Logging: Activation of logging system
    logger = setup_logging()

    # Argument Parser
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Bot")
    parser.add_argument("symbol", type=str, help="Trading Pair (e.g., BTCUSDT)") # name of the coin
    parser.add_argument("side", type=str, choices=["BUY", "SELL"], help="Order Side")
    parser.add_argument("type", type=str, choices=["MARKET", "LIMIT", "TWAP"], help="Order Type")
    parser.add_argument("quantity", type=float, help="Quantity") # amount to buy or sell
    parser.add_argument("--price", type=float, help="Price (Required for LIMIT)", default=None)
    parser.add_argument("--duration", type=int, help="TWAP Duration (minutes)", default=5)
    parser.add_argument("--splits", type=int, help="TWAP Splits", default=5)

    # It will parse the arguments from command line
    args = parser.parse_args()

    # validate inputs
    try:
        validate_order_input(args.symbol, args.side, args.type, args.quantity, args.price)
    except ValueError as e:
        print(f"Validation Error: {e}")
        logger.error(f"Validation Error: {e}")
        return

    # OrderManager to place orders
    manager = OrderManager()

    if args.type.upper() == "TWAP":
        manager.execute_twap(args.symbol, args.side, args.quantity, args.duration, args.splits)
    else:
        manager.place_order(args.symbol, args.side, args.type, args.quantity, args.price)

if __name__ == "__main__":
    main()