# Symmetric Tree: https://leetcode.com/problems/symmetric-tree/

# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).


# for this problem all we have to do is simply do a dfs and check if the opposite node is the same and traverse the opposite way

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def dfs(node1, node2):
            if not node1 and node2:
                return False
            if not node2 and node1:
                return False
            # The above is an xor to catch nodes that don't exist

            if node1 is None and node2 is None:
                return True

            if node1.val != node2.val:
                return False

            return dfs(node1.left, node2.right) and dfs(node1.right, node2.left)

        return dfs(root, root)

# The above works and is pretty simple but to be honest the q would work better
# as for my above solutions we use the stack space and it is more heavy
# it runs in O(N) and use o(N) space

# Score Card
# Did I need hints? Nope
# Did you finish within 30 min? 10 min
# Was the solution optimal? See above
# Were there any bugs? None
# 5 5 5 5 = 5
