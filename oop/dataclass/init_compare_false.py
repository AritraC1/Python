# Skipping Fields in Equality & Initialization with init=False, compare=False
# Exclude fields from constructor or comparisons.
# Use case: Add metadata (like timestamps) that shouldn't affect equality.

from dataclasses import dataclass, field
from time import time

@dataclass
class Session:
    user: str
    timestamp: float = field(default_factory=time, init=False, compare=False)

s1 = Session("admin")
s2 = Session("admin")

print(s1 == s2)  # True (ignores timestamp)
print(s1.timestamp)  # Current time