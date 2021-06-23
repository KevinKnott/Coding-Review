#  Subarray Sum Equals K: https://leetcode.com/problems/subarray-sum-equals-k/
#  Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.
class Solution:
    def subarraySum(self, nums, k):
        count = 0

        for index in range(len(nums)):
            sum = 0

            for j in range(index, len(nums)):
                sum += nums[j]

                if sum == k:
                    count += 1

        return count

# This works however is it optimal? Definitely not can we improve it? Instead of restarting and going across
# we can simply create a hash table and check difference in sum - k == 0 as each location will store the cum sum

    def subarraySum(self, nums, k):
        count, sum = 0, 0

        # Create a dictionary of values that correspond to the cumulative sum so we can check if the current
        # sum - k == a value within our dictionary (adding 0 because k - 0 = k so we need to have 0 as a potential result of count 1)
        seen = {}
        seen[0] = 1

        for num in nums:
            sum += num

            # Check if the difference in the cumaltive sum  now  - k is in count as we will know there is a dif of size k
            # For example in the array     1 2 1 3
            # we have a cumulative array   1 3 4 7
            # So if k = 3 then we can see two places where sum -k is in cumalitive for 1,3 and 4,7 so we have an output of2
            if seen[sum - k]:
                count += seen[sum - k]

            # Return either the sum or a default value of 0
            # We need to the current sum so we can check for it but the total number of possibilites may be greater than 1
            # as we could have values that loop are positive and negative and could make multiple answers
            seen[num] = seen.get(sum, 0) + 1


# Score Card
# Did I need hints? Y
# Did you finish within 30 min? Y
# Was the solution optimal? Y
# Were there any bugs? N
#  2 4 3 1 = 2.5
