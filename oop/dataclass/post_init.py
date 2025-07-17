# __post_init__
# A special method called after the dataclass __init__ is run. Useful for validation or computed values.
# Use case: Input validation after init, derived attributes.

from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float

    def __post_init__(self):
        if self.price < 0:
            raise ValueError("Price cannot be negative.")

p1 = Product("Laptop", 1200)
print(p1)
# p2 = Product("Phone", -500) # Raises ValueError