# Binary Tree From Inorder And Postorder
# https://www.interviewbit.com/problems/binary-tree-from-inorder-and-postorder/
#
# Given inorder and postorder traversal of a tree, construct the binary tree.
#
#  Note: You may assume that duplicates do not exist in the tree.
# Example :
#
# Input :
#         Inorder : [2, 1, 3]
#         Postorder : [2, 3, 1]
#
# Return :
#             1
#            / \
#           2   3
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # @param A : list of integers
    # @param B : list of integers
    # @return the root node in the tree
    def buildTree(self, inorder, postorder):
        if not postorder:
            return None

        root = TreeNode(postorder.pop())
        idx = inorder.index(root.val)

        root.left = self.buildTree(inorder[:idx], postorder[:idx])
        root.right = self.buildTree(inorder[idx + 1:], postorder[idx:])

        return root

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #




