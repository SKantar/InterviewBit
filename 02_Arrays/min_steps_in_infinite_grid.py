# Min Steps in Infinite Grid
# https://www.interviewbit.com/problems/min-steps-in-infinite-grid/
#
# You are in an infinite 2D grid where you can move in any of the 8 directions :
#
# (x,y) to (x+1, y), (x - 1, y), (x, y+1), (x, y-1), (x-1, y-1), (x+1,y+1), (x-1,y+1), (x+1,y-1)
#
# You are given a sequence of points and the order in which you need to cover the points. Give
# the minimum number of steps in which you can achieve it. You start from the first point.
#
# Example:
#
# Input : [(0, 0), (1, 1), (1, 2)]
# Output : 2
#
# It takes 1 step to move from (0, 0) to (1, 1). It takes one more step to move from (1, 1) to (1, 2).
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def coverPoints(self, A, B):
        prev = A.pop(0), B.pop(0)
        res = 0
        for elem in zip(A, B):
            res += max(abs(elem[0] - prev[0]), abs(elem[1] - prev[1]))
            prev = elem
        return res

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    A = [0, 1, 1]
    B = [0, 1, 2]

    s = Solution()
    print(s.coverPoints(A, B))