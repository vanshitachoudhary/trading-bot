from bot.client import BinanceClient
import logging

client = BinanceClient()

def place_order(symbol, side, order_type, quantity, price=None):
    try:
        order = client.create_order(
            symbol=symbol,
            side=side,
            type=order_type,
            quantity=quantity,
            price=price
        )
        logging.info(f"Order: {order}")
        return order
    except Exception as e:
        logging.error(str(e))
        return {"error": str(e)}