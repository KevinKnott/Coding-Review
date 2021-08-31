# Shortest Subarray with Sum at Least K: https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/

# Given an integer array nums and an integer k, return the length of the shortest non-empty subarray of nums with a sum of at least k. If there is no such subarray, return -1.
# A subarray is a contiguous part of an array.

from collections import deque
from types import List

# This problem can be quite difficult as we can try and o(N^2) manually check between every i and j but that is super efficient
# to optimize this we can take the prefix sum to help calculate at every point we can create a sliding window that checks
# if we can reach the subarray sum of k in a possible o(N) solution


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)

        result = float('inf')
        q = deque()

        for right in range(len(prefix)):

            # Remove negative cycles aka if the cur prefix is smaller than the most
            # recent on q
            while q and prefix[q[-1]] > prefix[right]:
                q.pop()

            while q and prefix[right] - prefix[q[0]] >= k:
                result = min(result, right - q.popleft())

            q.append(right)

        return result if result != float('inf') else -1

# Boom we are donezo
# This runs in O(N) time and space

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 17
# Was the solution optimal? This is optimal
# Were there any bugs? No
#  5 5 5 5 = 5
