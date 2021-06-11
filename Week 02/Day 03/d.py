# Add Two Numbers: https://leetcode.com/problems/add-two-numbers/

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# This is a pretty simple solution you create the nodes as you go along
# Add them up (including carryover) change node val
# increment lists and boom done
# This is an o(n) where n is the max(len(l1), len(l2)) and o(n) space with the same condition
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0)
        head = ListNode(0)
        head.next = result
        carryOver = 0

        while l1 or l2 or carryOver:
            cur = ListNode(0)
            if l1 and l2:
                temp = l1.val + l2.val + carryOver
            elif l1 is None and l2 is not None:
                temp = l2.val + carryOver
            elif l1 is not None and l2 is None:
                temp = l1.val + carryOver
            else:
                temp = carryOver

            carryOver, cur.val = divmod(temp, 10)
            result.next = cur
            result = result.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return head.next.next

# Is there an optimization for space?
# there in fact is you can go through the above except you keep track of prev l1 and append the new value over the existing node and then
# return that from the sentinel node
    def addTwoNumbersSpaceOptimize(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        head.next = l1
        prev = head
        carryOver = 0

        while l1 or l2 or carryOver:
            # Pick cur to be whatever node exists
            cur = l1 if l1 else l2
            if l1 and l2:
                temp = l1.val + l2.val + carryOver
            elif l1 is None and l2 is not None:
                temp = l2.val + carryOver
            elif l1 is not None and l2 is None:
                temp = l1.val + carryOver
            else:
                temp = carryOver
                cur = ListNode(1)

            carryOver, cur.val = divmod(temp, 10)
            prev.next = cur
            prev = prev.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return head.next

# I think that I could improve the way this works because it is kind of a burden to check each condition
# we could probably check if exist then add value and increment to clean this up a bit

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 10
# Was the solution optimal? My initial is optimal for time but not space and the second one is fully optimal
# Were there any bugs? I forgot that I need to create a new node if the other two nodes didn't exist and we have a carry over
#  5 5 5 4 = 4.75
