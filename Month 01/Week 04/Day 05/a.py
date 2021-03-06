# Last Stone Weight: https://leetcode.com/problems/last-stone-weight/
# We have a collection of stones, each stone has a positive integer weight.

# Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

# If x == y, both stones are totally destroyed;
# If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
# At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

import heapq


class Solution:
    def lastStoneWeight(self, stones) -> int:
        # It is o(N) to heapify or we can go through and heappush in nlogn
        # Although I just realized we need to use a max heap so we need to invert the sign
        for i in range(len(stones)):
            stones[i] *= -1

        heapq.heapify(stones)

        # we need to loop until we have size >= 2
        while len(stones) >= 2:
            y, x = heapq.heappop(stones) * -1, heapq.heappop(stones) * -1

            if x == y:
                continue
            else:
                heapq.heappush(stones, -1 * (y-x))

        return 0 if len(stones) == 0 else (heapq.heappop(stones) * -1)

# This works and is pretty optimal although I think we could improve the space complexity if we wanted to increase the
# time complexity o(nlogn) and o(n) time/space

# After looking at the solution mine is pretty optimal but apparently we can use a bucketing system/ counting sort to solve
# this in a  linear time however this solution requires the bucketing to be of the same length of the highest stone
# so it can quickly be outperformed by the previous algo


# Score Card
# Did I need hints? N
# Did you finish within 30 min? 10
# Was the solution optimal? If our array is large mine is optimal for a small max size there is a more optimal solution
# Were there any bugs? Negative
#  5 5 3 5 = 4.5
