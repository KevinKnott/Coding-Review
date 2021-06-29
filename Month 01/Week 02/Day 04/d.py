# Number of Connected Components in an Undirected Graph: https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
# You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.
# Return the number of connected components in the graph.

from collections import deque


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0
        ourGraph = {}

        for source, dest in edges:
            if source not in ourGraph:
                ourGraph[source] = []
            ourGraph[source].append(dest)

            if dest not in ourGraph:
                ourGraph[dest] = []
            ourGraph[dest].append(source)

        # Simple dfs or bfs probably bfs on account of iterative
        seen = set()
        q = deque()

        for i in range(n):

            if i not in seen:
                count += 1

                if i not in ourGraph:
                    continue

                q.appendleft(i)

                while q:
                    node = q.pop()
                    if node in seen:
                        continue

                    seen.add(node)
                    for edge in ourGraph[node]:
                        q.appendleft(edge)

        return count

# This turns out to be the optimal solution however I did have one bug where I didn't add any nodes that were on there own like 0 in the example edges = [[2,3],[1,2],[1,3]]
# The time/space complexity is o(E+V)  o(E) for building ourGraph and o(E+V) for bfs and o(E+V) as we keep a list of edges and a set of visted verticies

# That being said apparently this has an optimization where we have a disjoint set union although I didn't have a fast enough time to try implementation

# Score Card
# Did I need hints? N (But the second solution did)
# Did you finish within 30 min? Y
# Was the solution optimal? It is optimal enough, technically you can improve from o(E+V ) to o(e and the ackermanfunction(n)) and sapce could be just o(V) instead
# Were there any bugs? I did have one bug where I didn't add any nodes that were on there own like 0 in the example edges = [[2,3],[1,2],[1,3]]
# 4 5 3 3 =  3.75
