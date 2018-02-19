# Minimum Characters required to make a String Palindromic
# https://www.interviewbit.com/problems/minimum-characters-required-to-make-a-string-palindromic/
#
# You are given a string. The only operation allowed is to insert characters in the beginning of the string. How many minimum characters are needed to be inserted to make the string a palindrome string
#
# Example:
# Input: ABC
# Output: 2
# Input: AACECAAAA
# Output: 2
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    def is_palindrome(self, A):
        for i in range(len(A) // 2):
            if A[i] != A[len(A) - 1 - i]:
                return False
        return True

    # @param A : string
    # @return an integer
    def solve(self, A):

        if len(A) == 0:
            return 0

        for i in range(len(A) - 1, 0, -1):
            if self.is_palindrome(A[:i + 1]):
                return len(A) - 1 - i

        return len(A) - 1

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.solve("ABC"))
    print(s.solve("AACECAAAA"))
    print(s.solve(""))
    print(s.solve("00"))
