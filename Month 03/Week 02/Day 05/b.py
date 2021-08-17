# Couples Holding Hands: https://leetcode.com/problems/couples-holding-hands/

# There are n couples sitting in 2n seats arranged in a row and want to hold hands.
# The people and seats are represented by an integer array row where row[i] is the ID of the person sitting in the ith seat. The couples are numbered in order, the first couple being (0, 1), the second couple being (2, 3), and so on with the last couple being (2n - 2, 2n - 1).
# Return the minimum number of swaps so that every couple is sitting side by side. A swap consists of choosing any two people, then they stand up and switch seats.

# I think the best way to do this problem is to make it into a simple graph/hashmap where you know where the correct partner is sitting
# and then you go through and anytime your partner is not in the correct swap it in the row and in the graph so that we can get the correct
# solution this should be O(N) for both time and complexity

from collections import defaultdict


class Solution:
    def minSwapsCouples(self, row) -> int:
        ourGraph = defaultdict(int)

        for i in range(0, len(row), 2):
            ourGraph[i] = i + 1
            ourGraph[i+1] = i

        result = 0
        # now that we know where we are we simply have to loop through
        # and swap any values that aren't the appropriate pair
        for i in range(0, len(row), 2):
            ourVal = row[i]
            partner = row[i] ^ 1

            if ourGraph[ourVal] != row[i+1]:
                result += 1

            coupleIndex = row.index(partner)
            row[i+1], row[coupleIndex] = row[coupleIndex], row[i+1]

        return result

# So the above works and is actually clever but honestly we can improve this ever so slightly
# to do this we can jus use onlyl the xor value and remove our graph because our row is technically
# the same thing since we are using row.index to find the correct index

    def minSwapsCouples(self, row):
        result = 0
        # now that we know where we are we simply have to loop through
        # and swap any values that aren't the appropriate pair
        for i in range(0, len(row), 2):
            ourVal = row[i]
            partner = row[i] ^ 1

            if partner != row[i+1]:
                result += 1

            coupleIndex = row.index(partner)
            row[i+1], row[coupleIndex] = row[coupleIndex], row[i+1]

        return result

# This runs in O(N) and uses O(1) additional space

# Score Card
# Did I need hints? No
# Did you finish within 30 min? 10
# Was the solution optimal? Yee
# Were there any bugs? Nope
# 5 5 5 5 = 5
