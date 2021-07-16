# Reverse Linked List: https://leetcode.com/problems/reverse-linked-list/

# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# I have recently done a lot of this there are two solutions the recursive and iterative approach
# while the recursive solutions is simpler recursion is confusing to a lot of people so I will
# code the easier iterative solution

# Basically we will keep a pointer to the prev node and the current node
# With this we will get the currents next and put it in a temp var
# then we will point cur.next to prev
# then prev = cur
# and move cur to the temp  (this is akin to swapping to values in array)

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return head

        prev = None
        cur = head

        while cur is not None:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        return prev

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 4
# Was the solution optimal? Oh this runs in o(N) and uses o(1) space
# Were there any bugs? No Bugs
# 5 5 5 5 = 5
