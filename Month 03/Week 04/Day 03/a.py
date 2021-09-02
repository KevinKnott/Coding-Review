# Reverse Nodes in k-Group: https://leetcode.com/problems/reverse-nodes-in-k-group/

# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
# You may not alter the values in the list's nodes, only nodes themselves may be changed.

from types import Optional

# Definition for singly-linked list.

# In this problem we are asked to develop a solution in which every k nodes we rotate the linked list
# This problem is solved pretty easily in a recursive manor. We will count up to k nodes
# and then we will reverse those k at the end we create the new head as the returned result
# and then we will use the head (which will now be the last element) to attach to the next
# call of reverseKgroup this is an O(N) time and O(N/k) space we could reduce space to one
# with a complicated iterative approach of the same solution


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 0
        cur = head

        while cur and count < k:
            cur = cur.next
            count += 1

        # Do we have k grouping
        if count == k:
            newHead = self.reverse(head, k)

            # Head is now the tail as we reversed
            # cur is now one past where the k grouping is
            head.next = self.reverseKGroup(cur, k)

            return newHead

        return head

    def reverse(self, head, k):
        prev, cur = None, head

        for _ in range(k):
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        return prev


# So the above works and runs like I said (6 min)
# Now for the more optimal solution:


    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        lastTail = None
        result = None

        while cur:
            # Sam as before we need to update our head
            # but our last solution will be in lastTail or result
            cur = head
            count = 0

            while cur and count < k:
                cur = cur.next
                count += 1

            # Do we have k grouping
            if count == k:
                reversed = self.reverse(head, k)

                # First run so we update head pointer
                if not result:
                    result = reversed

                # So this is the same as before except that we need to point to the lastTail
                # Head is now the tail as we reversed
                # cur is now one past where the k grouping is
                if lastTail:
                    lastTail.next = reversed

                # The node that is the lastTail is the head node as we are updating head
                # and last tail at every iteration
                lastTail = head
                # And just like before cur must be the node after the ndoes we just swapped
                # so it has to be cur
                head = cur

        # Once we don't hit a k grouping we must still attach the last node if it exists
        if lastTail:
            lastTail.next = head

        return result if result else head


# Boom this is working it seems a bit complicated but it is more or less the same code as before
# just rearranged to make sure we don't need to use a stack

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 6 and 15
# Was the solution optimal? Y
# Were there any bugs? N
# 5 5 5 5 = 5
