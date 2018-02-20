# Palindrome String
# https://www.interviewbit.com/problems/palindrome-string/
#
# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
#
# Example:
#
# "A man, a plan, a canal: Panama" is a palindrome.
#
# "race a car" is not a palindrome.
#
# Return 0 / 1 ( 0 for false, 1 for true ) for this problem
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# class Solution:
#     # @param A : string
#     # @return an integer
#     def _clear_string(self, A):
#         return ''.join(c.lower() for c in A if c.isalnum())
#
#     def _is_palindrome(self, A):
#         for i in range(len(A) // 2):
#             if A[i] != A[len(A) - 1 - i]:
#                 return False
#         return True
#
#     def isPalindrome(self, A):
#         A = self._clear_string(A)
#         return 1 if self._is_palindrome(A) else 0

class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
        low, high = 0, len(A) - 1
        while low < high:

            while low < high and not A[low].isalnum():
                low += 1

            while low < high and not A[high].isalnum():
                high -= 1

            if A[low].lower() != A[high].lower():
                return 0

            low, high = low + 1, high - 1

        return 1

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome('A man, a plan, a canal: Panama"'))
    print(s.isPalindrome('race a car'))

