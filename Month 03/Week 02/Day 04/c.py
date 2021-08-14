# Design HashMap: https://leetcode.com/problems/design-hashmap/

# Design a HashMap without using any built-in hash table libraries.

# Implement the MyHashMap class:

# MyHashMap() initializes the object with an empty map.
# void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
# int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
# void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.

# So the way a hash table works is that we have a mapping of our key to a list of buckets (we can divide by using a prime number for optimal hashing)
# then we can simply linear search or binary search depending on the efficency we want but hopefully we wont have many collisions

class Bucket(object):
    def __init__(self):
        self.bucket = []

    def put(self, key, value):
        found = False

        for i, (k, _) in enumerate(self.bucket):
            if k == key:
                self.bucket[i][1] = value
                found = True
                break

        if not found:
            self.bucket.append([key, value])

    def get(self, key):
        for k, v in self.bucket:
            if k == key:
                return v

        return - 1

    def remove(self, key):
        for i, (k, _) in enumerate(self.bucket):
            if k == key:
                del(self.bucket[i])


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._mod = 2903
        self.map = [Bucket() for i in range(self._mod)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        index = key % self._mod
        self.map[index].put(key, value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        index = key % self._mod
        return self.map[index].get(key)

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        index = key % self._mod
        self.map[index].remove(key)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

# The above works and everything runs in O(N/k) where kis number of bucket and uses o(K + M) where k is the same
# and M is the number of unique keys that we have

# Score Card
# Did I need hints? Nope
# Did you finish within 30 min? 15
# Was the solution optimal? I am pretty sure this is optimal
# Were there any bugs? None
# 5 5 5 5 = 5
