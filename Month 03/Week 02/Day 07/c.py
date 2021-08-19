# Merge Intervals: https://leetcode.com/problems/merge-intervals/

# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

# So in this problem we are combining intervals and the easiest way to do this is to simply sort out by the starting time then we can on the fly ammend the first
# interval that we see to include any of the following and move to the right if the second interval is not a part of the previous interval

class Solution:
    def merge(self, intervals):
        if len(intervals) <= 1:
            return intervals

        intervals.sort(key=lambda x: x[0])
        result = []
        start, end = intervals[0][0], intervals[0][1]

        for i in range(1, len(intervals)):

            if intervals[i][0] >= start and intervals[i][0] <= end:
                end = max(intervals[i][1], end)
            else:
                result.append([start, end])
                start = intervals[i][0]
                end = intervals[i][1]

        if len(result) == 0 or result[-1] != [start, end]:
            result.append([start, end])

        return result

# This will run in O(nlogn) time as you have to sort by the starting time and it uses O(N) or O(logn) based on your sorting algo

# Score Card
# Did I need hints? Nope
# Did you finish within 30 min? 10 min
# Was the solution optimal? Yee
# Were there any bugs? Nee
# 5 5 5 5 = 5
