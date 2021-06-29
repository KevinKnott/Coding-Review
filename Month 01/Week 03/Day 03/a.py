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

# My thought is to go down the path with a dfs and start counting once we have hit a node with no children
# Then every step up we add one and take the max of steps down or 1


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameter = 0

        def dfs(node):
            # If we hit a leaf node return 0
            if node is None:
                return 0

            # Get length to left and right of current node
            left = dfs(node.left)
            right = dfs(node.right)

            # If the length is greater than any so far make it the result
            self.diameter = max(self.diameter, left + right)
            # Return the max so far +1 for the current node (In case the longest diameter is met somewhere in the middle instead of going through the root)
            return max(left, right) + 1

        dfs(root)
        return self.diameter

# Score Card
# Did I need hints? Yes I forgot that I need to compare the diameter to the left and the right before including the next value up
# Did you finish within 30 min? 15 min
# Was the solution optimal? Oh yeah this is a o(N) solution every node is visited one and that makes our stack space o of (N) or logn if it is a balanced tree
# Were there any bugs? Yeah see the hint
#  3 5 5 3 = 4
