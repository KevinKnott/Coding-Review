# Top K Frequent Elements: https://leetcode.com/problems/top-k-frequent-elements/

# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# This is the same as kth largest except we need to first get the count and then sort the nums based on that count
# The easiest solution is actually just to return the top values using a heap (max heap)
# however this is probably to easy so what we need to do is try using the quick sort which leaves all elements lower than the kth index to the left
# and higher to the right this is optimal since we can return the highest in any order

import heapq
from collections import Counter
from random import randint


class Solution:
    def topKFrequent(self, nums, k):
        # if there are only k elements in the list then you have your answer
        if k == len(nums):
            return nums

        nums = Counter(nums)

        # Now this is the easiest solution but we could of also done the following
        # Sort the numbers key (so we have a unique solution) by collection.get()
        # which provides us the number in count aka Counter.get(key) == count
        # nums = sorted(nums.keys(), key=nums.get, reverse=True)
        # result = []
        # while k > 0:
        #     result.append(k.pop())
        # return result

        return heapq.nlargest(k, nums.keys(), key=nums.get)


# Now is this the optimal? Definitely not using the same principles we just applied we can run the quick sort algo that I mentioned above

    def topKFrequent(self, nums, k):
        if k == len(nums):
            return nums

        count = Counter(nums)
        unique = list(count.keys())

        def partition(start, end):
            # Move pivot to the end
            pivot = randint(start, end)
            pivotFreq = count[unique[pivot]]
            unique[pivot], unique[end] = unique[end], unique[pivot]
            pivot = end

            # swapIndex to start
            swapIndex = start

            # start at the beginning, and move to the end
            for i in range(start, end):
                if count[unique[i]] < pivotFreq:
                    unique[swapIndex], unique[i] = unique[i], unique[swapIndex]
                    swapIndex += 1

            # Swap pivot back
            unique[pivot], unique[swapIndex] = unique[swapIndex], unique[pivot]
            return swapIndex

        def search(k, start=0, end=len(unique) - 1):
            if start == end:
                return

            potentialIndex = partition(start, end)

            if potentialIndex < k:
                search(k, potentialIndex + 1, end)
            elif potentialIndex > k:
                search(k, start, potentialIndex - 1)
            else:
                return

        search(len(unique) - k)
        return unique[len(unique) - k:]

# Boom this is the optimal solution although it took me a little while as my swapping wasn't actually working because I accidently messed up the swapIndex with potential in the middle


# Score Card
# Did I need hints? Nope
# Did you finish within 30 min? 45
# Was the solution optimal? So technically the best solution is the first as it will run in o(nlogk) and n(n+k) but the quicksort runs in o(n^2) and o(n)
# Were there any bugs? See the above little blurb
# 5 3 4 3 = 3.75
