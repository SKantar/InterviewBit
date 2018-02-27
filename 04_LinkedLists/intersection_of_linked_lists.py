# Intersection of Linked Lists
# https://www.interviewbit.com/problems/intersection-of-linked-lists/
#
# Write a program to find the node at which the intersection of two singly linked lists begins.
#
# For example, the following two linked lists:
#
#
# A:          a1 → a2
#                    ↘
#                      c1 → c2 → c3
#                    ↗
# B:     b1 → b2 → b3
#
# begin to intersect at node c1.
#
#     Notes:
#
#         If the two linked lists have no intersection at all, return null.
#         The linked lists must retain their original structure after the function returns.
#         You may assume there are no cycles anywhere in the entire linked structure.
#         Your code should preferably run in O(n) time and use only O(1) memory.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def len(self, A):
        cnt = 0
        while A:
            cnt += 1
            A = A.next
        return cnt

    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def getIntersectionNode(self, A, B):
        na, nb = self.len(A), self.len(B)

        diff = abs(na - nb)

        if na > nb:
            while diff:
                A = A.next
                diff -= 1
        else:
            while diff:
                B = B.next
                diff -= 1

        while A and B:
            if A is B:
                return A
            A, B = A.next, B.next

        return None

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


