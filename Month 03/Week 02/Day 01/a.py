# Shortest Subarray with Sum at Least K: https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/

# Given an integer array nums and an integer k, return the length of the shortest non-empty subarray of nums with a sum of at least k. If there is no such subarray, return -1.
# A subarray is a contiguous part of an array

class Solution:
    def shortestSubarray(self, nums, k):
        return

# Score Card
# Did I need hints? N
# Did you finish within 30 min? N (45 or so)
# Was the solution optimal? I believe so we could make some slight optimization but this will run in o(n^2) because of the multiplicity we would go through once and then again to multiply
#  and o(n) space
# Were there any bugs? I listed bugs in the above code
#  5 2 4 2 = 3.25
