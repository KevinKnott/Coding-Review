# Split Array Largest Sum: https://leetcode.com/problems/split-array-largest-sum/

# Given an array nums which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays.
# Write an algorithm to minimize the largest sum among these m subarrays.

class Solution:
    def splitArray(self, nums, m):
        return


# Score Card
# Did I need hints? N
# Did you finish within 30 min? N (45 or so)
# Was the solution optimal? I believe so we could make some slight optimization but this will run in o(n^2) because of the multiplicity we would go through once and then again to multiply
#  and o(n) space
# Were there any bugs? I listed bugs in the above code
#  5 2 4 2 = 3.25
