# Binary Tree Zigzag Level Order Traversal:https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# In this problem we will take advantage of the fact that we need to do a level order bfs but we need to push on the
# values of the result separately to get the right result as we add l->r or r<-l based on the depth


class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
        if not root:
            return

        result = []
        q = deque()
        q.append(root)
        level = 1

        while q:
            temp = deque()
            for _ in range(len(q)):
                node = q.pop()

                if node.left:
                    q.appendleft(node.left)

                if node.right:
                    q.appendleft(node.right)

                if level % 2 == 1:
                    temp.append(node.val)
                else:
                    temp.appendleft(node.val)

            result.append(temp)
            level += 1

        return result

# The above works like a charm the basic strategy is to do a level order traversal in the same order but know that we can swap around
# how our result gets value by using a deque to intelligently add to the right or left based on the level

# Score Card
# Did I need hints? Nope
# Did you finish within 30 min? 20 min
# Was the solution optimal? This is optimal as it runs in O(N) time and space
# Were there any bugs? None
# 5 5 5 5 = 5
