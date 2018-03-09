# Symmetric Binary Tree
# https://www.interviewbit.com/problems/symmetric-binary-tree/
#
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
#
# Example :
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# The above binary tree is symmetric.
# But the following is not:
#
#     1
#    / \
#   2   2
#    \   \
#    3    3
# Return 0 / 1 ( 0 for false, 1 for true ) for this problem
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Definition for a  binary tree node
# class TreeNode:
#   def __init__(self, x):
#       self.val = x
#	    self.left = None
#	    self.right = None

class Solution:

    def _isSymmetric(self, A, B):

        if not A and not B:
            return True
        elif (not A and B) or (A and not B):
            return False

        if A.val == B.val:
            return self._isSymmetric(A.left, B.right) and self._isSymmetric(A.right, B.left)
        return False

    # @param A : root node of tree
    # @return an integer
    def isSymmetric(self, A):
        if not A:
            return 1

        return int(self._isSymmetric(A.left, A.right))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


