# Number of Connected Components in an Undirected Graph: https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

# You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.
# Return the number of connected components in the graph.

# This is a super simple dfs solution where all you have to do is create an adjacency list and then dfs starting from every node
# and add the nodes you visit to visited any nodes that you grab from the for loop and not anoter dfs call increases the count by 1

# That being said you could easily implement a union find on this problem to increase the efficiency

from collections import defaultdict


class Solution:
    def countComponents(self, n: int, edges) -> int:
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        visited = set()

        def dfs(node):
            if node in visited:
                return

            visited.add(node)

            for i in graph[node]:
                dfs(i)

        count = 0
        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)

        return count

# The above is super simple for a dfs and runs in o(V + E) time and space as we visit every node and edge at least once


# Now can we do better? Like I said if we use a union find algo we can run this in o(N) and o(logn)

    def countComponents(self, n: int, edges) -> int:
        parent = [i for i in range(n)]

        def union(i, j):
            parentI = find(i)
            parentJ = find(j)
            # Find both parents
            parent[parentI] = parentJ

        def find(i):
            if parent[i] == i:
                return i
            return find(parent[i])

        # Combine every two nodes together!
        for edge1, edge2 in edges:
            union(edge1, edge2)

        connected = set()
        count = 0

        for i in range(n):
            root = find(i)
            if root not in connected:
                count += 1
            connected.add(root)

        return count

# The above works but could be optimized to not be recursive

# The below is kind of just the default solution for writing a DSU


class UnionFind(object):

    def __init__(self, n: int):
        self.parent = defaultdict(int)
        for i in range(n):
            self.parent[i] = i

    # This is a recursive find where you either return a node that is its own parent
    # or find the node that is the parent by searching to the connected node from
    # a union
    def find(self, i):
        if self.parent[i] == i:
            return i
        return self.find(self.parent[i])

    # This is a recursive union where you find the parent node of each element
    # and then point the parent of I to now be unioned with parent J

    def union(self, i, j):
        parentI = self.find(i)
        parentJ = self.find(j)
        # Find both parents
        self.parent[parentI] = parentJ


# Score Card
# Did I need hints? Yes for the Union Find as I haven't practiced it enough
# Did you finish within 30 min? 30
# Was the solution optimal? Y
# Were there any bugs?  Nope
# 5 5 4 5 = 4.75
