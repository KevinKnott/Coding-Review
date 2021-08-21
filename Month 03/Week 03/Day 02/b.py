# Insert Delete GetRandom O(1): https://leetcode.com/problems/insert-delete-getrandom-o1/

# Implement the RandomizedSet class:

# RandomizedSet() Initializes the RandomizedSet object.
# bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
# bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
# int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
# You must implement the functions of the class such that each function works in average O(1) time complexity.

# By combining the properties of two data structures we can achieve what we need. Those two are a hashmap for quick lookup
# and a array for storing the numbers to be accessed by a probability

import random


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.random = []
        self.lookup = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.lookup:
            return False

        # Add value to list and point the lookup to be the len as that is where it will be added
        self.lookup[val] = len(self.random)
        self.random.append(val)

        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.lookup:
            return False

        # For this we need to remove the val but to do this in O(1) we need to swap the element
        # to whatever is in the last place
        last, remove = self.random[-1], self.lookup[val]
        self.random[remove], self.lookup[last] = last, remove

        self.random.pop()
        del(self.lookup[val])

        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        index = random.randint(0, len(self.random) - 1)
        return self.random[index]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

# Alright this works pretty well the tricky part is updating the random/lookup when removing from the set
# because you have to update the location of the val so that you can properly remove it from both

# This all runs in O(1)

# Score Card
# Did I need hints? Y
# Did you finish within 30 min? 10
# Was the solution optimal? Y
# Were there any bugs? Messed up the swap piece real bad
# 4 5 5 4 = 4.5
