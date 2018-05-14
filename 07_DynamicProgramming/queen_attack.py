# Queen Attack
# https://www.interviewbit.com/problems/queen-attack/
#
# On a N * M chessboard, where rows are numbered from 1 to N and columns from 1 to M, there are
# queens at some cells. Return a N * M array A, where A[i][j] is number of queens that can attack
# cell (i, j). While calculating answer for cell (i, j), assume there is no queen at that cell.
#
# Notes:
#
#     Queen is able to move any number of squares vertically, horizontally or diagonally on a chessboard.
# A queen cannot jump over another queen to attack a position.
#     You are given an array of N strings, each of size M. Each character is either a 1 or 0 denoting
# if there is a queen at that position or not, respectively.
#     Expected time complexity is worst case O(N*M).
#
# For example,
#
# Let chessboard be,
# [0 1 0]
# [1 0 0]
# [0 0 1]
#
# where a 1 denotes a queen at that position.
#
# Cell (1, 1) is attacked by queens at (2, 1), (1,2) and (3,3).
# Cell (1, 2) is attacked by queen at (2, 1). Note that while calculating this, we assume that there is
# no queen at (1, 2).
# Cell (1, 3) is attacked by queens at (3, 3) and (1, 2).
# and so on...
#
# Finally, we return matrix
# [3, 1, 2]
# [1, 3, 3]
# [2, 3, 0]
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : list of strings
    # @return a list of list of integers
    def queenAttack(self, A):
        n, m = len(A), len(A) and len(A[0]) or 0

        dp = [[0] * m for _ in range(n)]
        
        directions = (
            (-1, -1), (-1, 0), (-1, 1), (0, 1),
            (1, 1), (1, 0), (1, -1), (0, -1)
        )

        for i in range(n):
            for j in range(m):
                if A[i][j] == '0':
                    continue
                for d in directions:
                    tx, ty = i + d[0], j + d[1]
                    while 0 <= tx < n and 0 <= ty < m:
                        dp[tx][ty] += 1
                        if A[tx][ty] == '1':
                            break
                        tx, ty = tx + d[0], ty + d[1]
        return dp

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":

    A = [ "111", "111", "111" ]

    s = Solution()
    print(s.queenAttack(A))


