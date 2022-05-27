

def second_largest(arr):
    maxi = max(arr)
    sec = arr[0]
    
    for i in range(1, len(arr)):
        if arr[i] > sec:
            if arr[i] < maxi:
                sec = arr[i]
            
    return f' Max: {maxi} Sec: {sec} '

arr = [10, 20, 30, 40]

print(second_largest(arr))