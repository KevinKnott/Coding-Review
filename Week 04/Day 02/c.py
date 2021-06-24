# Implement Queue using Stacks: https://leetcode.com/problems/implement-queue-using-stacks/

# Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

# Implement the MyQueue class:

#     void push(int x) Pushes element x to the back of the queue.
#     int pop() Removes the element from the front of the queue and returns it.
#     int peek() Returns the element at the front of the queue.
#     boolean empty() Returns true if the queue is empty, false otherwise.

# Notes:

#     You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
#     Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.

# Follow-up: Can you implement the queue such that each operation is amortized O(1) time complexity? In other words, performing n operations will take overall O(n) time even if one of those operations may take longer.


#   This problem is actually pretty simple we take two stacks and add onto one and if we need the top value we pop everything
#  and push it into stack two and then put it all back on stack 1

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = []
        self.backup = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.q.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        while len(self.q) > 1:
            self.backup.append(self.q.pop())
        result = self.q.pop()

        while self.backup:
            self.q.append(self.backup.pop())
        return result

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.q[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.q) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

# The above code works but could it be better? oh yea basically instead of doing the second step where I push all back on to the q
# we dont do that as we know everything up to that point on the q is completed. So we actually can leave those there unless it is empty


class MyQueue2:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = []
        self.stack = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        # Technically this won't happen but we should check if everything is empty before this op
        if self.empty():
            raise Exception('Pop called on empty q')
        self.peek()
        return self.q.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.q:
            while self.stack:
                self.q.append(self.stack.pop())

        return self.q[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.q and not self.stack

# Score Card
# Did I need hints? Nope
# Did you finish within 30 min? 15 min
# Was the solution optimal? Yes this technically runs in o(1) for push, peek and empty while it runs in o(1) amortized for pop because we
#  are only making a q after we have no more values on our q and only values in our stack
# Were there any bugs? None
# 5 5 5 5 = 5
