# Sub Matrices with sum Zero
# https://www.interviewbit.com/problems/sub-matrices-with-sum-zero/
#
# Given a 2D matrix, find the number non-empty sub matrices, such that the sum of the elements
# inside the sub matrix is equal to 0. (note: elements might be negative).
#
# Example:
#
# Input
#
# -8 5  7
# 3  7 -8
# 5 -8  9
#
# Output
# 2
#
# Explanation
# -8 5 7
# 3 7 -8
# 5 -8 9
#
# -8 5 7
# 3 7 -8
# 5 -8 9
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        n, m = len(A), len(A[0]) if A else 0

        if not (n and m):
            return 0

        dp_sum, ans = [[0] * (m + 1) for _ in range(n + 1)], 0

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp_sum[i][j] = dp_sum[i-1][j] + dp_sum[i][j-1] - dp_sum[i-1][j-1] + A[i-1][j-1]

        for i in range(1, n + 1):
            for j in range(i, n + 1):
                counti = {0: 1}
                for k in range(1, m + 1):
                    val = dp_sum[j][k] - dp_sum[i - 1][k]
                    if val in counti:
                        ans = ans + counti[val]
                        counti[val] = counti[val] + 1
                    else:
                        counti[val] = 1
        return ans

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":

    A = [
          [0, 0, 0],
          [0, 0, 0]
        ]

    s = Solution()
    print(s.solve(A))