# Add Two Numbers II: https://leetcode.com/problems/add-two-numbers-ii/

# You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Looking through this problem the easiest way to solve is to get the int val of both lists
# and then turn around and create the new linked this it will run in o(N) and use O(N) space


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1, num2 = 0, 0

        while l1:
            num1 = (10 * num1) + l1.val
            l1 = l1.next

        while l2:
            num2 = (10 * num2) + l2.val
            l2 = l2.next

        num1 += num2

        head = ListNode()
        cur = head
        for value in str(num1):
            cur.next = ListNode(value)
            cur = cur.next

        return head.next


# So this solution works and runs in the time I mentioned above. The question is can we do better?
# I believe that we could do better because if we find the lenght of both lists and use it to match
# up two pointers we can do the math of the right values. Once that is done we would need to do a second
# pass to deal with carry. In order to do this the created linked list will be created backwards
# and need to be reveresed. This would run in O(N) time and o(1) additional space


    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        len1, len2 = 0, 0
        currentL1, currentL2 = l1, l2
        while currentL1:
            len1 += 1
            currentL1 = currentL1.next

        while currentL2:
            len2 += 1
            currentL2 = currentL2.next

        # Now that we have the length of both we need to parse the values as we go down
        currentL1, currentL2 = l1, l2
        # Since we are creating the list backward we set head to nothing
        head = None
        while len1 and len2:
            tempVal = 0
            # If len1 is larger so we know to evaluate l1
            if len1 >= len2:
                tempVal += currentL1.val
                currentL1 = currentL1.next
                len1 -= 1

            # Now we check if len1 is smaller meaning we need to evaluate l2
            # Also this is a separte if else because we need to check the potential
            # of l2 being longer than l1 or the case where they are equal
            if len1 < len2:
                tempVal += currentL2.val
                currentL2 = currentL2.next
                len2 -= 1

            # Now we need to update our pointers
            curResult = ListNode(tempVal)
            curResult.next = head
            head = curResult

        # Now that we have the created list we need to parse for the carry over and then reverse the list
        cur, head = head, None
        carry = 0
        while cur:
            # Check if we need to make a carry
            carry, val = divmod(cur.val + carry, 10)

            curResult = ListNode(val)
            curResult.next = head
            head = curResult

            cur = cur.next

        # If we have a carry to the beginning
        if carry:
            curResult = ListNode(carry)
            curResult.next = head
            head = curResult

        return head

# Boo yeah the above works although it is kind of super complicated to write out honestly
# That being said it runs in O(N) (N = len(l1) + len(l2)) and uses o(1) additional space or O(N) if you are considering the output array

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 25
# Was the solution optimal? See above
# Were there any bugs? I accidently looped the list instead of creating a temporary head
# 5 5 5 4 = 4.75
