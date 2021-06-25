# Merge Sorted Array: https://leetcode.com/problems/merge-sorted-array/

# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

# Array  1 looks like 123450000
# Where we can place values at zero
# To sort this optimally we should start at the back and move from right to left swaping values from either nums1[m] or nums2[n] until m and n are 0

class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        swap = len(nums1) - 1
        m -= 1
        n -= 1

        while m != -1 or n != -1:
            if m == -1:
                nums1[swap] = nums2[n]
                n -= 1
            elif n == -1:
                nums1[swap] = nums1[m]
                m -= 1
            elif nums1[m] > nums2[n]:
                nums1[swap] = nums1[m]
                m -= 1
            else:
                nums1[swap] = nums2[n]
                n -= 1

            swap -= 1

# This works and runs in o(m + n) as we will have to traverse both arrays completely
# This is basically the last step of a merge sort which is kind of need

# I just thought of a slight optimization since we are always swapping one value I could replace my while loop with for swap in range(len(nums)-1, -1, -1)
# that would actually save me some time as range uses c++ to iterate and not python but big O would be the same


# Score Card
# Did I need hints? N
# Did you finish within 30 min? Y 12
# Was the solution optimal? Y I believe that this is the most optimal
# Were there any bugs? 0 bugs tested on paper first and had no issues
# 5 5 5 5 = 5
