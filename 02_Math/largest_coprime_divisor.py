# Largest Coprime Divisor
# https://www.interviewbit.com/problems/largest-coprime-divisor/
#
# You are given two positive numbers A and B. You need to find the maximum valued integer X such that:
#
#     X divides A i.e. A % X = 0
#     X and B are co-prime i.e. gcd(X, B) = 1
#
# For example,
#
# A = 30
# B = 12
# We return
# X = 5
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


class Solution:

    def _gcd(self, A, B):
        while B:
            A, B = B, A % B
        return A

    # @param A : integer
    # @param B : integer
    # @return an integer
    def cpFact(self, A, B):

        while True:
            gcd = self._gcd(A, B)

            if gcd == 1:
                break

            A = A // gcd

        return A

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":

    s = Solution()
    print(s.cpFact(15, 3))
    print(s.cpFact(14, 28))
    print(s.cpFact(30, 12))