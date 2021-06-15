#  Top K Frequent Elements: https://leetcode.com/problems/top-k-frequent-elements/

# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
# There are a couple ways to solve this problem
# the easiest being that we create a dictionary add the values freq
# sort with a lambda on the freq and then return from the kth position onward

from collections import Counter
import random


class Solution:
    def topKFrequent(self, nums, k):
        count = Counter(nums)

        # This sort is actually ridiculous to get correct
        count = sorted(count, key=count.get, reverse=True)
        result = []

        for i in count:
            result.append(i)
            if len(result) == k:
                break

        return result


# Okay the above is actually relatively fast Counter is created in o(n)/o(n) sort with o(nlogn) / o(1) depending on sort
# Loop to k (potentially up to n more times) o(n)

# The question is can we do better? the answer I believe is yes!
# We can technically use quick sort method which is a binary search which can potentially reveal the kth element and everything to the right that is larger


    def topKFrequentImproved(self, nums, k):
        # Ran out of time on this

        count = Counter(nums)
        unique = list(count.keys())

        def partition(start, end):
            # Move pivot to the end
            pivot = random.randint(start, end)
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
            unique[swapIndex], unique[pivot] = unique[pivot], unique[swapIndex]
            pivot = swapIndex
            return pivot

        def search(k, start=0, end=len(unique)-1):
            if start == end:
                return

            potentialIndex = partition(start, end)

            if potentialIndex < k:
                search(k, potentialIndex + 1, end)
            elif potentialIndex > k:
                search(k, start, potentialIndex - 1)
            else:
                return nums[potentialIndex:len(nums)]

        search(len(unique)-k)
        return unique[len(unique) - k:]

# Score Card
# Did I need hints? Yes unfortunately my pivot is failing in leetcode even though I double checked and see no difference in the code
# Did you finish within 30 min? n
# Was the solution optimal? Yes my first solution is optimal but the second could be faster if it didn't fail
# Were there any bugs? Y
#  4 1 3 1 = 4.5
