# Prime Sum
# https://www.interviewbit.com/problems/prime-sum/
#
# Given an even number ( greater than 2 ), return two prime numbers whose sum will be equal to given number.
#
# NOTE A solution will always exist. read Goldbach’s conjecture
#
# Example:
#
#
# Input : 4
# Output: 2 + 2 = 4
#
# If there are more than one solutions possible, return the lexicographically smaller solution.
#
# If [a, b] is one solution with a <= b,
# and [c, d] is another solution with c <= d, then
#
# [a, b] < [c, d]
#
# If a < c OR a==c AND b < d.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    def primesum(self, n):
        for i in range(2, n):
            if self.is_prime(i) and self.is_prime(n - i):
                return i, n - i

    def is_prime(self, n):
        if n < 2:
            return False

        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False

        return True

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.primesum(4))
    print(s.primesum(4))
