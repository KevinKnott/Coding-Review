# Merge Intervals: https://leetcode.com/problems/merge-intervals/

# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

from types import List


# In this problem we have to worry about merging the intervals together and this is actually a quite difficult proccess. We could compare
# every single interval from i -> j in an exhaustive n^2 search. However this is not optimal what we can do is actually sort based off
# of the starting times and then go through the list and whenever we have an overlapping time (start of 2nd is < end of first) we simply
# edit the end to be the max of both intervals and keep going until we are done

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        result = []

        for interval in intervals:
            # end of last result[-1] [1] < start interval[0]
            # Then there is no overlap and we need to append to result
            if not result or result[-1][1] < interval[0]:
                result.append(interval)
            else:
                # If there is an overlap update the end to be higher
                # of current interval or the prev interval end
                result[-1][1] = max(interval[1], result[-1][1])

        return result

# This works and is pretty optimal it runs in O(nlogn) for time and for space O(N) or O(logn) depending on algo for sorting


# Score Card
# Did I need hints? Nope
# Did you finish within 30 min? 10
# Was the solution optimal? Y
# Were there any bugs? None
# 5 5 5 5 = 5
