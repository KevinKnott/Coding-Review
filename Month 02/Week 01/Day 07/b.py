# Kth Smallest Element in a Sorted Matrix: https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

# Given an n x n matrix where each of the rows and columns are sorted in ascending order, return the kth smallest element in the matrix.
# Note that it is the kth smallest element in the sorted order, not the kth distinct element.

# Okay so I have a few thoughts on this problem we could merge all of the sorted arrays but I think that may be over kill
# We can take every matrix and add the first element to a heap and pop off 1 value at a time and add on that lists next value
# until the array is empty but if a matrix becomes empty what would we add next?
# Or we can simply do a binary search where we keep the minimum element we have seen and then close down the gap until we find the answer

import heapq


class Solution:
    def kthSmallest(self, matrix, k: int) -> int:
        smallest = []
        for row in range(len(matrix)):
            # initialize heap with value and location in matrix
            smallest.append((matrix[row][0], row, 0))

        heapq.heapify(smallest)

        # While we are less than k pop off a value and add the next one
        while k > 0:
            result, row, col = heapq.heappop(smallest)

            if col + 1 < len(matrix[row]):
                heapq.heappush(smallest, (matrix[row][col + 1], row, col+1))

            k -= 1

        return result

# This solution works and takes o(n) time and o(min(k, n)) space however it is quite intuitive!
# Now I think we can improve to log n time with the binary search so I am going to try and do that

    def kthSmallest(self, matrix, k):
        # So we need to count how man values are less than or equal to our midpoint
        def countLowerThan(mid):

            return
        # Then we add bst here

        lo, hi = 0,  matrix[-1][-1]
        # Get higest value and lowest value

        while lo < hi:
            mid = lo + (hi - lo) // 2

            count = countLowerThan(mid)

            if count < k:
                lo = mid + 1
            else:
                hi = mid

        return lo


# Score Card
# Did I need hints? Y for the second solution the bst is trickier than I thought
# Did you finish within 30 min? 30
# Was the solution optimal? My solution is optimal for time but the bst should be faster than the heap solution I just need to finish coding it
# Were there any bugs? I didn't find any bugs
# 4 3 4 5 = 4
