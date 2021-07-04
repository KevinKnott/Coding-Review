# Meeting Rooms II: https://leetcode.com/problems/meeting-rooms-ii/
# Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

# So this problem is actually asking for how many times is there an over lapping meeting at the same time. Since these are time based we could
# sort them by starting time and keep track of how many rooms we need by having a heap.
#
# the logic is that we have a new starting time that is before the earliest ending time we need to add it to the heap
# then if the start time is after that ending we need to pop it off the stack

import heapq


class Solution:
    def minMeetingRooms(self, intervals):
        if not intervals:
            return

        # We need to sort based off of start time so we know when we can pop or not
        intervals = sorted(intervals, key=lambda x: x[0])

        rooms = []
        # result = 0

        for start, end in intervals:
            if len(rooms) != 0 and start >= rooms[0]:
                heapq.heappop(rooms)

            heapq.heappush(rooms, end)
            # result = max(result, len(rooms))

        return len(rooms)

# So this works and runs in o(nlogn) time and potentially o(n) space the question is can we do any better?
# And the answer is I don't think that it is possible to do better. I think that we could create a similar
# solution using two pointers but it would have the same complexity

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 20
# Was the solution optimal? See my above comments
# Were there any bugs? I didn't have any bugs
# 5 5 5 5 = 5
