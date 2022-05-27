
def is_sorted(arr):
    n = True
    
    for i in range(0, len(arr) - 1):
        if arr[i] < arr[i + 1]:
            continue
        else:
            n = False
            break
        
    return n

arr = [10, 20, 5, 40, 50]

print(is_sorted(arr))
        