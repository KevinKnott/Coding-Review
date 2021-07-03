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

# So let us serialize the array by moving across and adding the elements by a list with a left node being index * 2  away and right node being index * 2 + 1 away


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return

        # If we use a bfs we can create the resulting list as we go down
        result = []
        q = deque()
        q.appendleft(root)

        while q:
            node = q.pop()

            # Serialize the values into a string
            result.append(str(node.val) if node else 'none')

            if node:
                q.appendleft(node.left)
                q.appendleft(node.right)

        return result

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        # This is the more complicated of the two we need to go through and for every node go through the math a left node
        # being index * 2  away and right node being index * 2 + 1
        if not data:
            return

        root = TreeNode(int(data[0]))
        q = deque()
        q.appendleft(root)

        index = 1
        while q and index < len(data):
            # Pop the current node to append left and right if they exist
            node = q.pop()

            # Create a left node if it exists
            if data[index] != 'none':
                left = TreeNode(int(data[index]))
                node.left = left
                q.appendleft(left)

            index += 1

            # Create a right node if it exists
            if data[index] != 'none':
                right = TreeNode(int(data[index]))
                node.right = right
                q.appendleft(right)
            index += 1

        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

# Boo yeah my initial thought was to create a list that represents the bt but I realized by using a q we don't have to do complicated math all we have to do is increase the counters by one every
# time we look at the node

# This runs in o(N) but we also have to have O(N) space to store all possible None and values in the tree

# Score Card
# Did I need hints? Nope
# Did you finish within 30 min? 40 minutes
# Was the solution optimal? I believe so
# Were there any bugs? Not really
# 5 4 4 5 = 4.5
