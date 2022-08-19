from HashMap import HashMap

hm = HashMap(10)
hm.assign('march 6', 130)
hm.assign('march 7', 30)
hm.assign('march 8', 230)

print(hm.array)

print(hm.retrieve('march 6'))

print(hm.remove('march 8'))

print(hm.array)