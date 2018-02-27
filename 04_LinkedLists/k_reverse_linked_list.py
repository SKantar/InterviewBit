# K reverse linked list
# https://www.interviewbit.com/problems/k-reverse-linked-list/
#
# Given a singly linked list and an integer K, reverses the nodes of the
#
# list K at a time and returns modified linked list.
#
#     NOTE : The length of the list is divisible by K
#
# Example :
#
# Given linked list 1 -> 2 -> 3 -> 4 -> 5 -> 6 and K=2,
#
# You should return 2 -> 1 -> 4 -> 3 -> 6 -> 5
#
# Try to solve the problem using constant extra space.
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
    def reverseList(self, A, B):

        head = last = None
        while A:
            start = A
            prev = A
            A = A.next
            for i in range(1, B):
                next = A.next
                A.next = prev
                prev = A
                A = next
            if last:
                last.next = prev
            last = start

            if not head:
                head = prev
        if last:
            last.next = None

        return head

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #