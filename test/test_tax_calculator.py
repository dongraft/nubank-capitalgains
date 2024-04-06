from decimal import Decimal
from unittest import TestCase

from capital_gains.constants import BUY, SELL
from capital_gains.operation import Operation
from capital_gains.portfolio import Portfolio
from capital_gains.tax_calculator import TaxCalculator


class TaxCalculatorTest(TestCase):
    def setUp(self):
        self.portfolio = Portfolio()
        self.operation_buy = Operation(
            action=BUY, unit_cost=Decimal("10.00"), quantity=100
        )
        self.operation_sell_1 = Operation(
            action=SELL, unit_cost=Decimal("2.00"), quantity=5
        )
        self.operation_sell_2 = Operation(
            action=SELL, unit_cost=Decimal("900.00"), quantity=20
        )
        self.operation_sell_3 = Operation(
            action=SELL, unit_cost=Decimal("1010.00"), quantity=20
        )

    def test_no_tax_when_not_buying(self):
        operation = self.portfolio.update(operation=self.operation_buy)
        self.assertEqual(Decimal("0"), operation.tax)

    def test_no_tax_when_no_profit(self):
        self.portfolio.update(operation=self.operation_buy)
        last_operation = self.portfolio.update(operation=self.operation_sell_1)

        self.assertLess(self.portfolio.tax_calculator.loss_carry, 0)
        self.assertEqual(Decimal("0"), last_operation.tax)

    def test_no_tax_when_free_of_tax_cost(self):
        self.portfolio.update(operation=self.operation_buy)
        self.portfolio.update(operation=self.operation_sell_1)
        last_operation = self.portfolio.update(operation=self.operation_sell_2)

        self.assertEqual(Decimal("0"), last_operation.tax)

    def test_tax_when_bigger_than_free_of_tax_cost(self):
        self.portfolio.update(operation=self.operation_buy)
        self.portfolio.update(operation=self.operation_sell_1)
        self.portfolio.update(operation=self.operation_sell_2)
        last_operation = self.portfolio.update(operation=self.operation_sell_3)

        self.assertEqual(Decimal("4000.00"), last_operation.tax)
