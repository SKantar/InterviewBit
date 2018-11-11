# ZigZag Level Order Traversal BT
# https://www.interviewbit.com/problems/zigzag-level-order-traversal-bt/
#
# Given a binary tree, return the zigzag level order traversal of its nodes’ values. (ie, from
# left to right, then right to left for the next level and alternate between).
#
#
# Example :
# Given binary tree
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return
#
# [
#          [3],
#          [20, 9],
#          [15, 7]
# ]
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def _zigzagLevelOrder(self, A, i, result):
        if not A:
            return

        if i == len(result):
            result.append([])

        self._zigzagLevelOrder(A.left, i + 1, result)
        result[i].append(A.val)
        self._zigzagLevelOrder(A.right, i + 1, result)

    # @param A : root node of tree
    # @return a list of list of integers
    def zigzagLevelOrder(self, A):
        result = []
        self._zigzagLevelOrder(A, 0, result)

        for i in range(1, len(result), 2):
            result[i] = list(reversed(result[i]))
        return result

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #