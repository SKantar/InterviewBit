# Remove Duplicates from Sorted Array II
# https://www.interviewbit.com/problems/remove-duplicates-from-sorted-array-ii/
#
# Remove Duplicates from Sorted Array
#
# Given a sorted array, remove the duplicates in place such that each element can appear atmost twice and return the new length.
#
# Do not allocate extra space for another array, you must do this in place with constant memory.
#
# Note that even though we want you to return the new length, make sure to change the original array as well in place
#
# For example,
# Given input array A = [1,1,1,2],
#
# Your function should return length = 3, and A is now [1,1,2].
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        i = 0
        while i < len(A) - 1:
            j = i + 2
            while j < len(A) and A[i] == A[j] :
                j += 1
            A[i + 2:j] = []
            i += 1
        return len(A)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
if __name__ == "__main__":
    s = Solution()
    A = [1, 1, 1, 2]
    s.removeDuplicates(A)
    print(A)

