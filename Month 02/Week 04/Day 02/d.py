# Lowest Common Ancestor of a Binary Tree: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# In this problem we will simply traverse until we find either node and use a class variable to keep track
# once we have found both we will simply set the result as the node we last checked

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if node:
                if node == p or node == q:
                    return node

                left = dfs(node.left)
                right = dfs(node.right)

                if left and right:
                    return node
                if left:
                    return left
                if right:
                    return right

        return dfs(root)

# The above works and runs in O(N) time and space

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 10
# Was the solution optimal? This is optimal
# Were there any bugs? No
#  5 5 5 5 = 5
