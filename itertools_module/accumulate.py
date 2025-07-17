# accumulate
# Returns running totals (prefix sums).

from itertools import accumulate

nums = [1, 2, 3, 4]
result = list(accumulate(nums))
print("Accumulate:", result)
