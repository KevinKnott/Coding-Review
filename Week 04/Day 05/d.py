# Shortest Subarray with Sum at Least K: https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/

# Return the length of the shortest, non-empty, contiguous subarray of nums with sum at least k.
# If there is no non-empty subarray with sum at least k, return -1.

# I don't think that this is the most optimal solution but we can loop through and find the sum at every point
# then calculate from size 1 to n if we get a sum >= k and then return that result or -1
# The above can actually be done with a sliding window

from collections import deque


class Solution:
    def shortestSubarray(self, nums, k: int) -> int:
        summation = [0]
        for num in nums:
            summation.append(summation[-1] + num)

        q = deque()
        result = float('inf')

        for index, curSum in enumerate(summation):
            # We need the index and the current number

            # If our curSum is smaller that means we have a decreasing value in nums
            # so we should pop of that value
            while q and q[-1][1] >= curSum:
                q.pop()

            # If our curSum - (our optimized sum ) is greater than k
            # Since the start of our q is the point we start summing from and we have a sum more than k
            # we can update result
            while q and curSum - q[0][1] >= k:
                # if our new possible result is smaller than result we can update it
                result = min(index - q[0][0], result)
                # We need to pop off from the left and then our new starting point with be at the
                # beginning this is because we pop off any decreasing values in the loop before
                q.popleft()

            # Always append our values
            q.append([index, curSum])

        return result if result != float('inf') else -1

#  Okay this is slightly more challenging of a problem than I initially thought. Basically we needed
#  to create a sliding window but instead of removing one node at a time on the left to shrink it
#  I optimized it to keep the current index and pop any decreasing values before hand
#  this will run in o(N) for time and space though

# Score Card
# Did I need hints? Yes
# Did you finish within 30 min? 30
# Was the solution optimal? This is optimal ( I think see comment above score line)
# Were there any bugs? Yeah I had a bit of bugs trying to improve the sliding window
# Also I am prettty sure that I can save some space and not optimize the sliding window
# 1 2 4 3 = 2.5
