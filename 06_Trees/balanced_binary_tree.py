# Balanced Binary Tree
# https://www.interviewbit.com/problems/balanced-binary-tree/
#
# Given a binary tree, determine if it is height-balanced.
#
#  Height-balanced binary tree : is defined as a binary tree in which the depth of the two
# subtrees of every node never differ by more than 1.
# Return 0 / 1 ( 0 for false, 1 for true ) for this problem
#
# Example :
#
# Input :
#           1
#          / \
#         2   3
#
# Return : True or 1
#
# Input 2 :
#          3
#         /
#        2
#       /
#      1
#
# Return : False or 0
#          Because for the root node, left subtree has depth 2 and right subtree has depth 0.
#          Difference = 2 > 1.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    from math import fabs
    def _isBalanced(self, A):
        if not A:
            return True, 0

        isBalancedLeft, heightLeft = self._isBalanced(A.left)
        isBalancedRight, heightRight = self._isBalanced(A.right)

        isBalanced = isBalancedLeft and isBalancedRight and Solution.fabs(heightLeft - heightRight) <= 1

        return isBalanced, max(heightLeft, heightRight) + 1

    # @param A : root node of tree
    # @return an integer
    def isBalanced(self, A):
        return int(self._isBalanced(A)[0])

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #