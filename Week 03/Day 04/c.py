#  Find the Most Competitive Subsequence: https://leetcode.com/problems/find-the-most-competitive-subsequence/

# Given an integer array nums and a positive integer k, return the most competitive subsequence of nums of size k.
# An array's subsequence is a resulting sequence obtained by erasing some (possibly zero) elements from the array.
# We define that a subsequence a is more competitive than a subsequence b (of the same length) if in the first position where a and b differ, subsequence a has a number less than the corresponding number in b. For example, [1,3,4] is more competitive than [1,3,5] because the first position they differ is at the final number, and 4 is less than 5.

# This seems like a backtracking problem in which you go down from every starting point
# and if you find a sequence that is less starting at the next index while going down
# you continue down until len (K) or you hit a subsequence with a higher val at index

from collections import deque


class Solution:
    def mostCompetitive(self, nums, k):
        self.result = []

        def dfs(current=[], index=0):
            if len(current) == k:
                if self.result != []:
                    for i in range(k):
                        if self.result[i] > current[i]:
                            self.result = current[:]
                        elif self.result[i] < current[i]:
                            return

                self.result = current[:]
                return

            for i in range(index, len(nums)):
                dfs(current + [nums[i]], i+1)

        dfs()
        return self.result

# Could we do better? Oh yeah the above goes through n! possible cases in the worst solution
# Since we know that we have a subsequence of numbers we can cheat with a deque
    def mostCompetitive(self, nums, k):
        result = []

        addition = len(nums) - k
        for i in nums:
            while len(result) > 0 and result[-1] > i and addition > 0:
                result.pop()
                addition -= 1
            result.append(i)

        while len(result) != k:
            result.pop()

        return list(result)


# Score Card
# Did I need hints? Yes
# Did you finish within 30 min? No
# Was the solution optimal? No my initial solution was n! bounded by k but the best solution is the second one where we use a deque to add numbersif we are
# under the max k and pop if the current val is less then what is on the queue or stack
# Were there any bugs?
# 4 1 2 3 = 2.5
