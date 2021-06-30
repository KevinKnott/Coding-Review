# Range Sum of BST: https://leetcode.com/problems/range-sum-of-bst/

# Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

# This problem is simple as all we really need to do is a dfs where we add the some of every node if it is between the range this would run in o(n) and probably isn't the best
# we know that this tree is in order so we can actually only go down nodes that are within the range don't go lower than left and higher than right it is still o(n) however
# it will have slightly better performance

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def dfs(node):
            # figure out if we can go down to the left
            if node:
                self.result += node.val if low <= node.val and node.val <= high else 0
                if node.val > low:
                    dfs(node.left)
                if node.val < high:
                    dfs(node.right)

        self.result = 0
        dfs(root)
        return self.result

# The slight optimization that I mentioned moved my performance to the top 98% on this problem from 47 %
# So knowing about how binary search tree works really does help although it is o(n) for space and time

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 10
# Was the solution optimal? This is optimal
# Were there any bugs? No
#  5 5 5 5 = 5
