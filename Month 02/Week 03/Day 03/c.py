# Search in Rotated Sorted Array: https://leetcode.com/problems/search-in-rotated-sorted-array/

# There is an integer array nums sorted in ascending order (with distinct values).
# Prior to being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
# Given the array nums after the rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
# You must write an algorithm with O(log n) runtime complexity.

# In this problem we are asked to find the value in a unique and sorted array which is simple enough (and adding multiple is simply adding one more line)
# The brute force/ naive solution is to do a linear scan which runs in o(N) with o(1) space which isn't bad but we can do better
# this is because we can do a binary search on any sorted values. Even if it is rotated to do this all we have to do is the usual process
# but if the value on the left > mid we know we are in the swapped part so we simply change how we move down the start/end

class Solution:
    def search(self, nums, target: int) -> int:
        start, end = 0, len(nums) - 1

        while start <= end:
            mid = start + (end - start) // 2

            if target == nums[mid]:
                return mid
            # We have two options Incorrectly sorted
            elif nums[mid] >= nums[start]:
                # Again we have to make sure it is sorted here as well
                if target >= nums[start] and target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1

            # Correctly sorted
            else:
                # Again we have to make sure it is sorted here as well
                if target <= nums[end] and target > nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1

        return -1

# This problem was simple enough as it is just your standard Binary search. The only curiosity is making sure that
# You are searching the right path by considering whether or not you are in a sorted or unsorted section between start -> end and start -> mid
# This will run in o(logn) time and o(1) space

# Score Card
# Did I need hints? Yes I forgot that we needed to check to make sure that there wasn't a split on either side of mid
# Did you finish within 30 min? 15
# Was the solution optimal? Yee
# Were there any bugs? Yup see the hints piece
# 4 5 5 4 = 4.5
