# Insert Delete GetRandom O(1): https://leetcode.com/problems/insert-delete-getrandom-o1/

# Implement the RandomizedSet class:

#     RandomizedSet() Initializes the RandomizedSet object.
#     bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
#     bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
#     int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.

# You must implement the functions of the class such that each function works in average O(1) time complexity.

# So I think that we can do everything here with a set because adding and removing is the same o(1)
# The only question is how would we getRandom? I think all we have to do is create a random int
# and then return that index using  although I am not sure this is possible

# My second solution would be to use an array of elements and add/remove with logn
# and use random to find an index and switch it to the end and pop it off the stack

# I think we may be able to combine my two thoughts for the correct solution

import random


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.valueLocation = []
        self.values = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        # Check if val is in values if it is return true
        if val in self.values:
            return False

        # Otherwise add it to the end of our list and put it in values as value -> index
        self.values[val] = len(self.valueLocation)
        self.valueLocation.append(val)

        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.values:
            return False

         # So to remove we need to swap the index with the last and update the swapped
        last, removeIndex = self.valueLocation[-1], self.values[val]
        self.valueLocation[removeIndex], self.values[last] = last, removeIndex

        # then we need to pop that element off of the hashmap and the list
        self.valueLocation.pop()
        del(self.values[val])

        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        # So all we need to do here is the same as above but with a random value for 0 len(nums) - 1
        randomElement = random.randint(0, len(self.valueLocation) - 1)
        return self.valueLocation[randomElement]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

# Score Card
# Did I need hints? Nope
# Did you finish within 30 min? 25
# Was the solution optimal? This is optimal all of these are o(1)
# Were there any bugs?  When swapping the value it took me some time to get the right swap mechanism for the dict
# 5 5 4 4 = 4.5
