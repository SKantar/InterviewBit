# Inorder Traversal of Cartesian Tree
# https://www.interviewbit.com/problems/inorder-traversal-of-cartesian-tree/
#
# Given an inorder traversal of a cartesian tree, construct the tree.
#
#  Cartesian tree : is a heap ordered binary tree, where the root is greater than all the elements in the subtree.
#  Note: You may assume that duplicates do not exist in the tree.
# Example :
#
# Input : [1 2 3]
#
# Return :
#           3
#          /
#         2
#        /
#       1
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : list of integers
    # @return the root node in the tree
    def buildTree(self, A):

        if not A:
            return None

        import operator
        max_index, max_value = max(enumerate(A), key=operator.itemgetter(1))

        root = TreeNode(max_value)
        root.left = self.buildTree(A[:max_index])
        root.right = self.buildTree(A[max_index + 1:])

        return root

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #