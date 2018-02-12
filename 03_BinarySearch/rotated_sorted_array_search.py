# Rotated Sorted Array Search
# https://www.interviewbit.com/problems/rotated-sorted-array-search/
#
# Suppose a sorted array is rotated at some pivot unknown to you beforehand.
#
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2 ).
#
# You are given a target value to search. If found in the array, return its index,
# otherwise return -1.
#
# You may assume no duplicate exists in the array.
#
# Input : [4 5 6 7 0 1 2] and target = 4
# Output : 0
#
#         NOTE : Think about the case when there are duplicates. Does your current solution work?
#                How does the time complexity change?*
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    def binarySearch(self, A, B):
        low, high = 0, len(A) - 1

        while low <= high:
            mid = (low + high) // 2
            if A[mid] == B:
                return mid
            elif B < A[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return -1

    def countRotations(self, A):
        low, high = 0, len(A) - 1

        while low <= high:
            if A[low] <= A[high]:
                return low

            mid = low + (high - low) // 2
            next = (mid + 1) % len(A)
            prev = (mid + len(A) - 1) % len(A)

            if A[prev] > A[mid] and A[next] > A[mid]:
                return mid
            elif A[mid] <= A[high]:
                high = mid - 1
            else:
                low = mid + 1

    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):
        rot = self.countRotations(A)

        low, high = 0, rot - 1
        res = self.binarySearch(A[low:high], B)

        if res == -1:
            low, high = rot, len(A) - 1
            res = self.binarySearch(A[low:high], B)
            if res == -1:
                return -1
            return rot + self.binarySearch(A[low:high], B)

        return res

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.search([4, 5, 6, 7, 0, 1, 2], 4))
