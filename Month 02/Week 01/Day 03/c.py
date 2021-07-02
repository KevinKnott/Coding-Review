# Two Sum II - Input array is sorted: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

# Given an array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.
# Return the indices of the two numbers (1-indexed) as an integer array answer of size 2, where 1 <= answer[0] < answer[1] <= numbers.length.
# The tests are generated such that there is exactly one solution. You may not use the same element twice.

# If we have an input list and we are told to get a sum that equals our target we can take advantage of the fact that
# moving up on the left increases our value and moving down on the right decreases our value with that we know
# if a number is small move the left pointer and if a number is to high decrease the right pointer
# and if the two pointers overlap we don't have a solution

class Solution:
    def twoSum(self, numbers, target: int):
        left, right = 0, len(numbers) - 1

        while left < right:
            curSum = numbers[left] + numbers[right]

            if curSum < target:
                left += 1
            elif curSum > target:
                right -= 1
            else:
                # I forgot that we need to index from one
                # according to the problem
                return [left + 1, right + 1]

        return -1

# This solution is correct and only uses o(n) time and o(1) space I don't think that we could really improve on this

# Score Card
# Did I need hints? Nope
# Did you finish within 30 min? 4 minutes
# Was the solution optimal? Oh yea see above
# Were there any bugs? None
# 5 5 5 5 = 5
