# https://www.interviewbit.com/problems/rotate-matrix/
#
# You are given an n x n 2D matrix representing an image.
#
# Rotate the image by 90 degrees (clockwise).
#
# You need to do this in place.
#
# Note that if you end up using an additional array, you will only receive partial score.
#
# Example:
#
# If the array is
#
#  1 2
#  3 4
#
# Then the rotated array becomes:
#
#  3 1
#  4 2
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def rotate(self, A):

        n = len(A) - 1

        for i in range(len(A) // 2):
            for j in range(i, n - i):
                t = A[i][j]
                A[i][j] = A[n - j][i]
                A[n - j][i] = A[n - i][n - j]
                A[n - i][n - j] = A[j][n - i]
                A[j][n - i] = t

        return A

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    matrix = [
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]
    ]

    s = Solution()
    s.rotate(matrix)
    print(matrix)

    matrix = [
      [ 5, 1, 9,11],
      [ 2, 4, 8,10],
      [13, 3, 6, 7],
      [15,14,12,16]
    ]

    s.rotate(matrix)
    print(matrix)
