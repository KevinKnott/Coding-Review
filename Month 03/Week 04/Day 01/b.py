# Meeting Rooms II: https://leetcode.com/problems/meeting-rooms-ii/

# Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

from types import List

# In this problem we have a couple of options but if we use a heap to check whether or not there is still someone who needs a room and simply
# pop off rooms as we no longer need them. To do this though we will have to sort first based off of the starting times so that we know
# whether we need a new room or if an old room will suffice.

import heapq


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[0])

        ourHeap = []
        heapq.heappush(ourHeap, intervals[0][1])

        for i in range(1, len(intervals)):
            # If a room the earliest room is past the start
            # we have freed that first room so we can add a different
            # time slot there
            if intervals[i][0] >= ourHeap[0]:
                heapq.heappop(ourHeap)

            heapq.heappush(ourHeap, intervals[i][1])

        return len(ourHeap)


# The above works and will run in O(nlogn) time and use O(N) space

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 8
# Was the solution optimal? Y
# Were there any bugs? N
# 5 5 5 5 = 5
