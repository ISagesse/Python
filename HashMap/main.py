class HashMap:
    def __init__(self, array_size):
        self.array_size = array_size
        self.array = [None for item in range(array_size)]

    def hash(self, key):
        key_bytes = key.encode()
        hash_code = sum(key_bytes)
        return hash_code

    def compressor(self, hash_code):
        return hash_code % self.array_size

    def assign(self, key, value):
        array_index = self.compressor(self.hash(key))
        self.array[array_index] = value

    def retrieve(self, key):
        array_index = self.compressor(self.hash(key))
        return self.array[array_index]


hm = HashMap(5)

hm.assign('one', 3)
hm.assign('two', 5)
hm.assign('three', 7)
hm.assign('four', 9)
hm.assign('five', 1)
