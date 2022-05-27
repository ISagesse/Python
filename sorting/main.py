import random
import math

mylist = []

for i in range(5):
    mylist.append(random.randrange(1, 9))
    
    
mylist.sort()
mylist.reverse()
    
for k in mylist:
    print(k, end=", ")
print()