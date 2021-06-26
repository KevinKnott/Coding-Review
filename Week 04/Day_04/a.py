# Split Array Largest Sum: https://leetcode.com/problems/split-array-largest-sum/

# Given an array nums which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays.
# Write an algorithm to minimize the largest sum among these m subarrays.

# So this solution will need to take advantage of a few things the main one being that a cumalitive sum of x can be retreived by getting the
# cumSum and subtracting the sub result out so  for 7 2 5 10 8 we would have an array of the sum 7 9 14 24 32 and at index 2
# the value would be 32 - 14 (sum[2]) = 18

# This means that at any point we can get the sub array pieces right basically this means that we need to create a for loop
# in which we increase the size of the subarrays to expand across all variations

# We can track this with a dp array in which we build the min maxed value for 1 to i where i is the size of largets possible subarray

class Solution:
    def splitArray(self, nums, m):
        ourSum = [0]
        for num in nums:
            ourSum.append(ourSum[-1] + num)

        # Since we want to know the minimized max we need to set our dp to infinity minus the starting point
        dp = [[float('inf')] * (len(nums) + 1) for _ in range(m+1)]
        dp[0][0] = 0

        # Loop through the whole dp aray
        i = 1
        while i <= len(nums):
            # For every possible size of j from 1 - m go across
            j = 1
            while j <= m:
                # Once we have the current max we need to check the previous sections max to update our dp table
                # It equals the minimum of what is in the dp array or the max of the cur sumation (sum[-1] - sum[i])
                # It needs to check every subarray from 0 to the current row
                k = 0
                while k < i:
                    # For visibility
                    print(i, j, k)
                    currentSolution = dp[i][j]
                    potentialSum = ourSum[i] - ourSum[k]
                    # This is the previous potential splitting
                    lastSeenSolution = dp[k][j-1]
                    dp[i][j] = min(currentSolution, max(
                        lastSeenSolution, potentialSum))
                    if k == 0:
                        k += 1
                    else:
                        k += k
                j += j
            i += i

        return dp[len(nums)][m]


# Unfortunately there is still a bug within this code but I am not sure what it is yet but my time is up
# This isn't even the most optimal solution as it runs in o(n^2 * m) time and o(n * m) space as we compute every possible solution until we find k

# Apparently the optimized solution requires you to have a binary search which I haven't had the chance to read throught this problem enough times to understand

# Also during review of this problem the following adjustments were needed we need to loop over the array backwards in order to succesfully solve this problem:
        ourSum = [0]
        for num in nums:
            ourSum.append(ourSum[-1] + num)

        # Since we want to know the minimized max we need to set our dp to infinity minus the starting point
        dp = [[float('inf')] * (len(nums) + 1) for _ in range(m+1)]
        dp[0][0] = 0

        # Loop through the whole dp aray
        for i in range(1,  m+1):
            # For every possible size of j from 1 - m go across
            for j in range(1, (len(nums)+1)):
                # Once we have the current max we need to check the previous sections max to update our dp table
                # It equals the minimum of what is in the dp array or the max of the cur sumation (sum[-1] - sum[i])
                # It needs to check every subarray from 0 to the current row
                for k in range(j-1, -1, -1):
                    # For visibility
                    print(i, j, k)
                    currentSolution = dp[i][j]
                    potentialSum = ourSum[j] - ourSum[k]
                    # This is the previous potential splitting
                    lastSeenSolution = dp[i-1][k]
                    dp[i][j] = min(currentSolution, max(
                        lastSeenSolution, potentialSum))

                    if potentialSum > dp[i-1][k]:
                        break

        return dp[-1][-1]


A = Solution()
print(A.splitArray([7, 2, 5, 10, 8], 2))

# Score Card
# Did I need hints? No although i did look at the optimal solution even though I didn't get to it
# Did you finish within 30 min? N
# Was the solution optimal? See above
# Were there any bugs? I listed bugs in the above code
#  1 1 1 1 = 1
