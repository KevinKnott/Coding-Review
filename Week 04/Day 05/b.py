# Binary Tree Maximum Path Sum: https://leetcode.com/problems/binary-tree-maximum-path-sum/

# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
# The path sum of a path is the sum of the node's values in the path.
# Given the root of a binary tree, return the maximum path sum of any path.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# So my initial intuition was to build a dfs straight down and it seems to work for the most part
# that being said the code is laking an overall best that is stored outside of our dfs
# this means that if ta sub tree has the most optimal path we will keep computing and ignore it

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return 0

            # So if this is negative we can just ignore it as we want max path
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            # update our result if the tree created from root the left and right is larger
            # our current result
            self.maxSum = max(self.maxSum, left + node.val + right)

            # otherwise we need to return the max path of left /right plus our nodfe
            return node.val + max(left, right)

        self.maxSum = -float('inf')
        dfs(root)

        return self.maxSum

# The above is optimal and runs in o(n) time and o(1) space the tricky part is actually determining
# which paths weneed to follow in this case we had to get the max result at every node of it
# and its paths to the left or right and the return the max of the biggest path up to that point
# it took me a minute to figure it out

# Score Card
# Did I need hints? N
# Did you finish within 30 min? Y 20 min
# Was the solution optimal? Y
# Were there any bugs?  I had one bug from when I was returning a complete path back up instead of the mac
# of the left or the right
# 5 5 5 4 = 4.75
