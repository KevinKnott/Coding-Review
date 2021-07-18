# Merge k Sorted Lists: https://leetcode.com/problems/merge-k-sorted-lists/

# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.

# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# This problem is actually just like the merge sort so if we write the merge function
# then we can simply loop through and merge 2 arrays at a time and then
# continue doing this until we have simply one array


class Solution:
    def mergeKLists(self, lists):
        if len(lists) == 0:
            return

        while len(lists) != 1:
            temp = []

            while len(lists) > 1:
                A, B = lists.pop(), lists.pop()

                temp.append(self.merge2List(A, B))

            if len(lists) == 1:
                temp.append(lists[0])

            lists = temp

        return lists[0]

    def merge2List(self, a, b):
        # For simplicity I am creating a completely new list
        head = ListNode()
        cur = head

        while a and b:
            if a.val <= b.val:
                cur.next = a
                a = a.next
            else:
                cur.next = b
                b = b.next

            cur = cur.next

        if a:
            cur.next = a
        if b:
            cur.next = b

        return head.next

# The above works in o(nlogn) time and uses o(n) space. You could definitely make some improvements in which you
# You can do this by in the merge 2 lists make sure you don't create a simple list to add to but place the correct
# value to A. After that you change the for loop to run in log(n) steps by reducing by  2 at every iteration and + 1
# more if it is odd

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 20
# Was the solution optimal? I ran out of time to implement the most optimal but this is really close
# Were there any bugs? No
#  5 5 5 5 = 5
