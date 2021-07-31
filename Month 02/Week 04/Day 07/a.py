# Kth Smallest Element in a Sorted Matrix: https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

# Given an n x n matrix where each of the rows and columns are sorted in ascending order, return the kth smallest element in the matrix.
# Note that it is the kth smallest element in the sorted order, not the kth distinct element.


class Solution:
    def kthSmallest(self, matrix, k: int) -> int:
        return

# Score Card
# Did I need hints? N
# Did you finish within 30 min? N (45 or so)
# Was the solution optimal? I believe so we could make some slight optimization but this will run in o(n^2) because of the multiplicity we would go through once and then again to multiply
#  and o(n) space
# Were there any bugs? I listed bugs in the above code
#  5 2 4 2 = 3.25
