# Invert Binary Tree: https://leetcode.com/problems/invert-binary-tree/

# Given the root of a binary tree, invert the tree, and return its root.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# This problem seems simple enough you go down the tree with a dfs and at every node
# you point the children to the opposite side

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:

        def dfs(node):
            if node:
                # Swap sides
                node.left, node.right = node.right, node.left
                # Traverse down
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        return root


# The above solution is very simple but it runs in O(N) time and O(1) space as we are simply editing in place


# Score Card
# Did I need hints? N
# Did you finish within 30 min?5
# Was the solution optimal? Yeah
# Were there any bugs? None
# 5 5 5 5 = 5
