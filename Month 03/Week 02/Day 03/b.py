# Find Median from Data Stream: https://leetcode.com/problems/find-median-from-data-stream/

# The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values.

#     For example, for arr = [2,3,4], the median is 3.
#     For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.

# Implement the MedianFinder class:

#     MedianFinder() initializes the MedianFinder object.
#     void addNum(int num) adds the integer num from the data stream to the data structure.
#     double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.


# In this problem we can simply add every value into a list and keep track of the number of values and immediately access mid and mid +1
# to get the solution the problem is that this would run in o(N) if we used insertion sort (sorting numbers) as we go and using o(N) space
# The question is can we do better? and the answer is yes since we don't need to have all the numbers sorted and we just need the max of the
# small numbers and the min of the big numbers we can use two heaps to reduce the time complexity down to o(logn) and o(N) space

import heapq


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lo = []  # max heap
        self.hi = []  # min heap
        self.count = 0

    def addNum(self, num: int) -> None:
        self.count += 1
        # add to lo
        top = -1 * heapq.heappushpop(self.lo, -num)

        # pop off lo and add to hi
        heapq.heappush(self.hi, top)

        # if hi is larger pop off and move to lo for balancing
        if len(self.hi) > len(self.lo):
            heapq.heappush(self.lo, -1 * heapq.heappop(self.hi))

    def findMedian(self) -> float:

        if self.count % 2 == 1:
            return -1 * self.lo[0]

        return ((-1 * self.lo[0]) + self.hi[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# Score Card
# Did I need hints? Niet
# Did you finish within 30 min? 10
# Was the solution optimal? This is optimal
# Were there any bugs? No bugs although it looks ugly as python doesnt support max heaps without negative numbers
# 5 5 5 5 = 5
