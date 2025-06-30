# Selection Sort (Select the minimums and swap, In-place sorting algorithm)

'''
Selection Sort is a simple comparison-based sorting algorithm.
It divides the input list into two parts: the sorted part at the beginning and the unsorted part at the end. 
It repeatedly selects the smallest (or largest) element from the unsorted part and swaps it with the leftmost unsorted element,
moving the boundary of the sorted part one step to the right.

Time Complexity:
  - Best Case: O(n^2)
  - Average Case: O(n^2)
  - Worst Case: O(n^2)

Space Complexity: O(1) - In-place sorting

Stable: No (can be made stable with modifications)
'''

def selection_sort(arr):
    n = len(arr)

    for i in range(0, n-1):
        min_index = i

        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap the found minimum element with the first element of the unsorted part
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr


arr = [13, 46, 24, 52, 20, 9]
print("Original Array: ", arr)

sorted_arr = selection_sort(arr)
print("Sorted Array: ", sorted_arr)


'''
Observations:

swap at index 0 & minimum index, range: [0 - n-1]
swap at index 1 & minimum index, range: [1 - n-1]
swap at index 2 & minimum index, range: [2 - n-1]
.
.
.
.
.
swap at index [n-2] & minimum index, range: [n-2 - n-1]
'''