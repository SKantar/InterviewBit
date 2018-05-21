# Level Order
# https://www.interviewbit.com/problems/level-order/
#
# Given a binary tree, return the level order traversal of its nodes’ values. (ie, from left to right, level by level).
#
# Example :
# Given binary tree
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
# return its level order traversal as:
#
# [
#   [3],
#   [9,20],
#   [15,7]
# ]
#
# Also think about a version of the question where you are asked to do a level order traversal of
# the tree when depth of the tree is much greater than number of nodes on a level.
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
    def levelOrder(self, A):
        from collections import deque

        def insert(el, lvl, lst):
            if len(ans) == lvl:
                lst.append([])
            lst[lvl].append(el)


        queue, ans = deque(), list()

        if A:
            queue.append((0, A))

        while len(queue) > 0:
            lvl, node = queue.popleft()
            insert(node.val, lvl, ans)

            for child in [node.left, node.right]:
                if child:
                    queue.append((lvl + 1, child))

        return ans
