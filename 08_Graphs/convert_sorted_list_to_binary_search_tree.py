# Convert Sorted List to Binary Search Tree
# https://www.interviewbit.com/problems/convert-sorted-list-to-binary-search-tree/
#
#
# Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
#
#     A height balanced BST : a height-balanced binary tree is defined as a binary tree in which the depth of
# the two subtrees of every node never differ by more than 1.
#
# Example :
#
#
# Given A : 1 -> 2 -> 3
# A height balanced BST  :
#
#       2
#     /   \
#    1     3
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def count(self, head):
        cnt = 0
        while head:
            cnt += 1
            head = head.next
        return cnt

    def _sortedListToBst(self, head, n):
        if n <= 0:
            return None, head

        left, head = self._sortedListToBst(head, n // 2)

        root = TreeNode(head.val)
        root.left = left

        head = head.next

        root.right, head = self._sortedListToBst(head, n - n // 2 - 1)

        return root, head

    def sortedListToBST(self, head):
        n = self.count(head)
        return self._sortedListToBst(head, n)[0]
