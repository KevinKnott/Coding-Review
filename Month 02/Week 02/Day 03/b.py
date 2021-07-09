# Number of Connected Components in an Undirected Graph: https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

# You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.
# Return the number of connected components in the graph.

# This is a super simple bfs/dfs problem where you just neeed to visit all nodes and see if they are connect (it will end with q/stack empty but still have some not in visited)

from collections import defaultdict


class Solution:
    def countComponents(self, n: int, edges) -> int:
        # create undirected graph
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        def dfs(node):
            if node not in visited:
                visited.add(node)

                for i in graph[node]:
                    if i not in visited:
                        dfs(i)

        visited = set()
        count = 0

        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)

        return count

# This solution is pretty optimal! it runs in o(V+E) and uses o(V+E) space as we visit every node and explore every edge
# Now is it optimal kinda honestly using a bfs and your own stack would increase performance although it still in O(V+E)
# Outside of this I think that we could solve this with a DSU as when we add a node we will know if they are already
#  connected this would lead to a slight improvement of going through (V + E) and o (V) Space

# https://www.youtube.com/watch?v=0jNmHPfA_yE

    def countComponentsUnionFind(self, n: int, edges) -> int:
        # create undirected graph
        # Map the nodes to a list and point them to themselves
        graph = [i for i in range(n)]

        # Try to union the two nodes together
        for edge1, edge2 in edges:
            self.union(graph, edge1, edge2)

        # Now that all nodes are connected together
        # We can do the same as above
        connected = set()
        count = 0

        # We go through the graph with all connected components and unconnected components
        for index in range(len(graph)):
            root = self.find(graph, index)
            # Since we know that all nodes that are connected
            # have been labeled with the same root we can
            # check if it is in connected
            if root not in connected:
                count += 1

            connected.add(root)

        return count

    def find(self, nodes, edge):
        root = edge
        # Continue until we are at the root of our edge
        while root != nodes[root]:
            root = nodes[root]

        while edge != root:
            ourNext = nodes[edge]
            nodes[edge] = root
            edge = ourNext
        return root

    def union(self, nodes, edge1, edge2):
        root1 = self.find(nodes, edge1)
        root2 = self.find(nodes, edge2)
        nodes[root1] = nodes[root2]


# Score Card
# Did I need hints? N
# Did you finish within 30 min? 15
# Was the solution optimal? No the Union Find is optimal but I need to learn how to code it
# Were there any bugs? None
# 5 5 3 5 = 4.5
