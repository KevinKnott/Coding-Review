# Diameter of Binary Tree: https://leetcode.com/problems/decode-ways/
# Given the root of a binary tree, return the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
# The length of a path between two nodes is represented by the number of edges between them.

# Initial thought is to create a dfs where you have the value of left + 1 + right


class initial():
    def diameter(self, root):
        self.maxDiameter = -float('inf')
        self.dfs(root)
        return self.maxDiameter

    def dfs(self, root):
        if not root:
            return 0

        left = self.dfs(root.left)
        right = self.dfs(root.right)

        self.maxDiameter = max(self.maxDiameter, left + right)
        return max(left, right) + 1


# Score Card
# Did I need hints? Y
# Did you finish within 30 min? Y
# 20
# Was the solution optimal yes
# Were there any bugs
# Unfortunately i started my initial thought finding the max distance from top down not bottom up
#  3 3 4 3 = 3.25
