# Sorted Insert Position
# https://www.interviewbit.com/problems/sorted-insert-position/
#
# Given a sorted array and a target value, return the index if the target is found. If not,
# return the index where it would be if it were inserted in order.
#
# You may assume no duplicates in the array.
#
# Here are few examples.
#
# [1,3,5,6], 5 → 2
# [1,3,5,6], 2 → 1
# [1,3,5,6], 7 → 4
# [1,3,5,6], 0 → 0
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:

    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def searchInsert(self, A, B):
        start, end = 0, len(A) - 1
        while start <= end:

            mid = (start + end) // 2

            if B == A[mid]:
                if mid + 1 >= len(A) or A[mid + 1] != B:
                    return mid
                start = mid + 1
            elif B < A[mid]:
                end = mid - 1
            else:
                start = mid + 1

        return start

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.searchInsert([1,3,5,6], 5))
    print(s.searchInsert([1,3,5,6], 2))
    print(s.searchInsert([1,3,5,6], 7))
    print(s.searchInsert([1,3,5,6], 0))
    print(s.searchInsert([1], 1))