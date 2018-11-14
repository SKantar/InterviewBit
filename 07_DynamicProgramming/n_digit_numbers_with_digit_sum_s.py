# N digit numbers with digit sum S
# https://www.interviewbit.com/problems/n-digit-numbers-with-digit-sum-s-/
#
# Find out the number of N digit numbers, whose digits on being added equals to a given number S.
# Note that a valid number starts from digits 1-9 except the number 0 itself. i.e. leading
# zeroes are not allowed.
#
# Since the answer can be large, output answer modulo 1000000007
#
# **
# N = 2, S = 4
# Valid numbers are {22, 31, 13, 40}
# Hence output 4.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, N, S):

        arr = [[0] * (S + 1) for _ in range(N + 1)]

        arr[0][0] = 1
        for n in range(N):
            for s in range(S):
                for digit in range(10):
                    if s + digit <= S:
                        arr[n + 1][s + digit] += arr[n][s]
                    else:
                        break

        return arr[N][S] % 1000000007

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #