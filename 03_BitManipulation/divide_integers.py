# Divide Integers
# https://www.interviewbit.com/problems/divide-integers/
#
# Divide two integers without using multiplication, division and mod operator.
#
# Return the floor of the result of the division.
#
# Example:
#
# 5 / 2 = 2
#
# Also, consider if there can be overflow cases. For overflow case, return INT_MAX.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def divide(self, A, B):
        sign = -1 if ((A < 0) ^ (B < 0)) else 1

        dividend, divisor = abs(A), abs(B)
        quotient = temp = 0

        for i in range(31, -1, -1):
            if temp + (divisor << i) <= dividend:
                temp += (divisor << i)
                quotient |= 1 << i

        return self._bound_result(sign * quotient)

    def _bound_result(self, res):
        if res > (1 << 31) - 1:
            return (1 << 31) - 1
        elif res < -(1 << 32):
            return -(1 << 32)
        else:
            return res

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.divide(1, 2))
