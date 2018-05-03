# Longest valid Parentheses
# https://www.interviewbit.com/problems/longest-valid-parentheses/
#
# Given a string containing just the characters '(' and ')', find the length of the longest valid
# (well-formed) parentheses substring.
#
# For "(()", the longest valid parentheses substring is "()", which has length = 2.
#
# Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    def longestValidParentheses(self, A):
        dp, ans = [0] * len(A), 0

        for i in range(1, len(A)):
            if A[i] == ')':
                if A[i - 1] == '(' :
                    dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
                elif i - dp[i - 1] > 0 and A[i - dp[i - 1] - 1] == '(':
                    dp[i] = dp[i - 1] + (dp[i - dp[i - 1] - 2] if (i - dp[i - 1]) >= 2 else 0) + 2
                ans = max(dp[i], ans)
        return ans


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == '__main__':
    s = Solution()
    print(s.longestValidParentheses("(()"))
    print(s.longestValidParentheses(")()())"))
    print(s.longestValidParentheses("()(())"))