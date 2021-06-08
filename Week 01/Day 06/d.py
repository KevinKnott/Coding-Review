# Kth Largest Element in an Array: https://leetcode.com/problems/kth-largest-element-in-an-array/
# Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.

import heapq
import random
# Note I have done this problem a number of times recently


class solution1:
    # First solution involves sorting because we know that the kth largest number in a sorted array will be at len(nums) - K spots
    # Note using this and a remove duplicates we could also go with kth largest unique number
    # Also part of this is because k is garunteed to be in 0 -> len(nums) although we could add checks
    def findKthLargest(self, nums, k):
        nums.sort()
        return nums[len(nums)-k]

    # Other than sorting which is o(nlogn) and o(1) we could potentially use a heap since we can use max heap to get largest and only update log(n) times and o(1)
    # as heap strucutres is in place
    def findKthLargestHeap(self, nums, k):
        heapq._heapify_max(nums)

        while k > 1:
            heapq._heappop_max(nums)
            k -= 1

        return heapq._heappop_max(nums)

    # The final option here
    # This solution takes advantage of two things one a quick sort on a random element will end up with an element in the correct place so
    # if that element is in the len(nums) - k place we end up with the solution other wise we can split the array in half or more depending
    #  on your selection  (using binary search)
    def findKthLargestQuickSort(self, nums, k):
        def helper(start, end):
            pivot = random.randint(start, end)
            nums[pivot], nums[end] = nums[end], nums[pivot]
            pivot = end

            slow = start
            for i in range(start, end):
                if nums[i] < nums[pivot]:
                    nums[i], nums[slow] = nums[slow], nums[i]
                    slow += 1

            nums[slow], nums[pivot] = nums[pivot], nums[slow]
            return slow  # (nums, slow)

        # aka binary search
        def selection(target, start=0, end=len(nums)-1):
            if start == end:
                return nums[start]

            potential = helper(start, end)

            if target > potential:
                return selection(target, potential + 1, end)
            elif target < potential:
                return selection(target, start, potential - 1)
            else:
                return nums[potential]

        return selection(len(nums) - k)


# Score Card
# Did I need hints? N
# Did you finish within 30 min? N
# Was the solution optimal? Y
# Were there any bugs? Y
# Unfortunately I am tired and missed on a couple things in my partition I forgot that I need to make the slow index = to start as we are already
# seraching using binary search and don't need to do whole list
#  5 3 5 3 = 4
