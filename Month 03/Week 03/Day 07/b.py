# Random Pick with Weight: https://leetcode.com/problems/random-pick-with-weight/

# You are given an array of positive integers w where w[i] describes the weight of ith index (0-indexed).
# We need to call the function pickIndex() which randomly returns an integer in the range [0, w.length - 1]. pickIndex() should return the integer proportional to its weight in the w array. For example, for w = [1, 3], the probability of picking the index 0 is 1 / (1 + 3) = 0.25 (i.e 25%) while the probability of picking the index 1 is 3 / (1 + 3) = 0.75 (i.e 75%).
# More formally, the probability of picking index i is w[i] / sum(w).

from types import List
import random

# This problem is actually quite simple all you need to do is create a strucutre in which you keep the sums aka the weighted value and than you can use random to create
# a number from 0 -> sum and return whatever index is below it. The optimal solution also involves using a binary search instead of a linear search so that
# we have an o(logn) time complexity with an o(N) construcutor but O(1) pick index


class Solution:

    def __init__(self, w: List[int]):
        curSum = 0
        self.values = []

        for weight in w:
            curSum += weight
            self.values.append(curSum)

    def pickIndex(self) -> int:
        if len(self.values) == 0:
            return 0

        pickedValue = random() * self.values[-1]
        start, end = 0, len(self.values)

        while start < end:
            mid = start + (end - start) // 2

            if pickedValue > self.values[mid]:
                start = mid + 1
            else:
                end = mid

        return start


# Yup this works and runs in O(logn) for the pick and o(N) for the init and uses O(1) space for pick and o(N) for init

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

# Score Card
# Did I need hints? Y
# Did you finish within 30 min? 10
# Was the solution optimal? Y
# Were there any bugs? N
# 5 5 5 5 = 5
