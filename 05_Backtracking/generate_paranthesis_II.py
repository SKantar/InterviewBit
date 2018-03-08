# Generate all Parentheses II
# https://www.interviewbit.com/problems/generate-all-parentheses-ii/
#
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses of length 2*n.
#
# For example, given n = 3, a solution set is:
#
# "((()))", "(()())", "(())()", "()(())", "()()()"
# Make sure the returned list of strings are sorted.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:

    def _valid(self, A):
        s = 0
        for a in A:
            s = s - (a == ')') + (a == '(')
            if s < 0:
                return False
        return s == 0

    def _generateParenthesis(self, A, tmp):
        if not A:
            return [tmp[:]] if self._valid(tmp) else []
        return self._generateParenthesis(A - 1, tmp + '(') + self._generateParenthesis(A - 1, tmp + ")")

    # @param A : integer
    # @return a list of strings
    def generateParenthesis(self, A):
        return self._generateParenthesis(A * 2, '')


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.generateParenthesis(3))