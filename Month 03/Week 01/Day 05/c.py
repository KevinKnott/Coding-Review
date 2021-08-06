# Maximum Subarray: https://leetcode.com/problems/maximum-subarray/

# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
# A subarray is a contiguous part of an array.

# This problem is actually kind of like a dynamic programming problem at every integer we decide wether we take the current sum + our value
# or just the value based off what is higher. The only interesting thing is that we need to store the max value at pretty much every step
# because the max could be reduced to a lesser value from the process.

class Solution:
    def maxSubArray(self, nums) -> int:
        result = nums[0]
        curSum = nums[0]

        for i in range(1, len(nums)):
            curSum = max(curSum + nums[i], nums[i])
            result = max(curSum, result)

        return result

# The above solution runs in O(N) time and uses O(1) space
# I think you could also do this problem with a divide and conquer
# but it is probably more complicated and also a worse time complexity

# Score Card
# Did I need hints? Nope
# Did you finish within 30 min? 4 minutes
# Was the solution optimal? See above
# Were there any bugs? None
# 5 5 5 5 = 5
