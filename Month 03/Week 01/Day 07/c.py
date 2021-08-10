# Reverse Nodes in k-Group: https://leetcode.com/problems/reverse-nodes-in-k-group/

# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
# You may not alter the values in the list's nodes, only nodes themselves may be changed.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# So for this problem I think that all we have is our classic reversal problem except
# we need to use recursion after every time we reverse so that we can swap every k nodes


class Solution:
    def reverseKGroup(self, head, k: int):
        # we need to find out if there are k nodes to swap
        count = 0
        cur = head
        while cur and count < k:
            cur = cur.next
            count += 1

        if count == k:
            # then we swap from head to k
            newHead = self.reverse(head, k)

            # and keep the cur which be at the end of the reversal and only the unprocessed values and our tail will be head
            # we will then call reverseKgroup for head.next (we use cur as the next spot)
            head.next = self.reverseKGroup(cur, k)
            return newHead

        return head

    # Basic reversal

    def reverse(self, head, k):
        prev, cur = None,  head

        for _ in range(k):
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        return prev


# This problem takes a bit of thinking but isn't too hard. I highly advise drawing out this problem as it really does help quite a bit
# The reversal isn't too complicated but thinking of how the values change is hard otherwise

# The above runs in O(N) and uses o(N/K) space for the stack. I think there is probably an optimization of this problem where
# we dont have recursion but I think it would be rather complicated.

# Score Card
# Did I need hints? Nope
# Did you finish within 30 min? 10 min
# Was the solution optimal? Optimal for time not space. I don't have a lot of time today
# Were there any bugs? None
# 5 5 3 5 = 4.5
