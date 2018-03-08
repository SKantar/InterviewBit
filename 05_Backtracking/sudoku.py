# Sudoku
# https://www.interviewbit.com/problems/sudoku/
#
# Write a program to solve a Sudoku puzzle by filling the empty cells.
# Empty cells are indicated by the character '.'
# You may assume that there will be only one unique solution.
#
#
# Example :
#
# For the above given diagrams, the corresponding input to your program will be
#
# [[53..7....], [6..195...], [.98....6.], [8...6...3], [4..8.3..1], [7...2...6], [.6....28.], [...419..5], [....8..79]]
# and we would expect your program to modify the above array of array of characters to
#
# [[534678912], [672195348], [198342567], [859761423], [426853791], [713924856], [961537284], [287419635], [345286179]]
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    def _valid(self, A, i, j):

        row, col, sqr = set(), set(), set()

        # Test row and column
        for k in range(9):
            if A[i][k] != '.':
                if A[i][k] in row:
                    return False
                row.add(A[i][k])

            if A[k][j] != '.':
                if A[k][j] in col:
                    return False
                col.add(A[k][j])

        # Test box
        sx, sy = (i // 3) * 3, (j // 3 * 3)
        for k in range(sx, sx + 3):
            for l in range(sy, sy + 3):
                if A[k][l] != '.':
                    if A[k][l] in sqr:
                        return False
                    sqr.add(A[k][l])
        return True

    def _solve(self, A, i, j):

        if i == 9:
            return A

        if A[i][j] != '.':
            return self._solve(A, i + (j + 1) // 9, (j + 1) % 9)

        for k in range(1, 10):
            A[i] = A[i][:j] + [str(k)] + A[i][j + 1:]
            if not self._valid(A, i, j):
                continue
            ans = self._solve(A, i + (j + 1) // 9, (j + 1) % 9)
            if ans:
                return ans
        A[i] = A[i][:j] + ['.'] + A[i][j + 1:]
        return []


    # @param A : list of list of chars
    # @return nothing
    def solveSudoku(self, A):
        self._solve(A, 0, 0)
        print(A)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.solveSudoku([
        ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
        ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
        ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
        ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
        ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
        ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
        ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
        ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
        ['.', '.', '.', '.', '8', '.', '.', '7', '9']
    ]))
