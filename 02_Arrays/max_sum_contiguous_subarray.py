# Max Sum Contiguous Subarray
# https://www.interviewbit.com/problems/max-sum-contiguous-subarray
#
# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
#
# For example:
#
# Given the array [-2, 1, -3, 4, -1, 2, 1, -5, 4],
# the contiguous subarray [4, -1, 2, 1] has the largest sum = 6.
#
# For this problem, return the maximum sum.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        tmp_max = tmp_sum = A[0]

        for i in range(1, len(A)):
            tmp_sum = max(A[i], tmp_sum + A[i])
            tmp_max = max(tmp_sum, tmp_max)
        return tmp_max

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

    s = Solution()
    print(s.maxSubArray(A))

