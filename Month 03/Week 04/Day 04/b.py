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

# In this problem all we have to do is a dfs as a the left most node will be the head and the right most node will be the tail
# then all we have to do is keep two variables outside of the loop or in the parameters. They will keep track of the prev
# node and the first node. That way we can link prev to next and cur to prev as well as at the very end point first
# to last and vice versa


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return

        self.first, self.prev = None, None

        def dfs(node):
            if node.left:
                dfs(node.left)

            if self.first is None:
                self.first = node

            if self.prev:
                self.prev.right = node
                node.left = self.prev

            self.prev = node

            if node.right:
                dfs(node.right)

        dfs(root)

        self.first.left = self.prev
        self.prev.right = self.first
        return self.first


# Eyyy another smooth problem. This one is relatively easy if you consider what needs to be done
# It runs in O(N) and uses O(1) space.

#  Score Card
# Did I need hints? N
# Did you finish within 30 min? 10
# Was the solution optimal? Y
# Were there any bugs? N
# 5 5 5 5 = 5
