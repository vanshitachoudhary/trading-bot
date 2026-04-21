import argparse
from bot.orders import place_order
from bot.validators import validate_side, validate_order_type
from bot.logging_config import setup_logging

setup_logging()

parser = argparse.ArgumentParser()
parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", type=float, required=True)
parser.add_argument("--price", type=float)

args = parser.parse_args()

validate_side(args.side)
validate_order_type(args.type)

result = place_order(
    symbol=args.symbol,
    side=args.side,
    order_type=args.type,
    quantity=args.quantity,
    price=args.price
)

print("\n===== ORDER RESULT =====")
print(result)