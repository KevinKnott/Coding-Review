# Kth Smallest Element in a Sorted Matrix: https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

# Given an n x n matrix where each of the rows and columns are sorted in ascending order, return the kth smallest element in the matrix.
# Note that it is the kth smallest element in the sorted order, not the kth distinct element.

# The almost optimal that is neat is using a heap to simple keep adding elements of each list and then
# moving through n times which is pretty optimal in o(min(K,n) + klogn) and o(min(k, n)) space

# For this problem the optimal solution is a binary search algo where you check if the middle value has k elements below it
# I will be focusing on this as the heap solution takes all of 5 min to code but the binary search is a lot harder


class Solution:
    def countLessThanMid(self, matrix, mid, smaller, larger):
        count, n = 0, len(matrix)
        row, col = n - 1, 0

        while row >= 0 and col < n:
            if matrix[row][col] > mid:
                larger = min(larger, matrix[row][col])
                row -= 1
            else:
                smaller = max(smaller, matrix[row][col])
                count += row + 1
                col += 1

        return count, smaller, larger

    def kthSmallest(self, matrix, k: int) -> int:

        n = len(matrix)
        # Garunteed to be square
        # So this is a basic binary search but we use the value instead of the index to find
        # correct element
        start, end = matrix[0][0], matrix[n-1][n-1]
        while start < end:
            mid = start + (end - start) / 2
            smaller, larger = matrix[0][0], matrix[n-1][n-1]

            count, smaller, larger = self.countLessThanMid(
                matrix, mid, smaller, larger)

            if count == k:
                return smaller
            elif count < k:
                start = larger
            else:
                end = smaller

        return start


# Score Card
# Did I need hints? Yes
# Did you finish within 30 min?  28
# Was the solution optimal? This is optimal
# Were there any bugs? No
# 3 5 5 5 = 4.5
