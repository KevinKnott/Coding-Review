# Binary Tree Zigzag Level Order Traversal: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

from collections import deque
from types import Optional, List

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# This problem seems rather difficult but it turns out that you simply can do a level order search
# but instead of always appending the result on the right or left side we can swap by using a
# double ended queue


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        curLevel = deque()
        level = 1
        result = []

        curLevel.appendleft(root)

        while curLevel:
            temp = deque()
            for _ in range(len(curLevel)):
                node = curLevel.pop()

                if node.left:
                    curLevel.appendleft(node.left)
                if node.right:
                    curLevel.appendleft(node.right)

                if level % 2 == 1:
                    temp.append(node.val)
                else:
                    temp.appendleft(node.val)

            # Once you have added the level in whatever order using temp
            # record it to result
            result.append(temp)
            level += 1

        return result

# The above works and runs in O(N) time and space


# Score Card
# Did I need hints? N
# Did you finish within 30 min? 8
# Was the solution optimal? Y
# Were there any bugs? N
# 5 5 5 5 = 5
