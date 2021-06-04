# Copy List with Random Pointer:
# A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.
# Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.
# For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.
# Return the head of the copied linked list.
# The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:
#     val: an integer representing Node.val
#     random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
# Your code will only be given the head of the original linked list.

# 2 pass solution
# run once and create all nodes
# run twice to get the random one and point it to the right node
# return new copy


class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


# Solved 17 min O(N) time and space (This solution actuall could be improved by making the dictionary a seperate call to create/get cloned nodes)
class initial():
    def copyRandomList(self, head):
        if head is None:
            return None

        result = Node(0)
        # Create a location hasmap based off of values
        location = {}

        orig = head
        copy = result.next
        while orig is not None:
            temp = Node(orig.val)
            location[orig] = temp
            copy.next = temp
            orig = orig.next
            copy = copy.next

        orig = head
        copy = result
        while orig is not None:
            if orig.random is None:
                copy.random = None
            else:
                copy.random = location[orig.random]
            orig = orig.next
            copy = copy.next
        return result.next

    def copyRandomList(self, head):
        if head is None:
            return None

        # Duplicate Node
        cur = head
        while cur is not None:
            temp = cur.next
            cur.next = Node(cur.val)
            cur.next.next = temp
            cur = temp

        # Copy random pointers
        cur = head
        while cur is not None:
            curPrime = cur.next
            curPrime.random = cur.random.next if cur.random is not None else None
            cur = cur.next.next

        # Separate
        cur = head
        newHead = cur.next
        curPrime = cur.next
        while cur is not None:
            cur.next = curPrime.next
            curPrime.next = cur.next.next if cur.next is not None else None
            cur = cur.next
            curPrime = curPrime.next

        return newHead


# Score Card
# Did I need hints? N
# Did you finish within 30 min? Y almost finished a second optimized approach but needed hints for it
# Was the solution optimal? The solution was optimal for time but not space and needed an interesting trick for manipulation
# Were there any bugs? I forgot that if rand is Null I cant check if none has a next pointer
#  4 4 4 4 = 4
