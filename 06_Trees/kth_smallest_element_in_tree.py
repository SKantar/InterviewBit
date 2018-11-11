# Kth Smallest Element In Tree
# https://www.interviewbit.com/problems/kth-smallest-element-in-tree/
#
# Given a binary search tree, write a function to find the kth smallest element in the tree.
#
# Example :
#
# Input :
#   2
#  / \
# 1   3
#
# and k = 2
#
# Return : 2
#
# As 2 is the second smallest element in the tree.
#  NOTE : You may assume 1 <= k <= Total number of nodes in BST
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def _kthsmallest(self, A, i, B):
        if not A:
            return None
        kthsmallest = self._kthsmallest(A.left, i, B)
        if kthsmallest is None:
            if i[0] == B:
                return A.val
            i[0] += 1
            kthsmallest = self._kthsmallest(A.right, i, B)
        return kthsmallest

    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, B):
        return self._kthsmallest(A, [1], B)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #