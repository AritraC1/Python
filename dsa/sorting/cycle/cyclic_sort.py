# Cyclic Sort (In-place sorting algorithm)

'''
Cyclic Sort is a very efficient algorithm for sorting arrays where:
  - The array contains 'n' DISTINCT numbers in the range from 1 to n (or 0 to n-1).
  - It works by placing each number at its correct index.

Idea:
  - For example, in an array from 1 to n, the number 1 should be at index 0,
    2 should be at index 1, ..., and n should be at index n-1.
  - It swaps elements until each number is at its correct position.

Time Complexity: O(n)
Space Complexity: O(1) [in-place]
Stable: No
Best used for: Arrays with a known range of distinct integers.

'''

def cyclic_sort(arr):
    i = 0
    while i < len(arr):
        correct_index = arr[i] - 1  # For 1 to n; use 'arr[i]' for 0 to n-1
        if arr[i] != arr[correct_index]:
            # Swap the current element to its correct position
            arr[i], arr[correct_index] = arr[correct_index], arr[i]
        else:
            i += 1
    return arr

arr = [3, 1, 5, 4, 2]
print("Original Array: ", arr)

sorted_arr = cyclic_sort(arr)
print("Sorted Array: ", sorted_arr)


'''
Note: For Cyclic Sort, array is only valid if most of its elements are within the range 1 to n (the length of the array).

For example: 
if n = 6
arr = [3, 1, 5, 4, 2] , here all the numbers are within range of 1-6 i.e. no number is greater than 6

'''