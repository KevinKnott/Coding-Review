# Symmetric Tree: https://leetcode.com/problems/symmetric-tree/

# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# In this problem will take the tree and at every point make sure if we swap the left and the right
# that they both return the reccurnce relationship that they are equal (the left and right being swapped)


class Solution:
    def isSymmetric(self, root):
        if root is None:
            return

        def swapSides(node1, node2):
            if node1 and node2:
                return node1.val == node2.val and swapSides(node1.left, node2.right) and swapSides(node1.right, node2.left)
            if node1 and not node2:
                return False
            if node2 and not node1:
                return False

            return True

        return swapSides(root, root)

# This works and is basically making sure you understand how exactly you can move through trees with a recurrence
# Our code runs in O(N) as it will have to visit every node

# Score Card
# Did I need hints? Y
# Did you finish within 30 min? 5
# Was the solution optimal? Y
# Were there any bugs? N
# 5 5 5 5 = 5
