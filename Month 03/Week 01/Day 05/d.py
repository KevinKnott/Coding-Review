# Range Sum of BST: https://leetcode.com/problems/range-sum-of-bst/

# Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# So the naive solution is to go through the whole entire tree and check if the node is between low and high and add it if it is
# which runs in O(N) which is pretty much optimal but to improve this we can use what we know about bst and not go to the left of low
# and to not go to the right of high which helps in the average case

class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        self.result = 0

        def dfs(node):
            if node.val >= low and node.val <= high:
                self.result += node.val

            if node.left and node.val > low:
                dfs(node.left)
            if node.right and node.val < high:
                dfs(node.right)

        dfs(root)
        return self.result


# Boom I started with the basic version and then improved the alog a little bit by not going down any farther if
# we hit the ends of the range this runs in O(N) and because of the stack we also store o(N) space

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 7
# Was the solution optimal? This is optimal
# Were there any bugs? No
#  5 5 5 5 = 5
