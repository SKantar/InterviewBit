# Coin Sum Infinite
# https://www.interviewbit.com/problems/coin-sum-infinite/
#
# You are given a set of coins S. In how many ways can you make sum
# N assuming you have infinite amount of each coin in the set.
#
# Note : Coins in set S will be unique. Expected space complexity of this problem is O(N).
#
# Example :
#
# Input :
# 	S = [1, 2, 3]
# 	N = 4
#
# Return : 4
#
# Explanation : The 4 possible ways are
# {1, 1, 1, 1}
# {1, 1, 2}
# {2, 2}
# {1, 3}
# Note that the answer can overflow. So, give us the answer % 1000007
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def coinchange2(self, A, B):
        dp = [0] * (B + 1)
        dp[0] = 1

        for a in A:
            for i in range(1, B + 1):
                if a <= i:
                    dp[i] = (dp[i] + dp[i - a]) % 1000007
        return dp[-1]

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == '__main__':
    s = Solution()
    print(s.coinchange2([1, 2, 3], 4))


