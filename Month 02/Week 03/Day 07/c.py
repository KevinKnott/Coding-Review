# Kth Largest Element in an Array: https://leetcode.com/problems/kth-largest-element-in-an-array/

# Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# For the easy and somewhat optimal solution to this problem we can simply use a heap
# to sort this with a max heap and pop off k values until you get the answer

import heapq
import random


class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        for i in range(len(nums)):
            nums[i] *= -1

        heapq.heapify(nums)

        while k > 1:
            heapq.heappop(nums)
            k -= 1

        return -1 * heapq.heappop(nums)

# The above runs in o(nlogn) and uses o(1) space as we technically are updating our input list
# if we needed to not update the input list we would use o(n)

# Now the problem here is we can do better by taking the principle of a quick select
# where you choose a random value and sort it into the correct spot by moving anything less than it to the left
# and greater to the right this has the advantage of having the potential of not needing to sort all nums
# to make an o(N) average case and o(N^2) if we pick indicies suboptimally
    def findKthLargest(self, nums, k: int) -> int:
        def select(start, end):
            pivot = random.randint(start, end)
            pivotVal = nums[pivot]
            nums[pivot], nums[end] = nums[end], nums[pivot]

            swap = start
            for i in range(start, end):
                if nums[i] < pivotVal:
                    nums[i], nums[swap] = nums[swap], nums[i]
                    swap += 1

            nums[swap], nums[end] = nums[end], nums[swap]
            return swap

        def find(target, start=0, end=len(nums) - 1):
            if start == end:
                return

            potential = select(start, end)

            if potential == target:
                return
            elif potential < target:
                find(target, potential + 1, end)
            else:
                find(target, start, potential - 1)

            return

        find(len(nums) - k)

        return nums[len(nums) - k]

# I already stated the above but you could change some of this up to make it a bit more optimized on the guessing
# but this works pretty well

# Score Card
# Did I need hints? Nope
# Did you finish within 30 min? 18 min
# Was the solution optimal? See blurb between two solutions
# Were there any bugs? None
# 5 5 5 5 = 5
