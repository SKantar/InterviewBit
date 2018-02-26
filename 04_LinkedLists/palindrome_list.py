# Palindrome List
# https://www.interviewbit.com/problems/palindrome-list/
#
# Given a singly linked list, determine if its a palindrome. Return 1 or 0 denoting if its a palindrome or not, respectively.
#
# Notes:
#
#     Expected solution is linear in time and constant in space.
#
# For example,
#
# List 1-->2-->1 is a palindrome.
# List 1-->2-->3 is not a palindrome.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mid(self, A):
        slow = fast = A
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverseList(self, A):
        tmp, prev = A, None
        while tmp:
            nxt = tmp.next
            tmp.next = prev
            prev = tmp
            tmp = nxt

        return prev


    # @param A : head node of linked list
    # @return an integer
    def lPalin(self, A):
        mid = self.mid(A)
        right = self.reverseList(mid)

        tmp_l, tmp_r = A, right

        while tmp_r:
            if tmp_l.val != tmp_r.val:
                return 0
            tmp_l, tmp_r = tmp_l.next, tmp_r.next

        return 1

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

