# Serialize and Deserialize Binary Tree: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.
# Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

# Definition for a binary tree node.
from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# So this problem is classified as hard but all it is just a simple dfs/bfs where you append nodes and nulls to a list


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return []

        q = deque()
        q.appendleft(root)
        result = []

        while q:
            node = q.pop()

            if node:
                result.append(str(node.val))
                q.appendleft(node.left)
                q.appendleft(node.right)
            else:
                result.append('null')

        return result

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return

        index = 1
        root = TreeNode(int(data[0]))
        q = deque()
        q.appendleft(root)

        while index < len(data) and q:
            node = q.pop()

            # Add left
            if data[index] != 'null':
                left = TreeNode(int(data[index]))
                node.left = left
                q.appendleft(left)

            index += 1

            # Add right
            if data[index] != 'null':
                right = TreeNode(int(data[index]))
                node.right = right
                q.appendleft(right)

            index += 1

        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

# This problem seems really confusing at first but it isn't too bad the only really tricky part is when deserializing
# we need to realize that we need to keep track of index as we don't want to try to parse too far and break things
# Other than that it is basically just a simple BFS parsing

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 10
# Was the solution optimal? This is optimal
# Were there any bugs? No
#  5 5 5 5 = 5
