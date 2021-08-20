# First Missing Positive: https://leetcode.com/problems/first-missing-positive/

# Given an unsorted integer array nums, return the smallest missing positive integer.
# You must implement an algorithm that runs in O(n) time and uses constant extra space.

# This problem is relatively empty except we have quite a few false positives
# so what we do is check if if 1 exists in the list if not we return false
# otherwise we will set all negative numbers and 0 to 1 after handling all the
# false positives we can set every possible number we see to negative if we see it
# make sure we always take abs(i) - 1 and then we can go through afterwards
# and look for the first positive number

class Solution:
    def firstMissingPositive(self, nums) -> int:
        hasOne = False

        for i in range(len(nums)):
            if nums[i] == 1:
                hasOne = True

            if nums[i] <= 0:
                nums[i] = 1

        if not hasOne:
            return 1

        for i in range(len(nums)):
            curNumIndex = abs(nums[i]) - 1

            if curNumIndex < len(nums) and nums[curNumIndex] > 0:
                nums[curNumIndex] *= -1

        for i in range(1, len(nums)):
            if nums[i] > 0:
                return i+1

        return len(nums) + 1


# This runs in O(N) time and O(1) space

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 10
# Was the solution optimal? Oh yee
# Were there any bugs? No bugs
# 5 5 5 5 = 5
