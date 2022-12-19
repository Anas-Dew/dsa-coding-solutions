# Hashmap
# it works like this BASICALLY!
# the key will be converted to a number by hashfunction

class Hashmap:
    def __init__(self):
        self.MAX = 100
        self.arr = [None] * self.MAX # 100 None elements in the arr.

    def get_hash(self, key):
        sum = 0
        for each_charecter in key:
            sum += ord(each_charecter) # ord is a built func which gives ASCII value of anything.
        return sum % self.MAX

    def __setitem__(self, key, value):
        hash = self.get_hash(key)
        self.arr[hash] = value

    def __getitem__(self, key):
        hash = self.get_hash(key)
        return self.arr[hash]

    def __delitem__(self, key):
        hash = self.get_hash(key)
        self.arr[hash] = None

    
if __name__ == "__main__":
    h  = Hashmap()
    h['a'] = 10
    h['a'] = 12 
    print(h['a'])
    # del h['a']
    # print(h['a'])