# Validate Binary Search Tree: https://leetcode.com/problems/validate-binary-search-tree/

# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

#     The left subtree of a node contains only nodes with keys less than the node's key.
#     The right subtree of a node contains only nodes with keys greater than the node's key.
#     Both the left and right subtrees must also be binary search trees.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# This problem boils down to keeping track of the range of a valid value in a bst
# so at every node we take a range -inf -> inf and update it depending on which node we move down
# then if we have anything that is outside of this range we know that we have an invalid number

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def dfs(node, left=-float('inf'), right=float('inf')):
            if not node:
                return True

            if node.val > left and node.val < right:
                return dfs(node.left,  left, node.val) and dfs(node.right, node.val, right)

            return False

        return dfs(root)

# The above works just peachy. This is really just a simple understanding of how a binary search tree works
# The above runs in O(N) and uses O(1) space

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 5
# Was the solution optimal? Yee
# Were there any bugs? None
# 5 5 5 5 = 5
