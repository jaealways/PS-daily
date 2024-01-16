import random

class RandomizedSet:
    def __init__(self):
        self.array=set([])
        self.num=0

    def insert(self, val: int) -> bool:
        if val in self.array:
            return False
        self.array.add(val)
        return len(self.array)

    def remove(self, val: int) -> bool:
        if val not in self.array:
            return False
        self.array.remove(val)
        return True

    def getRandom(self) -> int:
        self.num+=1
        return random.choice(list(self.array))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()