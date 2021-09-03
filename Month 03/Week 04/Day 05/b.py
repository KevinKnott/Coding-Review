# All Nodes Distance K in Binary Tree: https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

# Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.
# You can return the answer in any order.

# Definition for a binary tree node.
from types import List
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# All we have to do for this problem is iterate through it twice once to set the parent attribute in a treenode
# and then again to do a bfs in both directions!


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not root:
            return []

        def markParent(node, parent):
            node.parent = parent

            if node.left:
                markParent(node.left, node)

            if node.right:
                markParent(node.right, node)

        markParent(root, None)

        q = deque()
        q.appendleft((target, 0))
        result = []
        visited = set()

        while q:
            node, level = q.pop()

            if node.val in visited or level > k:
                continue

            visited.add(node.val)

            if level == k:
                result.append(node.val)
                continue

            if node.parent:
                q.appendleft((node.parent, level + 1))

            if node.left:
                q.appendleft((node.left, level + 1))

            if node.right:
                q.appendleft((node.right, level + 1))

        return result

# Boom
# This works and runs in O(N) (2N) and uses O(N) space for the q

# Score Card
# Did I need hints? Y
# Did you finish within 30 min? 6
# Was the solution optimal? Y
# Were there any bugs? None
# 5 5 5 5 = 5
