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

            low, hihj = low + 1, high - 1

        return 1
