# Is Graph Bipartite?: https://leetcode.com/problems/is-graph-bipartite/

# There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:

#     There are no self-edges (graph[u] does not contain u).
#     There are no parallel edges (graph[u] does not contain duplicate values).
#     If v is in graph[u], then u is in graph[v] (the graph is undirected).
#     The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.

# A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.

# Return true if and only if it is bipartite.

# This problem is actually pretty easy you recursively dfs through the nodes and label them in your visited with a color red/black or 0/1
# Continue this and if you ever try to color a node in an opposite color you return false else the problem is true


class Solution:
    def isBipartite(self, graph) -> bool:
        visited = {}
        self.hasFaled = False

        def dfs(node, color=0):
            if node in visited:
                if visited[node] ^ color:
                    self.hasFaled = True
                    return False

                return True

            visited[node] = color
            for nei in graph[node]:
                if not dfs(nei, color ^ 1):
                    return False

            return True

        for i in range(len(graph)):
            if i not in visited:
                if not dfs(i):
                    return False

        return True

# The above works and is actually kind of neat by coloring as we go we can limit this problem to a
# time complexity of O(V+E) and a space complexity of only O(V)


# Score Card
# Did I need hints? N
# Did you finish within 30 min? 10
# Was the solution optimal? This is optimal
# Were there any bugs? No
#  5 5 5 5 = 5
