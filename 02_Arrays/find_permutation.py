# Find Permutation
# https://www.interviewbit.com/problems/find-permutation/
#
# Given a positive integer n and a string s consisting only of letters D or I,
# you have to find any permutation of first n positive integer that satisfy
# the given input string.
#
# D means the next number is smaller, while I means the next number is greater.
#
# Notes
#
#     Length of given string s will always equal to n - 1
#     Your solution should run in linear time and space.
#
# Example :
# Input 1:
#
# n = 3
#
# s = ID
#
# Return: [1, 3, 2]
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:

    def _reverse(self, A, i, j):
        while i < j:
            A[i], A[j] = A[j], A[i]
            i, j = i + 1, j - 1

    # @param A : string
    # @param B : integer
    # @return a list of integers
    def findPerm(self, A, B):
        res = list(range(1, B + 1))

        start = None

        for i, a in enumerate(A):
            if a == 'D' and start is None:
                start = i

            if a == 'I' and start is not None:
                self._reverse(res, start, i)
                start = None

        if start is not None:
            self._reverse(res, start, len(res) - 1)

        return res



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.findPerm("IIIII", 6))
    print(s.findPerm("IIDII", 6))
    print(s.findPerm("IIDID", 6))
    print(s.findPerm("DIDID", 6))
    print(s.findPerm("DDDII", 6))
    print(s.findPerm("I", 2))