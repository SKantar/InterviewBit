# Min Sum Path in Triangle
# https://www.interviewbit.com/problems/min-sum-path-in-triangle/
#
# Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
#
# For example, given the following triangle
#
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
#
#  Note:
# Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def minimumTotal(self, A):
        from copy import copy

        if not len(A):
            return 0

        dp, dp_len = copy(A[-1]), len(A[-1])
        for i in range(dp_len - 2, -1, -1):
            for j in range(len(A[i])):
                dp[j] = min(dp[j], dp[j + 1]) + A[i][j]

        return dp[0]

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == '__main__':
    A = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]

    s = Solution()
    print(s.minimumTotal(A))