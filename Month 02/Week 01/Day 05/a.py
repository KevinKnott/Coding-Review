# Random Pick with Weight: https://leetcode.com/problems/random-pick-with-weight/

# You are given an array of positive integers w where w[i] describes the weight of ith index (0-indexed).
# We need to call the function pickIndex() which randomly returns an integer in the range [0, w.length - 1]. pickIndex() should return the integer proportional to its weight in the w array. For example, for w = [1, 3], the probability of picking the index 0 is 1 / (1 + 3) = 0.25 (i.e 25%) while the probability of picking the index 1 is 3 / (1 + 3) = 0.75 (i.e 75%).
# More formally, the probability of picking index i is w[i] / sum(w).

# For this problem we need to create a hash table or array in which we store the values and what number is used for picking them
# This number will be based on the total sum

# For instance in the above example  we would have an array something like [ ( 1, 1), (3, 4) ]  the second value is the sum as we added it and the first number is the number to return
# Then all we have to do is create a number between 0 .. sum and we can find where it lies in the above to return that integer (Normally we could do this with a linear scan but
# to be optimal we should use a binary search since the sum is already sorted!)

# Also in the above I realized we don't need the number as we are returning the index so we just need the sum at the index!

from random import random


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

        # Create random num for 0 .. curSum so lets use random to create a value that is from 0 .. 1 and multiply it by cursum
        ourPick = random() * self.curSum

        # Using a bs find the index where this occurs!
        lo, hi = 0, len(self.values) - 1

        while lo < hi:
            mid = lo + (hi - lo) // 2

            # Check if the value we picked is higher than the sum at mid point
            # then move to the right half
            if ourPick > self.values[mid]:
                lo = mid + 1
            # Otherwise the value is <= our mid so we choose the left side
            else:
                hi = mid

        # Once we have lo and hi meet we return that value
        return lo


# Score Card
# Did I need hints? N
# Did you finish within 30 min? 15
# Was the solution optimal? Yeah this is definitely optimal as we are using a time of o(logn) for each pickIndex and o(n) for init and only using a space of o(1) for pickIndex for o(n) for init
# Were there any bugs? None this is a simple binary search
# 5 5 5 5 = 5
