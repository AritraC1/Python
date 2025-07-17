# field()
# Use field() to set metadata, default_factory, or exclude a field from init/repr/etc.
# Use case: Hide sensitive fields, create mutable defaults (lists, dicts, etc.)

from dataclasses import dataclass, field
from typing import List

@dataclass
class ShoppingCart:
    items: List[str] = field(default_factory=list)
    secret_code: str = field(repr=False, default="xyz123")  # hidden from repr

cart = ShoppingCart()
cart.items.append("Apple")
print(cart)