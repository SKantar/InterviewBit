# Knight On Chess Board
# https://www.interviewbit.com/problems/knight-on-chess-board/
#
# Given any source point and destination point on a chess board, we need to find whether Knight can move to the destination or not.
#
# Knight's movements on a chess board
#
# The above figure details the movements for a knight ( 8 possibilities ). Note that a knight cannot go out of the board.
#
# If yes, then what would be the minimum number of steps for the knight to move to the said point.
# If knight can not move from the source point to the destination point, then return -1
#
# Input:
#
# N, M, x1, y1, x2, y2
# where N and M are size of chess board
# x1, y1  coordinates of source point
# x2, y2  coordinates of destination point
#
# Output:
#
# return Minimum moves or -1
#
# Example
#
# Input : 8 8 1 1 8 8
# Output :  6
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:

    steps = ((2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2))

    def _knight(self, N, M, x1, y1, x2, y2):
        from collections import deque

        if x1 == x2 and y1 == y2:
            return 0

        visited = [[-1] * M for _ in range(N)]

        queue = deque()
        queue.append((x1, y1))

        visited[x1][y1] = 0

        while queue:
            i, j = queue.popleft()

            for step in Solution.steps:
                tx, ty = step

                if i + tx == x2 and j + ty == y2:
                    return visited[i][j] + 1

                if 0 <= i + tx < N and 0 <= j + ty < M and visited[i + tx][j + ty] < 0:
                    visited[i + tx][j + ty] = visited[i][j] + 1
                    queue.append((i + tx, j + ty))
        return -1

    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @param E : integer
    # @param F : integer
    # @return an integer
    def knight(self, A, B, C, D, E, F):
        return self._knight(A, B, C - 1, D - 1, E - 1, F - 1)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.knight(8, 8, 1, 1, 8, 8))




