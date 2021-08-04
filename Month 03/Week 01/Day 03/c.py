# Find the Town Judge: https://leetcode.com/problems/find-the-town-judge/

# In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

# If the town judge exists, then:
#     The town judge trusts nobody.
#     Everybody (except for the town judge) trusts the town judge.
#     There is exactly one person that satisfies properties 1 and 2.
# You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.
# Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

# Based off of the given rules this seems like a graph problem where you have in degrees and out degrees
# the solution is whichever node has no out degrees and n -1 in degrees is the result

# This means all we have to do is setup a graph of all in degrees and one for all out degrees
# and loop through the n possibilities

from collections import defaultdict


class Solution:
    def findJudge(self, n: int, trust) -> int:
        inDegree = defaultdict(int)
        outDegree = defaultdict(int)

        for src, dest in trust:
            outDegree[src] += 1
            inDegree[dest] += 1

        for i in range(1, n+1):
            if outDegree[i] > 0:
                continue

            if inDegree[i] == n - 1:
                return i

        return -1

# So the above works just as I expected it to and it runs in O(N) time and space

# Score Card
# Did I need hints? Nope
# Did you finish within 30 min? 6 min
# Was the solution optimal? Nope
# Were there any bugs? None
# 5 5 5 5 = 5
