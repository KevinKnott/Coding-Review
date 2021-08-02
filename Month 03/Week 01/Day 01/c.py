# Reverse Linked List II: https://leetcode.com/problems/reverse-linked-list-ii/

# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# I think that there are two solutions that come to mind a bfs where we backtrack the fliipping of the nodes
# or going through an iterative traversal and keep tracking of the connecting node and where the next node
# at the end is which seems a bit complicated but since we know the right bound it shouldn't be too hard


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if head is None:
            return

        # For this algo we need iterate through the list until we find the starting point
        cur = head
        prev = None

        # As we go across we will decrement the counters
        while left > 1:
            prev = cur
            cur = cur.next
            left, right = left - 1, right - 1

        # once we are here we know we need to current pointer for the connector
        # and the node that will become our last node
        tail, con = cur, prev

        # As we iterate through all of our numbers we will simply iteratively reverse
        while right > 0:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
            right -= 1

        # Once we are at the end of our rotation we need to determine
        # if we are at head meaning that con is None since we never moved
        # or we connect the connector to our previous value
        if con:
            con.next = prev
        else:
            head = prev

        # Since we kept the start of our reversal as the tail
        # we need to point it to whatever is left after the iterative reversal
        tail.next = cur

        return head


# Score Card
# Did I need hints? Nope
# Did you finish within 30 min? 10
# Was the solution optimal? This is a simple o(N) and o(1) that is quite simple after you think about
# how the pieces need to be connected
# Were there any bugs? None
# 5 5 5 5 = 5
