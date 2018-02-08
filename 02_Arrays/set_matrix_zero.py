# Set Matrix Zeros
# https://www.interviewbit.com/problems/set-matrix-zeros/
#
# Given an m x n matrix of 0s and 1s, if an element is 0, set its entire row and column to 0.
#
# Do it in place.
#
# Example
#
# Given array A as
#
# 1 0 1
# 1 1 1
# 1 1 1
#
# On returning, the array A should be :
#
# 0 0 0
# 1 0 1
# 1 0 1
#
# Note that this will be evaluated on the extra memory used. Try to minimize the space and time complexity.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        # Empty matrix
        if len(matrix) == 0 or len(matrix[0]) == 0: return

        row = [False] * len(matrix)
        column = [False] * len(matrix[0])

        # Record the rows and columns with element(s) being zero.
        for rowIndex in range(len(matrix)):
            for colIndex in range(len(matrix[0])):
                if matrix[rowIndex][colIndex] == 0:
                    row[rowIndex] = True
                    column[colIndex] = True

        # Set the qualified entire row(s) and column(s) to zero.
        for rowIndex in range(len(matrix)):
            for colIndex in range(len(matrix[0])):
                if row[rowIndex] == True or column[colIndex] == True:
                    matrix[rowIndex][colIndex] = 0

        return matrix

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #