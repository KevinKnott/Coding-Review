# Product of Array Except Self: https://leetcode.com/problems/product-of-array-except-self/

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

# What we can do is create a prefix/suffix array and loop through and multiply everything together minus where you are at

class Solution:
    def productExceptSelf(self, nums):
        prefix = [1] * (len(nums))
        postfix = [1] * (len(nums))

        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]

        for i in range((len(nums)-2), -1, -1):
            postfix[i] = postfix[i+1] * nums[i+1]

        return [prefix[i] * postfix[i] for i in range(len(nums))]

# Can we possibly do better than the above o(N) time and space solution from above?
# not really I mean if we mutate the array and multiply across and then run through the second loop
# using a multiplication sum we could probably do it but that would end up mutating the original array/list

# Score Card
# Did I need hints? N
# Did you finish within 30 min? Y
# Was the solution optimal? Y
# Were there any bugs? N
#  4 4 5 5 = 4.5
