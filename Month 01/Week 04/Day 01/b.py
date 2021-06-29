# Kth Smallest Element in a Sorted Matrix: https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

# Given an n x n matrix where each of the rows and columns are sorted in ascending order, return the kth smallest element in the matrix.
# Note that it is the kth smallest element in the sorted order, not the kth distinct element.

import heapq


class Solution:
    def kthSmallest(self, matrix, k):
        indicies = [0 for _ in range(len(matrix))]

        while k > 0:
            lowest = None

            for i in range(len(matrix)):
                if indicies[i] >= len(matrix[i]):
                    continue
                if lowest is None or matrix[i][indicies[lowest]] < matrix[lowest][indicies[lowest]]:
                    lowest = i

            k -= 1
            if k > 0:
                indicies[lowest] += 1

        return matrix[lowest][indicies[lowest]]

# The above solution works bout could we be a bit more efficient? I think so in the above solution we have to constantly check all the values
# When really we can create a heap of all the lowest elements and pop the lowest and add the next val on until we are done (very similar to above)

    def kthSmallest(self, matrix, k):
        ourHeap = []

        for i in range(len(matrix)):
            ourHeap.append((matrix[i][0], i, 0))

        heapq.heapify(ourHeap)

        while k > 0:
            result, r, c = heapq.heappop(ourHeap)

            k -= 1
            if k == 0:
                return result

            if c+1 < len(matrix[r]):
                heapq.heappush(ourHeap, (matrix[r][c+1], r, c+1))

# This works pretty effecitvely in terms of space we use an auxilary o(M) where M is the len of the matricies
# However this works in  O(M) (for heap construction) + O(K log M) (for appending an element k times) = O(M + K log M) where M is the length of the matricies and

# Is there a better solution? It turns out that yes there is! Since we know that the smallest values is at [0,0] and the largest is at [M][M] we can actually
# use a binary search and solve this in O(N log N) time and o(1) space where N is the number of elements aka (M*M)
# The tricky part about this is at every mid point we have to count number of elements below the current to see if we are at K above or below it to binary search properly

# Score Card
# Did I need hints? Y for optimal
# Did you finish within 30 min? Y although I took some more time to review the binary search so I can try that next time
# Was the solution optimal? My solution is pretty close to optimal but there are some improvements I listed above
# Were there any bugs? Y my first solution with arrays (which is like the heap solution) doesn't keep track of which element to move across if all values are the same
# 3 4 2 2 = 2.75
