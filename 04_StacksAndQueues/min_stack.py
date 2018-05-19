# Min Stack
# https://www.interviewbit.com/problems/min-stack/
#
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
#         push(x) – Push element x onto stack.
#         pop() – Removes the element on top of the stack.
#         top() – Get the top element.
#         getMin() – Retrieve the minimum element in the stack.
#
# Note that all the operations have to be constant time operations.
#
# Questions to ask the interviewer :
#
# Q: What should getMin() do on empty stack?
# A: In this case, return -1.
#
# Q: What should pop do on empty stack?
# A: In this case, nothing.
#
# Q: What should top() do on empty stack?
# A: In this case, return -1
#
#     NOTE : If you are using your own declared global variables, make sure to clear them out in the constructor.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class MinStack:
    def __init__(self):
        self.stack = list()
        self.min = list()

    # @param x, an integer
    # @return an integer
    def push(self, x):
        top = self.top()
        m = min(self.getMin(), x) if top != -1 else x
        self.stack.append(x)
        self.min.append(m)

    # @return nothing
    def pop(self):
        if self.top() != -1:
            self.min.pop()
            return self.stack.pop()
        return None

    # @return an integer
    def top(self):
        return self.stack[-1] if self.stack else -1

    # @return an integer
    def getMin(self):
        top = self.top()
        if top == -1:
            return -1
        return self.min[-1]
