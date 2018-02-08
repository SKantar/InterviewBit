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
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:

    def _reverse(self, A, i, j):
        while i < j:
            A[i], A[j] = A[j], A[i]
            i, j = i + 1, j - 1

    def nextPermutation(self, nums):
        succ_pos, pivot = None, None

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                pivot = i
                break

        if pivot is not None:
            for i in range(len(nums) - 1, pivot, -1):
                if nums[pivot] < nums[i]:
                    succ_pos = i
                    break
            nums[pivot], nums[succ_pos] = nums[succ_pos], nums[pivot]
            self._reverse(nums, pivot + 1, len(nums) - 1)
        else:
            nums.reverse()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    A = [1]
    s.nextPermutation(A)
    print(A)

