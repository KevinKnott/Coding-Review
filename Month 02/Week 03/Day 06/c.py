# Trapping Rain Water: https://leetcode.com/problems/trapping-rain-water/

# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

# My initial though for solving this problem is by keeping a stack of indicies and then when we see a value higher than the stack
# We can check for adding in all the water between this new high and whatever is on the left. This is kind of tricky as we are actually
# needing to determine how highe the water is to the next step down as well as if ther are any steps down like 3 2 1 3

class Solution:
    def trap(self, height) -> int:
        stack = []
        result = 0

        for i in range(len(height)):
            while len(stack) != 0 and height[stack[-1]] < height[i]:
                # So we need to see if there is a step down
                top = stack.pop()

                # and make sure that there is something to the left
                # that is high enough to capture water
                if len(stack) > 0:
                    # Get width
                    curWidth = i - stack[-1] - 1
                    # Our height is whatever the lowest of the left bound or right bound
                    # minus the distance to the top of the bottom which we popped off
                    curHeight = min(height[stack[-1]], height[i]) - height[top]

                    result += curHeight * curWidth

            stack.append(i)

        return result

# So the above works and runs in o(N) and uses o(N) space in the worst case scenario
# The question is can we do better? The answer is actually yes as we can simply move
# Two pointers together slowly and add anything that is bounded on the side we have
# already parsed. Unless we see a new a new high value then we know water won't
# be at that spot

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

# The above works and runs in the same O(n) and uses o(1) space

# Score Card
# Did I need hints? Nope
# Did you finish within 30 min? 25
# Was the solution optimal? Oh yeah
# Were there any bugs? None
# 5 5 5 5 = 5
