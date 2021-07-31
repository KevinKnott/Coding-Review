# Subarray Sum Equals K: https://leetcode.com/problems/subarray-sum-equals-k/

# Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

# This problem is quite tricky as we would have to loop through n^2 times and simply try ever possibility
# That isn't exactly optimal as we are comparing lots of numbers  multiple times but by using a hashmap
# we can see if there is a sum that is k behind the current sum we know that there is a possible solution


class Solution:
    def subarraySum(self, nums, k: int) -> int:
        count, curSum = 0, 0
        possibleSums = {}
        # We need to add 0 as a sum of 1 so that we can solve any subarray that starts from 0
        # The 1 stands for the fact that we have 1 solution that starts at 0
        possibleSums[0] = 1

        for num in nums:
            curSum += num

            if curSum - k in possibleSums:
                # It is possible to have cycles so we can increase the dict values for the correct result
                count += possibleSums[curSum - k]

            # Now we need to update the value to have this prefix sum to return (0 or the seen possible sum) + 1 for our new result
            possibleSums[curSum] = (
                possibleSums[curSum] if curSum in possibleSums else 0) + 1

        return count

# Score Card
# Did I need hints? Yes
# Did you finish within 30 min? 20
# Was the solution optimal? This is optimal for time as it runs in o(N) compared to o(N^2) however it uses o(N) space where the other would use o(1)
# Were there any bugs? None
# 5 5 5 5 = 5
