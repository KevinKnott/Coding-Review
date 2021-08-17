# Search in Rotated Sorted Array: https://leetcode.com/problems/search-in-rotated-sorted-array/

# There is an integer array nums sorted in ascending order (with distinct values).
# Prior to being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
# Given the array nums after the rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
# You must write an algorithm with O(log n) runtime complexity.

# This is a basic binary search the only difference is that we need to check if the values are sorted from high to mid so that we know wether to follow the traditional patern
# or to traverse the other way as the shift occurs on the other side

class Solution:
    def search(self, nums, target: int) -> int:
        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2

            if nums[mid] == target:
                return mid
            else:

                # Is it properly sorted?
                if nums[mid] >= nums[lo]:
                    # Now since we know where it is supposed to be we need to check if it can be here
                    if target >= nums[lo] and target <= nums[mid]:
                        hi = mid - 1
                    else:
                        lo = mid + 1
                else:
                    if target <= nums[hi] and target > nums[mid]:
                        lo = mid + 1
                    else:
                        hi = mid - 1

        return -1

# So this is pretty standard the only weird hiccup is finding whether or not you have a sorted segment or not
# this runs in o(logn) and O(1)

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 10
# Was the solution optimal? This is optimal
# Were there any bugs? No
# 5 5 5 5 = 5
