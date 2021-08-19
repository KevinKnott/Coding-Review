#  Kth Smallest Element in a Sorted Matrix: https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

# Given an n x n matrix where each of the rows and columns are sorted in ascending order, return the kth smallest element in the matrix.
# Note that it is the kth smallest element in the sorted order, not the kth distinct element.


# The easiest way to do this problem is to use heaps to keep track of all of the best elements (especially since python use min heap)
# in each row and just pop off everyt time until you get to the very last k (so k pops) and then you can return result
# this will run in O(nlogn) and O(N) space

# The ideal solution would be to use a binary search algorithm as we know everything is already sorted however it is extremely complicated
# to figure out the count of items below it so we will se if I get to it

import heapq


class Solution:
    def kthSmallest(self, matrix, k: int) -> int:
        ourHeap = []

        for i in range(len(matrix)):
            ourHeap.append((matrix[i][0], i, 0))

        heapq.heapify(ourHeap)

        # Now that it is sorted we can actually go through k times and get the smallest at k and pop it off
        # then add the new one with the coordinates of the 2d array

        while k > 1:
            _, row, col = heapq.heappop(ourHeap)

            if col + 1 < len(matrix[row]):
                heapq.heappush(ourHeap, (matrix[row][col+1], row, col+1))

            k -= 1

        result, _, _ = heapq.heappop(ourHeap)
        return result

# The above works and is exactly as efficient as I said above I used about 10 min to finish this problem
# but I only have 30 more minutes to finish my other two problems so I wont write the slight more efficient
# binary search

# Score Card
# Did I need hints? Y
# Did you finish within 30 min? 10
# Was the solution optimal? Y
# Were there any bugs? N
# 5 5 5 5 = 5
