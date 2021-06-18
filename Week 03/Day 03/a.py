#  Diameter of Binary Tree: https://leetcode.com/problems/diameter-of-binary-tree/

# Given the root of a binary tree, return the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
# The length of a path between two nodes is represented by the number of edges between them.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        return

# Score Card
# Did I need hints? N (But the second solution did)
# Did you finish within 30 min? No 1:30
# Was the solution optimal? My initial solution is optimal however I messed up the initial coding of it
# Were there any bugs? I forgot that since it is possible to have [[[[]]]] I need to actually recurse
#  4 1 2 1 = 2
