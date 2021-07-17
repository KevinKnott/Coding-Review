# Add Two Numbers: https://leetcode.com/problems/add-two-numbers/

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# This problem is made easier by the fact that we the last number first
# this means we can at any step if l1/l2/carry exist add that value up and overwrite l1 or add l2 or add carry

# O(N) to create node as you go o(1) if we used longer l1/l2 which is an extra o(n) check

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        a, b = l1, l2
        result = ListNode()
        cur = result

        while a or b or carry == 1:
            value = 0
            # Count up a+b+carry
            if a:
                value += a.val
                a = a.next
            if b:
                value += b.val
                b = b.next
            if carry:
                value += carry

            # create carry over
            carry, value = divmod(value, 10)

            # Create new node
            cur.next = ListNode(value)
            cur = cur.next

            # go to next
            # if a:
            #     a = a.next
            # if b:
            #     b = b.next

        return result.next


# Score Card
# Did I need hints? N
# Did you finish within 30 min? 8
# Was the solution optimal? Yee
# Were there any bugs?  No
# 5 5 5 5 = 5
