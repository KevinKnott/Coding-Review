# Design HashMap: https://leetcode.com/problems/design-hashmap/

# Design a HashMap without using any built-in hash table libraries.

# Implement the MyHashMap class:

# MyHashMap() initializes the object with an empty map.
# void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
# int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
# void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.

# So this problem is basically implementing your own hash map which is a relatively easy problem especially since we know that we can have a bounded list
# The tricky part is that we actually need to use this array to go to a new array or bucket so that if we have multiple in case of collision
# we can still find an answer

# So let us start with creating the bucket with a new class as we can have updates as we go
# So this is just a key, value pair in a list

class Bucket:

    def __init__(self):
        self.bucket = []

    def get(self, key):
        for k, v in self.bucket:
            if k == key:
                return v

        return -1

    def put(self, key, value):
        found = False

        for index, (k, v) in enumerate(self.bucket):
            if k == key:
                self.bucket[index] = (key, value)
                found = True
                break

        if found is False:
            self.bucket.append((key, value))

    def rem(self, key):
        for index, (k, v) in enumerate(self.bucket):
            if k == key:
                del(self.bucket[index])
                return


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Create a random size of buckets large enough to store values
        # Technically since we know the size bound we could put that +1
        # but that isn't super important as we just need to increase
        # the size if we reach too many collisions or more thant 60% of
        # our fufillment
        self._modulo = 2203
        self.map = [Bucket() for _ in range(self._modulo)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        # So like any hash we need to hash the key and append it
        self.map[key % self._modulo].put(key, value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        return self.map[key % self._modulo].get(key)

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        self.map[key % self._modulo].rem(key)

# Oh yeah I killed this problem honestly this is pretty much what I learned in school so it is pretty easy
# The more tricky thing about this is actually creating the solution with a elegant OO design

# So most of these operations are dependent on how many keys over lap so the time would be O(N/K) as
# we have to loop through most of the buckets to the length of matching keys as for space this would
# simply be o(K + M) as we need K buckets and up to M unique keys /values to be stored

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 20 min
# Was the solution optimal? I belive so (I could increase the size of the modulo to help reduce time complexity)
# Were there any bugs?  I didn't really have any bugs
# 5 5 5 5 = 5
