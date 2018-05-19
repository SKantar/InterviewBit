# NQueens
# https://www.interviewbit.com/problems/nqueens/
#
# The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no
# two queens attack each other.
#
# N Queens: Example 1
#
# Given an integer n, return all distinct solutions to the n-queens puzzle.
#
# Each solution contains a distinct board configuration of the n-queens’ placement, where 'Q'
# and '.' both indicate a queen and an empty space respectively.
#
# For example,
# There exist two distinct solutions to the 4-queens puzzle:
#
# [
#  [".Q..",  // Solution 1
#   "...Q",
#   "Q...",
#   "..Q."],
#
#  ["..Q.",  // Solution 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def isValid(self, i, j, board):
        # main diagonal
        ti, tj = i - 1, j - 1
        while ti > -1 and tj > -1:
            if board[ti][tj] == 'Q':
                return False
            ti, tj = ti - 1, tj - 1

        ti, tj = i - 1, j + 1
        while ti > -1 and tj < len(board):
            if board[ti][tj] == 'Q':
                return False
            ti, tj = ti - 1, tj + 1

        # column
        ti, tj = i - 1, j
        while ti > -1:
            if board[ti][tj] == 'Q':
                return False
            ti -= 1

        return True

    def _solveNQueens(self, i, board):
        if i == len(board):
            return [board[:]]

        res = list()
        for j in range(len(board)):
            if self.isValid(i, j, board):
                board[i] = board[i][:j] + 'Q' + board[i][j + 1:]
                res.extend(self._solveNQueens(i + 1, board))
            board[i] = '.' * len(board)
        return res

    def solveNQueens(self, A):
        return self._solveNQueens(0, ['.' * A] * A)