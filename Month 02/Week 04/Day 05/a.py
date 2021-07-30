# Reverse Nodes in k-Group: https://leetcode.com/problems/reverse-nodes-in-k-group/

# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
# You may not alter the values in the list's nodes, only nodes themselves may be changed.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Okay this problem can actually  be broken into two separate pieces reveresing nodes (super easy)
# and iterating through the linked list the tricky part is how do we actaully point the end to the next piece
# because for instance in the first swap you actually get a new head right


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        # For this part of the algo we simply need to loop through and see if we can
        # actually reverse k nodes
        cur = head
        count = 0
        while cur and count != k:
            cur = cur.next
            count += 1

        # Now that we know we have a k group we need to  reverse just that group
        if count == k:
            # Simply reverse the group we just saw
            reversed = self.reverse(head, k)
            # Try reversing the next k group and if you can
            # attach it to the end of our cur which is actually head
            # as we have reversed the array
            head.next = self.reverseKGroup(cur, k)
            return reversed

        return head

    # The reversal is easy it is the standard algo except you swap k elements
    def reverse(self, head, k):
        prev, cur = None, head
        while k > 0:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
            k -= 1

        return prev


# Score Card
# Did I need hints? N
# Did you finish within 30 min? 18
# Was the solution optimal? This solution runs in o(N) time and space. This isn't the most optimal as you technically could
# remove the use of a stack and do this completely iteratively and using extra nodes but it adds a lot of complexity
# and I don't have enough time to code it
# Were there any bugs? No bugs
#  5 5 3 5 = 4.5
