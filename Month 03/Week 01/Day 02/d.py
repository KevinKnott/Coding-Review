# Shortest Subarray with Sum at Least K: https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/

# Given an integer array nums and an integer k, return the length of the shortest non-empty subarray of nums with a sum of at least k. If there is no such subarray, return -1.
# A subarray is a contiguous part of an array.

# So this problem is actually quite challenging but it really is just a sliding window problem. The tricky part is that we actually have the possibilities of cycles
# so instead of just removing values from left to right we need to actually keep track of the next possible solution in a q so we can skip false negatives that
# would expand our window instead of continuing to check


from collections import deque


class Solution:
    def shortestSubarray(self, nums, k: int) -> int:
        # The trick to this problem is actually computing the prefix sum
        # so we can quickly find any subarray sum from i to j
        prefixSum = [0]
        for num in nums:
            prefixSum.append(prefixSum[-1] + num)

        q = deque()
        result = float('inf')
        for right in range(len(prefixSum)):

            # Check if we have a negative cycle by checking the curSum
            while q and prefixSum[q[-1]] > prefixSum[right]:
                q.pop()

            # as we expand we need to check if our sum is over k and if it is a smaller result
            # keep it and reduce our window
            while q and prefixSum[right] - prefixSum[q[0]] >= k:
                # So here we check if the current result or the distance from left -> right is smaller
                # and pop off the first element to shrink our window
                result = min(result, right - q.popleft())

            # As always we need to add every possible element
            q.append(right)

        return -1 if result == float('inf') else result


# This problem is actually quite tricky if I do say so myself. Luckily since you can quickly compute
# the sum with a prefix sum array we can quickly reduce this problem to a sliding window problem.
# After that we just have to be careful of adding a negative cycle. Also we have to be sure to add
# a 0 to the prefix sum just in case the the first index is the left so we don't skip any possible
# results

# Score Card
# Did I need hints? Yea
# Did you finish within 30 min? 25
# Was the solution optimal? This is optimal
# Were there any bugs? Yeah I accidently made the result - inf instead of inf
# 4 5 5 4 = 4.5
