# Reorder List
# https://www.interviewbit.com/problems/reorder-list/
#
# Given a singly linked list
#
#     L: L0 → L1 → … → Ln-1 → Ln,
#
# reorder it to:
#
#     L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …
#
# You must do this in-place without altering the nodes’ values.
#
# For example,
# Given {1,2,3,4}, reorder it to {1,4,2,3}.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def divide(self, A):
        slow = fast = A
        while slow and fast and fast.next:
            fast = fast.next.next
            if fast is None:
                slow.next, slow = None, slow.next
            else:
                slow = slow.next
        else:
            if fast and not fast.next:
                slow.next, slow = None, slow.next

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
    # @return the head node in the linked list
    def reorderList(self, A):

        mid = self.divide(A)
        left, right, i = A, self.reverseList(mid), 1

        while right:
            if i % 2:
                next_left = left.next
                left.next = right
                left = next_left
            else:
                right_next = right.next
                right.next = left
                right = right_next
            i ^= 1
        return A

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

