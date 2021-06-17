# Merge Two Sorted Lists: https://leetcode.com/problems/merge-two-sorted-lists/

# Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# my initial thoughts for this problem is actually to do exactly as it says
# while i have both nodes compare otherwise append whatever is left

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0)
        cur = result

        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        if l1:
            cur.next = l1

        if l2:
            cur.next = l2

        return result.next

# Score Card
# Did I need hints? Nope
# Did you finish within 30 min? 4 minutes
# Was the solution optimal? Yup this runs in o(n+m) time in worst case and uses o(1) space
# Were there any bugs? None
# 5 5 5 5 = 5
