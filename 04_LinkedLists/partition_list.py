# Partition List
# https://www.interviewbit.com/problems/partition-list/
#
# Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
#
# You should preserve the original relative order of the nodes in each of the two partitions.
#
# For example,
# Given 1->4->3->2->5->2 and x = 3,
# return 1->2->2->4->3->5.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def partition(self, A, B):
        slw = sgt = lw = gt = None

        tmp = A
        while tmp:
            if tmp.val < B:
                if not lw:
                    slw = tmp
                else:
                    lw.next = tmp
                lw = tmp
            else:
                if not gt:
                    sgt = tmp
                else:
                    gt.next = tmp
                gt = tmp
            tmp = tmp.next

        gt.next = None
        if slw:
            lw.next = sgt
        return slw if slw else sgt

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #