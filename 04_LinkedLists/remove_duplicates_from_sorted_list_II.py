# Remove Duplicates from Sorted List II
# https://www.interviewbit.com/problems/remove-duplicates-from-sorted-list-ii/
#
# Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
#
# For example,
# Given 1->2->3->3->4->4->5, return 1->2->5.
# Given 1->1->1->2->3, return 2->3.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):

        first = ListNode(0)
        first.next = A

        tmp = first

        while tmp.next and tmp.next.next:
            start = end = tmp.next
            while end.next and end.next.val == start.val:
                end = end.next

            if start != end:
                tmp.next = end.next
            else:
                tmp = start
        return first.next

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    head = ListNode(1)
    node1 = ListNode(1)
    node2 = ListNode(1)
    node3 = ListNode(2)
    node4 = ListNode(2)
    node5 = ListNode(3)

    head.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    s = Solution()
    head = s.deleteDuplicates(head)
