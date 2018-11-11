# Flatten Binary Tree to Linked List
# https://www.interviewbit.com/problems/flatten-binary-tree-to-linked-list/
#
# Given a binary tree, flatten it to a linked list in-place.
#
# Example :
# Given
#
#
#          1
#         / \
#        2   5
#       / \   \
#      3   4   6
# The flattened tree should look like:
#
#    1
#     \
#      2
#       \
#        3
#         \
#          4
#           \
#            5
#             \
#              6
# Note that the left child of all nodes should be NULL.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def _concatenate(self, first, second):
        first.right = second
        first.left = None

    def _flatten(self, A):
        if not A:
            return None, None

        leftStart, leftEnd = self._flatten(A.left)
        rightStart, rightEnd = self._flatten(A.right)

        if leftStart:
            self._concatenate(A, leftStart)
            self._concatenate(leftEnd, rightStart)
        elif rightStart:
            self._concatenate(A, rightStart)
        return A, rightEnd if rightEnd else A

    # @param A : root node of tree
    # @return the root node in the tree
    def flatten(self, A):
        root, _ = self._flatten(A)
        return root

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #