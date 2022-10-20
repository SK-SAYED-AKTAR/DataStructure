def fun(arr):
    pos = 0
    n = len(arr)
    for i in range(n):
        min_val = arr[i]
        for j in range(i+1, n):
            if arr[j] < min_val:
                min_val = arr[j]
                pos = j
        arr[i], arr[pos] = min_val, arr[i]
    return arr    


arr = [3, 2, 1, 10, 0]
print(fun(arr))