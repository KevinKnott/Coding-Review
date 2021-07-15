# Diameter of Binary Tree: https://leetcode.com/problems/diameter-of-binary-tree/

# Given the root of a binary tree, return the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
# The length of a path between two nodes is represented by the number of edges between them.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Okay so this problem is looking for the longest possible paths through a tree. This seems like a simple dfs problem where we check
# the left side the right side and either take left + Mid + right or mid + max(left, right)  but mid is ignored as we have a path of x - 1

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.result = 0

        def dfs(node):
            # When the node is empty we can return there is no path so our result is 0
            if node is None:
                return 0

            # Traverse both sides
            left = dfs(node.left)
            right = dfs(node.right)

            # Compare the whole path at each node
            self.result = max(self.result, left + right)

            # move up 1 node plus whatever path was highest to this point
            return 1 + max(left, right)

        dfs(root)
        return self.result

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 10
# Was the solution optimal? Yup this is optimal o(N) and o(N) as we have to traverse every node with a stack
# Were there any bugs? 0 bugs for me today
# 5 5 5 5 = 5
