# OrderedDict
# A dict subclass that remembers insertion order. From Python 3.7+, built-in dict preserves order too. Still useful for: Older Python versions and Explicit intent for ordering

from collections import OrderedDict

od = OrderedDict()
od["first"] = 1
od["second"] = 2
od["third"] = 3

for key, value in od.items():
    print(f"{key}: {value}") # Output order will be: first, second, third