# Split Array Largest Sum: https://leetcode.com/problems/split-array-largest-sum/

# Given an array nums which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays.
# Write an algorithm to minimize the largest sum among these m subarrays.

# Right of the bat this feels like it will be a dynamic programming problem as I know that we can solve this almost instantaneously for
# m = 1 or m = 2 by using a prefix sum array and then calculating the result as we move the split across the array

# The challenge comes when we get higher than m = 2 as it is harder to calculate!
# So to solve this we simply track the highest value of spliting the previous row and compare that to adding a split
# from k -> j

# 7 2 5 10 8
# Basically we take one number and keep it to the left side and we add a split to every spot to anything to the left
# [7] [2] [5 10 8 ]
# [7] [2 5] [10 8 ]

# After doing each step keep the max at that point or what was before it
# then add another number to the left
# [7 2 ] [5] [10 8]


# Continue until you have the highest this is doable as we can take the min maxed value at every step and instantly calculate
# any subarray sum with the prefix sum array


class Solution:
    def splitArray(self, nums, m: int) -> int:
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(prefix[-1] + nums[i])

        # Now that we have our way of finding subarray sums
        # we need to loop through our dp list
        dp = prefix

        # This is having only one split so it is just the sum
        if m == 1:
            return dp[-1]

        # We need to start from m = 2 so we automatically add 0 to the left and start splitting
        # This is basically doing this
        # [7] [2] [5 10 8 ]
        for i in range(1, m):
            # Create the next levels dp
            # as we are updating it as we go
            cur = [float('inf')] * len(nums)
            for j in range(1, len(nums)):
                # We need to loop through the values
                # Adding one number to the left every time
                # Then loop through the rest of the k's
                for k in range(i-1, j):
                    # Now we need to compare the values
                    # prev is the resulting subarray sum from i -> k
                    prev = dp[k]

                    # Our current result is the subaray sum from k -> j
                    curSum = prefix[j] - prefix[k]

                    # Now we are taking the max of these possible answers
                    ourMax = max(prev, curSum)

                    # At this point we need to compare the min of the splits from the previous m or take our new min maxed subarray sum
                    cur[j] = min(cur[j], ourMax)

            # Then we update our cur as we only car about the previous row
            dp = cur

        # The answer is at the last spot
        return dp[-1]


# The above solution works and runs in O(n^2 * m) as we have to compute every possible split by traveling through i-1 -> j at every level
# until we reach m splits  the space it takes is o(n) as we are storing all values prefix sum and then the best possible split at every level

# Can we do better? Actually we can the above is kind of neat but by using a binary search and comparing the best split at every possible
# I don't have time to code it but if you can figure out how many splits you need to make the largest sum you can keep splitting them appart
# more intelligently

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 30
# Was the solution optimal? No the optimal solution is quite complicated as the original solution so I haven't had time to try it
# Were there any bugs? In the above I forgot that I already assume we have covered the case where we have m = 1 and I forgot to skip
# it so I was getting the wrong values
# 5 5 3 4 = 4.25
