#  Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts: https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/

# You are given a rectangular cake of size h x w and two arrays of integers horizontalCuts and verticalCuts where:

# horizontalCuts[i] is the distance from the top of the rectangular cake to the ith horizontal cut and similarly, and
# verticalCuts[j] is the distance from the left of the rectangular cake to the jth vertical cut.
# Return the maximum area of a piece of cake after you cut at each horizontal and vertical position provided in the arrays horizontalCuts and verticalCuts. Since the answer can be a large number, return this modulo 109 + 7.

# This problem seems simple enough given x amount of cuts determine the biggest rectangle you can make.
# This problem is actually supper easy if you consider the largest rectangle on a grid will be created by L x W
# Where you have the largets L in a set of Ls and the largest W in a set of Ws

# This means there are two solutions one when you search through the lists in o(N) and get the two largest
# or by using a heap and in nlog(n) determining the largest

import heapq


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts, verticalCuts):
        # Sort so we know that everything is in order so we can determine space between
        horizontalCuts.sort()
        verticalCuts.sort()

        mod = (10 ** 9) + 7

        maxW = 0
        maxH = 0

        # We need to check first and last cut as they are outside the normal checking pattern
        maxW = max(maxW, verticalCuts[0] - 0)
        maxH = max(maxH, horizontalCuts[0] - 0)

        maxW = max(maxW, w - verticalCuts[-1])
        maxH = max(maxH, h - horizontalCuts[-1])

        for i in range(1, len(horizontalCuts)):
            maxH = max(maxH, horizontalCuts[i] - horizontalCuts[i-1])

        for i in range(1, len(verticalCuts)):
            maxW = max(maxW, verticalCuts[i] - verticalCuts[i-1])

        return (maxH * maxW) % mod

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 13
# Was the solution optimal? This is the optimal solution as it runs in o(max(nlogn or mlogm)) and uses o(1) spaces
# Were there any bugs? I listed bugs in the above code
# 5 5 5 5 = 5
