# Insert Delete GetRandom O(1): https://leetcode.com/problems/insert-delete-getrandom-o1/

# Implement the RandomizedSet class:

# RandomizedSet() Initializes the RandomizedSet object.
# bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
# bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
# int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
# You must implement the functions of the class such that each function works in average O(1) time complexity.


# For this problem we will have an list and a key value pair where the key is the cur index
# that way we can return that variable in real time but move it around as needed


import random


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Store the value
        self.valueLocation = []
        # And keep track of the index in here so we can remove them when needed
        self.values = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.values:
            return False

        # For adding an element we simply add the value at the end of our list
        # and assign its index
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
        # Since we have an array we can literally just pull the value at random since we aren't removing it
        randomElement = random.randint(0, len(self.valueLocation) - 1)
        return self.valueLocation[randomElement]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

# The above works and runs in o(1) except when our list dynamically updates to double its len which is an o(n)
# however we all know that this is an average O(1) operation as it doesn't always happen


# Score Card
# Did I need hints? N
# Did you finish within 30 min? 25
# Was the solution optimal? Y
# Were there any bugs? Nope
# 5 5 5 5 = 5
