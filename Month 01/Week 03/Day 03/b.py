# Merge Intervals: https://leetcode.com/problems/merge-intervals/

# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

# This problem you could naively search through each pair and combine it with the next if they overlap in o(n^2) or you can
# sort by the starting time and merge any interval that falls within in o(nlogn)
class Solution:
    def merge(self, intervals):
        if len(intervals) <= 1:
            return intervals

        result = []
        intervals = sorted(intervals, key=lambda x: x[0])
        start, end = intervals[0][0], intervals[0][1]

        for i in range(1, len(intervals)):
            if end >= intervals[i][0]:
                end = max(end, intervals[i][1])
            else:
                result.append([start, end])
                start, end = intervals[i][0], intervals[i][1]

        if len(result) == 0 or result[-1] != [start, end]:
            result.append([start, end])

        return result


# Okay well this works but I actually messed up and forgot to check if result is empty  meaning we were able to combine
# everything into one interval

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 13
# Was the solution optimal? Y
# Were there any bugs? Read the above paragraph
# 5 5 5 3 = 4.5
