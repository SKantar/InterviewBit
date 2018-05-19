# Evaluate Expression
# https://www.interviewbit.com/problems/evaluate-expression/
#
# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
#
# Valid operators are +, -, *, /. Each operand may be an integer or another expression.
#
# Examples:
#
#   ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
#   ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


class Solution:
    # @param A : list of strings
    # @return an integer
    def evalRPN(self, A):
        stack = list()

        for e in A:
            if e in ['+', '-', '/', '*']:
                right = stack.pop()
                left = stack.pop()
                res = eval("int({}{}{})".format(left, e, right))
                stack.append(res)
            else:
                stack.append(e)
        return stack.pop()