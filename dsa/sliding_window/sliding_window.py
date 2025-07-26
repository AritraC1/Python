# Sliding Window/ Two-Pointer
# The sliding window algorithm is a technique used to reduce the time complexity of algorithms that involve nested loops by maintaining a subset of items (a 'window') that slides over the data structure.

'''
It is mostly used in problems involving:
- Subarrays or substrings
- Contiguous sequences
- Fixed or variable window sizes

There are two common types:
1. Fixed-size sliding window
2. Variable-size sliding window

When to use Sliding Window:
- You're working with contiguous elements (subarrays or substrings)
- You want to reduce a brute-force O(n^2) solution to O(n)

Patterns:
- For fixed window: move start and end together
- For variable window: expand end until condition met, then move start
'''

# EXAMPLE 1: Fixed-Size Sliding Window (Maximum Sum Subarray of Size k)
def max_sum_array(arr1, k):
    n = len(arr1)

    if n<k:
        return None
    
    # Initial window sum
    window_sum = sum(arr1[:k])
    max_sum = window_sum

    # Slide the window
    for i in range(k, n):
        # Subtract the element going out, add the one coming in
        window_sum += arr1[i] - arr1[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum


arr1 = [2, 1, 5, 1, 3, 2, 4, 6, 7, 0, 0, 1]
k = 3
print(f"Maximum sum of subarray: {max_sum_array(arr1, k)}" )

# EXAMPLE 2: Variable-Size Sliding Window (Smallest Subarray with Sum ≥ S)
def min_subarray_len(target, arr2):
    n = len(arr2)
    start = 0
    window_sum = 0
    min_len = float('inf')

    for end in range(n):
        window_sum += arr2[end]

        while window_sum >= target:
            min_len = min(min_len, end - start + 1)
            window_sum -= arr2[start]
            start += 1

    return min_len if min_len != float('inf') else 0

arr2 = [2, 3, 1, 2, 4, 3]
target = 7
print(f"Min subarray length: {min_subarray_len(target, arr2)}")
