# Maximum Longest Common Subsequence
# https://www.interviewbit.com/problems/maximum-longest-common-subsequence
#
# Defining substring
# For a string P with characters P1, P2 ,…, Pq, let us denote by P[i, j] the substring Pi, Pi+1 ,…, Pj.
#
# Defining longest common subsequence(LCS)
# A subsequence is a sequence that can be derived from another sequence by deleting some elements
# without changing the order of the remaining elements. LCS(A, B) of 2 sequences A and B is a
# subsequence, with maximal length, which is common to both the sequences.
#
# Here, rev(A) denotes reverse of string A.# Given a string S with small alphabet characters S1, S2 ,…, SN,
# return an array with two elements. First is the smallest j (1 ≤ j < N) for which LCS(S[1, j], rev(S[j + 1, N]))
# is maximal an second is the maximal value of LCS(S[1, j], rev(S[j + 1, N])).
#
# For example,
#
# S="abba"
#
# LCS(S[1, 1], rev(S[2, 4])) = LCS("a", "abb") = 1
# LCS(S[1, 2], rev(S[3, 4])) = LCS("ab", "ab") = 2
# LCS(S[1, 3], rev(S[4, 4])) = LCS("abb", "a") = 1
#
# Hence, we return [2, 2].
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : string
    # @return a list of integers
    def maxLCS(self, A):
        N = len(A) + 1
        dp = [[0] * N for _ in range(N)]

        for i in range(1, N):
            for j in range(1, N):
                if A[i - 1] == A[- j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

        answer = 1, 0

        for i in range(N):
            if dp[i][- i - 1] > answer[1]:
                answer = i, dp[i][- i - 1]

        return answer

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

