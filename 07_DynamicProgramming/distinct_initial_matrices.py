# Distinct Initial Matrices
# https://www.interviewbit.com/problems/distinct-initial-matrices
#
# For a A * B matrix of all distinct numbers from 1 to A * B, we first sort each column and then
# concatenate all columns in increasing order of indices to form an array of size A * B. Columns
# are numbered in increasing order from left to right.
#
# For example, if matrix is
#
# [1 5 6]
# [3 2 4]
#
# We first sort all columns to get
#
# [1 2 4]
# [3 5 6]
#
# Now, we concatenate columns in increasing order of indices to get an array
#
# [1, 3, 2, 5, 4, 6]
# Given this final array, you have to count how many distinct initial matrices are possible. Return the
# required answer modulo 109+7.
#
# Two matrices are distinct if:
#
# Either their dimensions are different.
# Or if any of the corresponding row in two matrices are different.
# Example:
#
# If input array is [1, 3, 2, 4], distinct initial matrices possible are:
#
# [1 3 2 4]
# -----------------------
# [1 2]
# [3 4]
# -----------------------
# [1 4]
# [3 2]
# -----------------------
# [3 2]
# [1 4]
# -----------------------
# [3 4]
# [1 2]
# -----------------------
#
# that is, a total of 5 matrices.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import math
class Solution:
    def _canCut(self, n, A):

        if len(A) % n != 0:
            return False

        part = len(A) // n

        for i in range(n):
            for j in range(1, part):
                if A[i * part + j] < A[i * part + j - 1]:
                    return False
        return True


    def _permWithRepetition(self, arr):
        n, tmp, div = len(arr), 1, 1
        for i in range(1, n):
            if arr[i - 1] == arr[i]:
                tmp += 1
            else:
                tmp = 1
                div *= math.factorial(tmp)
        return math.factorial(n) // div

    # @param A : list of integers
    # @return an integer
    def cntMatrix(self, A):
        n, count = len(A), 0

        for i in range(1, n + 1):
            if self._canCut(i, A):

                tmp, in_row = 1, n // i

                for j in range(1, i + 1):
                    tmp *= self._permWithRepetition(A[(j - 1) * in_row: j * in_row])
                count += tmp
        return int(count) % (10 ** 9 + 7)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #