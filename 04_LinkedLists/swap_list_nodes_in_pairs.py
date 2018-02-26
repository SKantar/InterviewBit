# Swap List Nodes in pairs
# https://www.interviewbit.com/problems/swap-list-nodes-in-pairs/
#
# Given a linked list, swap every two adjacent nodes and return its head.
#
# For example,
# Given 1->2->3->4, you should return the list as 2->1->4->3.
#
# Your algorithm should use only constant space. You may not modify the values in the list,
# only nodes itself can be changed.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def _has_3(self, node):
        return node and node.next and node.next.next

    # @param A : head node of linked list
    # @return the head node in the linked list
    def swapPairs(self, A):
        fake_head = ListNode(0)
        fake_head.next = A

        tmp = fake_head


        while self._has_3(tmp):
            nxt = tmp.next
            tmp.next = tmp.next.next
            nxt.next = tmp.next.next
            tmp.next.next = nxt

            tmp = tmp.next.next

        return fake_head.next

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
