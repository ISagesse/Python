
def target(arr, n):
    lst = []
    
    for i in range(0, len(arr) - 1):
        for j in range(1, len(arr)):
            if arr[i] + arr[j] == n:
                lst.append(arr[i])
                lst.append(arr[j])
                return lst
    
    return lst


arr = [1, 2, 4, 6, 8]
n = 14;

print(target(arr, n))