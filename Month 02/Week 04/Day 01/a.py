# Last Stone Weight: https://leetcode.com/problems/last-stone-weight/

# We have a collection of stones, each stone has a positive integer weight.

# Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

#     If x == y, both stones are totally destroyed;
#     If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.

# At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

class Solution:
    def lastStoneWeight(self, stones) -> int:
        return

# Score Card
# Did I need hints? N
# Did you finish within 30 min? N (45 or so)
# Was the solution optimal? I believe so we could make some slight optimization but this will run in o(n^2) because of the multiplicity we would go through once and then again to multiply
#  and o(n) space
# Were there any bugs? I listed bugs in the above code
#  5 2 4 2 = 3.25
