# Reverse Linked List II: https://leetcode.com/problems/reverse-linked-list-ii/

# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:

        # Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# So my intial thought for this problem is that we have a standard reversing of a linked list
# There are two distinctions until we get to the node we simply keep iterating across
# Then once we found the starting place we need to connect what we had before by storing a
# pointer to the prev of where we started then we can go ahead and reverse until we reach right
# then if we had a previous point it to the next otherwise update our head
# after that we simply return the new head/ old head


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head:
            return None

        cur = head
        prev = None

        while left > 1:
            prev = cur
            cur = cur.next
            left, right = left - 1, right - 1

        tail, con = cur, prev

        while right > 0:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
            right -= 1

        if con:
            con.next = prev
        else:
            head = prev

        tail.next = cur

        return head

# Score Card
# Did I need hints? Nope
# Did you finish within 30 min? 16 min
# Was the solution optimal? This solution runs in o(n) time and o(1) space I believe it is optimal as we have no way of reversing without visiting all the nodes
# Were there any bugs? I forgot that we need to keep track of whether the head swaps as part of the traversal
# 4 4 5 5 = 4.5
