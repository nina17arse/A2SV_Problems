class RandomizedSet:

    def __init__(self):
        self.randomSet=set()
        

    def insert(self, val: int) -> bool:
        
        if val not in self.randomSet:
            self.randomSet.add(val)
            return True
        


    def remove(self, val: int) -> bool:
        if val  in self.randomSet:
            self.randomSet.remove(val)
            return True
        

    def getRandom(self) -> int:
        v=random.choice(list(self.randomSet))
        return v
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()