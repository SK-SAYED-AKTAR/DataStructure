def fun(arr, target):
    low = 0
    high = len(arr)
    mid = low + (high - low)//2

    while low <= high:
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
            mid = mid = low + (high - low)//2
        else:
            low = mid + 1
            mid = mid = low + (high - low)//2
    return -1    
arr = [1, 2, 3, 5, 10, 20]
print(fun(arr, 5))