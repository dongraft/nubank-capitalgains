from decimal import Decimal

from capital_gains.constants import FREE_OF_TAX_AMOUNT, SELL, TAX_PERCENTAGE
from capital_gains.operation import Operation


class TaxCalculator:
    def __init__(self):
        self.loss_carry: Decimal = Decimal("0")

    def calculate_tax(
        self, operation: Operation, weighted_average_price: Decimal
    ) -> Decimal:
        if operation.action != SELL:
            return Decimal("0")

        profit = (operation.unit_cost - weighted_average_price) * operation.quantity

        self.loss_carry += profit
        if self.loss_carry < 0:
            return Decimal("0")

        operation_profit = self.loss_carry
        self.loss_carry = Decimal("0")

        if operation.cost > FREE_OF_TAX_AMOUNT:
            tax = operation_profit * TAX_PERCENTAGE
            return tax.quantize(Decimal("0.01"))

        return Decimal("0")
