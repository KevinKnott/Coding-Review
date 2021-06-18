# Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts: https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/

# You are given a rectangular cake of size h x w and two arrays of integers horizontalCuts and verticalCuts where:

#     horizontalCuts[i] is the distance from the top of the rectangular cake to the ith horizontal cut and similarly, and
#     verticalCuts[j] is the distance from the left of the rectangular cake to the jth vertical cut.

# Return the maximum area of a piece of cake after you cut at each horizontal and vertical position provided in the arrays horizontalCuts and verticalCuts. Since the answer can be a large number, return this modulo 109 + 7.

class Solution:
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        return

# Score Card
# Did I need hints? Y for index math on getting the split point
# Did you finish within 30 min? Y
# Was the solution optimal? My initial solution is optimal however I needed to a bit of extra refactoring for using another metho
# Were there any bugs? I initially was off by one on length because of hitting -1  and not changing length with a minus 1
#  4 4 3 2 = 3.25
