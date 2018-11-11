# Invert the Binary Tree
# https://www.interviewbit.com/problems/invert-the-binary-tree/
#
# Given a binary tree, invert the binary tree and return it.
# Look at the example for more details.
#
# Example :
# Given binary tree
#
#      1
#    /   \
#   2     3
#  / \   / \
# 4   5 6   7
# invert and return
#
#      1
#    /   \
#   3     2
#  / \   / \
# 7   6 5   4
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def _invertTree(self, A):
        if not A:
            return

        A.left, A.right = A.right, A.left
        self._invertTree(A.left)
        self._invertTree(A.right)

    # @param A : root node of tree
    # @return the root node in the tree
    def invertTree(self, A):
        self._invertTree(A)
        return A

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #