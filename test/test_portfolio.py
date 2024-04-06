from decimal import Decimal
from unittest import TestCase

from capital_gains.constants import BUY, SELL
from capital_gains.operation import Operation
from capital_gains.portfolio import Portfolio


class PortfolioTest(TestCase):
    def setUp(self):
        self.portfolio = Portfolio()

    def test_stock_quantity_update(self):
        self.portfolio.update(
            operation=Operation(action=BUY, unit_cost=Decimal("10.00"), quantity=10)
        )
        self.assertEqual(10, self.portfolio.current_stock_quantity)
        self.portfolio.update(
            operation=Operation(action=SELL, unit_cost=Decimal("10.00"), quantity=5)
        )
        self.assertEqual(5, self.portfolio.current_stock_quantity)
        self.portfolio.update(
            operation=Operation(action=BUY, unit_cost=Decimal("10.00"), quantity=30)
        )
        self.assertEqual(35, self.portfolio.current_stock_quantity)

    def test_weighted_average_price(self):
        self.portfolio.update(
            operation=Operation(action=BUY, unit_cost=Decimal("20.00"), quantity=20)
        )
        self.assertEqual(Decimal("20.00"), self.portfolio.weighted_average_price)
        self.portfolio.update(
            operation=Operation(action=BUY, unit_cost=Decimal("40.00"), quantity=20)
        )
        self.assertEqual(Decimal("30.00"), self.portfolio.weighted_average_price)
        self.portfolio.update(
            operation=Operation(action=BUY, unit_cost=Decimal("60.00"), quantity=20)
        )
        self.assertEqual(Decimal("40.00"), self.portfolio.weighted_average_price)
