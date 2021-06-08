# Find Median from Data Stream: https://leetcode.com/problems/find-median-from-data-stream/
# The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values.

#     For example, for arr = [2,3,4], the median is 3.
#     For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.

# Implement the MedianFinder class:

#     MedianFinder() initializes the MedianFinder object.
#     void addNum(int num) adds the integer num from the data stream to the data structure.
#     double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.


# Brute force O(N) to add number into sorted array  honestly a linked list would be better as we insert at O(N) and not have to move elements
# That would mean that we have to make the median an o(n) complexity to get to the midpoint
import heapq


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.values = []

    def addNum(self, num: int) -> None:
        if len(self.values) == 0:
            self.values.append(num)

        index = 0
        while index < len(self.values) and num > self.values[index]:
            index += 1

        self.values.insert(index, num)
        return

    def findMedian(self) -> float:
        midPoint = len(self.values) / 2

        if len(self.values) % 2 == 0:
            return (self.values[midPoint - 1] + self.values[midPoint]) / 2

        return self.values[midPoint]


class MedianFinderOptimal:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lower = []  # max heap
        self.higher = []  # min heap

    # This needs improvement so instead of adding in o(n) we could potentially use a heap or two to get largest of the smallest half and smallest of the largest half
    # that way we have o(klogn) where k  for updates and o(1) for find median still
    def addNum(self, num: int) -> None:
        # Add a number to lower (this is a max heap so we need to invert number)
        topLower = heapq.heappushpop(self.lower, -1 * num)

        # Pop from lower to insert into higher
        heapq.heappush(self.higher, -1 * topLower)

        # if the higher heap is larger even out (we prefer the value on top of lowest in an odd)
        if len(self.higher) > len(self.lower):
            heapq.heappush(self.lower, -1 * heapq.heappop(self.higher))

        return

    def findMedian(self) -> float:

        if (len(self.lower) + len(self.higher)) % 2 == 0:
            return (-1 * self.lower[0] + self.higher[0]) / 2

        return -1 * self.lower[0]

# Potentiall better solution? Apparently so you can use a AVL tree or any Self-balancing Binary Search Tree to keep median in one spot and then use two pointers to track it
# The problem is AVL trees are hard to implement however python doesn't have one withtin the std library


# Score Card
# Did I need hints? N
# Did you finish within 30 min? Y
# Was the solution optimal? Y
# Were there any bugs? Y  (no support for max heaps made me use negatives and I forgot to handle them properly)
#  5 5 5 3 = 4.5
