# 203. Remove Linked List Elements: https://leetcode.com/problems/remove-linked-list-elements/
# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

# Do the following:
# simply check if node.next.val == val
# if it does skip over that node
# The edge case here is if head is null but we can create a new node and point the node.next to the head


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# This is an o(n) time and o(1) space complexity
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        result = ListNode(0)
        result.next = head

        prev, cur = result, head
        while cur:
            if cur.val == val:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next

        return result.next

    # Can we improve this? technically you could make this more efficient by cutting out this result node and instead doing
    # two operations one remove all 6's at the beginning and then do what we did
    def removeElementsBetter(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return

        while head and head.val == val:
            head = head.next

        # So we know for a fact that we aren't at our value right
        # This means our prev node can be the start of the list
        # and we can update as we go through
        prev, cur = head, head
        while cur:
            if cur.val == val:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next

        return head


# Score Card
# Did I need hints? N
# Did you finish within 30 min? Y
# Was the solution optimal? Y
# Were there any bugs? Y  (no support for max heaps made me use negatives and I forgot to handle them properly)
#  2 1 3 4 = 2.5
