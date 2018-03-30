# Interleaving Strings
# https://www.interviewbit.com/problems/interleaving-strings/
#
# Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.
#
# Example,
# Given:
#
# s1 = "aabcc",
# s2 = "dbbca",
# When s3 = "aadbbcbcac", return true.
# When s3 = "aadbbbaccc", return false.
#
# Return 0 / 1 ( 0 for false, 1 for true ) for this problem
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : string
    # @param B : string
    # @param C : string
    # @return an integer
    def isInterleave(self, A, B, C):
        n, m = len(A), len(B)

        if len(C) != n + m:
            return 0

        dp = [[0] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(1, n + 1):
            dp[i][0] = dp[i - 1][0] * (A[i - 1] == C[i - 1])

        for j in range(1, m + 1):
            dp[0][j] = dp[0][j - 1] * (B[j - 1] == C[j - 1])

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if A[i - 1] == C[i + j - 1]:
                    dp[i][j] = dp[i - 1][j]
                if not dp[i][j] and B[j - 1] == C[i + j - 1]:
                    dp[i][j] = dp[i][j - 1]

        return dp[-1][-1]

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.isInterleave('aabcc', 'dbbca', 'aadbbcbcac'))
    print(s.isInterleave('aabcc', 'dbbca', 'aadbbbaccc'))
    print(s.isInterleave('aabc', 'abad', 'aabadabc'))
    print(s.isInterleave('a', '', 'c'))
    print(s.isInterleave('', 'b', 'b'))


