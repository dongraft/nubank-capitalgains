from unittest import TestCase

from capital_gains import CapitalGains
from capital_gains.capital_gains import calculate_taxes


class CapitalGainsTest(TestCase):
    def setUp(self):
        self.capital_gains = CapitalGains()

    def test_no_tax_due_to_low_total_amount(self):
        operations = [
            {"operation": "buy", "unit-cost": 8.00, "quantity": 100},
            {"operation": "sell", "unit-cost": 20.00, "quantity": 50},
            {"operation": "sell", "unit-cost": 20.00, "quantity": 50},
        ]
        expected = [{"tax": 0.00}, {"tax": 0.00}, {"tax": 0.00}]

        current_taxes = calculate_taxes(operations_list=operations)
        self.assertEqual(expected, current_taxes)

    def test_profit_with_tax_calculation(self):
        operations = [
            {"operation": "buy", "unit-cost": 10.00, "quantity": 10000},
            {"operation": "sell", "unit-cost": 20.00, "quantity": 5000},
        ]
        expected = [{"tax": 0.00}, {"tax": 10000.00}]
        current_taxes = calculate_taxes(operations_list=operations)
        self.assertEqual(expected, current_taxes)

    def test_loss_with_no_tax(self):
        operations = [
            {"operation": "buy", "unit-cost": 10.00, "quantity": 10000},
            {"operation": "sell", "unit-cost": 5.00, "quantity": 5000},
        ]
        expected = [{"tax": 0.00}, {"tax": 0.00}]
        current_taxes = calculate_taxes(operations_list=operations)
        self.assertEqual(expected, current_taxes)
