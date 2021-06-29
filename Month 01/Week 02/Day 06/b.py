# Top K Frequent Elements: https://leetcode.com/problems/top-k-frequent-elements/
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Obviously this is a super easy dictionary question but optimally we can use the count
from collections import Counter
import heapq


class Solution:
    # This solution takes nlog(n) time and o(n+k) space where k is the number of elements to return

    def topKFrequent(self, nums, k):
        count = {}

        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1

        # Honestly you could do the same thing with a heap and it would probably be a bit more efficient
        # running in o(logn) time instead of nlogn
        count = sorted(count, reverse=True, key=count.get)

        result = []

        for i in range(k):
            result.append(count[i])

        return result

    #  Using a heap this time

    def topKFrequent(self, nums, k):
        count = {}

        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1

        # Honestly you could do the same thing with a heap and it would probably be a bit more efficient
        # running in o(logn) time instead of nlogn

        return heapq.nlargest(k, count.keys(), key=count.get)

# Is there a more optimal way of doing this problem?
# So this problem is actually mimicing grabbing the kth largest element except in this case we are using a count
# So to imrpove this algorithm we can do the same thing that we did for find kth largets
# which is using the quick select to binary search and return an unsorted list of all elements higher than k
# this is only possible because the return order doesn't matter we just want the kth largest

# Score Card
# Did I need hints? N
# Did you finish within 30 min? Y
# Was the solution optimal? N I didn't think of the quick select solution and I would still have to implement it
# Were there any bugs? Y my sorting took me a while to figure out my keys actually needed to be baseed off of count.get instead of count
#  4 3 3 2 = 3
