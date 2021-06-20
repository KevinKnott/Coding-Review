# Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts: https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/

# You are given a rectangular cake of size h x w and two arrays of integers horizontalCuts and verticalCuts where:

#     horizontalCuts[i] is the distance from the top of the rectangular cake to the ith horizontal cut and similarly, and
#     verticalCuts[j] is the distance from the left of the rectangular cake to the jth vertical cut.

# Return the maximum area of a piece of cake after you cut at each horizontal and vertical position provided in the arrays horizontalCuts and verticalCuts. Since the answer can be a large number, return this modulo 109 + 7.

# We need to check the max size between cuts so if we want to do this we need to sort cuts and take the distance between cuts horizontally and multiply them by thee vertical cuts to get  a result
# Of course keeping the modulo

class Solution:
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        horizontalCuts.sort()
        verticalCuts.sort()

        mod = (10 ** 9) + 7

        maxHeight = -float('inf')
        maxWidth = -float('inf')
        height = 0
        width = 0
        for i in range(len(horizontalCuts)):
            maxHeight = max(horizontalCuts[i]-height, maxHeight) % mod
            height = horizontalCuts[i]

        maxHeight = max(h - height, maxHeight) % mod

        for i in range(len(verticalCuts)):
            maxWidth = max(verticalCuts[i] - width, maxWidth) % mod
            width = verticalCuts[i]

        maxWidth = max(w - width, maxWidth) % mod

        return (maxWidth * maxHeight) % mod

# It looks like my solution works but is it optimal?
#  The current solution is o(nlogn) time and o(1) space (depending on the sort algo)
#  I would say that this would be pretty optimal although you might be able improve this
# with some sort of a bucketing algorithm that was mentioned in comments

# Score Card
# Did I need hints? N
# Did you finish within 30 min? Y
# Was the solution optimal? Yup
# Were there any bugs? N
#  4 5 3 5 = 4.25
