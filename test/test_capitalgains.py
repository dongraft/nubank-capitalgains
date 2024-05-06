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

    def test_selling_more_stock_than_available(self):
        operations = [
            {"operation": "buy", "unit-cost": 10, "quantity": 10000},
            {"operation": "sell", "unit-cost": 20, "quantity": 11000},
        ]
        expected = [{"tax": 0.00}, {"error": "Can't sell more stocks than you have"}]

        current_taxes = calculate_taxes(operations_list=operations)
        self.assertEqual(expected, current_taxes)

    def test_selling_more_stock_than_available_but_retry(self):
        operations = [
            {"operation": "buy", "unit-cost": 10, "quantity": 10000},
            {"operation": "sell", "unit-cost": 20, "quantity": 11000},
            {"operation": "sell", "unit-cost": 20, "quantity": 5000},
        ]
        expected = [
            {"tax": 0},
            {"error": "Can't sell more stocks than you have"},
            {"tax": 10000},
        ]

        current_taxes = calculate_taxes(operations_list=operations)
        self.assertEqual(expected, current_taxes)

    def test_disabling_account_after_several_errors(self):
        operations = [
            {"operation": "sell", "unit-cost": 20, "quantity": 10000},
            {"operation": "sell", "unit-cost": 20, "quantity": 10000},
            {"operation": "sell", "unit-cost": 20, "quantity": 10000},
            {"operation": "buy", "unit-cost": 10, "quantity": 10000},
            {"operation": "buy", "unit-cost": 10, "quantity": 10000},
            {"operation": "sell", "unit-cost": 20, "quantity": 10000},
        ]

        expected = [
            {"error": "Can't sell more stocks than you have"},
            {"error": "Can't sell more stocks than you have"},
            {"error": "Can't sell more stocks than you have"},
            {"error": "Your account is blocked"},
            {"error": "Your account is blocked"},
            {"error": "Your account is blocked"},
        ]

        current_taxes = calculate_taxes(operations_list=operations)
        self.assertEqual(expected, current_taxes)

    def test_disabling_account_after_several_errors(self):
        operations = [
            {"operation": "sell", "unit-cost": 20, "quantity": 10000},
            {"operation": "sell", "unit-cost": 20, "quantity": 10000},
            {"operation": "buy", "unit-cost": 10, "quantity": 10000},
            {"operation": "sell", "unit-cost": 20, "quantity": 110000},
            {"operation": "sell", "unit-cost": 20, "quantity": 110000},
            {"operation": "sell", "unit-cost": 20, "quantity": 110000},
            {"operation": "buy", "unit-cost": 10, "quantity": 10000},
            {"operation": "sell", "unit-cost": 20, "quantity": 10000},
        ]
        expected = [
            {"error": "Can't sell more stocks than you have"},
            {"error": "Can't sell more stocks than you have"},
            {"tax": 0.0},
            {"error": "Can't sell more stocks than you have"},
            {"error": "Can't sell more stocks than you have"},
            {"error": "Can't sell more stocks than you have"},
            {"error": "Your account is blocked"},
            {"error": "Your account is blocked"},
        ]

        current_taxes = calculate_taxes(operations_list=operations)
        self.assertEqual(expected, current_taxes)

    def test_disabling_account_after_several_errors(self):
        operations = [
            {"operation": "sell", "unit-cost": 20, "quantity": 10000},
            {"operation": "sell", "unit-cost": 20, "quantity": 10000},
            {"operation": "buy", "unit-cost": 10, "quantity": 10000},
            {"operation": "sell", "unit-cost": 20, "quantity": 110000},
            {"operation": "sell", "unit-cost": 20, "quantity": 110000},
            {"operation": "sell", "unit-cost": 20, "quantity": 110000},
            {"operation": "buy", "unit-cost": 10, "quantity": 10000},
            {"operation": "sell", "unit-cost": 20, "quantity": 10000},
        ]
        expected = [
            {"error": "Can't sell more stocks than you have"},
            {"error": "Can't sell more stocks than you have"},
            {"tax": 0.0},
            {"error": "Can't sell more stocks than you have"},
            {"error": "Can't sell more stocks than you have"},
            {"error": "Can't sell more stocks than you have"},
            {"error": "Your account is blocked"},
            {"error": "Your account is blocked"},
        ]

        current_taxes = calculate_taxes(operations_list=operations)
        self.assertEqual(expected, current_taxes)

    def test_multiple_operations_a(self):
        operations = [
            {"operation": "buy", "unit-cost": 10, "quantity": 10000, "ticker": "AAPL"},
            {"operation": "buy", "unit-cost": 15, "quantity": 10000, "ticker": "MANU"},
            {"operation": "sell", "unit-cost": 30, "quantity": 10000, "ticker": "MANU"},
            {"operation": "sell", "unit-cost": 5, "quantity": 10000, "ticker": "AAPL"},
        ]

        expected = [{"tax": 0}, {"tax": 0}, {"tax": 30000}, {"tax": 0}]

        current_taxes = calculate_taxes(operations_list=operations)
        self.assertEqual(expected, current_taxes)
