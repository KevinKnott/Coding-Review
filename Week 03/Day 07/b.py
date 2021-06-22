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
        amount = len(lists)
        round = 1

        # This is some cool math
        while round < amount:
            # Basically we are looping by a smaller and smaller durration but increasing the interval between nodes
            # This is an optimization where you are saving space by not poping off elements as you go down
            for i in range(0, amount - round, round * 2):
                lists[i] = self.mergeList(lists[i], lists[i+round])

            round *= 2

        # You could also do something along the lines of creating a temp list and merging 2 and adding it to temp list
        # and then make that your list but it is slightly less efficient

        return lists[0] if amount > 0 else None

    def mergeList(self, A, B):
        dummy = ListNode(0)
        head = dummy

        while A and B:
            if A.val <= B.val:
                head.next = A
                A = A.next
            else:
                head.next = B
                B = B.next

            head = head.next

        if A:
            head.next = A
        if B:
            head.next = B

        return dummy.next


# Score Card
# Did I need hints? N
# Did you finish within 30 min? Y
# Was the solution optimal? N I didn't think of the quick select solution and I would still have to implement it
# Were there any bugs? Y my sorting took me a while to figure out my keys actually needed to be baseed off of count.get instead of count
#  4 3 3 2 = 3
