# Sorted Permutation Rank with Repeats
# https://www.interviewbit.com/problems/sorted-permutation-rank-with-repeats/
#
# Given a string, find the rank of the string amongst its permutations sorted lexicographically.
# Note that the characters might be repeated. If the characters are repeated, we need to look at the rank in unique permutations.
# Look at the example for more details.
#
# Example :
#
# Input : 'aba'
# Output : 2
#
# The order permutations with letters 'a', 'a', and 'b' :
# aab
# aba
# baa
#
# The answer might not fit in an integer, so return your answer % 1000003
#
#     NOTE: 1000003 is a prime number
#     NOTE: Assume the number of characters in string < 1000003
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:

    def _fac(self, n):
        return 1 if n <= 1 else n * self._fac(n - 1)


    def _populate_qty(self, A):
        dp = [0] * 256

        for a in A:
            dp[ord(a)] += 1

        cnt = list(dp)

        for i in range(1, len(dp)):
            dp[i] += dp[i - 1]

        return dp, cnt

    def _update_qty(self, char, dp):
        for i in range(ord(char),  len(dp)):
            dp[i] -= 1

    def _calc_divider(self, char, cnt):
        res = 1
        for i in range(0, 256):
            if cnt[i] > 1:
                res *= self._fac(cnt[i])
        return res

    # @param A : string
    # @return an integer
    def findRank(self, A):

        dp, cnt = self._populate_qty(A)
        mul, rank = self._fac(len(A)), 1

        for i, a in enumerate(A):
            mul = mul // (len(A) - i)

            rank += (dp[ord(a) - 1]) * mul // self._calc_divider(a, cnt)
            self._update_qty(a, dp)

            cnt[ord(a)] -= 1

        return rank % 1000003


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.findRank("bbbcccaaa"))




