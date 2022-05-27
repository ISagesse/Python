
def left_rotate1(arr):
    n = len(arr)
    x = arr[0]
     
    for i in range(1, n):
        arr[i - 1] = arr[i]
    arr[n - 1] = x
    
    return arr



arr = [10, 20, 30, 40, 50]

print(left_rotate1(arr))
print(arr[3:] + arr[:3])