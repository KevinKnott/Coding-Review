# Convert Binary Search Tree to Sorted Doubly Linked List: https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/

# Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.
# You can think of the left and right pointers as synonymous to the predecessor and successor pointers in a doubly-linked list. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.
# We want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. You should return the pointer to the smallest element of the linked list.


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# So my initial thought for this problem is that we can go through the bst and convert
# add nodes to a deque left in front then right in back

# Once all the nodes are in order you can loop through and update the pointers

# I think it actually may be better to use a list and do a dfs


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return

        self.last, self.first = None, None

        def dfs(node):
            if node:
                # Go down the left side
                dfs(node.left)

                # If we have seen a node before we need to link it
                if self.last:
                    self.last.right = node
                    # We also need to link our current node to the previous
                    node.left = self.last

                # Otherwise we are as far left as we can go!
                else:
                    # So we need to set the start of the list
                    self.first = node

                # We also need to set the last node as we come back up the recursion
                self.last = node
                # Now we go down the right
                dfs(node.right)

        dfs(root)

        # Once we are at the very end we need to make this a cirular dfs
        self.first.left = self.last
        self.last.right = self.first
        return self.first

# So honestly after looking at the dfs we can probably update pointers as we go

# This is actually a pretty easy problem. It is literally a dfs except you can track the previous node (and we know that we can) update the pointers as
# we come back up the recursion

# This will run in O(n) time and o(n) space as we have to put all the nodes onto the stack at some point

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 22 min
# Was the solution optimal? This is optimal since we have to visit every node and update all the pointers and this is done in o(n) time and space
# Were there any bugs? I forgot to close off the circularly linked list at first
# 4 5 5 3 =  4.25
