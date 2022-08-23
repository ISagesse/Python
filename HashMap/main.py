from HashMap import HashMap

hm = HashMap(10)
hm.assign('march 6', 130)
hm.assign('march 7', 30)
hm.assign('march 8', 230)
hm.assign('march 17', 300)
hm.assign('march 18', 120)
hm.assign('march 22', 450)

print(hm.array)
print()
# print(hm.retrieve('march 18'))

print(hm.remove('march 8'))

print(hm.array)