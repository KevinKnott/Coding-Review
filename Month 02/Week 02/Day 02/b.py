# Subarray Sum Equals K: https://leetcode.com/problems/subarray-sum-equals-k/

# Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

# So my initial thought is that this could be a sliding window problem
# you move left to right across the array adding values in and if you = k increase counter
# if you go over k pop off the left value until you are below
""" 
def subarraySum(self, nums, k: int) -> int:
        count = 0
        curSum = nums[0]
        left = 0

        for right in range(1, len(nums)):
            if curSum == k:
                count += 1
            
            curSum += nums[right]

            while left < right and curSum > k:
                curSum -= nums[left]
                left += 1
            
            
        count += 1 if curSum == k else 0
        return count 
"""

# I just realized that if we do what I said in the above it won't work as we have negative numbers and the breaks sliding windows

# Instead we can create array of the summation then we can check do a n^2 check to determine the sum between i, j and count if it
# equals k


class Solution:
    def subarraySum(self, nums, k: int) -> int:
        prefixSum = [nums[0]]
        count = 0

        for index in range(1, len(nums)):
            prefixSum.append(prefixSum[-1] + nums[index])

        # Now that we have our sum we can compare from 0 -> k 1 -> k etc
        # This is doable as the sum at i -> k is the same as prefixSum[k] -prefixSum[i]
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if prefixSum[j] - prefixSum[i] == k:
                    count += 1

        return count

# Okay so the above works but is it optimal? It runs in o(N^2) and o(N) (or 1 if you worked hard enough)
# So that isn't really optimal the thing is we can solve this in o(n) time and space if we use a hashmap
# and store anytime we have a sum of x and then we later need to find cur sum - k and it is x
# we can increase our count (this can even handle cyclic as in 1, -1, 1, -1)
    def subarraySumOptimal(self, nums, k: int) -> int:
        count, curSum = 0, 0
        ourMap = {}
        ourMap[0] = 1

        for i in range(len(nums)):
            curSum += nums[i]
            if curSum - k in ourMap:
                count += ourMap[curSum - k]

            # Now that we have our potential we need to add the value to our map
            # And either put 1 (as we have a new potential solution) or if we
            # already had a solution put solution + 1
            ourMap[curSum] = (ourMap[curSum] if curSum in ourMap else 0) + 1

        return count

# Score Card
# Did I need hints? Yes (I slightly forgot exactly how the mapping process worked )
# Did you finish within 30 min? 23 min
# Was the solution optimal? Y although I messed up the thought process of how to solve the problem at first
# Were there any bugs?  I didn't really have any bugs
# 3 5 5 5 = 4.5
