# Search in Rotated Sorted Array: https://leetcode.com/problems/search-in-rotated-sorted-array/

# There is an integer array nums sorted in ascending order (with distinct values).
# Prior to being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
# Given the array nums after the rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
# You must write an algorithm with O(log n) runtime complexity.

from types import List

# The first solution that comes to mind is doing a linear scan to find where the values swap which would be the easy solution.
# however this would not be optimal as we know this list is still sorted and if we know that a list is sorted we know
# that we can apply a binary search. The difficulty in this problem is making sure that you are searching down the right
# half. To do this we will find a mid and compare that the values are sorted from lo -> mid and if it is we know that
# we can proceed like normal and if it isn't we can do the opposite


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Not really needed
        # if len(nums) == 0:
        #     return -1

        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2

            if nums[mid] == target:
                return mid

            # Properly sorted
            if nums[lo] <= nums[mid]:
                # Number between lo and mid search that segment
                if nums[lo] <= target and target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            # Not properly sorted
            else:
                if target <= nums[hi] and target > nums[mid]:
                    lo = mid + 1
                else:
                    hi = mid - 1

        return -1

# In this problem we can break down the flow especially if we look at an example or two
# this runs in o(logn) and uses O(1) space

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 9
# Was the solution optimal? Y
# Were there any bugs? N
# 5 5 5 5 = 5
