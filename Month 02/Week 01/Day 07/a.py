# Find the Town Judge: https://leetcode.com/problems/find-the-town-judge/

# In a town, there are n people labelled from 1 to n.  There is a rumor that one of these people is secretly the town judge.

# If the town judge exists, then:

#     The town judge trusts nobody.
#     Everybody (except for the town judge) trusts the town judge.
#     There is exactly one person that satisfies properties 1 and 2.

# You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

# If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.

# So this problem seems like we need to create a count of how many inbound connections there are which means this is a graph problem
# We will create a adj list and create all connections to each node and check for a node who has num people - 1 connections in
# and no connections out

class Solution:
    def findJudge(self, n, trust) -> int:
        countIn = {}
        countOut = {}

        # Initiallize graph
        for i in range(1, n + 1):
            countIn[i] = 0
            countOut[i] = 0

        # Connect all nodes
        for src, dest in trust:
            countIn[dest] += 1
            countOut[src] += 1

        # Check if there are no outgoing connections and only incoming
        for i in range(1, n + 1):
            if countOut[i] == 0 and countIn[i] == (n - 1):
                return i

        # If we get here nothing was found
        return -1

# Boo to the yeah this works and runs in o(n) time and space

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 12
# Was the solution optimal? Yuhhh
# Were there any bugs? None
# 5 5 5 5 = 5
