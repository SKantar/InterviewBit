# Capture Regions on Board
# https://www.interviewbit.com/problems/capture-regions-on-board/
#
# Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.
#
# A region is captured by flipping all 'O's into 'X's in that surrounded region.
#
# For example,
#
# X X X X
# X O O X
# X X O X
# X O X X
# After running your function, the board should be:
#
# X X X X
# X X X X
# X X X X
# X O X X
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    moves = ((0, 1), (1, 0), (0, -1), (-1, 0))

    def _dfs(self, A, i, j):
        if A[i][j] != 'O':
            return

        A[i][j] = '1'

        for move in Solution.moves:
            tx, ty = move
            if 0 <= i + tx < len(A) and 0 <= j + ty < len(A[i + tx]):
                self._dfs(A, i + tx, j + ty)


    def _prepare_output(self, A):
        for i in range(len(A)):
            for j in range(len(A[i])):
                if A[i][j] == 'O':
                    A[i][j] = 'X'
                elif A[i][j] == '1':
                    A[i][j] = 'O'

    def solve(self, A):

        if not A:
            return

        for i in range(len(A)):
            if A[i][0] == 'O':
                self._dfs(A, i, 0)
            if A[i][len(A[i]) - 1] == 'O':
                self._dfs(A, i, len(A[i]) - 1)

        for j in range(len(A[0])):
            if A[0][j] == 'O':
                self._dfs(A, 0, j)
            if A[len(A) - 1][j] == 'O':
                self._dfs(A, len(A) - 1, j)

        self._prepare_output(A)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    A = [
        ['X', 'X', 'X', 'X'],
        ['X', 'O', 'O', 'X'],
        ['X', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'X']
    ]

    A = [["O", "O", "O"],["O", "O", "O"],["O", "O", "O"]]

    s = Solution()
    s.solve(A)
    print(A)