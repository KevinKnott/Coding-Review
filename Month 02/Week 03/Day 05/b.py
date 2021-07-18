# Merge Intervals: https://leetcode.com/problems/merge-intervals/

# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.


# So you could solve this problem by going through every interval and comparing it to every other interval combining them as you go which would
# end up with an o(n^2) solution

# Or we could be a little bit more intelligent and instead sort the intervals based off of their start time. Once this is done we simply
# need to move through the list once and compare the current node to the previous and see if they overlap aka start is after the prev start and before
# or equal to the end of the prev

class Solution:
    def merge(self, intervals):
        if len(intervals) == 1:
            return intervals

        result = []

        # Sort intervals by start time
        intervals = sorted(intervals, key=lambda x: x[0])
        # We are garunteed to have at least one interval
        curInterval = intervals[0]

        for i in range(1, len(intervals)):
            # If we have an interval starting between the start and end of the prev
            if curInterval[1] >= intervals[i][0]:
                curInterval[1] = max(intervals[i][1], curInterval[1])
            # Otherwise if the node is starting after the prev we need to push the last
            # interval into our result and makke our new interval
            else:
                result.append(curInterval)
                curInterval = intervals[i]

        if len(result) == 0 or result[-1] != curInterval:
            result.append(curInterval)

        return result

# The above is solid and runs in o(nlogn) time and uses up to o(N) space. Is there a posibility of doing better?
# We could reduce the space complexity by updating the list as we go but that would add some considerable extra

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 15 m
# Was the solution optimal? See blurb
# Were there any bugs?  I didn't really have any bugs
# 5 5 5 5 = 5
