# Maximum Subarray: https://leetcode.com/problems/maximum-subarray/

# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# My initial thought is that if we are going across the array we can either start the subarray from where we are
# or we can add the value so if that value is higher than adding the value we simply need to reset our val
# and record if we have a new max

class Solution:
    def maxSubArray(self, nums) -> int:
        result = -float('inf')
        curSum = -float('inf')

        for num in nums:
            result = max(result, curSum)
            curSum = max(num, curSum + num)

        return max(result, curSum)


# This solution is actually correct and runs in o(n) and o(1) which is pretty optimal
# luckily I know this from my days studing in college but apparently there is a version of
# this solution that exists using a divide and conquer algo which makes sense because the
# because you should be able to create contiguous subarrays down to size one and then
# build up. Especially since the above algo is a dp problem with tabulation that being said
# I think I won't be coding it up as it seems quite complicated and honestly doesn't
# have enough improvement to warrent coding. Although it is an interesting idea.


# Score Card
# Did I need hints? N
# Did you finish within 30 min? 5 min
# Was the solution optimal? Yes
# Were there any bugs?  None
# 5 5 5 5 = 5
