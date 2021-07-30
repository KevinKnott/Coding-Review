# Top K Frequent Elements: https://leetcode.com/problems/top-k-frequent-elements/

# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# This problem is actually super easy all we have to do is use a heap after getting a frequency of every single element
# The more optimal way is to use quick select divide and conquer to get an even faster solution

from collections import Counter
from random import randint
import heapq


class Solution:
    def topKFrequent(self, nums, k):

        count = Counter(nums)

        return heapq.nlargest(k, count, key=count.get)

# This will run in O(NlogK) and uses o(N+k) space for the counter
# however by using the divide and conquer quickselect we can get o(N) time and space


class Solution:
    def topKFrequent(self, nums, k):
        count = Counter(nums)
        unique = list(count.keys())

        def conquer(start, end):
            pivot = randint(start, end)
            pivotVal = count[unique[pivot]]

            unique[end], unique[pivot] = unique[pivot], unique[end]

            swap = start
            for i in range(start, end):
                if count[unique[i]] < pivotVal:
                    unique[i], unique[swap] = unique[swap], unique[i]
                    swap += 1

            unique[swap], unique[end] = unique[end], unique[swap]
            return swap

        def search(start=0, end=len(unique)-1):
            if start == end:
                return

            potential = conquer(start, end)

            if potential == target:
                return
            elif potential < target:
                search(potential + 1, end)
            else:
                search(start, potential - 1)

        target = len(unique) - k
        search()
        return unique[target:]

# So the above is easy to figure out as it is simply the quick select sorting algo and I have practiced quite a bit
# the only tricky part is converting it to use the counter instead of just the basic value itself

# Score Card
# Did I need hints? Nope
# Did you finish within 30 min? 15
# Was the solution optimal? See blurb in middle
# Were there any bugs? None
# 5 5 5 5 = 5
