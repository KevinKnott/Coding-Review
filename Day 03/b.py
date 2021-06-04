# Kth Largest Element in an Array: https://leetcode.com/problems/kth-largest-element-in-an-array/
# Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Repeating a problem given an array we can solve already
# Last time we took the array sorted for a O(nlogn) space o(1/n) space depending on sorting
# Also previously just created a heap

import heapq


class initial():
    def findKthLargest(self,  nums, k):
        nums.sort()
        return nums[len(nums) - k]

    def findKthLargestHeap(self,  nums, k):
        heapq._heapify_max(nums)
        while k > 1:
            heapq._heappop_max(nums)
            k -= 1

        return heapq._heappop_max(nums)

# Score Card
# Did I need hints?
# Did you finish within 30 min?
# Was the solution optimal?
# Were there any bugs?
#  3 3 4 3 = 3.25


a = [3, 2, 1, 5, 6, 4]
k = 6
sol = initial()
print(sol.findKthLargestHeap(a, k))
