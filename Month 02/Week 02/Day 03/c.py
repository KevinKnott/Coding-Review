# Shortest Subarray with Sum at Least K: https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/

# Return the length of the shortest, non-empty, contiguous subarray of nums with sum at least k.
# If there is no non-empty subarray with sum at least k, return -1.

# The brute force is to use a n^2 loop and check every posible for the shortest len
# buuuut since we know that we can only have positive k we can do an o(n) scan
# using a sweet sliding window

from collections import deque


class Solution:
    def shortestSubarray(self, nums, k: int) -> int:
        result = float('inf')
        curSum, left = 0, 0

        for right in range(len(nums)):
            curSum += nums[right]

            # If we get to the popping condition
            while curSum >= k:
                # Check for best result
                result = min((right - left) + 1, result)

                # Pop off left
                curSum -= nums[left]
                left += 1

        return -1 if result == float('inf') else result

# So the above doesn't work as we might have a potential spot where we need to keep decreasing the value
# in the case of negative numbers so we need to modify the above to keep track any spot where we see
# potential sum > k

    def shortestSubarray(self, nums, k: int) -> int:
        # Create a sum array that takes a sum at a given spot
        # So we can dynamically generate sum of i to j
        # Also we start the subarray sum with 0 as we want to see if the first
        # element will satisfy the condition!
        summation = [0]
        for i in range(len(nums)):
            summation.append(summation[-1] + nums[i])

        result = float('inf')
        q = deque()

        curSum = 0

        # Instead of looping over our nums loop over our summation
        for i, curSum in enumerate(summation):

            # Close the window if we have found any result that is negative
            while q and q[-1][1] >= curSum:
                q.pop()

            # At this point we need to check all possible spots in q where we have a potential
            # to get over k from any spot we have seen
            while q and curSum - q[0][1] >= k:
                result = min(i - q[0][0], result)
                q.popleft()

            # always add current value into sliding window
            q.append([i, curSum])

        return -1 if result == float('inf') else result

# This second piece is almost identical to the one above except it handles negative numbers by queuing the starting positon
# it runs in o(n) time and space

# Score Card
# Did I need hints? Yes I forgot about negative numbers
# Did you finish within 30 min? 30
# Was the solution optimal? This should be optimal but the discussions talk about a more efficient solution
# Were there any bugs? see negative bug
# 3 3 4 4 = 3.5
