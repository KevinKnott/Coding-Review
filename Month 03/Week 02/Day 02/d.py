# Binary Tree Right Side View: https://leetcode.com/problems/binary-tree-right-side-view/

# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

# Definition for a binary tree node.

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# In this problem what we have is a level order traversal in which we record the last element
# There are a couple ways to do this one with push a None val at the end of every level
# and keeping prev. Or you could just create the level as a new q and when the q has one element
# you push it onto the result


class Solution:
    def rightSideView(self, root):
        if not root:
            return

        result = []
        nextLevel = deque()
        nextLevel.appendleft(root)

        while nextLevel:
            curLevel = nextLevel
            nextLevel = deque()

            while curLevel:
                cur = curLevel.pop()

                if cur.left:
                    nextLevel.appendleft(cur.left)
                if cur.right:
                    nextLevel.appendleft(cur.right)

                if len(curLevel) == 0:
                    result.append(cur.val)

        return result

# Easy peasy lemon squeezy. This is a pretty basic level order traversal with a bfs the only trick is making sure
# you are resetting the nextLevel as lists  are pass by reference

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 10
# Was the solution optimal? This is optimal
# Were there any bugs? No
# 5 5 5 5 = 5
