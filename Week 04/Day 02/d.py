#  Lowest Common Ancestor of a Binary Tree: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Simple solution is to take a recursive decent until you have p or q  and save that path
# Once you have saved both traverse down the node until you find the first mismatch


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        self.pPath, self.qPath = [], []

        def dfs(node, path=[]):
            if self.pPath != [] and self.qPath != []:
                return
            if node.val == p.val:

                self.pPath = path[:] + [node]
            if node.val == q.val:
                self.qPath = path[:] + [node]

            if node.left:
                dfs(node.left, path + [node])
            if node.right:
                dfs(node.right, path + [node])

        dfs(root)
        i = 0
        while i < len(self.qPath) and i < len(self.pPath) and self.qPath[i].val == self.pPath[i].val:
            i += 1

        return self.qPath[i-1]

# Okay so this solution works however it is very inefficient as I didn't realize we were supposed to return the actual node of the result
# So this ends  up storing the o(n) nodes and runs in o(n) time (although it is split between the finding path and parsing common)

# How do we improve then well instead of actually tracking the whole path we can use recursion and keep track of when we find both nodes
# and we return that node from dfs
    def lowestCommonAncestor(self, root, p, q):
        def dfs(node):
            if node is None:
                return False
            if node == p or node == q:
                return node

            left = dfs(node.left)
            right = dfs(node.right)

            if left and right:
                return node
            elif left:
                return left
            else:
                return right

        return dfs(root)

# This ends up working and is faster than most although in worst case it is still o(N) for time and space
# You could also make an approach where you keep track of a pointer to the parent node which I should probably explore

# Score Card
# Did I need hints? Nope
# Did you finish within 30 min? N
# Was the solution optimal? I ended up with an optimal solution
# Were there any bugs? Yes I mentioned it at the end of my first solution also it took me a second to realize I needed to
# track both paths down and mark them
# 5 3 4 2 = 3.5
