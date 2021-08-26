# Subarray Sum Equals K: https://leetcode.com/problems/subarray-sum-equals-k/

# Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

from types import List

# In this problem we can use the fact that we can calculate any subarray sum by using a prefix sum array. Once we know that
# all we have to do is move across our array and keep track of all possible i's and j's with a n^2 loop to check for
# every possible outcome. This however is not the most optimal but the easiest to code.

# The most optimal solution would be to realize that any value that has a diff of k is needed so with creating prefix sum
# we can leverage a hashmap and see if the solution sum -k is in the map and then if it is increase our counts by the
# val in hashmap (as we can have loops from negative numbers)


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count, ourSum = 0, 0
        seenSums = {0: 1}

        for i in range(len(nums)):
            ourSum += nums[i]

            if ourSum - k in seenSums:
                count += seenSums[ourSum - k]

            # Add either 1 or the number we have seen before + 1
            seenSums[ourSum] = seenSums.get(ourSum, 0) + 1

        return count

# Aww snap here we go again
# This runs in O(N) time and space but is relatively difficult to figure out

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 10
# Was the solution optimal? This is optimal
# Were there any bugs? No
#  5 5 5 5 = 5
