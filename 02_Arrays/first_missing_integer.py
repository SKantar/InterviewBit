# Given an unsorted integer array, find the first missing positive integer.
#
# Example:
#
# Given [1,2,0] return 3,
#
# [3,4,-1,1] return 2,
#
# [-8, -7, -6] returns 1
#
# Your algorithm should run in O(n) time and uses constant space.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:

    def _segregate(self, A):
        j = 0
        for i in range(len(A)):
            if A[i] <= 0:
                A[i], A[j] = A[j], A[i]
                j += 1

        return j


    def _firstMissingPositive(self, A):
        for i in range(len(A)):
            if abs(A[i]) <= len(A):
                A[abs(A[i]) - 1] = - abs(A[abs(A[i]) - 1])

        for i in range(len(A)):
            if A[i] > 0:
                return i + 1

        return len(A) + 1 if len(A) > 0 else 1

    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        neg_cnt = self._segregate(A)
        return self._firstMissingPositive(A[neg_cnt:])

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    A = [0, 2, 1]
    print(s.firstMissingPositive(A))
