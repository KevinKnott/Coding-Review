# Merge Intervals: https://leetcode.com/problems/merge-intervals/

# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

class Solution:
    def merge(self, intervals):
        return


# Score Card
# Did I need hints? Y
# Did you finish within 30 min? Y
# Was the solution optimal? Y
# Were there any bugs? I actually had two bugs one was not considering that I need to check incoming/outgoing connections
# and two my indexs start at 0 and the positions start at 1 should of caught it but I didn't do an example first
#  3 4 3 3 = 3.25
