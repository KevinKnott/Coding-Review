# All Nodes Distance K in Binary Tree: https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

# Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.
# You can return the answer in any order.

# Definition for a binary tree node.

from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# This problem I think is relatively easy all we have to do is go through the tree twice
# once by dfs to update add parent pointers and then once again with a bfs (bidirectional)
# to find anything n nodes away


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int):
        def addParent(node, parent):
            if node:
                node.parent = parent

                addParent(node.left, node)
                addParent(node.right, node)

        addParent(root, None)

        q = deque()
        q.appendleft([target, 0])
        visited = set()
        result = []

        while q:
            node, level = q.pop()

            if node in visited or node is None:
                continue

            visited.add(node)

            if level == k:
                result.append(node.val)
                continue
            else:
                q.appendleft([node.parent, level + 1])
                q.appendleft([node.left, level + 1])
                q.appendleft([node.right, level + 1])

        return result

# I was dead on this works in O(N) and o(N)

# Score Card
# Did I need hints? Nope
# Did you finish within 30 min? 5 minutes
# Was the solution optimal? Yup
# Were there any bugs? None
# 5 5 5 5 = 5
