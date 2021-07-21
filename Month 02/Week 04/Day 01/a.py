# Last Stone Weight: https://leetcode.com/problems/last-stone-weight/

# We have a collection of stones, each stone has a positive integer weight.

# Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

#     If x == y, both stones are totally destroyed;
#     If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.

# At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

# For the solution all we have to do is use a max heap and then we can get the next highest number in logn
# then all we have to do is the above logic

import heapq


class Solution:
    def lastStoneWeight(self, stones) -> int:
        for i in range(len(stones)):
            stones[i] *= -1

        heapq.heapify(stones)

        while len(stones) > 1:
            y = -1 * heapq.heappop(stones)
            x = -1 * heapq.heappop(stones)

            if x != y:
                heapq.heappush(stones, -1 * (y - x))

        return 0 if len(stones) == 0 else -1 * stones.pop()

# The above works and runs in O(nlogn) and uses o(1) additional space as it modifies the existing list
# Is there a better solution not really there is a interesting solution in which you could use bucketing
# however it is definitely more complicated and uses more space as you need k buckets where
# k is the largest val so if it was 90000 it would be quite horrible

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 15
# Was the solution optimal? Oh yea
# Were there any bugs? None!
# 5 5 5 5 = 5
