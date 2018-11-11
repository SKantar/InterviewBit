# Least Common Ancestor
# https://www.interviewbit.com/problems/least-common-ancestor/
#
# Find the lowest common ancestor in an unordered binary tree given two values in the tree.
#
#  Lowest common ancestor : the lowest common ancestor (LCA) of two nodes v and w in a tree or
# directed acyclic graph (DAG) is the lowest (i.e. deepest) node that has both v and w as descendants.
# Example :
#
#
#         _______3______
#        /              \
#     ___5__          ___1__
#    /      \        /      \
#    6      _2_     0        8
#          /   \
#          7    4
# For the above tree, the LCA of nodes 5 and 1 is 3.
#
#  LCA = Lowest common ancestor
# Please note that LCA for nodes 5 and 4 is 5.
#
# You are given 2 values. Find the lowest common ancestor of the two nodes represented by val1 and val2
# No guarantee that val1 and val2 exist in the tree. If one value doesn’t exist in the tree then return -1.
# There are no duplicate values.
# You can use extra memory, helper functions, and can modify the node struct but, you can’t add a parent pointer.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    def _lca(self, A, B, C):
        if not A:
            return False, False, None

        leftHasB, leftHasC, leftHasAns = self._lca(A.left, B, C)
        rightHasB, rightHasC, rightHasAns = self._lca(A.right, B, C)

        isParentOfB = leftHasB or rightHasB or A.val == B
        isParentOfC = leftHasC or rightHasC or A.val == C

        ans = A if isParentOfB and isParentOfC else None
        ans = leftHasAns or rightHasAns or ans

        return isParentOfB, isParentOfC, ans

    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return an integer
    def lca(self, A, B, C):
        _, _, ans = self._lca(A, B, C)
        return ans.val if ans else -1

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #