def sum_arr(arr):
    if not arr:
        return 0
    
    return arr[0] + sum_arr(arr[1:])
    

arr = [1,2,3,4,5]
print(sum_arr(arr))
