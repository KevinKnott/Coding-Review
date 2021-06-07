#  Invert Binary Tree:  https://leetcode.com/problems/invert-binary-tree/
# Given the root of a binary tree, invert the tree, and return its root.

# Okay this is another problem where we use a dfs solution except we should just be flipping as we go down
# Basic solution
class Solution:
    def invertTree(self, root):
        def dfs(root):
            if root:
                root.left, root.right = root.right, root.left

                dfs(root.left)
                dfs(root.right)

        dfs(root)
        return root

# Can we improve?
# we can probably remove the nested function and we can call the invert while we swap
# This was accepted and a little bit better


class Solution2:
    def invertTree(self, root):
        if root is None:
            return None

        root.left, root.right = self.invertTree(
            root.right), self.invertTree(root.left)

        return root

# Can we improve?
# we can probably remove the nested function and we can call the invert while we swap
# Also we could probably do this iteratively to reduce stack to a deque for improvements

# Score Card
# Did I need hints? Nope
# Did you finish within 30 min? Yup 10 min
# Was the solution optimal? Yes although I didn't write out the optimal version with the iterative but it is really the same thing
# Were there any bugs? Nope
#  5 5 5 5 = 5
