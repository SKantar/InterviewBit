# Postorder Traversal
# https://www.interviewbit.com/problems/postorder-traversal/
#
# Given a binary tree, return the postorder traversal of its nodes’ values.
#
# Example :
#
# Given binary tree
#
#    1
#     \
#      2
#     /
#    3
# return [3,2,1].
#
# Using recursion is not allowed.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def postorderTraversal(self, A):

        ans, stack = list(), list()

        if A:
            stack.append(A)

        while stack:
            node, finished = stack[-1], True

            if node.right and not hasattr(node.right, 'visited'):
                stack.append(node.right)
                finished = False
            if node.left and not hasattr(node.left, 'visited'):
                stack.append(node.left)
                finished = False

            if finished:
                stack.pop()
                ans.append(node.val)
                node.visited = True

        return ans

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
