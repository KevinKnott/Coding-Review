# All Nodes Distance K in Binary Tree: https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

# We are given a binary tree (with root node root), a target node, and an integer value k.
# Return a list of the values of all nodes that have a distance k from the target node.  The answer can be returned in any order.

# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# So my first thought when solving this problem is to actually map each node to its parent and then bfs to the nodes above and
# below it until you reach a distance of k


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int):
        def dfs(node, par=None):
            if node:
                node.par = par
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root)
        # With the above we now have the pointer to each parent so we can simply expand outward
        # the trick is that we need to go up and then consider up and down
        q = deque()
        q.appendleft((target, k))
        visited = set()  # Can only be used as we have unique vals otherwise this would be a dict
        result = []

        while q:
            node, dist = q.pop()

            visited.add(node.val)

            if dist == 0:
                result.append(node.val)
                continue
            else:
                for nei in (node.left, node.right, node.par):
                    if nei and nei.val not in visited:
                        q.appendleft((nei, dist - 1))

        return result


# My initial thought works like a charm it runs in O(N) time and space

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 20
# Was the solution optimal? This is optimal
# Were there any bugs? No
#  5 5 5 5 = 5
