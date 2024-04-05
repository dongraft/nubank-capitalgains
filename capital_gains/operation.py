from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Operation:
    kind: str
    unit_cost: Decimal
    quantity: int

    @property
    def cost(self):
        return Decimal(self.quantity * self.unit_cost)
