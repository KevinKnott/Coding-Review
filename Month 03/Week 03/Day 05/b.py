# Top K Frequent Elements: https://leetcode.com/problems/top-k-frequent-elements/

# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

from types import List
from typing import Counter
from random import randint

# For this problem we know that a very fast solutions is to use a heap and then you can simply create a counter to keep track of the most
# common elements and this will be an O(nlogk) solution with O(N) space. However there is a slightly more improved method that
# is actually to use the quick sort algo and random pick a swap between the start/end and divide and conquer. this will use O(N) time
# and space as we have to keep track of all the unique values


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        uniq = list(count.keys())

        def sort(start, end):
            potential = randint(start, end)
            potentialVal = count[uniq[potential]]

            uniq[end], uniq[potential] = uniq[potential], uniq[end]

            swap = start
            for i in range(start, end):
                if count[uniq[i]] < potentialVal:
                    uniq[i], uniq[swap] = uniq[swap], uniq[i]
                    swap += 1

            uniq[end], uniq[swap] = uniq[swap], uniq[end]
            return swap

        def quick(start=0, end=len(uniq) - 1):

            potentialIndex = sort(start, end)

            if potentialIndex == target:
                return
            elif potentialIndex < target:
                quick(potentialIndex + 1, end)
            else:
                quick(start, potentialIndex - 1)

        target = len(uniq) - k
        quick()
        return uniq[target:]

# Boom this problem is done and dusted, honestly this was rather the difficult the first time but I have gotten quite used to it.

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 10
# Was the solution optimal? Y although Nope
# Were there any bugs?  I didn't really have any bugs
# 5 5 5 5 = 5
