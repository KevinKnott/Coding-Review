class initial():
    def solution(self, nums):
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]

        for j in range(len(nums)-2, -1, -1):
            suffix[j] = suffix[j+1] * nums[j+1]

        return [prefix[i] * suffix[i] for i in range(len(nums))]


# https://leetcode.com/problems/product-of-array-except-self/
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

# Score Card
# Did I need hints
# Did you finish within 30 min
# Finished in 20 min
# Was the solution optimal
# The solution is optimal for time but not space
# Were there any bugs
# I forgot to correctly  multiply the first nums by i-1 so that result wasn't quite right and wasted 4 min

# test case 1
nums = [1, 2, 3, 4]
# output = [24,12,8,6]

sol = initial()
print(sol.solution(nums))
