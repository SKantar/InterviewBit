# Sort List
# https://www.interviewbit.com/problems/sort-list/
#
# Sort a linked list in O(n log n) time using constant space complexity.
#
# Example :
#
# Input : 1 -> 5 -> 4 -> 3
#
# Returned list : 1 -> 3 -> 4 -> 5
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def divide(self, A):
        """ Divade in two lists """
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

    def min(self, A, B):
        """ Find Min node """
        if A is None:
            return B
        elif B is None:
            return A
        else:
            return A.val < B.val and A or B


    def mergeTwoLists(self, A, B):
        """ Merge two sorted list """
        head = tmp = self.min(A, B)

        if head == None:
            return None

        A = A.next if tmp is A else A
        B = B.next if tmp is B else B

        while A or B:
            minn = self.min(A, B)
            tmp.next = minn
            tmp = minn

            A = A.next if tmp is A else A
            B = B.next if tmp is B else B
        return head

    def merge_sort(self, A):
        """ Merge sort """
        B = self.divide(A)

        if B is None:
            return A

        first = self.merge_sort(A)
        second = self.merge_sort(B)

        return self.mergeTwoLists(first, second)

    # @param A : head node of linked list
    # @return the head node in the linked list
    def sortList(self, A):
        return self.merge_sort(A)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #