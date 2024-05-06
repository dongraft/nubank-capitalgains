from decimal import Decimal

from capital_gains.constants import BUY, SELL
from capital_gains.operation import Operation


class Portfolio:
    def __init__(self):
        self.tickers = {}
        self.error_count = 0

    def init_ticker(self, ticker):
        ticker_dict = {
            "current_stock_quantity": 0,
            "weighted_average_price": Decimal("0"),
        }
        self.tickers[ticker] = ticker_dict

    def update(self, operation: Operation) -> None:
        if operation.ticker not in self.tickers:
            self.init_ticker(operation.ticker)

        ticker_dict = self.tickers[operation.ticker]

        if self.error_count > 2:
            raise ValueError("Your account is blocked")

        if operation.action == BUY:
            previous_weighted_average_cost = (
                ticker_dict["current_stock_quantity"]
                * ticker_dict["weighted_average_price"]
            )
            ticker_dict["current_stock_quantity"] += operation.quantity
            ticker_dict["weighted_average_price"] = (
                previous_weighted_average_cost + operation.cost
            ) / ticker_dict["current_stock_quantity"]
            ticker_dict["weighted_average_price"] = ticker_dict[
                "weighted_average_price"
            ].quantize(Decimal("0.01"))
        elif operation.action == SELL:
            if ticker_dict["current_stock_quantity"] < operation.quantity:
                self.error_count += 1
                raise ValueError("Can't sell more stocks than you have")
            ticker_dict["current_stock_quantity"] -= operation.quantity

        self.tickers[operation.ticker] = ticker_dict

        self.error_count = 0

    def get_weighted_average_price(self, ticker) -> Decimal:
        return self.tickers[ticker]["weighted_average_price"]
