# Reverse Nodes in k-Group: https://leetcode.com/problems/reverse-nodes-in-k-group/

# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
# You may not alter the values in the list's nodes, only nodes themselves may be changed.

# Definition for singly-linked list.
from types import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# The easiest solution to this problem is actually using recursion to move down the list until you reach k nodes
# at that point pass off the list to a reversal. When it gets back you  Can update the head and then point the
# tail node (which is now head) to the next recursion of the next head (cur)


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 0
        cur = head

        while cur and count < k:
            cur = cur.next
            count += 1

        if count == k:
            newHead = self.reverse(head, k)
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

# So we have crushed this problem although there is an iterative approach to this but it is rather more convulted
# but basically you use an if statement to check if you update the actual head or a connection node

# The current solution runs in O(N) time and space as we have to use a recursive stack
# but the other solution I mentioned would run in O(1) space


# Score Card
# Did I need hints? N
# Did you finish within 30 min? 10
# Was the solution optimal? This is optimal
# Were there any bugs? No
#  5 5 5 5 = 5
