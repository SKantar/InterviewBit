# Unique Paths in a Grid
# https://www.interviewbit.com/problems/unique-paths-in-a-grid/
#
# Given a grid of size m * n, lets assume you are starting at (1,1) and your goal is to reach (m,n). At any instance, if you are on (x,y), you can either go to (x, y + 1) or (x + 1, y).
#
# Now consider if some obstacles are added to the grids. How many unique paths would there be?
# An obstacle and empty space is marked as 1 and 0 respectively in the grid.
#
# Example :
# There is one obstacle in the middle of a 3x3 grid as illustrated below.
#
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# The total number of unique paths is 2.
#
#  Note: m and n will be at most 100.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def uniquePathsWithObstacles(self, A):

        if not len(A):
            return 0

        H, W = len(A), len(A[0])

        mat = [[0] * W for _ in range(H)]

        ins = 1
        for i in range(H):
            if A[i][0]:
                ins = 0
            mat[i][0] = ins

        ins = 1
        for j in range(W):
            if A[0][j]:
                ins = 0
            mat[0][j] = ins

        for i in range(1, H):
            for j in range(1, W):
                if not A[i][j]:
                    mat[i][j] = mat[i - 1][j] + mat[i][j - 1]

        return mat[-1][-1]

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    A = [[0,1]]

    s = Solution()
    print(s.uniquePathsWithObstacles(A))