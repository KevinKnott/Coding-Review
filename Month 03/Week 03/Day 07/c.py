# Insert Delete GetRandom O(1): https://leetcode.com/problems/insert-delete-getrandom-o1/

# Implement the RandomizedSet class:

# RandomizedSet() Initializes the RandomizedSet object.
# bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
# bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
# int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
# You must implement the functions of the class such that each function works in average O(1) time complexity.

# In this problem we are simply combining two data structures together to make a more optimal set with the added bonus of being able to still remove in O(1)
# to do this we will use a hashmap to track where values are indexed at and a list to store the actual values. The list will be able to get a random index
# so we can return a random element and the hashmap will let us remove a certain value in O(1) still

from random import randint


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lookup = {}
        self.random = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.lookup:
            return False

        self.lookup[val] = len(self.random)
        self.random.append(val)

        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.lookup:
            return False

        last, remove = self.random[-1], self.lookup[val]
        self.random[remove], self.lookup[last] = last, remove

        self.random.pop()
        del(self.lookup[val])

        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        index = randint(0, len(self.random) - 1)
        return self.random[index]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

# This works out it may seem a bit confusing but the only hard part is setting the location of the removed value with the value you are swapping with
# and once that is done you also set that val in the look up after that you simply pop off the end of the list o(1) and remove from the hashmap
# also O(1)

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 8
# Was the solution optimal? Yup
# Were there any bugs? None
# 5 5 5 5 = 5
