# Find Median from Data Stream
# The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values.

# For example, for arr = [2,3,4], the median is 3.
# For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
# Implement the MedianFinder class:

# MedianFinder() initializes the MedianFinder object.
# void addNum(int num) adds the integer num from the data stream to the data structure.
# double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.

import heapq


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []
        return

    def addNum(self, num):
        Initital insertion O(N) not quite fast enough could improve through binary search and then insert which would be o(log(n)) or o(nlogn)
        index = 0
        while len(self.nums) > 0 and index < len(self.nums) and self.nums[index] < num:
            index += 1
        #  technically this is 2n because the insert may have to insert and then move everything
        self.nums.insert(index, num)

        return

    def findMedian(self):
        if len(self.nums) == 0:
            return 0

        midpoint = len(self.nums) // 2

        if len(self.nums) % 2 == 0:
            return (self.nums[midpoint] + self.nums[midpoint+1]) // 2

        return self.nums[midpoint]


# Time Limit Exceeded for this result but it works in o(N) insert o(1) find median

# I checked the solution and it recommended that we don't need to sort all of the numbers and maybe there is a data structure that can
# Find the highest point of the low and the lowest point of the high and then we can always solve for the median
# ITS A HEAP!

# Python is trash for max heaps I had to multiply by negative 1 to do everything

class MedianFinder2():

    def __init__(self):
        """
        initialize your data structure here.
        """
        # self.nums = []
        self.low = []
        self.high = []
        heapq.heapify(self.low)
        heapq.heapify(self.high)
        return

    def addNum(self, num):
        # push onto low
        topLow = heapq.heappushpop(self.low, -1 * num)

        # grab top of low and push onto the max  (to keep them even)
        heapq.heappush(self.high, -1 * topLow)

        # print(self.low, self.high)

        # If high is greater switch back the last element
        if len(self.low) < len(self.high):
            heapq.heappush(self.low, -1 * heapq.heappop(self.high))

        return

    def findMedian(self):

        return -1 * self.low[0] if len(self.low) != len(self.high) else ((-1 * self.low[0] + self.high[0]) / 2)

# Score Card
# Did I need hints?
# Did you finish within 30 min?
# Was the solution optimal?
# Were there any bugs?
#  1 1 2 2 = 1.5
