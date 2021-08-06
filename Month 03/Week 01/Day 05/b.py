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

# Okay this problem seems a bit crazy but we can combine another problem that I have seen where we get the longest path
# with this problem basically at any node in the tree we need to  dfs down and calculate the value of keeping left
# or right path sum + node or if the three combined are the max but the problem is we can return both
# so we will take advantage of the class to keep a global max

# Also for negative numbers we should consider not even taking it by saying take the max( dfs(left), 0)


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.result = -float('inf')

        def dfs(node):
            if node is None:
                return 0

            # Remember to cut off negatives
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            # Get the max of left + root + right at every node
            self.result = max(self.result, left + node.val + right)

            return max(left, right) + node.val

        dfs(root)
        return self.result

# Boo yeah I absolutely crushed this problem basically it is a dfs with speciallized pruning
# This will run in O(N) and uses O(1) space

# Score Card
# Did I need hints? Y
# Did you finish within 30 min? 10
# Was the solution optimal? Yeah
# Were there any bugs?  IForgot to intialize result to -inf
# 5 5 5 5 = 5
