# Vertical Order traversal of Binary Tree
# https://www.interviewbit.com/problems/vertical-order-traversal-of-binary-tree/
#
# Given a binary tree, print a vertical order traversal of it.
#
# Example :
# Given binary tree:
#
#       6
#     /   \
#    3     7
#   / \     \
#  2   5     9
# returns
#
# [
#     [2],
#     [3],
#     [6 5],
#     [7],
#     [9]
# ]
#
#
# Note : If 2 Tree Nodes shares the same vertical level then the one with lesser depth will come first.
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
    # @return a list of list of integers
    def verticalOrderTraversal(self, A):
        from collections import deque, defaultdict
        queue, result = deque(), defaultdict(lambda: [])

        queue.append((0, A))

        while queue:
            lvl, node = queue.popleft()

            if not node:
                continue

            result[lvl].append(node.val)
            queue += (lvl - 1, node.left), (lvl + 1, node.right)

        return [result[key] for key in sorted(result.keys())]

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #