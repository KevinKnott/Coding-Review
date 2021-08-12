# Clone Graph: https://leetcode.com/problems/clone-graph/

# Given a reference of a node in a connected undirected graph.
# Return a deep copy (clone) of the graph.
# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.


# Definition for a Node.
from collections import deque


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

# My initial solution to this problem is to traverse it twice once to simply create all nodes
# and store them in a hashmap and then a second traversal to link the connected neighbors


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return

        ourGraph = {}
        q = deque()
        q.appendleft(node)

        while q:
            cur = q.pop()

            if cur.val in ourGraph:
                continue

            ourGraph[cur.val] = Node(cur.val)

            for nei in cur.neighbors:
                q.appendleft(nei)

        q.appendleft(node)
        visited = set()
        while q:
            cur = q.pop()

            if cur.val in visited:
                continue

            visited.add(cur.val)
            for nei in cur.neighbors:
                ourGraph[cur.val].neighbors.append(ourGraph[nei.val])
                q.appendleft(nei)

        return ourGraph[node.val]


# Boo yeah this works in O(N+M) time and space and is optimal! It comes down to a special
# dfs or bfs that has you create new nodes and store them as you go. I think you could probably
# optimize the second bfs just a bit by only using the cur.val instead of the whole node in the
# q but it is still the same overal complexity

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 10
# Was the solution optimal? Yee yee
# Were there any bugs? Nope
# 5 5 5 5 = 5
