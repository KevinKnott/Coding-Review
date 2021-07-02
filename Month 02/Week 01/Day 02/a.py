# Split Array Largest Sum: https://leetcode.com/problems/split-array-largest-sum/

# Given an array nums which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays.
# Write an algorithm to minimize the largest sum among these m subarrays.

# Let us construct a sum array which will allows us to get the subarray sum at any point
# then we can create a dp array in which we keep the max sum of window size i
# keep increasing window size  as we go up and then find max of each
# When doing this we will need to make sure that we leave m - 1  also

class Solution:
    def splitArray(self, nums, m):
        sum = []
        sum.append(nums[0])
        for i in range(1, len(nums)):
            sum.append(sum[-1] + nums[i])

        if m == 1:
            return sum[-1]

        # dp(m, len(nums)) = min of max( sub sum when splitting num[:j] into m groups)
        # because [7,2,5,10]  [8] = [7][2,5,10] , [7,2][5,10] or [7,2,5][10] or the remaining subarray [8]
        #  so the result would be max(3 sub problems or 8)
        # you can continue this pattern adding one more to the last subarray every iteration
        # Techincally the base case is f(1, len(nums)) because that is the cum sum
        dp = sum

        # So we neeed to loop for adding another value to split
        for i in range(1, m):
            curRow = [float('inf')] * len(nums)
            for j in range(1, len(nums)):
                for k in range(i-1, j):
                    # So this is the minimum of the previous split or the smallest of the range we have seen (we calc every size of k see line 22)
                    # Split by p
                    # Smallest seen in previous iteration of so if m = 2 for above example and j = 4
                    # [7], [2, 5] or [7, 2], [5] so the previous should be 7 (as we took max of that row)
                    # This is the left side which we already calculated max of smallest
                    left = dp[k]
                    # Move split left -> right from i - 1 to len(nums)
                    right = sum[j] - sum[k]
                    # Take new max split from right or keep the smallest split we have seen previously
                    maxSeen = max(left, right)
                    # Find the min between all sums we have seen before or the new split
                    curRow[j] = min(curRow[j], maxSeen)
            # Update the next row to do math based of prev row ()
            dp = curRow

        return dp[-1]

# So this solution works! It is a little bit complicated and took me quite some time to understand
# However it isn't the optimal solution as this runs in o(mn^2) and o(mn) space
# After looking at the solution it looks like we can decide which side to split by doing a little bit of smart spliting
# The math above remains the same except we need to split whichever side has the largest sum

# Checkout https://www.youtube.com/watch?v=FrZ_yV2TfLE for the detailed explanation this is kind of ridiculously hard

# Score Card
# Did I need hints? Y
# Did you finish within 30 min? 2 hours
# Was the solution optimal? See my blurb from above
# Were there any bugs? While calculating the dp I kept ignoring the fact that we need to check previous values even
# though I knew this was a dp
# 1 1 2 3 = 2.75
