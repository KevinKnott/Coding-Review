# Product of Array Except Self: https: // leetcode.com/problems/product-of-array-except-self/

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

# In this problem we have to simply calculate the prefix and suffix sums at each point
# then all we have to do is return the result of prefix * postfix at every index

class Solution:
    def productExceptSelf(self, nums):
        prefix, suffix = [0] * len(nums),  [0] * len(nums)
        prefix[0] = 1
        suffix[-1] = 1

        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]

        for i in reversed(range(len(nums) - 1)):
            suffix[i] = suffix[i+1] * nums[i+1]

        return [prefix[i] * suffix[i] for i in range(len(nums))]

# Aww snap this is a super neat way of doing this and it runs
# in O(N) time to calc the prefix and postfix and then all you
# have is o(N) space for creating the three of them
# technically you could reduce this to O(1) additional space
# if you create the prefix as the result and kept the suffix as a
# variable and multiplied as you solve for the suffix

# Score Card
# Did I need hints? Y
# Did you finish within 30 min? 7
# Was the solution optimal? Kinda (techincally we could do O(1) additional space but it is really still O(N))
# Were there any bugs? N
# 5 5 5 5 = 5
