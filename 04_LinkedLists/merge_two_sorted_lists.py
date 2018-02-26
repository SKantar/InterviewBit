# Merge Two Sorted Lists
# https://www.interviewbit.com/problems/merge-two-sorted-lists/
#
# Merge two sorted linked lists and return it as a new list.
# The new list should be made by splicing together the nodes of the first two lists, and should also be sorted.
#
# For example, given following linked lists :
#
#   5 -> 8 -> 20
#   4 -> 11 -> 15
#
# The merged list should be :
#
# 4 -> 5 -> 8 -> 11 -> 15 -> 20
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution(object):
    def min(self, A, B):
        if A is None:
            return B
        elif B is None:
            return A
        else:
            return A.val < B.val and A or B

    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def mergeTwoLists(self, A, B):

        head = tmp = self.min(A, B)

        if head == None:
            return None

        A = A.next if tmp is A else A
        B = B.next if tmp is B else B

        while A or B:
            minn = self.min(A, B)
            tmp.next = minn
            tmp = minn

            A = A.next if tmp is A else A
            B = B.next if tmp is B else B
        return head

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #