from bot.client import BinanceClient
import logging

client = BinanceClient()



def place_order(symbol, side, order_type, quantity, price=None):

    try:

        logging.info(
            f"ORDER REQUEST -> Symbol: {symbol}, "
            f"Side: {side}, Type: {order_type}, "
            f"Quantity: {quantity}, Price: {price}"
        )

        order = client.create_order(
            symbol=symbol,
            side=side,
            type=order_type,
            quantity=quantity,
            price=price
        )

        logging.info(f"{order_type} ORDER RESPONSE -> {order}")

        return order

    except Exception as e:

        logging.error(f"ORDER ERROR -> {str(e)}")

        return {
            "success": False,
            "error": str(e)
        }