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

# In this problem we are encoding and decoding a tree into a list. To do this we can simply use a BFS technique and anytime we see a None value we simply push on a string None
# Then to decode we do the same thing in reverse.


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        if not root:
            return ''

        encoded = []
        q = deque()
        q.appendleft(root)

        while q:
            node = q.pop()

            if node is None or node == "None":
                encoded.append("None")
            else:
                encoded.append(str(node.val))
                q.appendleft(node.left)
                q.appendleft(node.right)

        return ' '.join(encoded)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return

        data = data.split(' ')

        i = 1
        total = len(data)
        head = TreeNode(int(data[0]))

        q = deque()
        q.appendleft(head)

        while i < total and q:
            node = q.pop()

            # Append left
            if data[i] != 'None':
                left = TreeNode(int(data[i]))
                node.left = left
                q.appendleft(left)

            i += 1

            # Append right
            if data[i] != 'None':
                right = TreeNode(int(data[i]))
                node.right = right
                q.appendleft(right)

            i += 1

        return head

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

# So I am pretty sure I have the correct solution and it should run in O(N) and uses O(N) additional space


# Score Card
# Did I need hints? N
# Did you finish within 30 min? 12
# Was the solution optimal? Y
# Were there any bugs? N
# 5 5 5 5 = 5
