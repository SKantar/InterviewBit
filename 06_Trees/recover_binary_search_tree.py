# Recover Binary Search Tree
# https://www.interviewbit.com/problems/recover-binary-search-tree/
#
# Two elements of a binary search tree (BST) are swapped by mistake.
# Tell us the 2 values swapping which the tree will be restored.
#
#  Note:
# A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?
# Example :
#
#
# Input :
#          1
#         / \
#        2   3
#
# Output :
#        [1, 2]
#
# Explanation : Swapping 1 and 2 will change the BST to be
#          2
#         / \
#        1   3
# which is a valid BST
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def _inorder(self, root, pfs):
        if not root:
            return

        self._inorder(root.left, pfs)

        if not pfs[0]:
            pfs[0] = root
        else:
            if root.val < pfs[0].val:
                if not pfs[1]:
                    pfs[1] = pfs[0]
                pfs[2] = root
            pfs[0] = root

        self._inorder(root.right, pfs)

    # @param A : root node of tree
    # @return a list of integers
    def recoverTree(self, A):
        pfs = [None, None, None]
        self._inorder(A, pfs)
        return sorted([pfs[1].val, pfs[2].val])

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #