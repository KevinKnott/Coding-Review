# Convert Binary Search Tree to Sorted Doubly Linked List: https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/

# Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.
# You can think of the left and right pointers as synonymous to the predecessor and successor pointers in a doubly-linked list. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.
# We want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. You should return the pointer to the smallest element of the linked list.


# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# For this problem we will have to do a simple dfs and then as we go down we should store the node that we are push the current node to the next
# This is because as we go down the tree to the left we will get the prev node right then as we come back up that node should point
# to the next node

# Also the first time we reach the very end to the left we need to set it to the head and at the end point it to the last and vice versa to make it
# a circle

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if root is None:
            return

        self.first = None
        self.last = None

        # This is a basic in order traversal

        def dfs(node):
            if node is not None:
                # Traverse left side
                dfs(node.left)

                # If there is a node
                # Check if we have a last node so we can point it to the next node
                if self.last is not None:
                    self.last.right = node
                    node.left = self.last

                # One you have updated the pointer check if we need to update first
                else:
                    self.first = node

                self.last = node

                dfs(node.right)

        # Run through the automation
        dfs(root)

        # Point first to last and vice versa
        self.first.left = self.last
        self.last.right = self.first

        return self.first

# The above works pretty well as it is a simple dfs  with an in order traversal
# At the the only tricky part is figuring out when we need to update when we have the first node
# This will run in o(N) Time and space as we have to put every node on the stack and visit it

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 15N (45 or so)
# Was the solution optimal? See above
# Were there any bugs? Nope
# 5 5 5 5 = 5
