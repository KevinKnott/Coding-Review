# Number of Connected Components in an Undirected Graph: https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

# You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.
# Return the number of connected components in the graph.

# So this problem is relatively easy it is a simple dfs where you go from 0 -> N and do a dfs
# you keep a visted set and anytime you see a new number you can simple do a dfs from there
# to mark all nodes in this connected componenet

# The more optimal solution is to write a union find as it is slighty more efficient than the
# o(V+E) solution of above

from collections import defaultdict


class Solution:
    def countComponents(self, n: int, edges) -> int:
        count = 0
        visited = set()
        ourGraph = defaultdict(list)

        for src, dest in edges:
            ourGraph[src].append(dest)
            ourGraph[dest].append(src)

        def dfs(node):
            if node:
                visited.add(node)

                for nei in ourGraph[node]:
                    if nei not in visited:
                        dfs(nei)

        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)

        return count

# Like I said above this was super simple and runs in O(V+E)
# by using a union find we can reduce this to O(V+E) and O(V)

    def countComponents(self, n: int, edges) -> int:
        # With union find we simply create a list of nodes pointing to each other
        parent = [i for i in range(n)]

        # For the union we combine the two separated edges i -> j
        # so that they will now share a root as we are adding them to each others
        # set
        def union(i, j):
            # Find the root node of both and update
            # the first root to change to point to the second
            # root as we have added the two nodes together
            first = find(i)
            second = find(j)
            parent[first] = second

        # for find we will simply iterate through a node until we find the root
        # aka where the node[i] points to itself as the head
        # O(E)
        def find(i):
            # Basecase is we are pointing to self
            if i == parent[i]:
                return i
            # Otherwise we traverse until we are pointing to self
            return find(parent[i])

        # for every node that we have we perform a union and point one to the other
        # if they are connected
        for x, y in edges:
            union(x, y)

        # Basically this part is the same
        visited = set()
        count = 0

        for i in range(n):
            ourRoot = find(i)
            if ourRoot not in visited:
                count += 1

            visited.add(ourRoot)

        return count

# Score Card
# Did I need hints? Nope
# Did you finish within 30 min? 25 min
# Was the solution optimal? See in between two solutions
# Were there any bugs? None
# 5 5 5 5 = 5
