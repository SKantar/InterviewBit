# Remove Nth Node from List End
# https://www.interviewbit.com/problems/remove-nth-node-from-list-end/
#
# Given a linked list, remove the nth node from the end of list and return its head.
#
# For example,
# Given linked list: 1->2->3->4->5, and n = 2.
# After removing the second node from the end, the linked list becomes 1->2->3->5.
#
#     Note:
#
#         If n is greater than the size of the list, remove the first node of the list.
#
# Try doing it using constant additional space.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def len(self, A):
        cnt, tmp = 0, A
        while tmp:
            cnt, tmp = cnt + 1, tmp.next
        return cnt

    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def removeNthFromEnd(self, A, B):
        n = max(0, self.len(A) - B)

        fake = ListNode(0)
        fake.next = A
        tmp = fake

        while n:
            n, tmp = n - 1, tmp.next

        tmp.next = tmp.next.next

        return fake.next

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #