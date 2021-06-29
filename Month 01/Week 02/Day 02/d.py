# 206. Reverse Linked List: https://leetcode.com/problems/reverse-linked-list/
# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Simply just do it


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return

        prev, cur = None, head
        while cur.next is not None:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        cur.next = prev
        return cur

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 10
# Was the solution optimal? This is optimal although I suppose you could recurse which would be worse
# Were there any bugs? I forgot to check if node was null at the start
#  5 5 5 4 = 4.75
