# Top K Frequent Elements: https://leetcode.com/problems/top-k-frequent-elements/

# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# The easy trick to do here is actually to use a heap for the counts and simply pop off as many as you need

# The optimal trick is given here:
# So if we are given an array of integers that is unsorted we can find the counts of every variable and then use it
# this count to use a quick sort to solve this problem

import heapq
from random import randint


class Solution:
    def topKFrequent(self, nums, k: int):
        if k == len(nums):
            return nums

        # Create a counter of how many there are
        freq = {}

        for num in nums:
            if num not in freq:
                freq[num] = 0

            freq[num] += 1

        # Add all of the values into our heap (using -v since heapq is a min heap and we want max values)
        heap = [(-v, k) for k, v in freq.items()]

        # Create the heap
        heapq.heapify(heap)

        # Pop off the k values that we need
        result = []
        while k > 0:
            result.append(heapq.heappop(heap)[1])
            k -= 1

        return result

# This problem is pretty straight forward and the above runs in o(nlogn) and uses o(n) space
# Using the quick sort method wherw we simply choose a random index and try to sort based of its
# values

    def topKFrequent(self, nums, k: int):
        if k == len(nums):
            return nums

        # Create a counter of how many there are
        freq = {}

        for num in nums:
            if num not in freq:
                freq[num] = 0

            freq[num] += 1

        unique = list(freq.keys())

        def conquer(start, end):

            pivot = randint(start, end)
            pivotValue = freq[unique[pivot]]
            unique[pivot], unique[end] = unique[end], unique[pivot]
            pivot = end

            swap = start
            for i in range(start, end):
                if freq[unique[i]] < pivotValue:
                    unique[swap], unique[i] = unique[i], unique[swap]
                    swap += 1

            unique[swap], unique[end] = unique[end], unique[swap]
            return swap

        def divide(target, start=0, end=len(unique) - 1):
            if start == end:
                return

            potential = conquer(start, end)

            if potential == target:
                return
            elif potential < target:
                divide(target, potential + 1, end)
            else:
                divide(target, start, potential - 1)

        target = len(unique) - k
        divide(target)
        return unique[target:]


# The above works and I only had one slight bug while programming it!
# It runs in o(N^2) in worst case assuming we chose wrong pivots but avgs to o(N)
# it uses o(n) space so it is pretty good.

# Score Card
# Did I need hints? Nope
# Did you finish within 30 min? 40
# Was the solution optimal? Yeah
# Were there any bugs? I accidently was swapping the wrong variable
# 5 4 5 5 = 4.75
