# Sort by Color
# https://www.interviewbit.com/problems/sort-by-color/
#
# Given an array with n objects colored red, white or blue,
# sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.
#
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
#
# Note: Using library sort function is not allowed.
#
# Example :
#
# Input : [0 1 2 0 1 2]
# Modify array so that it becomes : [0 0 1 1 2 2]
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : list of integers
    # @return A after the sort
    def sortColors(self, A):
        r, b = 0, len(A) - 1
        i = 0

        while i <= b:
            if A[i] == 0:
                A[r], A[i] = A[i], A[r]
                r = r + 1
                i = max(i, r)
            elif A[i] == 2:
                A[b], A[i] = A[i], A[b]
                b = b - 1
            else:
                i += 1
        return A

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    A = [0]
    s.sortColors(A)
    print(A)