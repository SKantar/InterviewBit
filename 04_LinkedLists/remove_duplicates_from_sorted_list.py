# Remove Duplicates from Sorted List
# https://www.interviewbit.com/problems/remove-duplicates-from-sorted-list/
#
# Given a sorted linked list, delete all duplicates such that each element appear only once.
#
# For example,
# Given 1->1->2, return 1->2.
# Given 1->1->2->3->3, return 1->2->3.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        if A is None or A.next is None:
            return A

        prev, tmp = A, A.next

        while tmp:
            if prev.val == tmp.val:
                prev.next = tmp.next
                tmp = prev.next
            else:
                prev = tmp
                tmp = tmp.next
        return A

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #