# Search in Rotated Sorted Array: https://leetcode.com/problems/search-in-rotated-sorted-array/

# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
# Given the array nums after the rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
# You must write an algorithm with O(log n) runtime complexity.

# Okay the simplest solution to this problem is to do a simple linear search which would take o(n) and is trivial
# so to improve on this normally what we do is a binary search because it is shifted there is probably a slight
# difference

# Actually you can quickly determine if you are including a part of the switch by comparing the first value in you search
# to the middle if the start is < mid point then you know it is sorted and you can continually normally
# otherwise y ou know that there was a switch and you need to go the opposite direction

class Solution:
    def search(self, nums, target):
        start, end = 0, len(nums) - 1

        while start <= end:
            mid = start + (end - start) // 2

            if nums[mid] == target:
                return mid

            # if we have a normal bs then we know that
            elif nums[mid] >= nums[start]:
                # Check if our target is between start and mid
                # Or if it is in the previous section as we rotated across
                if target >= nums[start] and target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            # other wise we know we need to search in rotated across area
            else:
                if target <= nums[end] and target > nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1

        # if we didn't find the value return -1
        return -1

# This problem seemed really hard at first but honestly since we know that it is a normal binary search if we look at the start and mid point we can
# quickly revert this to an almost normal implementation of the binary search algo

# This should run in o(log(n)) time and o(1) space as we are cutting the array in half every time and storing no information outside of that array

# Score Card
# Did I need hints? Slightly I kept messing up the moving of the start and end points
# Did you finish within 30 min? 22
# Was the solution optimal? Yup this runs in o(n+m) time in worst case and uses o(1) space
# Were there any bugs? See my hints
# 4 4 5 3 = 4
