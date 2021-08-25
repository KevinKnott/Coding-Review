# Find the Most Competitive Subsequence: https://leetcode.com/problems/find-the-most-competitive-subsequence/

# Given an integer array nums and a positive integer k, return the most competitive subsequence of nums of size k.

# An array's subsequence is a resulting sequence obtained by erasing some (possibly zero) elements from the array.
# We define that a subsequence a is more competitive than a subsequence b (of the same length) if in the first position where a and b differ, subsequence a has a number less than the corresponding number in b. For example, [1,3,4] is more competitive than [1,3,5] because the first position they differ is at the final number, and 4 is less than 5.

from types import List

# For this problem I think that we should use a stack to help parse through this list we have two options at any given point assuming
# we can drop len(nums) - k elements basically if you find a value that is less and we can pop off numbers of the stack we should
# otherwise we simply append the number. We will continue to do this until we have finished parsing, at that point it is still possible
# that we have more than k numbers on the stack (1, 2, 3, 4) so the most competitive will be the first k elements so we will pop
# off the back until we have arrived at our result


class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        possible = len(nums) - k

        for num in nums:
            while possible and stack and stack[-1] > num:
                stack.pop()
                possible -= 1

            stack.append(num)

        # Since we know that if you have strictly increasing numbers we will have a
        # stack greater than k and we know the first k elements are all increasing
        # pop off extra nums
        while len(stack) > k:
            stack.pop()

        return stack

# The above is correct and runs in O(N) time and space the question is can we actually do better?
# I don't think we can as creating all the possibilites or possible subsequences will require
# time or space

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 6
# Was the solution optimal? Y
# Were there any bugs? N
# 5 5 5 5 = 5
