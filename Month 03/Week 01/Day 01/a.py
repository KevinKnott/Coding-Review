# Copy List with Random Pointer: https://leetcode.com/problems/copy-list-with-random-pointer/

# A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

# Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

# For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

# Return the head of the copied linked list.

# The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

# val: an integer representing Node.val
# random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
# Your code will only be given the head of the original linked list.


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


# So the easiest solution for this problem is actually to use a hash map as we iterate through the list twice
# The first time we create all nodes

# The second time we use the reference to point to the random node and use the dictionary to use the new cloned
# node

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return

        cloneMapping = {}
        cur, last = head, None
        while cur is not None:
            cloneMapping[cur] = Node(cur.val)
            if last:
                cloneMapping[last].next = cloneMapping[cur]
            last = cur
            cur = cur.next

        # Now that we have all of the cloned items we can go through and actually
        # update for the random pointers

        cur = head
        while cur is not None:
            cloneMapping[cur].random = cloneMapping[cur.random] if cur.random else None
            cur = cur.next

        return cloneMapping[head]


# So the above code works and is pretty efficient this will run in O(N) time and o(N) space
# the problem is we could optimize the space by simply using the same proccess but using
# the list itself as a temporary holder. This still uses o(N) space but it isn't
# O(N) additional space


    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return

        # Loop through once and add the new nodes just to the right of our nodes
        cur = head
        while cur is not None:
            newNext = Node(cur.val)
            newNext.next = cur.next
            cur.next = newNext
            cur = cur.next.next

        # Loop through the nodes 2 at a time and link  the next node and random node
        cur = head
        while cur is not None:
            cur.next.random = cur.random.next if cur.random else None
            cur = cur.next.next

        # Loop through a third time and decouple the two lists
        cur = head
        newHead = cur.next
        curPrime = cur.next
        while cur is not None:
            cur.next = cur.next.next
            curPrime.next = curPrime.next.next if curPrime.next else None

            cur = cur.next
            curPrime = curPrime.next

        return newHead

# I mentioned above but this is O(N) time and O(1) additional space which is as optimal as I can get it

# Score Card
# Did I need hints? No
# Did you finish within 30 min? 20
# Was the solution optimal? I believe so we could make some slight optimization but this will run in o(n^2) because of the multiplicity we would go through once and then again to multiply
#  and o(n) space
# Were there any bugs? I accidently forgot to check for null when decoupling the two lists
# 5 5 5 4 = 4.75
