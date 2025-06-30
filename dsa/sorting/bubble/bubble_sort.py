# Bubble Sort (In-place sorting algorithm, Pushes the maximum to last by adjacent swaps)

'''
Bubble Sort is a simple comparison-based sorting algorithm.
It repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. 
This process is repeated until the list is sorted.

Time Complexity:
    Best Case: O(n)        [when the array is already sorted]
    Average Case: O(n^2)
    Worst Case: O(n^2)

Space Complexity: O(1)     [in-place]
Stable: Yes
'''

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        # Flag to optimize if the array is already sorted
        swapped = False
        for j in range(0, n - i - 1):  # Reduce comparisons after each pass
            if arr[j] > arr[j + 1]:
                # Swap adjacent elements if they are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break  # No swaps means the array is already sorted
    return arr


arr = [13, 46, 24, 52, 20, 9]
print("Original Array: ", arr)

sorted_arr = bubble_sort(arr)
print("Sorted Array: ", sorted_arr)

