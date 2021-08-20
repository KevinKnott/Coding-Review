# Reverse Nodes in k-Group: https://leetcode.com/problems/reverse-nodes-in-k-group/

# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
# You may not alter the values in the list's nodes, only nodes themselves may be changed.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# So in this problem there are two problems and we can solve them separately. The first one is reversing a linked list
# which is pretty trivial the other is knowing how to swap every k elements. The easy approach to doing this is with a
# dfs and the more optimal way of doing this is with an iterative approach in which you have to carefully approach
# swaping the head and the potential new head aroun. I don't have lots of time today so I will be completing the
# dfs


class Solution:
    def reverseNodes(self, head, k):
        prev = None

        for _ in range(k):
            temp = head.next
            head.next = prev
            prev = head
            head = temp

        return prev

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        count = 0
        cur = head
        while cur and count < k:
            cur = cur.next
            count += 1

        if k == count:
            newHead = self.reverseNodes(head, k)
            # New head is our new head
            # our current head is actually the end of our swapped
            # and cur is the actuall next node
            head.next = self.reverseKGroup(cur, k)
            return newHead
        return head

# Yup this problem is getting easier. Honestly if I had a bit more time today I think that making this iterative isn't
# too hard but reduces this from O(N) and O(N/k) to O(N) and O(1) as we modify the list as we go

# Score Card
# Did I need hints? Nope
# Did you finish within 30 min? 10
# Was the solution optimal? Ye
# Were there any bugs? None
# 5 5 5 5 = 5
