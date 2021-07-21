# Kth Smallest Element in a Sorted Matrix: https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

# Given an n x n matrix where each of the rows and columns are sorted in ascending order, return the kth smallest element in the matrix.
# Note that it is the kth smallest element in the sorted order, not the kth distinct element.

# So I think that there are a number of solutions to this problem the first being that we could merge all lists together and sort
# which would be nlogn time and o(1) space. Or we could use a heap witht the val and index and keep pushing on values as we pop
# to get the lowest in the k rows. Lastly if we did a binary search we could count how many numbers below the midpoint there
# are and simply search for the right k.

# I am going to start with the heap solution and then if I have time will move to the bs solution

import heapq


class Solution:
    def kthSmallest(self, matrix, k: int) -> int:
        ourHeap = []

        for i in range(len(matrix)):
            heapq.heappush(ourHeap, (matrix[i][0], i, 0))

        while k > 1:
            _, row, col = heapq.heappop(ourHeap)

            if col + 1 < len(matrix[row]):
                heapq.heappush(ourHeap, (matrix[row][col+1], row, col+1))

            k -= 1

        result, _, _ = heapq.heappop(ourHeap)
        return result

# The above works and runs in min(k,n) and then X + K log x as we are at every k removing and adding a val
# and the initial heap construction (o of x normally but xlogx as I am doing it the wrong way)
# With this we end up at O(min(k,n) + klog(x)) time and using o(min(k, n)) space


# However a bst could work here we just have to figure out some math on finding the count < mid point

    def kthSmallest(self, matrix, k: int) -> int:

        def countLessEqual(mid, smaller, larger):
            count, n = 0, len(matrix)
            row, col = n - 1, 0

            while row >= 0 and col < n:
                if matrix[row][col] > mid:

                    # As matrix[row][col] is bigger than the mid, let's keep track of the
                    # smallest number greater than the mid
                    larger = min(larger, matrix[row][col])
                    row -= 1

                else:

                    # As matrix[row][col] is less than or equal to the mid, let's keep track of the
                    # biggest number less than or equal to the mid

                    smaller = max(smaller, matrix[row][col])
                    count += row + 1
                    col += 1

            return count, smaller, larger

        n = len(matrix)
        # Get lowest and highest values
        start, end = matrix[0][0], matrix[n-1][n-1]

        while start < end:
            mid = start + (end - start) / 2

            # Keep track of smaller val and largerval
            smaller, larger = (matrix[0][0], matrix[n-1][n-1])

            count, smaller, larger = countLessEqual(mid, smaller, larger)

            # Basic binary search
            if count == k:
                return smaller
            elif count < k:
                start = larger
            else:
                end = smaller

        return start


# I didn't quite finish the above it turned out to be a bit more complex than I expected


# Score Card
# Did I need hints? Yeah for the binary search piece
# Did you finish within 30 min? 30
# Was the solution optimal? I have to figure out the binary search solution
# Were there any bugs? None
# 3 4 4 2 = 3.25
