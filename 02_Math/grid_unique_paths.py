# Grid Unique Paths
# https://www.interviewbit.com/problems/grid-unique-paths/
#
# A robot is located at the top-left corner of an A x B grid (marked ‘Start’ in the diagram below).
#
# Path Sum: Example 1
#
# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked ‘Finish’ in the diagram below).
#
# How many possible unique paths are there?
#
# Note: A and B will be such that the resulting answer fits in a 32 bit signed integer.
#
# Example :
#
# Input : A = 2, B = 2
# Output : 2
#
# 2 possible routes : (0, 0) -> (0, 1) -> (1, 1)
#               OR  : (0, 0) -> (1, 0) -> (1, 1)
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def uniquePaths(self, A, B):
        mat = [[1] * B] * A
        for i in range(1, A):
            for j in range(1, B):
                mat[i][j] = mat[i - 1][j] + mat[i][j - 1]

        return mat[-1][-1]

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":

    s = Solution()
    print(s.uniquePaths(15, 3))
    print(s.uniquePaths(14, 28))
    print(s.uniquePaths(7, 3))