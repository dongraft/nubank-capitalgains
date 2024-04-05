from decimal import Decimal

from capital_gains.constants import SELL
from capital_gains.operation import Operation
from capital_gains.portfolio import Portfolio


class TaxCalculator:
    TAX_PERCENTAGE = Decimal(0.20)
    FREE_OF_TAX_AMOUNT = 20000

    def __init__(self):
        self.profit_carry_over_loss: Decimal = Decimal(0)

    def calculate_tax(self, operation: Operation, portfolio: Portfolio) -> Decimal:
        if operation.kind != SELL:
            return Decimal(0)

        profit = (
            operation.unit_cost - portfolio.get_weighted_average_price()
        ) * operation.quantity

        if profit < 0:
            self.profit_carry_over_loss += -profit
            return Decimal(0)

        profit_after_loss = profit - self.profit_carry_over_loss
        if profit_after_loss < 0:
            self.profit_carry_over_loss -= profit
            return Decimal(0)

        self.profit_carry_over_loss = Decimal(0)

        if operation.cost > self.FREE_OF_TAX_AMOUNT:
            tax = profit_after_loss * self.TAX_PERCENTAGE
            return tax.quantize(Decimal("0.01"))

        return Decimal(0)
