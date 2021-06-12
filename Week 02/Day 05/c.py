# Validate Binary Search Tree: https://leetcode.com/problems/validate-binary-search-tree/
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

#     The left subtree of a node contains only nodes with keys less than the node's key.
#     The right subtree of a node contains only nodes with keys greater than the node's key.
#     Both the left and right subtrees must also be binary search trees.

# This is a recursion dfs problem in which we keep track of the largest and smallest value we have seen before
# And we know if we go to the right we can't have anything smaller than the smallest
# and we know if we go to the left  we can't have anything larger than the largest

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# This works and is o(N) where n is the number of nodes
# but it is also o(n) space alternatively we could write this as an interative version with a stack
class Solution:
    def isValidBST(self, root):
        def dfs(node, smallest, largest):
            if node is None:
                return True

            if node.val < smallest:
                return False

            if node.val > largest:
                return False

            return dfs(node.left, smallest, node.val) and dfs(node.right, node.val, largest)

        return dfs(root, -float(inf), float(inf))


# Alternatively we could potentially use the fact that an in-order search of a bst results in a sorted list and if we find an element where the
# next element is > then the previous we return false but it is the same complexity and more confusing


# Score Card
# Did I need hints? Y for index math on getting the split point
# Did you finish within 30 min? Y
# Was the solution optimal? My initial solution is optimal however I needed to a bit of extra refactoring for using another metho
# Were there any bugs? I initially was off by one on length because of hitting -1  and not changing length with a minus 1
#  4 4 3 2 = 3.25
