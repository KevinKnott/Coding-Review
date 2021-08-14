# Diameter of Binary Tree: https://leetcode.com/problems/diameter-of-binary-tree/

# Given the root of a binary tree, return the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
# The length of a path between two nodes is represented by the number of edges between them.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Okay for this problem we will need to do a dfs down to every end node and as we come up we will take the max
# of every left or right + 1 or the left + right for the mid node we will store the max in a class var
# to make our life easy


class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        self.maxDiameter = 0

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            self.maxDiameter = max(self.maxDiameter, left + right)

            return max(left, right) + 1

        dfs(root)
        return self.maxDiameter

# Boo yeah this works and basically is like a lot of other problems in trees like find max path sum where you need to selectively take
# possible paths and determine if the max is with the node you are at and the left and right or the bigger of left/right and the current
# node

# This will run in O(N) time and uses O(1) space


# Score Card
# Did I need hints? N
# Did you finish within 30 min? 5
# Was the solution optimal? This is optimal
# Were there any bugs? No
#  5 5 5 5 = 5
