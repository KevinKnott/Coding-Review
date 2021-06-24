# Split Array Largest Sum: https://leetcode.com/problems/split-array-largest-sum/

# Given an array nums which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays.
# Write an algorithm to minimize the largest sum among these m subarrays.

# This sounds like a sliding window problem or two pointer problem
# Where we create a pointer and and split the two arrays and keep track of the min(max(left, right), result)
# This wont work as m can increase up to len (m)

class Solution:
    def splitArray(self, nums, m):
        result = float('inf')
        left, right = 0, 0

        for num in nums:
            right += num

        # As we move left to right across we remove that value from
        for num in range(0, len(nums) - 1):
            left += num
            right -= num
            result = min(result, max(left, right))

        return result

# So how do we expand this for a more efficient solution? We can take the above and boil it down to a dp problem but it is something quite complicated

    def splitArrayDP(self, nums, m):
        # Potential results
        f = [[float('inf')] * (len(nums) + 1) for _ in range(m+1)]
        # cumulative sum
        sub = [0] * (len(nums) + 2)

        for i in range(len(nums)):
            sub[i + 1] = sub[i] + nums[i]

        f[0][0] = 0

        # We use the same recurence from above but now we have to calculate the largest sum of adding values starting
        # at some point by using the cumulative sum array
        for i in range(1, (len(nums) + 1)):
            for j in range(1, m + 1):
                for k in range(0, i):
                    f[i][j] = min(f[i][j], max(f[k][j-1], sub[i] - sub[k]))

        return f[-1][-1]

# My above code still doesn't quite work so I need to work on it honestly this problem is super fucking unrealistic for interview question

# Score Card
# Did I need hints? Y
# Did you finish within 30 min? I don't even understand this problem so it would take a year in a real setting to do this
# Was the solution optimal? My dp doesn't even work so no idea
# Were there any bugs? Yeah the whole thing
# 1 1 1 1 =1
