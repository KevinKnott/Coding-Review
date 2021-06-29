# 155. Min Stack: https://leetcode.com/problems/min-stack/
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:

#     MinStack() initializes the stack object.
#     void push(val) pushes the element val onto the stack.
#     void pop() removes the element on the top of the stack.
#     int top() gets the top element of the stack.
#     int getMin() retrieves the minimum element in the stack.


# This is actually super easy you just have to understand that on a stack you can have pairs
# my solution technically doesn't check for empty stacks but in production you would want to
# have the commented out checks or raising an exception
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append((val, val))
        else:
            self.stack.append((val, min(val, self.getMin())))

    def pop(self) -> None:
        return self.stack.pop()[0]  # if len(self.stack) != 0 else None

    def top(self) -> int:
        return self.stack[-1][0]  # if len(self.stack) != 0 else None

    def getMin(self) -> int:
        return self.stack[-1][1]  # if len(self.stack) != 0 else None

    # Score Card
    # Did I need hints? N
    # Did you finish within 30 min? Y 6 min
    # Was the solution optimal? Y
    # Were there any bugs? N
    #  5 5 5 5 = 5
