# Binary Tree Maximum Path Sum: https://leetcode.com/problems/binary-tree-maximum-path-sum/

# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
# The path sum of a path is the sum of the node's values in the path.
# Given the root of a binary tree, return the maximum path sum of any path.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        return


# Score Card
# Did I need hints? Y
# Did you finish within 30 min? Y
# Was the solution optimal? Y although I messed up the thought process of how to solve the problem
# Were there any bugs?  I didn't really have any bugs
#  2 3 3 5 = 3.25
