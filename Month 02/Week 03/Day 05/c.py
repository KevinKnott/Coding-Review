# Product of Array Except Self: https://leetcode.com/problems/product-of-array-except-self/

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

# In this problem we can take advantage of the fact that we need to calc every other number except self
# and from l -> r which will give you the product from l -> i and then we go through a second time and
#  go from r -> l which will give you the product from r -> i which is the solution


class Solution:
    def productExceptSelf(self, nums):
        prefix, postfix = [0] * len(nums), [0] * len(nums)

        curProd = 1
        for i in range(len(nums)):
            prefix[i] = curProd
            curProd *= nums[i]

        curProd = 1
        for i in reversed(range(len(nums))):
            postfix[i] = curProd
            curProd *= nums[i]

        return [prefix[i] * postfix[i] for i in range(len(nums))]


# The above works pretty well! It runs in o(N) (technically 3n as we loop through the n nums 3 times)
# Basically we use a dp table to keep a current product ove every number to the left in prefix
# and then the same for  the product to the right of i in postfix  then all we have to do is multiply
# l -> i * r -> i

# Score Card
# Did I need hints? Nope
# Did you finish within 30 min? 10
# Was the solution optimal? See the above
# Were there any bugs? None
# 5 5 5 5 = 5
