# Find the Most Competitive Subsequence: https://leetcode.com/problems/find-the-most-competitive-subsequence/

# Given an integer array nums and a positive integer k, return the most competitive subsequence of nums of size k.
# An array's subsequence is a resulting sequence obtained by erasing some (possibly zero) elements from the array.
# We define that a subsequence a is more competitive than a subsequence b (of the same length) if in the first position where a and b differ, subsequence a has a number less than the corresponding number in b. For example, [1,3,4] is more competitive than [1,3,5] because the first position they differ is at the final number, and 4 is less than 5.

# My first thought is that a backtracking solution would be the brute force as it would take n^k time to solve
# That being said can we do something better? I think that the answer is yes! Since we can take the value
# that comes after and use a queue to get a more optimal answer.

# To do the above we add a value to the queue if it is the lowest we have seen and we aren't above k
# after we pop off the value that is lower than the current we can do this because we know we can drop
# k - len(nums) values

class Solution:
    def mostCompetitive(self, nums, k):
        # I first thought about using deque but honestly we can use a stack
        result = []

        # Keep track of the number of values you can drop
        canDrop = len(nums) - k
        for i in nums:
            # Pop any values that is higher than our current top of stack if we have values to drop
            while len(result) > 0 and result[-1] > i and canDrop > 0:
                result.pop()
                canDrop -= 1
            result.append(i)

        # Return our result without the highest number as
        # we are only keeping values that are smaller on the stack
        while len(result) != k:
            result.pop()

        return list(result)


# Score Card
# Did I need hints? N
# Did you finish within 30 min? 20
# Was the solution optimal? This runs in o(n) time and space so I think it is pretty optimal
# Were there any bugs? I forgot at the end that we need to pop off any extra values as we can end up with a
# list of bigger and bigger numbers and we only need the len to be k
# 5 5 5 3 = 4.5
