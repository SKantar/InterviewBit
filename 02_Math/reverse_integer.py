# Reverse integer
# https://www.interviewbit.com/problems/reverse-integer/
#
# Reverse digits of an integer.
#
# Example1:
#
# x = 123,
#
# return 321
# Example2:
#
# x = -123,
#
# return -321
#
# Return 0 if the result overflows and does not fit in a 32 bit signed integer
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : integer
    # @return an integer
    def reverse(self, A):

        sign = -1 if A < 0 else 1
        res, A = 0, abs(A)
        while A > 0:
            res = res * 10 + A % 10
            A = A // 10

        return 0 if res > 1 << 32 - 1 else sign * res

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.reverse(-123))