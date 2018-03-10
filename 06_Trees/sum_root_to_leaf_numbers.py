# Sum Root to Leaf Numbers
# https://www.interviewbit.com/problems/sum-root-to-leaf-numbers/
#
# Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
#
# An example is the root-to-leaf path 1->2->3 which represents the number 123.
#
# Find the total sum of all root-to-leaf numbers % 1003.
#
# Example :
#
#     1
#    / \
#   2   3
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
#
# Return the sum = (12 + 13) % 1003 = 25 % 1003 = 25.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def _sumNumbers(self, node, tmp):
        if not node:
            return 0

        tmp = tmp * 10 + node.val

        if not node.left and not node.right:
            return tmp

        return self._sumNumbers(node.left, tmp) + self._sumNumbers(node.right, tmp)

    # @param A : root node of tree
    # @return an integer
    def sumNumbers(self, A):
        return self._sumNumbers(A, 0) % 1003

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
