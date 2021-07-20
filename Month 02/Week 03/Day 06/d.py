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

# I think this is a simple problem where all we have to do is a dfs/bfs and put the value
# or null into the list we are creating or vice versa


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return []

        result = []

        q = deque()
        q.appendleft(root)

        while q:
            node = q.pop()

            if node is not None:
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

        # Create a bfs where we create the new nodes
        index = 1
        root = TreeNode(int(data[0]))
        q = deque()
        q.append(root)

        # While we are below the index and have values to parse
        while index < len(data) and q:
            # Pop off nodes
            node = q.pop()

            # Add the left node
            if data[index] != 'null':
                left = TreeNode(int(data[index]))
                node.left = left
                q.appendleft(left)

            # Move because we have parsed one more digit
            index += 1

            # Add the right node
            if data[index] != 'null':
                right = TreeNode(int(data[index]))
                node.right = right
                q.appendleft(right)

            # Move because we have parsed one more digit
            index += 1

        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

# Boo yeah the above works and runs in a simple o(N) for time and space. I dont believe there is a more optimal solution.
# this is because we have to parse every value to make sure it is serialized correctly

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 20
# Was the solution optimal? This is optimal
# Were there any bugs? No
#  5 5 5 5 = 5
