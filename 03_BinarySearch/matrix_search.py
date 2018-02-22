# Matrix Search
# https://www.interviewbit.com/problems/matrix-search/
#
# Write an efficient algorithm that searches for a value in an m x n matrix.
#
# This matrix has the following properties:
#
#         Integers in each row are sorted from left to right.
#         The first integer of each row is greater than or equal to the last integer of the previous row.
#
# Example:
#
# Consider the following matrix:
#
# [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
#
# Given target = 3, return 1 ( 1 corresponds to true )
#
# Return 0 / 1 ( 0 if the element is not present, 1 if the element is present ) for this problem
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer

    def binarySearch(self, A, B):
        low, high = 0, len(A) - 1

        while low <= high:
            mid = (low + high) // 2
            if A[mid] == B:
                return 1
            elif B < A[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return 0

    def searchMatrix(self, A, B):
        low, high = 0, len(A) - 1

        while low <= high:
            mid = low + (high - low) // 2
            if A[mid][0] <= B and A[mid][-1] >= B:
                return self.binarySearch(A[mid], B)
            elif A[mid][-1] < B:
                low = mid + 1
            else:
                high = mid - 1
        return 0

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.searchMatrix([
        [1,   3,  5,  7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ], 3))