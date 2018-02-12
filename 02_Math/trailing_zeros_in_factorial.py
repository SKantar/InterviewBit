# Trailing Zeros in Factorial
# https://www.interviewbit.com/problems/trailing-zeros-in-factorial/
#
# Given an integer n, return the number of trailing zeroes in n!.
#
# Note: Your solution should be in logarithmic time complexity.
#
# Example :
#
# n = 5
# n! = 120
# Number of trailing zeros = 1
# So, return 1
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


class Solution:
    def trailingZeroes(self, n):
        """ Find occurrences of 5, 25, 125, 625 ..."""
        count, i = 0, 5

        while n // i >= 1:
            count += n // i
            i *= 5
        return count

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.trailingZeroes(5))
    print(s.trailingZeroes(10))
    print(s.trailingZeroes(100))


