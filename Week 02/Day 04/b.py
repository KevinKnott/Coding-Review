# 155. Min Stack: https://leetcode.com/problems/min-stack/
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:

#     MinStack() initializes the stack object.
#     void push(val) pushes the element val onto the stack.
#     void pop() removes the element on the top of the stack.
#     int top() gets the top element of the stack.
#     int getMin() retrieves the minimum element in the stack.


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """

    def push(self, val: int) -> None:

    def pop(self) -> None:

    def top(self) -> int:

    def getMin(self) -> int:

        # Score Card
        # Did I need hints? N (But the second solution did)
        # Did you finish within 30 min? No 1:30
        # Was the solution optimal? My initial solution is optimal however I messed up the initial coding of it
        # Were there any bugs? I forgot that since it is possible to have [[[[]]]] I need to actually recurse
        #  4 1 2 1 = 2
