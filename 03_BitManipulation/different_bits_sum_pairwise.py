# Different Bits Sum Pairwise
# https://www.interviewbit.com/problems/different-bits-sum-pairwise/
#
# We define f(X, Y) as number of different corresponding bits in binary representation of X and Y.
# For example, f(2, 7) = 2, since binary representation of 2 and 7 are 010 and 111, respectively.
# The first and the third bit differ, so f(2, 7) = 2.
#
# You are given an array of N positive integers, A1, A2 ,…, AN. Find sum of f(Ai, Aj) for all
# pairs (i, j) such that 1 ≤ i, j ≤ N. Return the answer modulo 109+7.
#
# For example,
#
# A=[1, 3, 5]
#
# We return
#
# f(1, 1) + f(1, 3) + f(1, 5) +
# f(3, 1) + f(3, 3) + f(3, 5) +
# f(5, 1) + f(5, 3) + f(5, 5) =
#
# 0 + 1 + 1 +
# 1 + 0 + 2 +
# 1 + 2 + 0 = 8
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : list of integers
    # @return an integer
    def cntBits(self, A):
        flag, n, ans = 1, len(A), 0

        for i in range(32):
            cnt = 0
            for a in A:
                cnt += (a & flag) > 0

            ans = (ans + cnt * (n - cnt)) % 1000000007

            flag <<= 1

        return (ans * 2) % 1000000007

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.cntBits([1, 3, 5]))
