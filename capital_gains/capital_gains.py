import json
import sys
from decimal import Decimal

from capital_gains.operation import Operation
from capital_gains.portfolio import Portfolio
from capital_gains.tax_calculator import TaxCalculator


def format_taxes(taxes: list) -> list:
    return [{"tax": float(tax["tax"])} for tax in taxes]


def calculate_taxes(operations_list: list):
    portfolio = Portfolio()
    tax_calculator = TaxCalculator()
    operations = [
        Operation(
            action=operation_dict["operation"],
            unit_cost=Decimal(operation_dict["unit-cost"]),
            quantity=int(operation_dict["quantity"]),
        )
        for operation_dict in operations_list
    ]
    taxes = []
    for operation in operations:
        portfolio.update(operation)
        tax = tax_calculator.calculate_tax(
            operation=operation,
            weighted_average_price=portfolio.get_weighted_average_price(),
        )
        taxes.append({"tax": tax})
    return format_taxes(taxes)


class CapitalGains:
    def run(self):
        for line in sys.stdin:
            operations_list = json.loads(line)
            taxes = calculate_taxes(operations_list)
            print(json.dumps(taxes))
