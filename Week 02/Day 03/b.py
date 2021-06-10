# . Find the Town Judge: https://leetcode.com/problems/find-the-town-judge/
# In a town, there are n people labelled from 1 to n.  There is a rumor that one of these people is secretly the town judge.

# If the town judge exists, then:

# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
# You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

# If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        return

# Score Card
# Did I need hints? N
# Did you finish within 30 min? Y
# Was the solution optimal? Y
# Were there any bugs? Y  (no support for max heaps made me use negatives and I forgot to handle them properly)
#  5 5 3 5 = 4.5
