# Binary Search

# Binary Search is an efficient algorithm to find the position of a target value within a sorted array.
# It works by repeatedly dividing the search interval in half:
# Compare the target with the middle element of the array.
# If they are equal, return the index.
# If the target is smaller, continue searching the left half.
# If the target is larger, continue searching the right half.

# This reduces the time complexity to O(log n).

def binary_search(arr, target):
    start, end = 0, len(arr) - 1  # Initialize pointers to start and end of array
    
    while start <= end:
        mid = start + (end - start) // 2;  # Find the middle index
        
        if arr[mid] == target:
            return mid  # Target found at mid index
        elif arr[mid] < target:
            start = mid + 1  # Search right half
        else:
            end = mid - 1  # Search left half
            
    return -1  # Target not found in the array  # Target not found in the array

if __name__ == "__main__":
    sorted_list = [1, 3, 5, 7, 9, 11, 13]
    target_value = 7
    
    result = binary_search(sorted_list, target_value)

    if result != -1:
        print(f"Target {target_value} found at index {result}.")
    else:
        print(f"Target {target_value} not found in the list.")