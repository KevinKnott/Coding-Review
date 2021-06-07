# Convert Binary Search Tree to Sorted Doubly Linked List:
# Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.
# You can think of the left and right pointers as synonymous to the predecessor and successor pointers in a doubly-linked list. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.
# We want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. You should return the pointer to the smallest element of the linked list.

# Okay this problem seems like a sort of problem where a dfs to get the order and then loop through to link the values

class init():
    def treeToDoublyList(self, root):
        if root is None:
            return None

        def dfs(node):
            nonlocal first, last
            if node:
                dfs(node.left)
                if last is None:
                    first = node
                else:
                    last.right = node
                    node.left = last

                last = node
                dfs(node.right)

        first, last = None, None
        dfs(root)

        first.left = last
        last.right = first

        return first

# Score Card
# Did I need hints? Y
# I went to a very similar solution first however I tried using a list as an inbetween
# Did you finish within 30 min? Y
# Was the solution optimal? Y although my first solution had added complexity since My thought process wasn't quite completed
# Were there any bugs? N
# I didn't have any big bugs but using non local within nested functions tripped me up because I didn't remember that it was needed
# Also nested functions get a bit tricky
#  3 4 4 2 = 3.25
