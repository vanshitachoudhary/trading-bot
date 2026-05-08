import argparse
import logging

from bot.orders import place_order
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)
from bot.logging_config import setup_logging

setup_logging()

parser = argparse.ArgumentParser(
    description="Binance Futures Testnet Trading Bot"
)

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", type=float, required=True)
parser.add_argument("--price", type=float)

args = parser.parse_args()

try:

    validate_side(args.side)
    validate_order_type(args.type)
    validate_quantity(args.quantity)
    validate_price(args.type, args.price)

    print("\n===== ORDER REQUEST =====")
    print(vars(args))

    result = place_order(
        symbol=args.symbol,
        side=args.side,
        order_type=args.type,
        quantity=args.quantity,
        price=args.price
    )

    if result.get("success") is False:

        print("\n===== ORDER FAILED =====")
        print(result["error"])

    else:

        print("\n===== ORDER SUCCESS =====")
        print(f"Order ID: {result.get('orderId')}")
        print(f"Status: {result.get('status')}")
        print(f"Executed Qty: {result.get('executedQty')}")
        print(f"Average Price: {result.get('avgPrice')}")

except Exception as e:

    logging.error(f"CLI ERROR -> {str(e)}")

    print(f"\nERROR: {str(e)}")