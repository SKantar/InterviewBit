# Length of Longest Subsequence
# https://www.interviewbit.com/problems/length-of-longest-subsequence/
#
# Given an array of integers, find the length of longest subsequence which is first increasing then decreasing.
#
# **Example: **
#
# For the given array [1 11 2 10 4 5 2 1]
#
# Longest subsequence is [1 2 10 4 2 1]
#
# Return value 6
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestSubsequenceLength(self, A):
        n = len(A)
        inc = [1] * n
        for i in range(1, n):
            for j in range(0, i):
                if A[i] > A[j] and inc[j] + 1 > inc[i]:
                    inc[i] = inc[j] + 1

        dec = [1] * n
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if A[i] > A[j] and dec[j] + 1 > dec[i]:
                    dec[i] = dec[j] + 1
        maximum = 1
        for x, y in zip(inc, dec):
            maximum = max(maximum, x + y)
        return maximum - 1

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #