# Regular Expression Match
# https://www.interviewbit.com/problems/regular-expression-match/
#
# Implement wildcard pattern matching with support for '?' and '*'.
#
# '?' : Matches any single character.
# '*' : Matches any sequence of characters (including the empty sequence).
# The matching should cover the entire input string (not partial).
#
# The function prototype should be:
#
# int isMatch(const char *s, const char *p)
# Examples :
#
# isMatch("aa","a") → 0
# isMatch("aa","aa") → 1
# isMatch("aaa","aa") → 0
# isMatch("aa", "*") → 1
# isMatch("aa", "a*") → 1
# isMatch("ab", "?*") → 1
# isMatch("aab", "c*a*b") → 0
# Return 1/0 for this problem.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def isMatch(self, A, B):
        if len(B) - B.count('*') > len(A):
            return 0
        dp = [True] + [False] * len(A)
        for c in B:
            if c == '*':
                for n in range(1, len(A) + 1):
                    dp[n] = dp[n - 1] or dp[n]
            else:
                for n in range(len(A) - 1, -1, -1):
                    dp[n + 1] = dp[n] and (c == A[n] or c == '?')
                dp[0] = dp[0] and c == '*'
        return 1 if dp[-1] else 0

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.isMatch('a', '?'))
    print(s.isMatch('cc', '?'))