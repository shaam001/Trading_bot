import logging
import time
from binance.enums import * # pre made variables from binance
from binance.exceptions import BinanceAPIException
from bot.client import BinanceClientWrapper

logger = logging.getLogger(__name__)

class OrderManager:
    # Initialize the Binance Client
    def __init__(self):
        self.wrapper = BinanceClientWrapper()
        self.client = self.wrapper.get_client()

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            logger.info(f"Sending Order: {side} {quantity} {symbol} ({order_type})")
            
            if order_type.upper() == 'MARKET':
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side.upper(),
                    type=ORDER_TYPE_MARKET,
                    quantity=quantity
                )
            elif order_type.upper() == 'LIMIT':
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side.upper(),
                    type=ORDER_TYPE_LIMIT,
                    timeInForce=TIME_IN_FORCE_GTC, # Good Till Cancelled, it tells the order to remain active until it is filled or cancelled
                    quantity=quantity,
                    price=price
                )
            else:
                logger.error("Unsupported order type in place_order")
                return None

            # Requirement: Print output details
            print("\n--- Order Success ---")
            print(f"Order ID: {order.get('orderId')}")
            print(f"Status: {order.get('status')}")
            print(f"Executed Qty: {order.get('executedQty')}")
            print(f"Avg Price: {order.get('avgPrice', 'N/A')}")
            
            logger.info(f"Order Success: {order}")
            return order

        except BinanceAPIException as e:
            logger.error(f"Binance API Error: {e.message}")
            print(f"\n API Error: {e.message}")
        except Exception as e:
            logger.error(f"Network/Unknown Error: {str(e)}")
            print(f"\n Error: {str(e)}")

    # TWAP Implementation: Time-Weighted Average Price
    def execute_twap(self, symbol, side, total_quantity, duration_minutes, splits):
        """TWAP Strategy"""
        logger.info(f"Starting TWAP: {side} {total_quantity} {symbol} over {duration_minutes} min")
        
        chunk_size = round(total_quantity / splits, 3) # Simple rounding to 3 decimal places
        # wait time between orders in seconds
        delay = (duration_minutes * 60) / splits

        for i in range(splits):
            print(f"\n--- TWAP Round {i+1}/{splits} ---")
            self.place_order(symbol, side, 'MARKET', chunk_size)
            
            # don't wait for the last order to complete
            if i < splits - 1:
                print(f"Waiting {delay} seconds...")
                time.sleep(delay)
        
        logger.info("TWAP Completed")