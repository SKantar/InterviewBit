# Power Of Two Integers
# https://www.interviewbit.com/problems/power-of-two-integers/
#
# Given a positive integer which fits in a 32 bit signed integer, find if it can be
# expressed as A^P where P > 1 and A > 0. A and P both should be integers.
#
# Example
#
# Input : 4
# Output : True
# as 2^2 = 4.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : integer
    # @return an integer
    def isPower(self, A):
        """B^E = A, B > 0, E > 1 """
        from math import ceil, floor
        for e in range(2, 33):
            sol = A ** (1.0 / e)

            if ceil(sol) ** e  == A or floor(sol) ** e == A:
                return 1
        return 0

if __name__ == "__main__":
    s = Solution()
    print(s.isPower(823543))