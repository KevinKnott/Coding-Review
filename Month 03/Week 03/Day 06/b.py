# Reverse Linked List II: https://leetcode.com/problems/reverse-linked-list-ii/

# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

from types import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# In this problem all we have to do is traverse until we find left and then go ahead and reverse every node up to the right
# the only trick to keep note of is if the head node is the left we will also need to reassing our head  node.


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head is None:
            return

        if left == right:
            return head

        cur = head
        prev = None

        # We want to keep the previous node so we go until left == 1 (indexed from 1 as well)
        while left > 1:
            prev = cur
            cur = cur.next
            left -= 1
            right -= 1

        # Now to reverse (we know the tail will end up in our cur pointer and that we need to connect the previous to the reversed nodes)
        tail, connection = cur, prev

        while right > 0:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
            right -= 1

        # Now we know if our connector is None that we actually started reversing at the first node so we will update head
        if connection is None:
            head = prev
        else:
            connection.next = prev

        # Now we need to make sure that our tail of the swapped node points to the next node
        tail.next = cur

        return head

# This runs in O(N) as we will only traverse once and uses O(1) as we simply are reversing in place
# I think you could have also solved this with backtracking but it is more complicated

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 10
# Was the solution optimal? Ye
# Were there any bugs? Ne
# 5 5 5 5 = 5
