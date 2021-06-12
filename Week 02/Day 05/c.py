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


class Solution:
    def isValidBST(self, root):
        return

# Score Card
# Did I need hints? Y for index math on getting the split point
# Did you finish within 30 min? Y
# Was the solution optimal? My initial solution is optimal however I needed to a bit of extra refactoring for using another metho
# Were there any bugs? I initially was off by one on length because of hitting -1  and not changing length with a minus 1
#  4 4 3 2 = 3.25
