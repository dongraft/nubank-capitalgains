from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Operation:
    action: str
    unit_cost: Decimal
    quantity: int
    ticker: str

    @property
    def cost(self):
        return Decimal(self.quantity * self.unit_cost)
