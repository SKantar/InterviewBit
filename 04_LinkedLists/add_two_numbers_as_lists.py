# Add Two Numbers as Lists
# https://www.interviewbit.com/problems/add-two-numbers-as-lists/
#
# You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
#
#     342 + 465 = 807
#
# Make sure there are no trailing zeros in the output list
# So, 7 -> 0 -> 8 -> 0 is not a valid response even though the value is still 807.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

#Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def addTwoNumbers(self, A, B):
        extra = 0
        a, b = A, B
        head = tmp = None
        while a or b:
            if a and b:
                no = (a.val + b.val + extra) % 10
                extra = (a.val + b.val + extra) // 10
            elif a:
                no = (a.val + extra) % 10
                extra = (a.val + extra) // 10
            else:
                no = (b.val + extra) % 10
                extra = (b.val + extra) // 10

            node = ListNode(no)
            if tmp:
                tmp.next = node
            else:
                head = node
            tmp = node
            a = a.next if a else a
            b = b.next if b else b

        if extra:
            tmp.next = ListNode(extra)

        return head

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #