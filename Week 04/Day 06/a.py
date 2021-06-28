# Binary Tree Maximum Path Sum: https://leetcode.com/problems/binary-tree-maximum-path-sum/

# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
# The path sum of a path is the sum of the node's values in the path.
# Given the root of a binary tree, return the maximum path sum of any path.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def dfs(node):
            if node is None:
                return 0

            # Go down Left/right if it is negative we don't really need to consider it
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            # Check if you have a max path including this node as the root
            self.maxSum = max(self.maxSum, left + node.val + right)

            # Return only the max path not all three
            return max(left, right) + node.val

        self.maxSum = -float('inf')
        dfs(root)
        return self.maxSum

# Luckily I just did this problem yesterday so it was fresh in my head. The main thing to note in this problem is that we have 2 checks
# One is if the current subnode has the path through it or if the current node is in the path.
# To check for this we make sure that we get the max of the node as the passthrough and then return the max path (left/right) or 0
# Another tricky thing is that we need to not consider if we return just a negative number as our max sum step will grab the negative
# And not have the correct value if one side has a negative value

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 10 min
# Was the solution optimal? Yes this is optimal and runs in o(n) and o(1) time and space
# Were there any bugs? Nope no bugs for me
# 5 5 5 5 = 5
