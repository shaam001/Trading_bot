"""Validates user inputs before sending to API."""

# symbol: str, means symbol is expected to be a string
def validate_order_input(symbol: str, side: str, order_type: str, quantity: float, price: float = None):

    if not symbol or not isinstance(symbol, str):
        raise ValueError(f"Invalid symbol: {symbol}")
    
    # Validate side, order_type, quantity, and price
    if side.upper() not in ['BUY', 'SELL']:
        raise ValueError(f"Invalid side: {side}. Must be BUY or SELL.")
    
    if order_type.upper() not in ['MARKET', 'LIMIT', 'TWAP']:
        raise ValueError(f"Invalid order type: {order_type}")
    
    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")
    
    if order_type.upper() == 'LIMIT' and (price is None or price <= 0):
        raise ValueError("Price must be greater than 0 for LIMIT orders")

    return True