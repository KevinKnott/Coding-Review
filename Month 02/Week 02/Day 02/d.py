# Clone Graph: https://leetcode.com/problems/clone-graph/

# Given a reference of a node in a connected undirected graph.
# Return a deep copy (clone) of the graph.

# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

# class Node {
#     public int val;
#     public List<Node> neighbors;
# }


# Test case format:
# For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.
# An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.
# The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

# This problem is actually pretty simple we (using a dfs) create all nodes and store them in a dict
# where we have the value point to the new node

# then using the above dict do another dfs and assign the appropriate neighbors


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return

        graph = {}

        def createNodes(node):
            if node.val not in graph:
                graph[node.val] = Node(node.val)
                for nei in node.neighbors:
                    createNodes(nei)

        def connectNodes(node, visited=set()):
            if node.val not in visited:
                visited.add(node.val)

                for nei in node.neighbors:
                    graph[node.val].neighbors.append(graph[nei.val])
                    connectNodes(nei, visited)

        createNodes(node)
        connectNodes(node)
        return graph[node.val]

# The above works and is pretty optimal it runs in two bfs steps that take o(V+E) as we visit each node and vertex once
# the same goes for space as we need to store an identical copy so that is o(E)

# If you wanted you could create an iterative approach to the above for combining the two steps

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 20
# Was the solution optimal? This is optimal
# Were there any bugs? No
# 5 5 5 5 = 5
