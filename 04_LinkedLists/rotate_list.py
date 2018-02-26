# Rotate List
# https://www.interviewbit.com/problems/rotate-list/
#
# Given a list, rotate the list to the right by k places, where k is non-negative.
#
# For example:
#
# Given 1->2->3->4->5->NULL and k = 2,
# return 4->5->1->2->3->NULL.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    @staticmethod
    def _len( A):
        cnt, tmp = 0, A
        while tmp:
            cnt, tmp = cnt + 1, tmp.next
        return cnt

    @staticmethod
    def _find_new_head(A, B):
        new_head = A
        while B:
            new_head = new_head.next if new_head.next else A
            B = B - 1
        return new_head

    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def rotateRight(self, A, B):

        if A is None or not B:
            return A

        length = Solution._len(A)

        B = length - (B % length)

        new_head = Solution._find_new_head(A, B)

        if new_head is A:
            return A

        tmp = A
        while tmp.next and not tmp.next is new_head:
            tmp = tmp.next

        tmp.next = None

        tmp = new_head
        while tmp.next:
            tmp = tmp.next

        tmp.next = A

        return new_head

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #





