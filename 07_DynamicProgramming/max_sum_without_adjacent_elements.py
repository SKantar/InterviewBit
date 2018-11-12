# Max Sum Without Adjacent Elements
# https://www.interviewbit.com/problems/max-sum-without-adjacent-elements/
#
# Given a 2 * N Grid of numbers, choose numbers such that the sum of the numbers
# is maximum and no two chosen numbers are adjacent horizontally, vertically or diagonally, and return it.
#
# Example:
#
# Grid:
# 	1 2 3 4
# 	2 3 4 5
# so we will choose
# 3 and 5 so sum will be 3 + 5 = 8
#
#
# Note that you can choose more than 2 numbers
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def adjacent(self, A):
        if not A:
            return 0
        m = len(A[0])
        dp = [0] * m

        for i in range(m):
            if i < 2:
                dp[i] = max(A[0][i], A[1][i])
            elif i == 2:
                dp[i] = dp[i - 2] + max(A[0][i], A[1][i])
            else:
                dp[i] = max(dp[i - 2], dp[i - 3]) + max(A[0][i], A[1][i])

        return dp[-1] if m == 1 else max(dp[-1], dp[-2])

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #