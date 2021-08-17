# Remove Linked List Elements: https://leetcode.com/problems/remove-linked-list-elements/

# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# So in this problem we need to remove extra nodes that have a value v
# to do this we have two different kinds removing them from the front
# as we have to update our head and removing from the middle in which we just skip
# a node


class Solution:
    def removeElements(self, head, val: int):
        while head and head.val == val:
            head = head.next

        if head is None:
            return

        cur = head
        while cur is not None:
            while cur.next and cur.next.val == val:
                cur.next = cur.next.next if cur.next.next else None
            cur = cur.next

        return head

# So the above works and runs in O(N) time and O(1) although technically we can make a slight modification
# and remove the nested while to make this slightly more efficient
    def removeElement(self, head, val):
        while head and head.val == val:
            head = head.next

        if head is None:
            return

        cur = head

        # Instead of checking the next val we simply update our prev to only update if it is not the val
        # we are checking for
        while cur is not None:
            if cur.val == val:
                prev.next = cur.next

            else:
                prev = cur
            cur = cur.next

        return head

# Score Card
# Did I need hints? Nope
# Did you finish within 30 min? 4 minutes
# Was the solution optimal? Yup this runs in o(n) time in worst case and uses o(1) space
# Were there any bugs? None
# 5 5 5 5 = 5
