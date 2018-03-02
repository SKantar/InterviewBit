# Valid Sudoku
# https://www.interviewbit.com/problems/valid-sudoku/
#
# Determine if a Sudoku is valid, according to: http://sudoku.com.au/TheRules.aspx
#
# The Sudoku board could be partially filled, where empty cells are filled with the character ‘.’.
#
#
#
# The input corresponding to the above configuration :
#
# ["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79"]
# A partially filled sudoku which is valid.
#
#  Note:
# A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
# Return 0 / 1 ( 0 for false, 1 for true ) for this problem
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : tuple of strings
    # @return an integer
    def isValidSudoku(self, A):

        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        sqrs = [set() for i in range(9)]

        for i in range(9):
            for j in range(9):
                if A[i][j] != '.':
                    square = (i // 3) * 3 + j // 3
                    if A[i][j] in rows[i] or A[i][j] in cols[j] or A[i][j] in sqrs[square]:
                        return 0
                    rows[i].add(A[i][j])
                    cols[j].add(A[i][j])
                    sqrs[square].add(A[i][j])
        return 1

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.isValidSudoku([
        '53..7....',
        '6..195...',
        '.98....6.',
        '8...6...3',
        '4..8.3..1',
        '7...2...6',
        '.6....28.',
        '...419..5',
        '....8..79'
    ]))



