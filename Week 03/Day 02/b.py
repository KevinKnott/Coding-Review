# Meeting Rooms II: https://leetcode.com/problems/meeting-rooms-ii/

# Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required


# So my first thought is to sort the list of intervals by start time
# have interval start and end then go to next if the start time lies within interval
# increase our count by one and figure out the first meeting to end
# While the above works I am not sure how to code it

import heapq


class Solution:
    def minMeetingRooms(self, intervals):
        # Sort on start time nlogn
        if len(intervals) == 1:
            return 1

        intervals = sorted(intervals, key=lambda x: x[0])

        rooms = []
        # If we make a heap we can pop off the top element if our start is past its end

        # push on the end of the first interval
        heapq.heappush(rooms, intervals[0][1])

        for i in range(1, len(intervals)):

            if intervals[i][0] >= rooms[0]:
                heapq.heappop(rooms)

            heapq.heappush(rooms, intervals[i][1])

        return len(rooms)

# This runs in nlogn time and uses up to n spaces if they are all overlapping

# Can we do better I am not sure we can
# That being said there is a slightly different approach that we could use that actually ends up using a two pointer
# solution that is very similar to the above
    def minMeetingRooms2Pointer(self, intervals):
        if len(intervals) == 1:
            return 1

        curRooms = 0

        startArray = sorted([i[0] for i in intervals])
        endArray = sorted(i[1] for i in intervals)
        startIndex, endIndex = 0, 0

        while startIndex < len(intervals):
            if startArray[startIndex] >= endArray[endIndex]:
                curRooms -= 1
                endIndex += 1

            curRooms += 1
            startIndex += 1

        return curRooms


# Score Card
# Did I need hints? Y
# Did you finish within 30 min? Y
# Was the solution optimal? Y although I messed up the thought process of how to solve the problem
# Were there any bugs?  I didn't really have any bugs
#  2 3 3 5 = 3.25
