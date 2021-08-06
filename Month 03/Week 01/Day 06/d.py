# Random Pick with Weight: https://leetcode.com/problems/random-pick-with-weight/

# You are given an array of positive integers w where w[i] describes the weight of ith index (0-indexed).
# We need to call the function pickIndex() which randomly returns an integer in the range [0, w.length - 1]. pickIndex() should return the integer proportional to its weight in the w array. For example, for w = [1, 3], the probability of picking the index 0 is 1 / (1 + 3) = 0.25 (i.e 25%) while the probability of picking the index 1 is 3 / (1 + 3) = 0.75 (i.e 75%).
# More formally, the probability of picking index i is w[i] / sum(w).

# This problem is actually quite easy we keep a rolling total and then go across
# from left to right until we are over that value and return it

import random


class Solution:

    def __init__(self, w):
        self.curSum = 0
        self.values = []

        for weight in w:
            self.curSum += weight
            self.values.append(self.curSum)

    def pickIndex(self) -> int:
        if len(self.values) <= 1:
            return 0

        weightedPick = random() * self.curSum

        for i in range(len(self.values)):
            if self.values[i] > weightedPick:
                return i

# Now the above runs in o(N) but we can do this in O(nlogn) as it is really easy
# to binary search through sorted numbers like the weighted sum (based off of cum sum)

    def pickIndex(self) -> int:
        if len(self.values) <= 1:
            return 0

        # Create random num for 0 .. curSum so lets use random to create a value that is from 0 .. 1 and multiply it by cursum
        ourPick = random() * self.curSum

        lo, hi = 0, len(self.values) - 1

        while lo < hi:
            mid = lo + (hi - lo) // 2

            if ourPick > self.values[mid]:
                lo = mid + 1
            else:
                hi = mid

        return lo

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 15
# Was the solution optimal? This is optimal
# Were there any bugs? No
#  5 5 5 5 = 5
