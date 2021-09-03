# Merge k Sorted Lists: https://leetcode.com/problems/merge-k-sorted-lists/

# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.

from types import List, Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# This problem is actually just a merge sort no need to explain really
# There are two solutions one with a for loop that creates a new list of ll
# and one that simply merges the current list which saves us o (N) space
# to become O(1)


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists is None or len(lists) == 0:
            return None

        interval = 1
        total = len(lists)

        while interval < total:
            for i in range(0, total - interval, interval * 2):
                lists[i] = self.merge2(lists[i], lists[i + interval])

            interval *= 2

        return lists[0] if total > 0 else []

    def merge2(self, l1, l2):
        dummy = ListNode()
        cur = dummy

        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next

            cur = cur.next

        if l1:
            cur.next = l1
        else:
            cur.next = l2

        return dummy.next

# This works although I forgot that my range needs to decrease then number of nodes to review
# by the number of merged (going up 2 at a time)

# This runs in o(nlogk) where k is the number of ll and uses O(1) additional space


# Score Card
# Did I need hints? Nope
# Did you finish within 30 min? 12
# Was the solution optimal? Yup
# Were there any bugs? None
# 5 5 5 5 = 5
