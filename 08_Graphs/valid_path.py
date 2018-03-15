# Valid Path
# https://www.interviewbit.com/problems/valid-path/
#
# There is a rectangle with left bottom as  (0, 0) and right up as (x, y). There are N
# circles such that their centers are inside the rectangle. Radius of each circle is R.
# Now we need to find out if it is possible that we can move from (0, 0) to (x, y)
# without touching any circle.
# Note : We can move from any cell to any of its 8 adjecent neighbours and we cannot move
# outside the boundary of the rectangle at any point of time.
#
# Constraints
#  0 <= x , y , R <= 100
#  1 <= N <= 1000
# Center of each circle would lie within the grid
#
# Input
# Input contains x, y , N , R  and two array of size N containing centers of circles.
# The ith index of first array contains x co-ordinate of the ith circle and ith index of
# second array contains the y co-ordinate of the ith circle.
#
# Output
# YES or NO depending on weather it is possible to reach cell  (x,y) or not starting from (0,0).
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    import sys
    sys.setrecursionlimit(100000000)
    moves = ((0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1))

    def in_circle(self, D, E, F, y, x):
        for z in range(len(E)):
            if ((E[z] - x) ** 2 + (F[z] - y) ** 2) ** 0.5 <= D:
                return True
        return False

    def _dfs(self, y, x, visited, A, B, C, D, E, F):
        if x == A and y == B:
            return True

        visited[y][x] = True

        for move in Solution.moves:
            tx, ty = move
            if 0 <= y + ty <= B and 0 <= x + tx <= A and not visited[y + ty][x + tx]:
                if not self.in_circle(D, E, F, y + ty, x + tx) and self._dfs(y + ty, x + tx, visited, A, B, C, D, E, F):
                    return True
        return False


    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @param E : list of integers
    # @param F : list of integers
    # @return a strings
    def solve(self, A, B, C, D, E, F):
        visited = [[False] * (A + 1) for _ in range(B+1)]
        return 'YES' if self._dfs(0, 0, visited, A, B, C, D, E, F) else 'NO'

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.solve(2, 3, 1, 1, [2], [3]))
    print(s.solve(41, 67, 5, 0, [5, 17, 16, 12, 0, 40], [5, 52, 61, 61, 25, 31]))



