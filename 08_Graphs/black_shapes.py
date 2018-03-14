# Black Shapes
# https://www.interviewbit.com/problems/black-shapes/
#
# Given N * M field of O's and X's, where O=white, X=black
# Return the number of black shapes. A black shape consists of one or more adjacent X's (diagonals not included)
#
# Example:
#
# OOOXOOO
# OOXXOXO
# OXOOOXO
#
# answer is 3 shapes are  :
# (i)    X
#      X X
# (ii)
#       X
#  (iii)
#       X
#       X
# Note that we are looking for connected shapes here.
#
# For example,
#
# XXX
# XXX
# XXX
# is just one single connected black shape.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:

    moves = ((0, 1), (1, 0), (0, -1), (-1, 0))

    def _dfs(self, A, i, j, flag):
        if A[i][j] != 'X':
            return

        A[i] = A[i][:j] + str(flag) + A[i][j + 1:]

        for move in Solution.moves:
            tx, ty = move
            if 0 <= i + tx < len(A) and 0 <= j + ty < len(A[i + tx]):
                self._dfs(A, i + tx, j + ty, flag)

    # @param A : list of strings
    # @return an integer
    def black(self, A):
        cnt = 0
        for i in range(len(A)):
            for j in range(len(A[i])):
                if A[i][j] == 'X':
                    self._dfs(A, i, j, '1')
                    cnt += 1

        return cnt


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    # print(s.black([
    #     'OOOXOOO',
    #     'OOXXOXO',
    #     'OXOOOXO'
    # ]))
    # print(s.black([
    #     'XXX',
    #     'XXX',
    #     'XXX'
    # ]))

    A = [
        'OOOXOOXOXXOXXOOXO',
        'XXOOXOXOOOOOXOOOX',
        'OXXXXOOOXXOXOXOXO',
        'OOXXXOOOXXXOOXOXX',
    ]


    print(s.black(A))

    print(A)