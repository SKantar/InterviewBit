# Next Permutation
# https://www.interviewbit.com/problems/next-permutation/
#
# Implement next permutation, which rearranges numbers into the lexicographically next greater
# permutation of numbers.
#
# If such arrangement is not possible, it must rearrange it as the lowest possible order
# (ie, sorted in ascending order).
#
# The replacement must be in-place, do not allocate extra memory.
#
# Here are some examples. Inputs are in the left-hand column and its corresponding outputs
# are in the right-hand column.
#
# Example:
#
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
# 20, 50, 113 → 20, 113, 50
#
# Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
#
# Warning : DO NOT USE LIBRARY FUNCTION FOR NEXT PERMUTATION. Use of Library functions will
# disqualify your submission retroactively and will give you penalty points.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:

    def _reverse(self, A, i, j):
        while i < j:
            A[i], A[j] = A[j], A[i]
            i, j = i + 1, j - 1

    # @param A : list of integers
    # @return the same list of integer after modification
    def nextPermutation(self, A):
        succ_pos, pivot = None, None

        for i in range(len(A) - 2, -1, -1):
            if A[i] < A[i + 1]:
                pivot = i
                break

        if pivot is not None:
            for i in range(len(A) - 1, pivot, -1):
                if A[pivot] < A[i]:
                    succ_pos = i
                    break
            A[pivot], A[succ_pos] = A[succ_pos], A[pivot]
            self._reverse(A, pivot + 1, len(A) - 1)
        else:
            A.reverse()
        return A

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    A = [1]
    s.nextPermutation(A)
    print(A)

