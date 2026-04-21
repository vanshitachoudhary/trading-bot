import os
from dotenv import load_dotenv

load_dotenv()

class BinanceClient:
    def __init__(self):
        self.mock = True

    def create_order(self, **kwargs):
        return {
            "orderId": 123456,
            "status": "FILLED",
            "symbol": kwargs.get("symbol"),
            "side": kwargs.get("side"),
            "type": kwargs.get("type"),
            "executedQty": kwargs.get("quantity"),
            "avgPrice": kwargs.get("price", "MARKET_PRICE")
        }