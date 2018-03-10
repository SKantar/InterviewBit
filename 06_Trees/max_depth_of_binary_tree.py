# Max Depth of Binary Tree
# https://www.interviewbit.com/problems/max-depth-of-binary-tree/
#
# Given a binary tree, find its maximum depth.
#
# The maximum depth of a binary tree is the number of nodes along the longest path from the root node down to the farthest leaf node.
#
#  NOTE : The path has to end on a leaf node.
# Example :
#
#          1
#         /
#        2
# max depth = 2.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    # @param A : root node of tree
    # @return an integer
    def maxDepth(self, A):
        if A is None:
            return 0
        return max(self.maxDepth(A.left), self.maxDepth(A.right)) + 1

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #