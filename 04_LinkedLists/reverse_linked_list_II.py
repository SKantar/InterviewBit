# Reverse Link List II
# https://www.interviewbit.com/problems/reverse-link-list-ii/
#
# Reverse a linked list from position m to n. Do it in-place and in one-pass.
#
# For example:
# Given 1->2->3->4->5->NULL, m = 2 and n = 4,
#
# return 1->4->3->2->5->NULL.
#
#     Note:
#     Given m, n satisfy the following condition:
#     1 ≤ m ≤ n ≤ length of list.
#
#     Note 2:
#     Usually the version often seen in the interviews is reversing the whole linked list which is obviously an easier version of this question.
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
    # @param C : integer
    # @return the head node in the linked list
    def reverseBetween(self, A, B, C):
        prev = other = start = None
        end = tmp = A
        i = 1

        while tmp:
            if i == B - 1:
                start = tmp

            if i == B:
                end = tmp

            if i >= B and i <= C:
                next = tmp.next
                tmp.next = prev
                prev = tmp
                tmp = next
            else:
                tmp = tmp.next

            if i == C:
                other = tmp

            i += 1

        end.next = other
        if start: start.next = prev
        return prev if B == 1 else A

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #