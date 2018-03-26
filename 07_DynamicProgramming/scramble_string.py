# Scramble String
# https://www.interviewbit.com/problems/scramble-string/
#
# Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.
#
# Below is one possible representation of s1 = “great”:
#
#
#     great
#    /    \
#   gr    eat
#  / \    /  \
# g   r  e   at
#            / \
#           a   t
#
#
# To scramble the string, we may choose any non-leaf node and swap its two children.
#
# For example, if we choose the node “gr” and swap its two children, it produces a scrambled string “rgeat”.
#
#     rgeat
#    /    \
#   rg    eat
#  / \    /  \
# r   g  e   at
#            / \
#           a   t
#
# We say that “rgeat” is a scrambled string of “great”.
#
# Similarly, if we continue to swap the children of nodes “eat” and “at”, it produces a scrambled string “rgtae”.
#
#     rgtae
#    /    \
#   rg    tae
#  / \    /  \
# r   g  ta  e
#        / \
#       t   a
#
# We say that “rgtae” is a scrambled string of “great”.
#
# Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1. Return 0/1 for this problem.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:

    def __init__(self):
        self._cache = {}

    def isScramble(self, A, B):

        if (A, B) in self._cache:
            return self._cache[(A, B)]

        if len(A) != len(B) or sorted(A) != sorted(B):
            self._cache[(A, B)] = 0
            return 0

        if len(A) == 1 or A == B:
            self._cache[(A, B)] = 1
            return 1

        for i in range(1, len(A)):
            if self.isScramble(A[:i], B[:i]) and self.isScramble(A[i:], B[i:]):
                self._cache[(A, B)] = 1
                return 1
            elif self.isScramble(A[:i], B[-i:]) and self.isScramble(A[i:], B[:-i]):
                self._cache[(A, B)] = 1
                return 1
        self._cache[(A, B)] = 0
        return 0

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.isScramble('rgtae', 'great'))
    print(s.isScramble('rgtae', 'great'))