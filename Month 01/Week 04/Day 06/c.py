# Is Graph Bipartite?: https://leetcode.com/problems/is-graph-bipartite/

# There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:

#     There are no self-edges (graph[u] does not contain u).
#     There are no parallel edges (graph[u] does not contain duplicate values).
#     If v is in graph[u], then u is in graph[v] (the graph is undirected).
#     The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.

# A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.

# Return true if and only if it is bipartite.
class Solution:
    def isBipartite(self, graph) -> bool:
        # ourGraph = {}

        # # First we need to take our list and create our graph
        # for node in graph:
        #     for value in graph[node]:
        #         ourGraph[node].add(value)

        def dfs(index, color):
            if index in visited:
                if visited[index] != color:
                    return False
                return True

            # Mark Color and Visisted
            visited[index] = color

            for i in graph[index]:
                if not dfs(i, color ^ 1):
                    return False

            return True

        visited = {}
        result = True
        # Then we need to start at a node color Red and go through B/R
        # for i in our list and dont go to a visited node
        for i in range(len(graph)):
            if i not in visited:
                result = result and dfs(i, 0)

        return result

# This solution works and it will run in O(V+E) and store o(V)  could we improve this?
# I think we could I simply took the easy approach of using recursion but you could
# definitely improve the performance slightly by converting this into a iterative solution
# Also having to track the recursion result could be improved in the iterative approach

# Score Card
# Did I need hints? Nope
# Did you finish within 30 min? 30
# Was the solution optimal? See my blurb from above
# Were there any bugs? I don't really have
# 5 5 5 5 = 5
