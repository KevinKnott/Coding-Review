# Kth Largest Element in an Array: https://leetcode.com/problems/kth-largest-element-in-an-array/

# Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.

class Solution:
    def findKthLargest(self, nums, k):
        return


# Score Card
# Did I need hints? Y
# Did you finish within 30 min? Noooooo oh god
# Was the solution optimal? Oh yea however I needed lots of hints although the backtracking was actually not the hard part
# Were there any bugs? I initially messed up passing in the next row/col by not increasing row when overflowing
#  1 1 3 3 = 2
