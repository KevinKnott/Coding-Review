# Reverse Linked List II: https://leetcode.com/problems/reverse-linked-list-ii/

# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head, left, right):
        return


# Score Card
# Did I need hints? N
# Did you finish within 30 min? N
# Was the solution optimal? It is optimal enough however I think I could make some slight improvements
# Were there any bugs? I am having issues with double negative values
# 5 1 3 3 = 3
