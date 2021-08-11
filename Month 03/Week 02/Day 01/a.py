# Shortest Subarray with Sum at Least K: https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/

# Given an integer array nums and an integer k, return the length of the shortest non-empty subarray of nums with a sum of at least k. If there is no such subarray, return -1.
# A subarray is a contiguous part of an array

# In this problem our basic solution would be to go through every possible n^2 possibility of [i][j] subarrays. The question is can we do better?
# I believe the answer should be yes as we can probably calculate the subarray as we go across with a sliding window. To do this we will
# add numbers to the right until we reach k then we will try to remove every possible left until we can no longer make k. Then using a min var
# we can keep track of the result

# Unfortunately we can't really use a regular sliding window as we can have negative numbers that make the value less than k
# but there is still a shorter possible solution to the right for example 1 1 1 1 -3 1 1 4 5 2


from collections import deque


class Solution:
    def shortestSubarray(self, nums, k):
        # To fix this the negative cycle problem we will need to use a deque
        # to move through the possible solutions where we have removed all
        # negative numbers from the possible solutions in the q
        q = deque()
        result = float('inf')

        # we will also need a prefix sum which includes 0 in the case the total uses the first element
        # this prefix will let us skip over negative numbers and get any instantaneous subarray sum
        prefix = [0]

        for num in nums:
            prefix.append(prefix[-1] + num)

        for right in range(len(prefix)):
            # We remove any number that is less than our current prefix sum
            # as we know that means the number added a negative cycle
            while len(q) and prefix[q[-1]] > prefix[right]:
                q.pop()

            while len(q) > 0 and prefix[right] - prefix[q[0]] >= k:
                result = min(result, right - q.popleft())

            q.append(right)

        return -1 if result == float('inf') else result


# The above works pretty well although it takes some thinking about to figure out the optimization of skipping over the negative numbers by
# popping and checking result on the farthest left of the window

# This runs in O(N) and uses potentially O(N) space

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 20
# Was the solution optimal? Oh yea
# Were there any bugs? Nope
# 5 5 5 5 = 5
