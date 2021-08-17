# Merge k Sorted Lists: https://leetcode.com/problems/merge-k-sorted-lists/

# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.

# This problem can be broken down into two steps one merging two separate linked lists together
# this is easy as it is the same as the merge sort method and secondly updating the n lists
# until you only have one the easy way to do this is to use extra space and return a new list
# from every merge you do and then keep iterating until there is only one list left and return it.
# However the optimal solution is to actually update these in place by overwritting the A array
# every time and iterating log(n) times

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwo(self, A, B):
        dummy = ListNode()
        cur = dummy

        while A and B:
            if A.val <= B.val:
                cur.next = A
                A = A.next
            else:
                cur.next = B
                B = B.next

            cur = cur.next

        if A:
            cur.next = A
        if B:
            cur.next = B

        return dummy.next

    def mergeKLists(self, lists):
        if lists is None or len(lists) == 0:
            return None

        while len(lists) > 1:
            temp = []

            for i in range(1, len(lists), 2):
                temp.append(self.mergeTwo(lists[i-1], lists[i]))

            if len(lists) % 2 == 1:
                temp.append(lists[-1])

            lists = temp

        return lists[0]

# The above is pretty optimal it runs in O(nlogn) time and uses o(N) space you could slightly improve by just updating
# the lists in real time but it would be more complicated and would give you O(1) space


# Score Card
# Did I need hints? N
# Did you finish within 30 min? 15
# Was the solution optimal? Almost just need to improve space but I have limited time today
# Were there any bugs? No bugs
# 5 5 5 5 = 5
