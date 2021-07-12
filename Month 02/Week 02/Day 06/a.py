# Trapping Rain Water: https://leetcode.com/problems/trapping-rain-water/

# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

# In this problem we can utilize a stack to append the left barrier as we move across the array when we meet a right barrier that is also
# of equal size or higher we can solve how much water can go between them.  This is actually kind of tricky as we need to know if there are
# any smaller blocks within this bigger bound


class Solution:
    def trap(self, height) -> int:
        if len(height) == 0:
            return 0

        stack = []
        water = 0

        for i in range(len(height)):

            # Check if the current height is >= to the left bound (or if the stack is empty skip)
            while len(stack) != 0 and height[stack[-1]] < height[i]:
                # So if there is something bounded on the right and left we need to check if water can go in between
                top = stack.pop()

                # get the width of water
                if len(stack) != 0:
                    # get the width of water
                    distance = i - stack[-1] - 1
                    # The above is our current spot minus the new left bound
                    # get the depth of water
                    trappedHeight = min(
                        height[i], height[stack[-1]]) - height[top]
                    # The above will be the minimum of the left or right height plus the distance from 0 to the top
                    # because we may have a case like 4 1 2 3 where the water cant fill straight to the bottom

                    # append to result
                    water += distance * trappedHeight

            # We have to add on every single thing!
            stack.append(i)

        return water


# So I have found out the above works and it is pretty smart it runs in o(N) time and o(N) space which is better than the
# brute force o(n^2) solution that I orignally thought of. Basically this runs on the principle that any time you see
# a increase on the right we try to automatically fill it up so if there is a case where we have 3 2 1 2 3 we can
# start adding water ourselves at the lowest point and fill it to the top so we don't have to do any weird calcs
#
#
# The question is can we do better? I think that it is quite possible that we can do better as I know that we could
# if we look at the solution we are just calculating if there is a left and right that allows us to be bounded
# so if we took a loop and pushed in from either side always evaluating the highest number we could probably solve
# as we go by storing the highest on left and right and then simply filling to the bottom

    def trap(self, height) -> int:
        water = 0
        left, right = 0, len(height) - 1
        maxLeft, maxRight = 0, 0

        while left <= right:
            # So we need to check which side is higer to move down
            if height[left] <= height[right]:
                if height[left] >= maxLeft:
                    maxLeft = height[left]
                else:
                    water += maxLeft - height[left]

                left += 1
            else:
                # We have two option if we have a new highest just update the highest
                if height[right] >= maxRight:
                    maxRight = height[right]
                # otherwise we can add water bounded by left max/right max
                else:
                    # Take the lowest bound and multiply to current depth
                    water += maxRight - height[right]

                right -= 1

        return water

# This runs in o(n) and o(1)!

# Score Card
# Did I need hints? Yup
# Did you finish within 30 min? N (45 or so)
# Was the solution optimal? Yup the last solution was optimal but hard to figure out
# Were there any bugs? Nope
# 3 2 5 5 = 3.75
