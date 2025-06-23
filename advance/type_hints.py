# Python Type Hints

# Variable type hint
age: int = 25  # 'age' is expected to be of type 'int'
print(f"Age as integer: {age}")

# Python does NOT enforce this type at runtime
# You can reassign a different type
age = "twenty-five"  # This will work at runtime, but a static type checker (like mypy) will flag it
print(f"Age reassigned to string: {age}")

# Type hints with functions
# Function with argument and return type hints
def greet(name: str) -> str:
    return f"Hello, {name}!"

print(greet("Alice"))

# Function with multiple parameters and types
def add(x: int, y: int) -> int:
    return x + y

print(add(3, 4))  # Correct usage

# Type hints with collections
from typing import List, Tuple, Dict, Union, Optional

# List of integers
scores: List[int] = [85, 90, 78]
print(f"Scores: {scores}")

# Tuple with specific types
user: Tuple[str, int] = ("Bob", 30)
print(f"User: {user}")

# Dictionary with string keys and integer values
inventory: Dict[str, int] = {"apple": 10, "banana": 5}
print(f"Inventory: {inventory}")

# Union and Optional types
# Union means a variable can be more than one type
data: Union[int, str] = 10
print(f"Data as int: {data}")
data = "ten"
print(f"Data as str: {data}")

# Optional means the value can be of the specified type or None
nickname: Optional[str] = None
print(f"Nickname: {nickname}")
nickname = "Ace"
print(f"Nickname updated: {nickname}")