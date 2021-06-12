# Last Stone Weight: https://leetcode.com/problems/last-stone-weight/
# We have a collection of stones, each stone has a positive integer weight.

# Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

#     If x == y, both stones are totally destroyed;
#     If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.

# Two thoughts come to mind initially one is to loop through and get two most everytime o(n) and do math
# or use a heap get the max twice o(log(n)) and append the result and repeat although the same works if you just sort it
import heapq


class Solution:
    def lastStoneWeight(self, stones):
        heap = []
        for stone in stones:
            heapq.heappush(heap, -1 * stone)

        while len(heap) > 1:
            y, x = (-1 * heapq.heappop(heap)), (-1 * heapq.heappop(heap))
            if x < y:
                y = y - x
                heapq.heappush(heap, -1 * y)

        return -1 * heap[0] if len(heap) == 1 else 0

# Boo yah this works although I could of just multipled all values by -1 and then removed all -1 in here
# Also why the fuck doesn't python have a heap function?

# Is there an improvement? Apparently so, we need to create a bucket for each of the values and  then
# we can go through it backwards and keep track of the biggest weight and do all the math that is need on the way down
# this other approach is o(N+w) where n is the number of elements and w is the width of those elemens in an array

# Score Card
# Did I need hints? N
# Did you finish within 30 min? Y 25
# Was the solution optimal? Y
# Were there any bugs? N
#  5 5 5 5 = 5
