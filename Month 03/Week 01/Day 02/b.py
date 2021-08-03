# Search in Rotated Sorted Array: https://leetcode.com/problems/search-in-rotated-sorted-array/

# There is an integer array nums sorted in ascending order (with distinct values).
# Prior to being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
# Given the array nums after the rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
# You must write an algorithm with O(log n) runtime complexity.

# So this problem seems really complicated at first but since we know the values are sorted we have the easiest solution being a binary search
# normally the rotation would mess this up but we can simply check whether or not the values are sorted in the range we need to look at
# and determing if we need to search to the left half or the right half

# Also the worst case we can do for this problem is still a linear scan so there is that


class Solution:
    def search(self, nums, target):
        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2

            if target == nums[mid]:
                return mid
            else:
                # So if the number is below the value in the mid
                # we can check if we have sorted numbers from low to mid because it should be on the left
                # if it is sorted we go to the left
                if nums[mid] >= nums[lo]:
                    # Again we have to make sure it is sorted here as well
                    if target >= nums[lo] and target < nums[mid]:
                        hi = mid - 1
                    else:
                        lo = mid + 1

                # Correctly sorted
                else:
                    # Again we have to make sure it is sorted here as well
                    if target <= nums[hi] and target > nums[mid]:
                        lo = mid + 1
                    else:
                        hi = mid - 1

        return -1

# This is optimal and runs in O(nlogn) and o(1)

# Score Card
# Did I need hints? Nope
# Did you finish within 30 min? 20
# Was the solution optimal? Yeee
# Were there any bugs? I initially was searching for if the value was hi or lower than mid
# because I forgot that I need to check for the sorted order first
# 5 5 5 4 = 4.75
