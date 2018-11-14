# Max Sum Path in Binary Tree
# https://www.interviewbit.com/problems/max-sum-path-in-binary-tree/
#
# Given a binary tree, find the maximum path sum.
#
# The path may start and end at any node in the tree.
#
# Example :
# Given the below binary tree,
#        1
#       / \
#      2   3
# Return 6.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:

    def maxPathSum(self, node):
        if node is None:
            return -float('inf')

        max_sum_left = self.maxPathSum(node.left)
        max_sum_right = self.maxPathSum(node.right)

        sum_left = node.left and node.left.max_sum or 0
        sum_right = node.right and node.right.max_sum or 0

        node.max_sum = max(sum_left + node.val, sum_right + node.val, node.val)

        return max(max_sum_left, max_sum_right, sum_left + sum_right + node.val, node.max_sum)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #