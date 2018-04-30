# Coins in a Line
# https://www.interviewbit.com/problems/coins-in-a-line/
#
# There are N coins (Assume N is even) in a line. Two players take turns to take a coin from one of the ends of the line until there are no more coins left. The player with the larger amount of money wins. Assume that you go first.
#
# Write a program which computes the maximum amount of money you can win.
#
# Example:
#
# suppose that there are 4 coins which have value
# 1 2 3 4
# now you are first so you pick 4
# then in next term
# next person picks 3 then
# you pick 2 and
# then next person picks 1
# so total of your money is 4 + 2 = 6
# next/opposite person will get 1 + 3 = 4
# so maximum amount of value you can get is 6
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


class Solution:
    # @param A : list of integers
    # @return an integer
    def maxcoin(self, A):

        if not A:
            return 0

        n = len(A)

        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = A[i]

        for i in range(0, n - 1):
            dp[i][i + 1] = max(A[i], A[i + 1])

        for k in range(3, n + 1):
            for j in range(0, n - k + 1):
                dp[j][j + k - 1] = max(
                    A[j] + min(dp[j + 2][j + k - 1],  dp[j + 1][j + k - 2]),
                    A[j + k - 1] + min(dp[j + 1][j + k - 2], dp[j][j + k - 3])
                )
        return dp[0][-1]


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == '__main__':
    A = [1, 2, 3, 4]
    s = Solution()
    # print(s.maxcoin([8, 15, 3, 7]))
    # print(s.maxcoin([2, 2, 2, 2]))
    # print(s.maxcoin([20, 30, 2, 2, 2, 10]))
    print(s.maxcoin([1, 100, 500, 10]))
