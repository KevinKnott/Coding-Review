# Trapping Rain Water: https://leetcode.com/problems/trapping-rain-water/

# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

# So this is kind of a super tricky problem basically what we have is a problem in which we need to compare two pointers left and right
# and find out if these bounds are high enough to have water in them. That being said to try and evaluate the difference between each level
# is quite difficult so I think that the optimal solution would use a stack to keep the left and then you just calc the difference in height
# and find the distance between the current right and the last thing on the stack.

class Solution:
    def trap(self, height) -> int:
        stack = []
        result = 0

        for right in range(len(height)):
            while stack and height[stack[-1]] <= height[right]:
                middle = stack.pop()

                # It must the middle must be bound on the left
                if stack:
                    left = stack[-1]
                    bounded = min(height[left], height[right]) - height[middle]
                    result += bounded * (right - left - 1)

            stack.append(right)

        return result

# Oh yeah I crushed this first piece it runs in O(N) and uses O(N) as well. 10 min
# The question is can we do better and the answer is yes basically we can do the above
# by using two pointers and keeping track of the bounds of left and right by always moving left or right based on whichever one has the smaller height
# then we do the same calc as bounded from that node unless it is a new high bound

    def trap(self, height) -> int:
        left, right = 0, len(height) - 1
        leftMax, rightMax = 0, 0
        result = 0

        while left <= right:
            if height[left] < height[right]:
                if height[left] > leftMax:
                    leftMax = height[left]
                else:
                    result += leftMax - height[left]
                left += 1
            else:
                if height[right] > rightMax:
                    rightMax = height[right]
                else:
                    result += rightMax - height[right]

                right -= 1

        return result

# Done this runs in O(N) but uses O(1) time


# Score Card
# Did I need hints? N
# Did you finish within 30 min? 20 (10 for each solution)
# Was the solution optimal?Y
# Were there any bugs? N
# 5 5 5 5 = 5
