# defaultdict
# Like a regular dict, but provides a default value if key is missing. Avoids KeyError.

from collections import defaultdict

# Default value is 0 (int constructor)
dd = defaultdict(int)

dd["apple"] += 1
dd["banana"] += 2
print("Defaultdict:", dict(dd))  # {'apple': 1, 'banana': 2}

# Accessing a missing key returns default value
print("Missing key:", dd["cherry"])  # 0