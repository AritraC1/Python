# Linear Search

# Linear Search is a simple searching algorithm.
# It works by checking each element of the list one by one
# until the target element is found or the end of the list is reached.

# Time Complexity: O(n), where n is the number of elements in the list.
# Best Case: O(1) - if the element is at the beginning
# Worst Case: O(n) - if the element is at the end or not present
# Space Complexity: O(1) - it does not use extra space


def linear_search(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    
    return -1

arr = [10, 25, 30, 45, 50]
target = 30

result = linear_search(arr, target)

if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found in the list.")