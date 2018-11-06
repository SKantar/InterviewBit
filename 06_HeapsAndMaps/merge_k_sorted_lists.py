# Merge K Sorted Lists
# https://www.interviewbit.com/problems/merge-k-sorted-lists/
#
# Merge k sorted linked lists and return it as one sorted list.
#
# Example :
#
# 1 -> 10 -> 20
# 4 -> 11 -> 13
# 3 -> 8 -> 9
# will result in
#
# 1 -> 3 -> 4 -> 8 -> 9 -> 10 -> 11 -> 13 -> 20
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : list of linked list
    # @return the head node in the linked list
    def mergeKLists(self, A):
        from heapq import heappop, heappush

        heap = list()
        head = tail = None

        for i in range(len(A)):
            if A[i]:
                heappush(heap, (A[i].val, i))

        while heap:
            a, row = heappop(heap)
            node = ListNode(a)

            if not head:
                head  = tail = node
            else:
                tail.next = node
                tail = node

            A[row] = A[row].next
            if A[row]:
                heappush(heap, (A[row].val, row))

        return head

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #




