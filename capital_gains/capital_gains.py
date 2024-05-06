import json
import sys
from decimal import Decimal

from capital_gains.operation import Operation
from capital_gains.portfolio import Portfolio
from capital_gains.tax_calculator import TaxCalculator


def calculate_taxes(operations_list: list):
    portfolio = Portfolio()
    tax_calculator = TaxCalculator()
    operations = [
        Operation(
            action=operation_dict["operation"],
            unit_cost=Decimal(operation_dict["unit-cost"]),
            quantity=int(operation_dict["quantity"]),
            ticker=operation_dict["ticker"],
        )
        for operation_dict in operations_list
    ]
    taxes = []
    for operation in operations:
        try:
            portfolio.update(operation)
            tax = tax_calculator.calculate_tax(
                operation=operation,
                weighted_average_price=portfolio.get_weighted_average_price(
                    ticker=operation.ticker
                ),
            )
            taxes.append({"tax": float(tax)})
        except ValueError as e:
            taxes.append({"error": f"{e}"})

    return taxes


class CapitalGains:
    def run(self):
        for line in sys.stdin:
            operations_list = json.loads(line)
            taxes = calculate_taxes(operations_list)
            print(json.dumps(taxes))
