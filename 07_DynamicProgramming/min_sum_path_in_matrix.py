# Min Sum Path in Matrix
# https://www.interviewbit.com/problems/min-sum-path-in-matrix/
#
#   Given a m x n grid filled with non-negative numbers, find a path from top left
# to bottom right which minimizes the sum of all numbers along its path.
#
#  Note: You can only move either down or right at any point in time.
# Example :
#
# Input :
#
#     [  1 3 2
#        4 3 1
#        5 6 1
#     ]
#
# Output : 8
#      1 -> 3 -> 2 -> 1 -> 1
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def minPathSum(self, A):
        if not A:
            return 0

        n, m = len(A), len(A[0])

        dp = [[0] * m for _ in range(n)]

        dp[0][0] = A[0][0]

        for j in range(1, m):
            dp[0][j] = dp[0][j - 1] + A[0][j]

        for i in range(1, n):
            dp[i][0] = dp[i - 1][0] + A[i][0]

        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + A[i][j]

        return dp[-1][-1]

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #