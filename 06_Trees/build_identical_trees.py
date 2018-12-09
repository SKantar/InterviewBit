# Build Identical Trees
# https://www.interviewbit.com/problems/build-identical-trees
#
# Given two binary trees T1 and T2, you have to find minimum number of insertions to be done in
# T1 to make it structurally identical to T2. Return -1 if not possible.
#
# Notes
#
# Assume insertions are done in a normal fashion in the BSTs.
# Assume while inserting, if the value of a node v is equal to value being inserted, we
# insert it in left subtree of node v.
# You can insert any positive or negative integer.
# Example :
#
# Input 1:
#
# T1:       10
#          / \
#         9   20
#
# T2:       5
#          / \
#         2   7
#        /
#       1
#
# If you insert 8 into T1, it will be structurally identical to T2. Hence answer is 1.
#
#
# Input 2:
#
# T1:       10
#          / \
#         9   20
#
# T2:       5
#            \
#             7
#
# You cannot make T1 and T2 structurally identical. Hence answer is -1.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:

    def _num(self, A):
        if not A:
            return 0
        return 1 + self._num(A.left) + self._num(A.right)

    def _cntMatrix(self, A, B):
        if not A and not B:
            return 0

        if not A and B:
            return self._num(B)

        if not B and A:
            return -1

        left = self._cntMatrix(A.left, B.left)
        right = self._cntMatrix(A.right, B.right)

        if left == -1 or right == -1:
            return - 1

        return left + right

    # @param A : root node of tree
    # @param B : root node of tree
    # @return an integer
    def cntMatrix(self, A, B):
        return self._cntMatrix(A, B)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
