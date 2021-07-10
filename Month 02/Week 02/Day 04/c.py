# Find Median from Data Stream: https://leetcode.com/problems/find-median-from-data-stream/

# The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values.

# For example, for arr = [2,3,4], the median is 3.
# For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
# Implement the MedianFinder class:

# MedianFinder() initializes the MedianFinder object.
# void addNum(int num) adds the integer num from the data stream to the data structure.
# double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.

# This problem would normally be dificult when we add we would have to do an insertion sort in o (N) time and then
# have the medium end up being an o(1) call but we can improbe this to an o(logn) by using two heaps
# It is simple we have a low max heap and a higher min heap and then we count values we put in and can cal the values
# based of the top of the heaps

# Our way of pushing onto the stack is simply push onto the smaller then pop off and add it to the higher
# then even out just to make sure we stay level

import heapq


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lower = []
        self.higher = []
        self.count = 0

    def addNum(self, num: int) -> None:
        self.count += 1
        # Push onto lower
        topLower = heapq.heappushpop(self.lower, -1 * num)

        # Then pop from lower to higher
        heapq.heappush(self.higher, - 1 * topLower)

        # Then balance the two
        if len(self.higher) > len(self.lower):
            botHigher = heapq.heappop(self.higher)
            heapq.heappush(self.lower, -1 * botHigher)

    def findMedian(self) -> float:

        if self.count % 2 == 0:
            return ((-1 * self.lower[0]) + self.higher[0]) / 2

        return -1 * self.lower[0]

# Score Card
# Did I need hints? Nope
# Did you finish within 30 min? 10 min
# Was the solution optimal? Yuh check my blurb at the top!
# Were there any bugs? None
# 5 5 5 5 = 5
