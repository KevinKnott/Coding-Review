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

# This problem seems hard intitially until you realize with a dfs you get the correct order going from left most node to right most node
# All we have to do is update the self.left to point to the previous node somehow. Oh and we should also grab the most deep left node
# as our first node. Once we do these two things we should have a pretty solid solution


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return

        self.start = None
        self.previous = None

        def dfs(node):
            if node is not None:
                dfs(node.left)

                if self.previous is None:
                    self.start = node
                else:
                    # Assign previous
                    self.previous.right = node
                    node.left = self.previous

                self.previous = node
                dfs(node.right)

        dfs(root)

        # Point ends to each other
        self.start.left = self.previous
        self.previous.right = self.start

        return self.start

# Aww snap basic tree and pointer manipulation right here this runs in O(N) and uses o(1) space

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 15
# Was the solution optimal? Y
# Were there any bugs? Nope
# 5 5 5 5 = 5
