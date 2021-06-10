# Design HashMap: https://leetcode.com/problems/design-hashmap/
# Design a HashMap without using any built-in hash table libraries.

# Implement the MyHashMap class:

#     MyHashMap() initializes the object with an empty map.
#     void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
#     int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
#     void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.


class Bucket(object):
    def __init__(self):
        self.bucket = []

    def get(self, key):
        for curKey, curVal in self.bucket:
            if key == curKey:
                return curVal

        return -1

    def update(self, key, value):
        found = False

        for index, kv in enumerate(self.bucket):
            if key == kv[0]:
                found = True
                self.bucket[index] = (key, value)
                break

        if not found:
            self.bucket.append((key, value))

    def delete(self, key):
        for index, kv in enumerate(self.bucket):
            if key == kv[0]:
                del(self.bucket[index])
                break


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = [Bucket() for _ in range(2203)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        # Create the hash function
        ourBucket = key % 2203
        return self.map[ourBucket].update(key, value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        ourBucket = key % 2203
        return self.map[ourBucket].get(key)

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        ourBucket = key % 2203
        return self.map[ourBucket].delete(key)


# Score Card
# Did I need hints? N
# Did you finish within 30 min? Y
# Was the solution optimal? Y (there isn't really too much optimization as this is building a standard data structure)
# Were there any bugs? Not a bug but initially I didn't create a Bucket class but it makes things more complicated
#  4 5 5 3 = 4.25
