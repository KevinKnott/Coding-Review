# Number of Connected Components in an Undirected Graph: https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
# You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.
# Return the number of connected components in the graph.


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        return

# Score Card
# Did I need hints? N (But the second solution did)
# Did you finish within 30 min? No 1:30
# Was the solution optimal? My initial solution is optimal however I messed up the initial coding of it
# Were there any bugs? I forgot that since it is possible to have [[[[]]]] I need to actually recurse
#  4 1 2 1 = 2
