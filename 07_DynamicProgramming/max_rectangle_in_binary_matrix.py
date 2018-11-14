# Max Rectangle in Binary Matrix
# https://www.interviewbit.com/problems/max-rectangle-in-binary-matrix/
#
# Given a 2D binary matrix filled with 0’s and 1’s, find the largest rectangle containing all ones and return its area.
#
# Bonus if you can solve it in O(n^2) or less.
#
# Example :
#
# A : [  1 1 1
#        0 1 1
#        1 0 0
#     ]
#
# Output : 4
#
# As the max area rectangle is created by the 2x2 rectangle created by (0,1), (0,2), (1,1) and (1,2)
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    def largest_rectangle_histogram(self, array):
        array.append(0)  # dummy bar
        stack = [-1]
        max_area = 0
        for i, curr in enumerate(array):
            while curr < array[stack[-1]]:
                height = array[stack.pop()]
                width = i - stack[-1] - 1
                curr_area = width * height
                max_area = max(max_area, curr_area)
            stack.append(i)
        array.pop()
        return max_area

    # @param matrix : list of list of integers
    # @return an integer
    def maximalRectangle(self, matrix):
        # preprocess matrix
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]:
                    matrix[i][j] += matrix[i - 1][j]

        # find largest rectangle in histogram for each row
        max_area = 0
        for row in matrix:
            max_area = max(max_area, self.largest_rectangle_histogram(row))
        return max_area

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #