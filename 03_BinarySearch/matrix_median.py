# Matrix Median
# https://www.interviewbit.com/problems/matrix-median/
#
# Given a N cross M matrix in which each row is sorted, find the overall median of the matrix. Assume N*M is odd.
#
# For example,
#
# Matrix=
# [1, 3, 5]
# [2, 6, 9]
# [3, 6, 9]
#
# A = [1, 2, 3, 3, 5, 6, 6, 9, 9]
#
# Median is 5. So, we return 5.
#
# Note: No extra memory is allowed.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:

    def calc_se(self, A, x):
        from bisect import bisect_left, bisect_right
        smaller = equal = 0

        for row in A:
            l, r = bisect_left(row, x), bisect_right(row, x)
            smaller += l
            equal += r - l

        return smaller, equal

    # @param A : list of list of integers
    # @return an integer
    def findMedian(self, A):
        n, m = len(A), len(A[0])
        k = (n * m + 1) // 2

        l, r = min([row[0] for row in A]), max([row[-1] for row in A])


        while l <= r:
            mid = (l + r) >> 1

            smaller, equal = self.calc_se(A, mid)

            if smaller < k and smaller + equal >= k:
                return mid
            elif smaller >= k:
                r = mid - 1
            else:
                l = mid + 1

        return -1

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    A = [
        [1, 3, 5],
        [2, 6, 9],
        [3, 6, 9],
    ]

    s = Solution()
    print(s.findMedian(A))