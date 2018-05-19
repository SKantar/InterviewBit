# Search for a Range
# https://www.interviewbit.com/problems/search-for-a-range/
#
# Given a sorted array of integers, find the starting and ending position of a given target value.
#
# Your algorithm’s runtime complexity must be in the order of O(log n).
#
# If the target is not found in the array, return [-1, -1].
#
# Example:
#
# Given [5, 7, 7, 8, 8, 10]
#
# and target value 8,
#
# return [3, 4].
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


class Solution:

    def bs_left(self, A, B):
        """ Find left most """
        low, high = 0, len(A) - 1

        while low <= high:
            mid = (low + high) // 2

            if A[mid] == B:
                if mid == 0 or A[mid - 1] != B:
                    return mid
                high = mid - 1
            elif B < A[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return -1


    def bs_right(self, A, B):
        """ Find right most """
        low, high = 0, len(A) - 1

        while low <= high:
            mid = (low + high) // 2

            if A[mid] == B:
                if mid + 1 >= len(A) or A[mid + 1] != B:
                    return mid
                low = mid + 1
            elif B < A[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return -1

    def searchRange(self, A, B):
        return [self.bs_left(A, B), self.bs_right(A, B)]

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.searchRange([1], 1))