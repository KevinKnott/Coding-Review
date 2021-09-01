# Add Two Numbers II: https://leetcode.com/problems/add-two-numbers-ii/

# You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

from types import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# For this problem we actually have a number of solutions the most optimal is probably just reversing
# both lists doing the math and then reversing the result as this will be O(N) and O(1).
# Alternatively you could do the math the normal way by going through the nodes converting them
# to numbers and then creating a list from the result they all use the same time complexity
# so in the end I am just going to do the reversal for the practice


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)

        result = self.add(l1, l2)

        # Optional if we need to keep the list in the other direction
        # l1 = self.reverse(l1)
        # l2 = self.reverse(l2)

        return self.reverse(result)

    def reverse(self, head):
        prev = None
        cur = head

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        return prev

    def add(self, l1, l2):
        dummy = ListNode()
        cur = dummy
        carry = 0

        while l1 or l2 or carry:
            temp = 0

            if l1:
                temp += l1.val
                l1 = l1.next

            if l2:
                temp += l2.val
                l2 = l2.next

            if carry:
                temp += carry

            carry, temp = divmod(temp, 10)

            cur.next = ListNode(temp)
            cur = cur.next

        return dummy.next

# EZ Peezy
# This runs in O(N) and uses O(1) additional space (technically it would use max(len(l1) + len(l2)) + 1 in the worst case )

# Score Card
# Did I need hints? Nope
# Did you finish within 30 min? 8
# Was the solution optimal? Yup
# Were there any bugs? None
# 5 5 5 5 = 5
