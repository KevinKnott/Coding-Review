# Find the Most Competitive Subsequence: https://leetcode.com/problems/find-the-most-competitive-subsequence/

# Given an integer array nums and a positive integer k, return the most competitive subsequence of nums of size k.
# An array's subsequence is a resulting sequence obtained by erasing some (possibly zero) elements from the array.
# We define that a subsequence a is more competitive than a subsequence b (of the same length) if in the first position where a and b differ, subsequence a has a number less than the corresponding number in b. For example, [1,3,4] is more competitive than [1,3,5] because the first position they differ is at the final number, and 4 is less than 5.


# If so we simply keep increasing the result so long as we have >= k possible letters to be added
# by using a stack  we can check if the number we are checking is smaller and can pop off the bigger so long as the above condition is true

class Solution:
    def mostCompetitive(self, nums, k: int):
        stack = []
        addition = len(nums) - k

        for num in nums:
            while addition > 0 and len(stack) > 0 and stack[-1] > num:
                stack.pop()
                addition -= 1
            stack.append(num)

        while len(stack) != k:
            stack.pop()

        return stack

# The above works the trick is we need to figure out how many values we are allowed to remove while parsing so that we can always have
# the right amount of values in the subset. Then we can pop off any values if they are larger numbers on our parsing stack than our
# cur num

# This will run in O(N) for time and space and I believe it is optimal.

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 15
# Was the solution optimal? Yea
# Were there any bugs? I forgot that I need to pop off all numbers
# 5 5 5 4 = 4.75
