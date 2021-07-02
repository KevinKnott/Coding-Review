# Binary Tree Zigzag Level Order Traversal: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# My first thought on this problem is actually to create the levels in a bfs and pass a empty node to represent a break
# or to count the number of nodes added and just flip flop if you add left right or right left of node


class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
        if not root:
            return

        result = []
        q = deque()
        q.appendleft((root, 1))

        while q:
            nodesLeft = len(q)
            temp = deque()
            for _ in range(nodesLeft):
                node, level = q.pop()

                if level % 2 == 1:
                    temp.append(node.val)
                else:
                    temp.appendleft(node.val)

                if node.left:
                    q.appendleft((node.left, level + 1))
                if node.right:
                    q.appendleft((node.right, level + 1))

            result.append(temp)

        return result

# My first thought to change the order of how we append the nodes to the queue actually fails because I wasn't using the level that I am using now
# so it would switch but on the third round or so it would mess up. To fix this I just took advantage of the deque for appending to my list

# Now is this an optimal solution? I believe it would be while it is o(N) and o(N+W) where W is the widest width  I suppose that you could also do this
# with a dfs but honestly it would be convoluted and normally a level order or moving out from a fixed point is the main purpose of a BFS


# Score Card
# Did I need hints? N
# Did you finish within 30 min? 20
# Was the solution optimal? This is optimal
# Were there any bugs? See my first blurb after my code
#  5 5 5 3 = 4.5
