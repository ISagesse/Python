import random
import math

numList = []

for i in range(5):
    numList.append(random.randrange(1,10))
    
i = len(numList) - 1

while (i > 1):
    j = 0
    
    while j < i:
        
        print(f"\n {numList[j]} > {numList[j + 1]} ")
        
        if numList[j] > numList[j + 1]:
            print(f" Switch {numList[j]} with {numList[j + 1]} ")
            temp = numList[j]
            numList[j] = numList[j + 1]
            numList[j + 1] = temp
        else:
            print(f" cannot switch {numList[j]} with {numList[j + 1]} ")
    
        j += 1
        
        for k in numList:
            print(k, end=", ")
        print()
        
    print("End of round")
    i -= 1


for k in numList:
    print(k, end=", ")
print()
    
        