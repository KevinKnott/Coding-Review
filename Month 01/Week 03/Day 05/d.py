# Reverse Linked List II: https://leetcode.com/problems/reverse-linked-list-ii/

# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Reversing is simple enough however we need to adapt the algorithm to handle a variable range based off of the values instead
# There is one edge case that I can think of where the head is the start of the reversing and two

class Solution:
    def reverseBetween(self, head, left, right):
        if not head:
            return None

        # Return if there is nothing to reverse
        if left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        pre = dummy

        # Traverse across the linked list until you find the reversing place
        for i in range(left - 1):
            pre = pre.next

        # Set previous to be None or whatever was before
        prev = None
        cur = pre.next
        for i in range(right - left + 1):
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        pre.next.next = cur
        pre.next = prev

        return dummy.next


# Score Card
# Did I need hints? N
# Did you finish within 30 min? Y
# Was the solution optimal? I believe that it is optimal as it runs in o(n) time and doesn't really use any space
# Were there any bugs? It took me a second to realize that left and right were indexes to reverse at and  not values
# 3 3 3 3 = 3
