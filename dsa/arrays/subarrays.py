# Subarray
# A subarray is a contiguous non-empty sequence of elements within an array.

def find_all_subarrays(arr):
    n = len(arr)
    sub_arr = []

    for i in range(n):
        for j in range(i, n):
            curr = arr[i : j+1]
            sub_arr.append(curr)
    
    return sub_arr

arr = [1, 1, 2]
print(f"All the subarrays: {find_all_subarrays(arr)}")