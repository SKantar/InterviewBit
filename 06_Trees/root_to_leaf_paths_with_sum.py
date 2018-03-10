# Root to Leaf Paths With Sum
# https://www.interviewbit.com/problems/root-to-leaf-paths-with-sum/
#
# Given a binary tree and a sum, find all root-to-leaf paths where each path’s sum equals the given sum.
#
# For example:
# Given the below binary tree and sum = 22,
#
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
# return
#
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def _pathSum(self, node, tmp, tmp_sum, s):
        if node is None:
            return []

        tmp.append(node.val)
        tmp_sum += node.val

        if not node.left and not node.right:
            ans = [tmp[:]] if tmp_sum == s else []
        else:
            ans = self._pathSum(node.left, tmp, tmp_sum, s) + self._pathSum(node.right, tmp, tmp_sum, s)

        tmp.pop()
        tmp_sum -= node.val

        return ans

    # @param A : root node of tree
    # @param B : integer
    # @return a list of list of integers
    def pathSum(self, A, B):
        return self._pathSum(A, [], 0, B)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
