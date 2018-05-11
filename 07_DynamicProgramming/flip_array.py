# Flip Array
# https://www.interviewbit.com/problems/flip-array/
#
# Given an array of positive elements, you have to flip the sign of some of its elements such that the
# resultant sum of the elements of array should be minimum non-negative(as close to zero as possible).
# Return the minimum no. of elements whose sign needs to be flipped such that the resultant sum is minimum non-negative.
#
# Constraints:
#
#  1 <= n <= 100
#
# Sum of all the elements will not exceed 10,000.
#
# Example:
#
# A = [15, 10, 6]
#
# ans = 1 (Here, we will flip the sign of 15 and the resultant sum will be 1 )
#
# A = [14, 10, 4]
#
# ans = 1 (Here, we will flip the sign of 14 and the resultant sum will be 0)
#
#     Note that flipping the sign of 10 and 4 also gives the resultant sum 0 but flippings there are not minimum
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def solve(self, A):
        s, n = sum(A) // 2 + 1, len(A) + 1

        dp = [[i and float('inf') or 0] * (n) for i in range(s)]

        for i in range(s):
            for j in range(1, n):
                if i - A[j - 1] >= 0:
                    dp[i][j] = min(dp[i][j - 1], dp[i - A[j - 1]][j - 1] + 1)
                else:
                    dp[i][j] = dp[i][j - 1]

        for row in dp[::-1]:
            if row[-1] < float('inf'):
                return row[-1]
        return None

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.solve([ 10, 42, 8, 11, 23]))

