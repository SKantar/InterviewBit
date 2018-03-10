# Populate Next Right Pointers Tree
# https://www.interviewbit.com/problems/populate-next-right-pointers-tree/
#
# Given a binary tree
#
#     struct TreeLinkNode {
#       TreeLinkNode *left;
#       TreeLinkNode *right;
#       TreeLinkNode *next;
#     }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
#
# Initially, all next pointers are set to NULL.
#
#  Note:
# You may only use constant extra space.
# Example :
#
# Given the following binary tree,
#
#          1
#        /  \
#       2    3
#      / \  / \
#     4  5  6  7
# After calling your function, the tree should look like:
#
#          1 -> NULL
#        /  \
#       2 -> 3 -> NULL
#      / \  / \
#     4->5->6->7 -> NULL
#  Note 1: that using recursion has memory overhe
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Definition for a  binary tree node
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if not root:
            return

        curr, first_in_row, prev = root, None, None

        while curr:
            while curr:
                if curr.left:
                    if not prev:
                        first_in_row = curr.left
                    else:
                        prev.next = curr.left
                    prev = curr.left

                if curr.right:
                    if not prev:
                        first_in_row = curr.right
                    else:
                        prev.next = curr.right
                    prev = curr.right

                curr = curr.next

            curr = first_in_row
            prev = first_in_row = None

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #