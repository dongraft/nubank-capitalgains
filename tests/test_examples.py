import unittest
from unittest import TestCase

from capital_gains import CapitalGains


class CapitalGainsExamplesTest(TestCase):
    def setUp(self):
        self.capital_gains = CapitalGains()

    def test_case_1(self):
        operations = [
            {"operation": "buy", "unit-cost": 10.00, "quantity": 100},
            {"operation": "sell", "unit-cost": 15.00, "quantity": 50},
            {"operation": "sell", "unit-cost": 15.00, "quantity": 50},
        ]
        expected = [{"tax": 0.00}, {"tax": 0.00}, {"tax": 0.00}]

        current_taxes = self.capital_gains.calculate_taxes(operations_list=operations)
        self.assertEqual(current_taxes, expected)

    def test_case_2(self):
        operations = [
            {"operation": "buy", "unit-cost": 10.00, "quantity": 10000},
            {"operation": "sell", "unit-cost": 20.00, "quantity": 5000},
            {"operation": "sell", "unit-cost": 5.00, "quantity": 5000},
        ]
        expected = [{"tax": 0.00}, {"tax": 10000.00}, {"tax": 0.00}]
        current_taxes = self.capital_gains.calculate_taxes(operations_list=operations)
        self.assertEqual(current_taxes, expected)

    def test_case_3(self):
        operations = [
            {"operation": "buy", "unit-cost": 10.00, "quantity": 10000},
            {"operation": "sell", "unit-cost": 5.00, "quantity": 5000},
            {"operation": "sell", "unit-cost": 20.00, "quantity": 3000},
        ]
        expected = [{"tax": 0.00}, {"tax": 0.00}, {"tax": 1000.00}]
        current_taxes = self.capital_gains.calculate_taxes(operations_list=operations)
        self.assertEqual(current_taxes, expected)

    def test_case_4(self):
        operations = [
            {"operation": "buy", "unit-cost": 10.00, "quantity": 10000},
            {"operation": "buy", "unit-cost": 25.00, "quantity": 5000},
            {"operation": "sell", "unit-cost": 15.00, "quantity": 10000},
        ]
        expected = [{"tax": 0.00}, {"tax": 0.00}, {"tax": 0.00}]
        current_taxes = self.capital_gains.calculate_taxes(operations_list=operations)
        self.assertEqual(current_taxes, expected)

    def test_case_5(self):
        operations = [
            {"operation": "buy", "unit-cost": 10.00, "quantity": 10000},
            {"operation": "buy", "unit-cost": 25.00, "quantity": 5000},
            {"operation": "sell", "unit-cost": 15.00, "quantity": 10000},
            {"operation": "sell", "unit-cost": 25.00, "quantity": 5000},
        ]
        expected = [{"tax": 0.00}, {"tax": 0.00}, {"tax": 0.00}, {"tax": 10000.00}]
        current_taxes = self.capital_gains.calculate_taxes(operations_list=operations)
        self.assertEqual(current_taxes, expected)

    def test_case_6(self):
        operations = [
            {"operation": "buy", "unit-cost": 10.00, "quantity": 10000},
            {"operation": "sell", "unit-cost": 2.00, "quantity": 5000},
            {"operation": "sell", "unit-cost": 20.00, "quantity": 2000},
            {"operation": "sell", "unit-cost": 20.00, "quantity": 2000},
            {"operation": "sell", "unit-cost": 25.00, "quantity": 1000},
        ]
        expected = [
            {"tax": 0.00},
            {"tax": 0.00},
            {"tax": 0.00},
            {"tax": 0.00},
            {"tax": 3000.00},
        ]
        current_taxes = self.capital_gains.calculate_taxes(operations_list=operations)
        self.assertEqual(current_taxes, expected)

    def test_case_7(self):
        operations = [
            {"operation": "buy", "unit-cost": 10.00, "quantity": 10000},
            {"operation": "sell", "unit-cost": 2.00, "quantity": 5000},
            {"operation": "sell", "unit-cost": 20.00, "quantity": 2000},
            {"operation": "sell", "unit-cost": 20.00, "quantity": 2000},
            {"operation": "buy", "unit-cost": 20.00, "quantity": 10000},
            {"operation": "sell", "unit-cost": 15.00, "quantity": 5000},
            {"operation": "sell", "unit-cost": 30.00, "quantity": 4350},
            {"operation": "sell", "unit-cost": 30.00, "quantity": 650},
        ]
        expected = [
            {"tax": 0.00},
            {"tax": 0.00},
            {"tax": 0.00},
            {"tax": 0.00},
            {"tax": 0.00},
            {"tax": 0.00},
            {"tax": 3700.00},
            {"tax": 0.00},
        ]
        current_taxes = self.capital_gains.calculate_taxes(operations_list=operations)
        self.assertEqual(current_taxes, expected)

    def test_case_8(self):
        operations = [
            {"operation": "buy", "unit-cost": 10.00, "quantity": 10000},
            {"operation": "sell", "unit-cost": 50.00, "quantity": 10000},
            {"operation": "buy", "unit-cost": 20.00, "quantity": 10000},
            {"operation": "sell", "unit-cost": 50.00, "quantity": 10000},
        ]
        expected = [{"tax": 0.00}, {"tax": 80000.00}, {"tax": 0.00}, {"tax": 60000.00}]
        current_taxes = self.capital_gains.calculate_taxes(operations_list=operations)
        self.assertEqual(current_taxes, expected)

    def test_case_9(self):
        operations = [
            {"operation": "buy", "unit-cost": 5000.00, "quantity": 10},
            {"operation": "sell", "unit-cost": 4000.00, "quantity": 5},
            {"operation": "buy", "unit-cost": 15000.00, "quantity": 5},
            {"operation": "buy", "unit-cost": 4000.00, "quantity": 2},
            {"operation": "buy", "unit-cost": 23000.00, "quantity": 2},
            {"operation": "sell", "unit-cost": 20000.00, "quantity": 1},
            {"operation": "sell", "unit-cost": 12000.00, "quantity": 10},
            {"operation": "sell", "unit-cost": 15000.00, "quantity": 3},
        ]
        expected = [
            {"tax": 0.00},
            {"tax": 0.00},
            {"tax": 0.00},
            {"tax": 0.00},
            {"tax": 0.00},
            {"tax": 0.00},
            {"tax": 1000.00},
            {"tax": 2400.00},
        ]
        current_taxes = self.capital_gains.calculate_taxes(operations_list=operations)
        self.assertEqual(current_taxes, expected)


if __name__ == "__main__":
    unittest.main()
