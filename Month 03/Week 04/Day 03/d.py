# Kth Smallest Element in a Sorted Matrix: https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

# Given an n x n matrix where each of the rows and columns are sorted in ascending order, return the kth smallest element in the matrix.
# Note that it is the kth smallest element in the sorted order, not the kth distinct element.

from types import List

# So the first solution I think of in this problem is to use a heap and simply pop k nodes of in o(klogk) time (its a bit complicated
# so I may be a bit wrong). I think this could also be solved using a binary search but I am not exactly sure how to do it


import heapq


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        ourHeap = []
        for i in range(len(matrix)):
            ourHeap.append((matrix[i][0], i, 0))

        heapq.heapify(ourHeap)
        size = len(matrix[0])

        # reduce to only one above k so pop returns answer
        while k > 1:
            _, r, c = heapq.heappop(ourHeap)

            if c + 1 < size:
                heapq.heappush(ourHeap, (matrix[r][c+1], r, c+1))

            k -= 1

        result, _, _ = heapq.heappop(ourHeap)

        return result

# This works and is pretty optimal see above

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 6
# Was the solution optimal? This is optimal
# Were there any bugs? No
#  5 5 5 5 = 5
