from decimal import Decimal

from capital_gains.constants import BUY, SELL
from capital_gains.operation import Operation
from capital_gains.tax_calculator import TaxCalculator


class Portfolio:
    def __init__(self):
        self.current_stock_quantity: int = 0
        self.weighted_average_price: Decimal = Decimal("0")
        self.tax_calculator = TaxCalculator()

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

        tax = self.tax_calculator.calculate_tax(
            operation=operation, weighted_average_price=self.weighted_average_price
        )
        return Operation(
            action=operation.action,
            unit_cost=operation.unit_cost,
            quantity=operation.quantity,
            tax=tax,
        )
