from decimal import Decimal

from capital_gains.constants import SELL
from capital_gains.operation import Operation
from capital_gains.portfolio import Portfolio


class TaxCalculator:
    TAX_PERCENTAGE = Decimal(0.20)
    FREE_OF_TAX_AMOUNT = 20000

    def __init__(self):
        self.loss_carry: Decimal = Decimal(0)

    def calculate_tax(self, operation: Operation, portfolio: Portfolio) -> Decimal:
        if operation.kind != SELL:
            return Decimal(0)

        profit = (
            operation.unit_cost - portfolio.get_weighted_average_price()
        ) * operation.quantity

        self.loss_carry += profit
        if self.loss_carry < 0:
            return Decimal(0)

        operation_profit = self.loss_carry
        self.loss_carry = Decimal(0)

        if operation.cost > self.FREE_OF_TAX_AMOUNT:
            tax = operation_profit * self.TAX_PERCENTAGE
            return tax.quantize(Decimal("0.01"))

        return Decimal(0)
