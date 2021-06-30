# Trapping Rain Water: https://leetcode.com/problems/trapping-rain-water/

# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.


# The brute force method I think of is move across left to right and add 1 for each unit you go agross that is bounded on the left and right

# So my initial thought is again to move across the value adding things onto a stack until you find a value that is >= to it
# then you pop off the prev values

class Solution:
    def trap(self, height) -> int:
        if len(height) == 0:
            return 0

        result = 0
        # Keep track of left and right like a sliding window
        stack = []

        for current in range(len(height)):
            while not len(stack) == 0 and height[current] > height[stack[-1]]:
                top = stack.pop()
                # Do we have water above us?

                if not len(stack) == 0:
                    distance = current - stack[-1] - 1
                    boundedHeight = min(
                        height[current], height[stack[-1]]) - height[top]
                    result += boundedHeight * (distance)
            stack.append(current)

        return result

# The above code works you simply do what I mentioned in the steps above except that you need to check for how far down it is until you reach the basin
# hence why you check for the bounded height in the above code.

# This code runs in o(n) time and space! Is it optimal though? Unfortunately not you can do the same thing I did above with 2 pointers going
# and seeing where there are bounds and add them up that way it seems tricky but I didn't have time to implement it.

# Score Card
# Did I need hints? Yes (for optimal)
# Did you finish within 30 min? 30
# Was the solution optimal? See above
# Were there any bugs? None
# 3 2 3 3 = 2.75
