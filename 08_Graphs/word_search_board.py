# Word Search Board
# https://www.interviewbit.com/problems/word-search-board/
#
# Given a 2D board and a word, find if the word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The cell itself does not count as an adjacent cell.
# The same letter cell may be used more than once.
#
# Example :
#
# Given board =
#
# [
#   ["ABCE"],
#   ["SFCS"],
#   ["ADEE"]
# ]
# word = "ABCCED", -> returns 1,
# word = "SEE", -> returns 1,
# word = "ABCB", -> returns 1,
# word = "ABFSAB" -> returns 1
# word = "ABCD" -> returns 0
# Note that 1 corresponds to true, and 0 corresponds to false.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:

    moves = ((0, 1), (1, 0), (0, -1), (-1, 0))

    def _dfs(self, A, i, j, word, pos):

        if A[i][j] != word[pos]:
            return False

        if pos == len(word) - 1:
            return True

        for move in Solution.moves:
            tx, ty = move
            if 0 <= i + tx < len(A) and 0 <= j + ty < len(A[i + tx]):
                if self._dfs(A, i + tx, j + ty, word, pos + 1):
                    return True

        return False

    # @param A : list of strings
    # @param B : string
    # @return an integer
    def exist(self, A, B):
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == B[0]:
                    if self._dfs(A, i, j, B, 0):
                        return 1
        return 0

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":

    A = [
      'FEDCBECD',
      'FABBGACG',
      'CDEDGAEC',
      'BFFEGGBA',
      'FCEEAFDA',
      'AGFADEAC',
      'ADGDCBAA',
      'EAABDDFF',
    ]


    s = Solution()
    print(s.exist(A, 'BCDCB'))