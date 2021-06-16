# Random Pick with Weight: https://leetcode.com/problems/random-pick-with-weight/

# You are given an array of positive integers w where w[i] describes the weight of ith index (0-indexed).
# We need to call the function pickIndex() which randomly returns an integer in the range [0, w.length - 1]. pickIndex() should return the integer proportional to its weight in the w array. For example, for w = [1, 3], the probability of picking the index 0 is 1 / (1 + 3) = 0.25 (i.e 25%) while the probability of picking the index 1 is 3 / (1 + 3) = 0.75 (i.e 75%).
# More formally, the probability of picking index i is w[i] / sum(w).

import random


class Solution:

    def __init__(self, w):
        self.prefix = []
        prefix_sum = 0

        for weight in w:
            prefix_sum += weight
            self.prefix.append(prefix_sum)

        self.cumSum = prefix_sum

    def pickIndex(self):
        # Generate number from 0 -> cumulative sum
        target = self.cumSum * random.random()

        # Perform a linear scan to find the
        for i in range(len(self.prefix)):
            if target < self.prefix[i]:
                return i

# So this problem comes down to simply taking the weight to create a range to land at from a random value
# For instance in the case 1 1 1 4 we can say it can land between 1, 2, 3, 8 if the random number from 0, 8
# then whatever it is we take the number after it so if we got 3-8 we could return index of 8

# Can we actually imrpove this algo?

# I think we can since all of these values are actually given to us in sorted order we can actually
# Do what I said above by find the index using a binary search in log(n) time although init is technicaly o(n)
# it will also be amortized
    def pickIndexBinary(self):
        target = self.cumSum * random.random()

        # perform binary search
        start, end = 0, len(self.prefix)

        while start < end:
            mid = start + (end - start) // 2
            if target > self.prefix[mid]:
                start = mid + 1
            else:
                end = mid

        return start


# This problem was actually pretty easy however my solution was pretty difficult as I didn't comprehend how to
# appropriately sample this problem.

# Score Card
# Did I need hints? Y
# Did you finish within 30 min? Y
# Was the solution optimal? Y
# Were there any bugs? N
#  1 3 2 5 = 2.75
