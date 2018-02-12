# Implement Power Function
# https://www.interviewbit.com/problems/implement-power-function/
#
# Implement pow(x, n) % d.
#
# In other words, given x, n and d,
#
# find (xn % d)
#
# Note that remainders on division cannot be negative.
# In other words, make sure the answer you return is non negative.
#
# Input : x = 2, n = 3, d = 3
# Output : 2
#
# 2^3 % 3 = 8 % 3 = 2.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer
    def pow(self, x, n, d):
        if x == 0:
            return 0
        if n == 0:
            return 1
        elif n % 2 == 1:
            return (x * self.pow(x, n - 1, d)) % d
        return (self.pow(x, n // 2, d) ** 2) % d

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.pow(2, 3, 3))

