# Lowest Common Ancestor of a Binary Tree: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# Medium

# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”


# class TreeNode:
def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

# My initial thought for this problem is to take a dfs and keep track of how many of the targets we have seen
# and when both return the values are seen return that node


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        def dfs(node):
            # If we reach a leaf return False
            if node is None:
                return False
            # if we have found a node we need to return
            # This may add confusion but basically we keep track of if we have found
            # left or right and if left/right is below the other we know the first node
            # in common is the top node either left or right
            if node == p or node == q:
                return node

            # otherwise
            # Continue going down each point
            left = dfs(node.left)
            right = dfs(node.right)

            # If we have found both nodes return the node as we have the answer
            if left and right:
                return node

            # if we find only one of the answers down the path return it so when
            # we get both we have an answer
            if left:
                return left
            if right:
                return right

        return dfs(root)

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 20
# Was the solution optimal? Y this will run in o(n) and o(n) because of the stack space that is required
# That being said i think you could write a more optimal solution using an iterative approach
# Were there any bugs? I didn't see any bugs
# 5 5 3 5 = 4.5
