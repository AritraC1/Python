# Insertion Sort (In-place sorting algorithm, Take an element and place it in correct order)

'''
Insertion Sort builds the final sorted array one element at a time.
It takes each element from the input and inserts it into the correct position in the already-sorted part of the array.

Time Complexity:
    Best Case: O(n)         [already sorted]
    Average Case: O(n^2)
    Worst Case: O(n^2)

Space Complexity: O(1)      [in-place]
Stable: Yes
'''

def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1
        # Move elements of arr[0..i-1] that are greater than key to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        
    return arr

arr = [13, 46, 24, 52, 20, 9]
print("Original Array: ", arr)

sorted_arr = insertion_sort(arr)
print("Sorted Array: ", sorted_arr)