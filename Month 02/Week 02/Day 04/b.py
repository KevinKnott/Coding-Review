# Binary Tree Right Side View: https://leetcode.com/problems/binary-tree-right-side-view/

# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#  This solution is pretty simple if we do a bst and put a maker at the end of every level (or create a new q )
#  we can simply append the last node we saw and return that list


class Solution:
    def rightSideView(self, root: TreeNode):
        if root is None:
            return

        nextLevel = deque()
        nextLevel.appendleft(root)
        result = []

        while nextLevel:
            curLevel = nextLevel
            nextLevel = deque()

            while curLevel:
                node = curLevel.pop()

                if node.left:
                    nextLevel.appendleft(node.left)
                if node.right:
                    nextLevel.appendleft(node.right)

            result.append(node.val)

        return result

# Man we are on a speed run today! This is an optimal O(N) time algo where we do a simple bfs
# it takes o(N) space as well which I believe is optimal as you have to visit every node in the case
# That the right most node is oon the bottom left

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 10 min
# Was the solution optimal? See above
# Were there any bugs? Nope
# 5 5 5 5 = 5
