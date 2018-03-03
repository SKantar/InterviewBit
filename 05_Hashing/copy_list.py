# Copy List
# https://www.interviewbit.com/problems/copy-list/
#
# A linked list is given such that each node contains an additional random pointer which could
# point to any node in the list or NULL.
#
# Return a deep copy of the list.
#
# Example
#
# Given list
#
#    1 -> 2 -> 3
# with random pointers going from
#
#   1 -> 3
#   2 -> 1
#   3 -> 1
# You should return a deep copy of the list. The returned answer should not contain the same
# node as the original list, but a copy of them. The pointers in the returned list should not
# link to any node in the original input list.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, A):
        tmp, head = A, None

        while tmp:
            node = RandomListNode(tmp.label)
            node.next = tmp.next
            tmp.next = node
            tmp = tmp.next.next

        tmp = A
        while tmp:
            tmp.next.random = tmp.random.next if tmp.random else None
            tmp = tmp.next.next

        if A:
            tmp = A
            curr = head = A.next

            while curr.next:
                tmp.next = curr.next
                curr.next = curr.next.next
                curr = curr.next
                tmp = tmp.next
            tmp.next = None

        return head

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #