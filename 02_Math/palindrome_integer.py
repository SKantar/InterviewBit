# Palindrome Integer
# https://www.interviewbit.com/problems/palindrome-integer/
#
# Determine whether an integer is a palindrome. Do this without extra space.
#
# A palindrome integer is an integer x for which reverse(x) = x where reverse(x) is x with its digit reversed.
# Negative numbers are not palindromic.
#
# Example :
#
# Input : 12121
# Output : True
#
# Input : 123
# Output : False
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    def noDigits(self, A):
        no = 0
        while A:
            A //= 10
            no += 1
        return no


    # @param A : integer
    # @return an integer
    def isPalindrome(self, A):
        if A < 0:
            return 0
        n = self.noDigits(A)

        odd = False
        if n % 2:
            odd = True

        n //= 2

        nn = 0

        while n:
           nn = nn * 10 + A % 10
           A //=10
           n -= 1

        if odd:
            A //= 10

        return int(A == nn)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome(12121))
    print(s.isPalindrome(123))