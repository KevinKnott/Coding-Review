# Kth Largest Element in an Array: https://leetcode.com/problems/kth-largest-element-in-an-array/
# Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Repeating a problem given an array we can solve already
# Last time we took the array sorted for a O(nlogn) space o(1/n) space depending on sorting
# Also previously just created a heap

import heapq
import random


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

    # New method you can technically quick sort! because if you quick sort you can choose a range like binary sort
    # plus if your switch point ends at the kth index you just return the result!

    def findKthLargestQS(self, nums, k):
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

            random_pivot = helper(start, end)

            if target > random_pivot:
                return selection(target, random_pivot + 1, end)
            elif target < random_pivot:
                return selection(target, start, random_pivot - 1)
            else:
                return nums[random_pivot]

        return selection(len(nums) - k)

# Score Card
# Did I need hints?
# Did you finish within 30 min?
# Was the solution optimal?
# Were there any bugs?
#  3 3 4 3 = 3.25


a = [3, 2, 1, 5, 6, 4]
k = 3
sol = initial()
print(sol.findKthLargestQS(a, k))
