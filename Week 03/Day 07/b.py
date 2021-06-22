#  Merge k Sorted Lists: https://leetcode.com/problems/merge-k-sorted-lists/

# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists) -> ListNode:
        return


# Score Card
# Did I need hints? N
# Did you finish within 30 min? Y
# Was the solution optimal? N I didn't think of the quick select solution and I would still have to implement it
# Were there any bugs? Y my sorting took me a while to figure out my keys actually needed to be baseed off of count.get instead of count
#  4 3 3 2 = 3
