# Shortest Subarray with Sum at Least K: https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/

# Return the length of the shortest, non-empty, contiguous subarray of nums with sum at least k.
# If there is no non-empty subarray with sum at least k, return -1.

# This problems brute force solution is to try from every i going through the rest of j indicies until you find the first
# time the subarray sum is > than k and return that value

# My next thought is that we have a sliding window problem but the problem is  for a sliding problem it would end up being
# the same as above as we have a potential for negative numbers and cycles so we need to figure out how to get around these

from collections import deque


class Solution:
    def shortestSubarray(self, nums, k: int) -> int:
        # By using a q to push numbers on we can evaluate multiple different solutions
        # and skip over cycles. Also for this problem we will want to create a prefix sum
        # array to quickly calculate any sum
        prefix = [0]
        for i in range(len(nums)):
            prefix.append(prefix[-1] + nums[i])

        q = deque()
        result = float('inf')

        for right in range(len(prefix)):

            # Remove negative numbers from the stack from the same
            while q and prefix[right] < prefix[q[-1]]:
                q.pop()

            # Check if we have a better solution
            while q and prefix[right] - prefix[q[0]] >= k:
                result = min(result, right - q.popleft())

            # Always add the value onto our sliding window
            q.append(right)

        return -1 if result == float('inf') else result

# This problem requires you to be quiet clever with your slidding window
# You have to consider multiple cases at every value from the right

# Score Card
# Did I need hints? Yes
# Did you finish within 30 min? 15 min
# Was the solution optimal? Y although I messed up the thought process of how to solve the problem
# Were there any bugs?  I tried to move across the nums instead of the prefix array at first
# which causes a few issues.
# 3 5 5 4 = 4.25
