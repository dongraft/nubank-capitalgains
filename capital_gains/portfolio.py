from decimal import Decimal

from capital_gains.constants import BUY, SELL
from capital_gains.operation import Operation


class Portfolio:
    def __init__(self):
        self.current_stock_quantity: int = 0
        self.weighted_average_price: Decimal = Decimal("0")

    def update(self, operation: Operation) -> Operation:
        if operation.action == BUY:
            previous_weighted_average_cost = (
                self.current_stock_quantity * self.weighted_average_price
            )
            self.current_stock_quantity += operation.quantity
            self.weighted_average_price = (
                previous_weighted_average_cost + operation.cost
            ) / self.current_stock_quantity
            self.weighted_average_price = self.weighted_average_price.quantize(
                Decimal("0.01")
            )
        elif operation.action == SELL:
            self.current_stock_quantity -= operation.quantity

    def get_weighted_average_price(self) -> Decimal:
        return self.weighted_average_price
