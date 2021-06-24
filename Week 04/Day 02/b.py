# Symmetric Tree: https://leetcode.com/problems/symmetric-tree/

# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#  I have two thoughts on this problem recurse checking if the nodes of a traversal are == calling both sides in reverse
#  or using tow qs and iteratively going down either way


class Solution:
    def isSymmetric(self, root):
        def dfs(node1, node2):
            if not node1 and node2:
                return False
            if not node2 and node1:
                return False
            # The above is an xor to catch nodes that don't exist

            # Valid cases are if we both hit nulls at all leaf nodes
            if node1 is None and node2 is None:
                return True

            # Invalid if we catch a value that doesn't match
            if node1.val != node2.val:
                return False

            return dfs(node1.left, node2.right) and dfs(node1.right, node2.left)

        return dfs(root, root)

# This works quite well it is a bit confusing to think about but it runs in o(n) time and o(n) space

# As for the other approach I think it may be slightly faster but overall the big o is the same
    def isSymmetricIterative(self, root):
        q = deque()

        q.appendleft(root)
        q.appendleft(root)

        while q:
            # Get first two nodes the correspond to one from either of the two trees
            node1 = q.pop() if q else None
            node2 = q.pop() if q else None

            if not node1 and node2:
                return False
            if not node2 and node1:
                return False
            # The above is an xor to catch nodes that don't exist

            # Valid cases are if we both hit nulls at all leaf nodes
            if node1 is None and node2 is None:
                continue

            # Invalid if we catch a value that doesn't match
            if node1.val != node2.val:
                return False

            q.appendleft(node1.left)
            q.appendleft(node2.right)
            q.appendleft(node1.right)
            q.appendleft(node2.left)

        return True

# The above code works to be honest the iterative approach is almost assuredly faster
# as the internal stack is not used and we are in charge of the q

# Score Card
# Did I need hints? N
# Did you finish within 30 min? Y
# Was the solution optimal? Y (there is really no better way to do this)
# Were there any bugs? Not really although checking for an xor of the two nodes may have a slight improvement
# 4 5 5 5 = 4.75
