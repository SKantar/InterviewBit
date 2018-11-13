# Arrange II
# https://www.interviewbit.com/problems/arrange-ii/
#
# You are given a sequence of black and white horses, and a set of K stables numbered 1 to K.
# You have to accommodate the horses into the stables in such a way that the following conditions
# are satisfied:
#
#         You fill the horses into the stables preserving the relative order of horses.
#         For instance, you cannot put horse 1 into stable 2 and horse 2 into stable 1.
#         You have to preserve the ordering of the horses.
#         No stable should be empty and no horse should be left unaccommodated.
#         Take the product (number of white horses * number of black horses) for each
#         stable and take the sum of all these products. This value should be the minimum
#         among all possible accommodation arrangements
#
# Example:
#
# Input: {WWWB} , K = 2
# Output: 0
#
# Explanation:
# We have 3 choices {W, WWB}, {WW, WB}, {WWW, B}
# for first choice we will get 1*0 + 2*1 = 2.
# for second choice we will get 2*0 + 1*1 = 1.
# for third choice we will get 3*0 + 0*1 = 0.
#
# Of the 3 choices, the third choice is the best option.
#
# If a solution is not possible, then return -1
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    def _score(self, A):
        n, w = len(A), A.count('W')
        return w * (n - w)

    def _arrange(self, A, B, memo={}):

        if B > len(A) or B == 0:
            return -1

        if B == 1:
            return self._score(A)

        n = len(A)
        if n == B:
            return 0

        if (A, B) in memo:
            return memo[(A, B)]

        best = min(self._score(A[:i]) + self._arrange(A[i:], B - 1, memo) for i in range(1, n - B + 2))

        memo[(A, B)] = best
        return best

    # @param A : string
    # @param B : integer
    # @return an integer
    def arrange(self, A, B):
        return self._arrange(A, B)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #