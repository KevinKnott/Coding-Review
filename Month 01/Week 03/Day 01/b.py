# Merge k Sorted Lists: https://leetcode.com/problems/merge-k-sorted-lists/

# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# This problem kind of reminds of a merge sort except we have n lists to merge together and normally that is handled by
# the partition piece in order to do this I will make a function that merges (like merge sort) that returns a list
# and then take two list and merge them together and make that our list
class Solution:
    def mergeKLists(self, lists) -> ListNode:
        # Technically you can optimzie this but I will just be creating a new list
        def mergeTwoLists(A, B):
            result = ListNode()
            head = result
            # Merge Two

            while A and B:
                cur = ListNode()

                if A.val <= B.val:
                    cur.val = A.val
                    A = A.next
                else:
                    cur.val = B.val
                    B = B.next

                result.next = cur
                result = result.next

            if A:
                result.next = A

            if B:
                result.next = B

            return head.next

        if lists is None or len(lists) == 0:
            return None

        while len(lists) > 1:
            # Create a simple structure to hold merged list
            temp = []
            for i in range(1, len(lists), 2):
                temp.append(mergeTwoLists(lists[i-1], lists[i]))

            # If we have an odd number the last list needs to be appended
            if len(lists) % 2 == 1:
                temp.append(lists[-1])
            # make lists = our merged
            lists = temp

        return lists[0]

# This worked first try boo yah the question is could it be more efficient?
#  Currently this solution works in O(mlogn) where n is the number of lists and m is the longest
#  list after combining all of them time and the space is o(m) the size of the longest generated
#  That beings aid we can reduce space by taking either the node from A or B instead of creating
#  a new node

#  Also in order to save some more space instead of creating a new temp array I could create a
# loop that is actually being changed to increase by 2 every times since we know we are going to
# take log_2 of N where N is the number of intervals this would also require us to update
# the list itself as we go along


# Score Card
# Did I need hints? N
# Did you finish within 30 min? Y
# Was the solution optimal? Kind of we could make some slight improvements to help speed they are listed above
# Were there any bugs? N
#  5 5 3 5 = 4.5
