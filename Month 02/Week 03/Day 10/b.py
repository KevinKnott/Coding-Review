# Remove Linked List Elements: https://leetcode.com/problems/remove-linked-list-elements/

# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Simple removal separate out removing from the front because we have to move head
# and removal from between the list


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # Remove from the head of a list
        cur = head
        while cur is not None and cur.val == val:
            cur = cur.next

        # Update head
        head = cur

        # Loop to the end
        while cur is not None:
            # If we see val
            if cur.val == val:
                # push over it
                prev.next = cur.next
            else:
                # Otherwise we need to update our prev
                prev = cur
            # Continue looping
            cur = cur.next

        return head

# The above works! It runs in o(N) time and o(1) space there isn't anything especially tricky about this problem
# you just need to make sure you understand the different tops of removing a node from a linked list

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 9
# Was the solution optimal? Yup
# Were there any bugs? Nope
# 5 5 5 5 = 5
