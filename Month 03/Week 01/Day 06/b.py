# Find the Duplicate Number: https://leetcode.com/problems/find-the-duplicate-number/

# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
# There is only one repeated number in nums, return this repeated number.
# You must solve the problem without modifying the array nums and uses only constant extra space.

# So the naive solution to this problem since we have to use constant space is to simply use two pointers
# and do an n^2 search through the list. We could also probably do some smart sorting as well to check
# in nlogn time but the optimal solution is just taking the numbers and converting them to be negative if seen
# so if we go to check a number and it is already negative that is obviously the duplicate and we can return
# this is an o(n) approach

class Solution:
    def findDuplicate(self, nums) -> int:
        for i in range(len(nums)):
            # The index should be a positive number always
            potentiallySeen = abs(nums[i]) - 1

            if nums[potentiallySeen] < 0:
                return potentiallySeen + 1

            nums[potentiallySeen] *= -1

        return -1

# I am crusing through this problem this runs in O(N) and uses O(1)

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 5
# Was the solution optimal? Yuh
# Were there any bugs?  None
# 5 5 5 5 = 5
