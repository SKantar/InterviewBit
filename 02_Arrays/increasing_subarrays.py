# Increasing SubArrays
# https://www.interviewbit.com/problems/increasing-subarrays
#
# You are given an array of N positive integers, A1, A2 ,…, AN.
#
# Let’s denote by A[i, j] the subarray Ai, Ai+1 ,…, Aj.
#
# Count pairs (i, j) such that 1 ≤ i ≤ j ≤ N and subarray A[i, j] is increasing. Return the value
# modulo 109 + 7.
#
# Notes
#
# A subarray A1, A2 ,…, AN is increasing if Ai < Ai+1, for all 1 ≤ i < N.
# For example,
#
# A=[4, 5, 1, 2]
#
# All subarrays of size 1 are increasing.
#
# Subarrays A[1, 2], A[3, 4] of size 2 are increasing.
#
# No subarray of size 3 and 4 is increasing.
#
# So, total of 6 subarrays are increasing.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : list of integers
    # @return an integer
    def cntInc(self, A):
        n, answer = len(A), 0
        if n == 1:
            return 1

        start, end = 0, 1

        while end <= n:
            if end == n or A[end] <= A[end - 1]:

                l = end - start


                answer += (l * (l + 1)) // 2
                start = end
            end = end + 1

        return answer % ((10 ** 9) + 7)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
