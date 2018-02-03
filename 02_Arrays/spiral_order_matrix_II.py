# Spiral Order Matrix II
# https://www.interviewbit.com/problems/spiral-order-matrix-ii/
#
# Given an integer n, generate a square matrix filled with elements from 1 to n^    2 in spiral order.
#
# Example:
#
# Given n = 3,
#
# You should return the following matrix:
#
# [
#   [ 1, 2, 3 ],
#   [ 8, 9, 4 ],
#   [ 7, 6, 5 ]
# ]
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, A):

        mat = [[0] * A for i in range(A)]
        steps, curr = [(0, 1), (1, 0), (0, -1), (-1, 0)], 0
        i = j = k = 0   # current position (i, j), and current ring k
        tmp = 1         # current element


        while tmp <= A * A:
            mat[i][j] = tmp
            tmp += 1
            i, j = i + steps[curr][0], j + steps[curr][1]

            # check does current position match any corner or current ring (k)
            curr += (curr == 0 and j == A - 1 - k) + (curr == 1 and i == A - 1 - k) + (curr == 2 and j == k) + (curr == 3 and i == k)

            if curr == 4:
                i, j, k, curr = i + 1, j + 1, k + 1, 0

        return mat

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.generateMatrix(2))
    print(s.generateMatrix(3))
    print(s.generateMatrix(4))
    print(s.generateMatrix(5))
    print(s.generateMatrix(6))
