# Regular Expression II
# https://www.interviewbit.com/problems/regular-expression-ii/
#
# Implement regular expression matching with support for '.' and '*'.
#
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
#
# The matching should cover the entire input string (not partial).
#
# The function prototype should be:
#
# int isMatch(const char *s, const char *p)
#
# Some examples:
#
# isMatch("aa","a") → 0
# isMatch("aa","aa") → 1
# isMatch("aaa","aa") → 0
# isMatch("aa", "a*") → 1
# isMatch("aa", ".*") → 1
# isMatch("ab", ".*") → 1
# isMatch("aab", "c*a*b") → 1
#
# Return 0 / 1 ( 0 for false, 1 for true ) for this problem
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    # dp[i][j] does i chars of b match j chars of a
    def isMatch(self, A, B):

        m, n = len(A), len(B)

        dp = [[False] + [False] * m for _ in range(n + 1)]
        dp[0][0] = True

        for i in range(1, n + 1):
            if B[i - 1] == '.':
                for j in range(1, m + 1):
                    dp[i][j] = dp[i - 1][j - 1]
            elif B[i - 1] == '*':
                last = B[i - 2]
                for j in range(1, m + 1):
                    if dp[i - 2][j] or dp[i - 1][j]:
                        dp[i][j] = True
                    elif A[j - 1] == last or last == '.':
                        dp[i][j] = dp[i][j - 1]
            else:
                for j in range(1, m + 1):
                    dp[i][j] = dp[i - 1][j - 1] if A[j - 1] == B[i - 1] else False

        return int(dp[-1][-1])

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.isMatch('a', 'a'))
    print(s.isMatch("aa", "a"))
    print(s.isMatch("aa", "aa"))
    print(s.isMatch("aaa", "aa"))
    print(s.isMatch("aaa", "aa."))
    print(s.isMatch("aaa", "aa.."))
    print(s.isMatch("aa", "a*"))
    print(s.isMatch("aa", ".*"))
    print(s.isMatch("ab", ".*"))
    print(s.isMatch("abbbc", "ab*c"))
    print(s.isMatch("aab", "c*a*b"))