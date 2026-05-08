import os
from dotenv import load_dotenv
from binance.client import Client

load_dotenv()


class BinanceClient:

    def __init__(self):

        api_key = os.getenv("API_KEY")
        api_secret = os.getenv("API_SECRET")

        self.client = Client(api_key, api_secret)

        # Binance Futures Testnet URL
        self.client.FUTURES_URL = "https://testnet.binancefuture.com"

    def create_order(self, **kwargs):

        order_type = kwargs.get("type")

        params = {
            "symbol": kwargs.get("symbol"),
            "side": kwargs.get("side"),
            "type": order_type,
            "quantity": kwargs.get("quantity")
        }

        if order_type == "LIMIT":
            params["price"] = kwargs.get("price")
            params["timeInForce"] = "GTC"

        order = self.client.futures_create_order(**params)

        return {
            "orderId": order.get("orderId"),
            "status": order.get("status"),
            "symbol": order.get("symbol"),
            "side": order.get("side"),
            "type": order.get("type"),
            "executedQty": order.get("executedQty"),
            "avgPrice": order.get("avgPrice")
        }