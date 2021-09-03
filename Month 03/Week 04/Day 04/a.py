# Trapping Rain Water: https://leetcode.com/problems/trapping-rain-water/

# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

from types import List


# For this problem we need to traverse across the array and keep track of the values to the left which are less than or equal to the cur
# this way we can quickly see where water may fill in the valley. Any point that is lower we can check what the next item passed it to
# the left is and if then if it is higher we can do the math to fill in the valley

class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        total = 0

        for right in range(len(height)):

            while stack and height[right] >= height[stack[-1]]:
                valley = stack.pop()

                if stack:
                    left = stack[-1]
                    valleyHeight = min(
                        height[left], height[right]) - height[valley]
                    valleyWidth = right - left - 1

                    total += valleyHeight * valleyWidth

            stack.append(right)

        return total

# This is the first solution 7 min it runs in O(N) time and space and is all around pretty good
# Can we do better? I think so in this problem we are parsing with a stack but honestly
# by using a maxLeft and maxRight we can skip over using a stack.
    def trap(self, height: List[int]) -> int:
        maxLeft, maxRight, total = 0, 0, 0
        left, right = 0, len(height) - 1

        while left < right:
            if height[left] < height[right]:
                if maxLeft < height[left]:
                    maxLeft = height[left]
                else:
                    total += maxLeft - height[left]

                left += 1
            else:
                if maxRight < height[right]:
                    maxRight = height[right]
                else:
                    total += maxRight - height[right]

                right -= 1

        return total


# Oh yeah this is the one!
# It runs in O(N) but uses only O(1) space


# Score Card
# Did I need hints? N
# Did you finish within 30 min? 12
# Was the solution optimal? Y
# Were there any bugs? N
# 5 5 5 5 = 5
