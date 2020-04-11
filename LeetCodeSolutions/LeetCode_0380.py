class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._dict = {}
        self._array = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self._dict:
            self._dict[val] = len(self._array)
            self._array.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self._dict:
            return False
        idx = self._dict[val]
        last_elem = self._array[-1]
        self._array[idx], self._array[-1] = self._array[-1], self._array[idx]
        self._dict[last_elem] = idx
        self._dict.pop(val)
        self._array.pop()
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        import random
        return random.choice(self._array)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
