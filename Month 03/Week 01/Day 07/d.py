# Meeting Rooms II: https://leetcode.com/problems/meeting-rooms-ii/

# Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

# For this problem we have potentially two solutions both of them involve sorting. My optimal method would be to use a min heap and keep track
# of all of the end times we keep going through the intervals one at a time and keep track of the max len of it. Whenever we have a start time
# past the top end time we can pop off the top of the heap until that is no longer the case

import heapq


class Solution:
    def minMeetingRooms(self, intervals) -> int:
        if len(intervals) == 0:
            return 0

        rooms = []

        # We need to sort the intervals to be in order
        intervals = sorted(intervals, key=lambda x: x[0])

        for start, end in intervals:

            # I initially forgot we only need to remove a room at at time
            # since we can just use the heap to keep the count other wise we could
            # use a max val
            if len(rooms) != 0 and start >= rooms[0]:
                heapq.heappop(rooms)

            heapq.heappush(rooms, end)

        return len(rooms)


# Easy O(nlogn) and O(N) problem

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 10
# Was the solution optimal? This is optimal
# Were there any bugs? No
#  5 5 5 5 = 5
