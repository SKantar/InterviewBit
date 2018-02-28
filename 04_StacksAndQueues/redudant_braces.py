# Redundant Braces
# https://www.interviewbit.com/problems/redundant-braces/
#
# Write a program to validate if the input string has redundant braces?
# Return 0/1
#
# 0 -> NO
# 1 -> YES
#
# Input will be always a valid expression
#
# and operators allowed are only + , * , - , /
#
# Example:
#
# ((a + b)) has redundant braces so answer will be 1
# (a + (a + b)) doesn't have have any redundant braces so answer will be 0
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


class Solution:
    def braces(self, A):
        stack = list()
        for a in A:
            if a in ['-', '+', '*', '/', '(']:
                stack.append(a)
            elif a == ')':
                if stack[-1] == '(':
                    return 1
                while len(stack) > 0 and stack[-1] != '(':
                    stack.pop()
                stack.pop()
        return 0

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == '__main__':
    s = Solution()
    print(s.braces('1 + (2)'))
    print(s.braces('1 + (2 + 3)'))
    print(s.braces('1 + ((2 + 3))'))