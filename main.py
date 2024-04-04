import json
import sys
from dataclasses import dataclass
from decimal import Decimal

BUY = "buy"
SELL = "sell"


@dataclass
class Operation:
    kind: str
    unit_cost: Decimal
    quantity: int

    @property
    def cost(self):
        return Decimal(self.quantity * self.unit_cost)


class Portfolio:
    def __init__(self):
        self.total_quantity: int = 0
        self.weighted_average_price: Decimal = Decimal(0)

    def update(self, operation: Operation) -> None:
        if operation.kind == BUY:
            total_cost = self.total_quantity * self.weighted_average_price
            self.total_quantity += operation.quantity
            self.weighted_average_price = (
                total_cost + operation.cost
            ) / self.total_quantity
        elif operation.kind == SELL:
            self.total_quantity -= operation.quantity

    def get_weighted_average_price(self) -> Decimal:
        return self.weighted_average_price


class TaxCalculator:
    TAX_PERCENTAGE = Decimal(0.20)
    FREE_OF_TAX_AMOUNT = 20000

    def __init__(self):
        self.carry_over_loss: Decimal = Decimal(0)

    def calculate_tax(self, operation: Operation, portfolio: Portfolio) -> Decimal:
        if operation.kind != SELL:
            return Decimal(0)

        sell_amount = operation.cost
        profit_loss = (
            operation.unit_cost - portfolio.get_weighted_average_price()
        ) * operation.quantity

        if profit_loss <= 0:
            self.carry_over_loss += -profit_loss
            return Decimal(0)

        # Apply carry-over loss to the current profit
        profit_after_loss = profit_loss - self.carry_over_loss
        if profit_after_loss <= 0:
            self.carry_over_loss -= profit_loss
            return Decimal(0)

        self.carry_over_loss = Decimal(0)  # Reset carry-over loss after applying it

        # Tax calculation
        if sell_amount > self.FREE_OF_TAX_AMOUNT:
            tax = profit_after_loss * self.TAX_PERCENTAGE
            return tax.quantize(Decimal("0.01"))

        return Decimal(0)


class CapitalGains:
    @staticmethod
    def run():
        for line in sys.stdin:
            portfolio = Portfolio()
            tax_calculator = TaxCalculator()
            operations = [
                Operation(
                    kind=operation_dict["operation"],
                    unit_cost=Decimal(operation_dict["unit-cost"]),
                    quantity=int(operation_dict["quantity"]),
                )
                for operation_dict in json.loads(line)
            ]

            taxes = []
            for operation in operations:
                portfolio.update(operation)
                tax = tax_calculator.calculate_tax(operation, portfolio)
                taxes.append({"tax": float(tax)})
            print(json.dumps(taxes))


if __name__ == "__main__":
    capital_gains = CapitalGains()
    capital_gains.run()
