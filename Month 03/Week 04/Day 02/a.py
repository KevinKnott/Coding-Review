# Binary Tree Right Side View: https://leetcode.com/problems/binary-tree-right-side-view/

# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

from collections import deque
from types import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# For this problem all we need to do is traverse through the tree using a level order search and keep track of the last element
# that way we can add it to a separate list


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return

        nextLevel = deque()
        nextLevel.appendleft(root)
        result = []

        while nextLevel:
            curLevel = nextLevel
            nextLevel = deque()
            node = None

            while curLevel:
                node = curLevel.pop()

                if node.left:
                    nextLevel.appendleft(node.left)
                if node.right:
                    nextLevel.appendleft(node.right)

            # if node:
            result.append(node.val)

        return result

# The above works and runs in O(N) time and uses O(D) space where d is the diameter of the tree

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 6
# Was the solution optimal? Y
# Were there any bugs? N
# 5 5 5 5 = 5
