# Kth Largest Element in an Array: https://leetcode.com/problems/kth-largest-element-in-an-array/

# Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# There are a number of simple solutions to this problem but it is all about efficency
# We can sort the array and return len(nums) - k in an nlogn time
# we could use a heap to grab the max value every time and pop k -1 times and return result as pop() this is nlogk time
# or we could actually use the quick sort method to binary search and potentially grab the correct spot n time (wehere we chose the wrong n everytime)

import heapq
from random import randint


class Solution:
    def findKthLargestSort(self, nums, k):
        nums.sort()
        return nums[len(nums)-k]

    def findKthLargestHeap(self, nums, k):
        heapq.heapify(nums)
        # Get the n largest values and return the top of it
        return heapq.nlargest(k, nums)[-1]

    def findKthLargestQuickSort(self, nums, k):
        def conquer(start, end):
            pivot = randint(start, end)
            nums[pivot], nums[end] = nums[end], nums[pivot]
            pivot = end

            swap = start
            for i in range(start, end):
                if nums[i] < nums[pivot]:
                    nums[i], nums[swap] = nums[swap], nums[i]
                    swap += 1

            nums[swap], nums[pivot] = nums[pivot], nums[swap]

            return swap

        def divide(target, start, end):
            # I forgot if start == end there is only one val so we dont need to do anything
            if start == end:
                return nums[start]

            pivot = conquer(start, end)

            if pivot < target:
                return divide(target, pivot + 1, end)
            elif pivot > target:
                return divide(target, start, pivot - 1)
            else:
                return nums[pivot]

        return divide(len(nums) - k, 0, len(nums)-1)

# Score Card
# Did I need hints? N
# Did you finish within 30 min? Yuh
# Was the solution optimal? Yeah it is
# Were there any bugs? I forgot to return from my recursion
# 5 5 5 4 = 4.75
