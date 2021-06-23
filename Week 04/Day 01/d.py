#  Moving Average from Data Stream: https://leetcode.com/problems/moving-average-from-data-stream/

# Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.
# Implement the MovingAverage class:

#     MovingAverage(int size) Initializes the object with the size of the window size.
#     double next(int val) Returns the moving average of the last size values of the stream.

# very simple queue problem all we have to do is create a q of size size and then add values in
# keep track of the sum and divide by len(q)
# If we need to remove value we do so and remove it from sum

from collections import deque


class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.q = deque()
        self.size = size
        self.sum = 0

    def next(self, val: int) -> float:
        self.q.appendleft(val)
        self.sum += val

        if len(self.q) > self.size:
            self.sum -= self.q.pop()

        return self.sum / len(self.q)

# This is pretty much baller the time complexity of this solutions is O(1) as we are just adding a value and it isnt dependent on the size
# the space complexity is O(n) where n is the size of the window

# Could we do better? Instead of using a double ended queue we could probably use a circular and set the size to equal size
# and then place the value at the end using using a counter and some modulo that being said this code would be a bit confusing

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

# Score Card
# Did I need hints? N
# Did you finish within 30 min? Y
# Was the solution optimal? Y although you can read my blurb above about a potentially better solution it is rather complicated
# Were there any bugs? N
#  5 5 5 5 = 5
