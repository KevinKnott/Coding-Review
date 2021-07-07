# Split Array Largest Sum: https://leetcode.com/problems/split-array-largest-sum/

# Given an array nums which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays.
# Write an algorithm to minimize the largest sum among these m subarrays.

# This problem is rather difficult what we need to do is simulate finding the max value of all non-empty continuous sub-arrays after m splits
# This is easy in the base case but will get more difficult with more splits as we have more options to consider

# If we take the example 7 2 5 10 8 and m = 2 we can do the following
# Create a summation array for m = 1 as there is no split and the max value will be the total sum
# Then we can introduce a split and compare it to the previous amount of splits

# we need to loop adding the split as we go across the array
# then we need to find the summation on both sides and take the max then compare it to the minimum of the level or previous level

# Sum       [7 9 14 24 32]                  m = 3 will be the same as the left but adding in a new split on the right piece and then adding that to the other side
#           [7] [2 5 10 8]                       [7] [2][5 10 8]
#            7    32 - 7                         [7 2] [5] [10 8]           As you can see we can calculate the left side as it is already calculated in the previous step
#           [7 2 ] [5 10 8]
#              9      23
#
#  Once we have add a split take the min max we see then if we add aditional splits we already have the max split adding at each point
#  and we simply need to consider only a new split within these splits

import math


class Solution:
    def splitArray(self, nums, m: int) -> int:
        curSum = 0
        sumArr = []
        for num in nums:
            curSum += num
            sumArr.append(curSum)

        # The above creates our base case
        if m == 1:
            return sumArr[-1]

        # Create DP we need only the previous sums (base case) and the newly created base case at every step
        dp = sumArr

        # DP through the above array
        for i in range(1, m):
            # create the new row we will be constructing
            curRow = [math.inf] * len(nums)
            for j in range(1, len(nums)):
                # Now that we are looping through each number we need to consider adding a split at k
                for k in range(i-1, j):
                    # Get the previous result
                    prevVal = dp[k]
                    # Get the current split sum
                    curVal = sumArr[j] - sumArr[k]

                    # Our max will either be the max previous split that we have seen or the cur split
                    maxSeen = max(prevVal, curVal)

                    # Take the actuall min between all previous splits and the one we calculated for adding the a split at k
                    curRow[j] = min(curRow[j], maxSeen)

            # Now we need to update our dp as the next row only needs the current best min max of the split
            dp = curRow

        return dp[-1]

# I know this solution works as I have run through this problem quite a bit.
# However I know that this is not the optimal solution as it runs in an ungodly o(n^2 * m) and o(n * m) but how can we improve on this?
# If we can binary serach through the problem we can try adding more optimal splits than just testing every combination like the above
# this will run in o(nlogn ) and o(n)

# The only problem is how would we appropriately determine the way to move in a binary search? the solution comes down to taking the sum
# from 1 -> max val (as we need to have the max val by itself) and then determine the mid value before we should split and check against
# it by calculating the sum at every point # and keep count of the number of values if the split is less than k we know that the it is
# possible to split that piece up more to reduce this min max sum

    def splitArrayBS(self, nums, m: int) -> int:
        def count(mid, possible):
            # So we need to count the values left to right and if we get to a sum
            # higher than our mid we return
            sub = 1
            curSum = 0
            for num in nums:
                curSum += num
                if curSum > possible:
                    sub += 1
                    # Reset the cur sum as we count across
                    curSum = num

            return sub <= m

        start = max(nums)
        end = 0

        for num in nums:
            end += num

        while start <= end:
            mid = (start + end) // 2

            if count(mid):
                end = mid - 1
            else:
                start = mid + 1

        return start

# This works and actually runs a bit better than I thought because it runs in o(nlog(sum)) and o(1) we keep track of sum with just one var


# Score Card
# Did I need hints? Oh yeah this second solution is kind of crazy and even the initial dp is crazy af
# Did you finish within 30 min? 45
# Was the solution optimal? Yea read comments
# Were there any bugs? None
# 2 2 5 5 = 3.5
