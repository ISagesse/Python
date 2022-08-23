class HashMap:
    def __init__(self, array_size):
        self.array_size = array_size
        self.array = [[] for item in range(array_size)]

    def hash(self, key):
        hash_code = 0
        for e in key:
            hash_code += ord(e)
        return hash_code

    def compressor(self, hash_code):
        return hash_code % self.array_size

    def assign(self, key, value):
        array_index = self.compressor(self.hash(key))
        #implement collision with chaining methods
        found = False
        for idx, ele in enumerate(self.array[array_index]):
            if len(ele) == 2 and ele[0] == key:
                # checking to see if the user was trying to update that key current value, if so update it.
                self.array[array_index][idx] = (key, value)
                found = True
                break

        if found == False:
            # adding that key and value to that location in the array.
            self.array[array_index].append((key, value))

    def retrieve(self, key):
        array_index = self.compressor(self.hash(key))
        for element in self.array[array_index]:
            if element[0] == key:
                return element[1]

    def remove(self, key):
        array_index = self.compressor(self.hash(key))
        for idx, element in enumerate(self.array[array_index]):
            if element[0] == key:
                del self.array[array_index][idx]

