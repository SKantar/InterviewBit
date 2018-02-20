# Minimize the absolute difference
# https://www.interviewbit.com/problems/minimize-the-absolute-difference/
#
# Given three sorted arrays A, B and Cof not necessarily same sizes.
#
# Calculate the minimum absolute difference between the maximum and minimum number from the triplet a, b, c
# such that a, b, c belongs arrays A, B, C respectively.
#
# i.e. minimize | max(a,b,c) - min(a,b,c) |.
#
# Example :
#
# Input:
#
# A : [ 1, 4, 5, 8, 10 ]
# B : [ 6, 9, 15 ]
# C : [ 2, 3, 6, 6 ]
#
# Output:
#
# 1
#
# Explanation: We get the minimum difference for a=5, b=6, c=6 as | max(a,b,c) - min(a,b,c) | = |6-5| = 1.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        ia = ib = ic = 0
        diff = float("INF")
        while True:
            diff = min(diff, abs(max(A[ia], B[ib], C[ic]) - min(A[ia], B[ib], C[ic])))

            if ia < len(A) - 1 and B[ib] >= A[ia] <= C[ic]:
                ia += 1
            elif ib < len(B) - 1 and A[ia] >= B[ib] <= C[ic]:
                ib += 1
            elif ic < len(C) - 1 and A[ia] >= C[ic] <= B[ib]:
                ic += 1
            else:
                break
        return diff


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
if __name__ == "__main__":
    A = [ 1, 4, 5, 8, 10 ]
    B = [ 6, 9, 15 ]
    C = [ 2, 3, 6, 6 ]

    s = Solution()
    print(s.solve(A, B, C))