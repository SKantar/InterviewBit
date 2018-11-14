# Distinct Subsequences
# https://www.interviewbit.com/problems/distinct-subsequences/
#
# Given two sequences S, T, count number of unique ways in sequence S, to form a subsequence
# that is identical to the sequence T.
#
#  Subsequence : A subsequence of a string is a new string which is formed from the original
# string by deleting some (can be none ) of the characters without disturbing the relative
# positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).
# Example :
#
# S = "rabbbit"
# T = "rabbit"
# Return 3. And the formations as follows:
#
# S1= "ra_bbit"
# S2= "rab_bit"
# S3="rabb_it"
# "_" marks the removed character.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def numDistinct(self, A, B):
        n, m = len(B), len(A)

        if n > m:
            return 0

        dp = [[1] * (m + 1)] + [[0] * (m + 1) for _ in range(n)]

        for i in range(1, n + 1):
            for j in range(i, m + 1):
                dp[i][j] = dp[i][j - 1]
                if B[j - 1] == A[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]

        return dp[-1][-1]

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #