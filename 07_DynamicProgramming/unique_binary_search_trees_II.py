# Unique Binary Search Trees II
# https://www.interviewbit.com/problems/unique-binary-search-trees-ii/
#
# Given A, how many structurally unique BST’s (binary search trees) that store values 1...A?
#
# Example :
#
# Given A = 3, there are a total of 5 unique BST’s.
#
#
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:

    def _numTrees(self, A, dp={}):
        if A == 1:
            return 1
        if A not in dp:
            s = 0
            for i in range(1, A):
                s += self._numTrees(i) * self._numTrees(A - i)
            dp[A] = s

        return dp[A]

    # @param A : integer
    # @return an integer
    def numTrees(self, A):
        return self._numTrees(A + 1)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #