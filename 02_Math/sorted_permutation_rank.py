# Sorted Permutation Rank
# https://www.interviewbit.com/problems/sorted-permutation-rank/
#
# Given a string, find the rank of the string amongst its permutations sorted lexicographically.
# Assume that no characters are repeated.
#
# Example :
#
# Input : 'acb'
# Output : 2
#
# The order permutations with letters 'a', 'c', and 'b' :
# abc
# acb
# bac
# bca
# cab
# cba
#
# The answer might not fit in an integer, so return your answer % 1000003
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:

    def _fac(self, n):
        return 1 if n <= 1 else n * self._fac(n - 1)


    def _populate_qty(self, A):
        dp = [0] * 256

        for a in A:
            dp[ord(a)] += 1

        for i in range(1, len(dp)):
            dp[i] += dp[i - 1]

        return dp

    def _update_qty(self, char, dp):
        for i in range(ord(char),  len(dp)):
            dp[i] -= 1

    # @param A : string
    # @return an integer
    def findRank(self, A):

        dp = self._populate_qty(A)
        mul, rank = self._fac(len(A)), 1

        for i, a in enumerate(A):
            mul = mul // (len(A) - i)
            rank += dp[ord(a) - 1] * mul

            self._update_qty(a, dp)

        return rank % 1000003


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.findRank("acb"))



