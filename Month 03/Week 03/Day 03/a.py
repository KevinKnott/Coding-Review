# Lowest Common Ancestor of a Binary Tree: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# In this problem we can do a dfs and keep an external track (or in parameters) of the whether we have found
# p or q and when we have found both and are returned to the node we simply return that node otherwise
# we return nothing

# The other possible solution is knowing that as soon as we have found p or q anything below it is irrelevant
# as we know at the very least that node is the parent if it is below. Then all we have to do is search the other
# side and if we find the other side we know that the node that sent it down to each side is the parent.


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

# In the above the worst case scenario is that we have to go down completely in the tree which is O(N) time
# and we use O(1) space as we are simply returning the result as soon as we find it and are not storing it

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 15
# Was the solution optimal? Oh yeah
# Were there any bugs? Nope
# 5 5 5 5 = 5
