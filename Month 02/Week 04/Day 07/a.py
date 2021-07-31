# Kth Smallest Element in a Sorted Matrix: https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

# Given an n x n matrix where each of the rows and columns are sorted in ascending order, return the kth smallest element in the matrix.
# Note that it is the kth smallest element in the sorted order, not the kth distinct element.

# For this problem we need to go through each of the values and use a heap of all of the values
# up until we reach k this should be an o(nlogn) and o(N) where n is length

import heapq


class Solution:
    def kthSmallest(self, matrix, k: int) -> int:
        ourHeap = []

        for i in range(len(matrix)):
            ourHeap.append((matrix[i][0], i, 0))

        heapq.heapify(ourHeap)

        while k > 1:
            _, listIndex,  index = heapq.heappop(ourHeap)

            if index + 1 < len(matrix[listIndex]):
                heapq.heappush(
                    ourHeap, (matrix[listIndex][index + 1], listIndex, index + 1))

            k -= 1

        result, _, _ = heapq.heappop(ourHeap)
        return result

# The above solution works! However is this the most optimal solution? Definitely not
# by using a binary search and counting the numbers below the middle nubmer we can
# also solve this in o(nlogn) and o(1) as we wouldnt create a ehap but just use our list

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 15
# Was the solution optimal? See above
# Were there any bugs? none
# 5 5 3 5 = 4.5
