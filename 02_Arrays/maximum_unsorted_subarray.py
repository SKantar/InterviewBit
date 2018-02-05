# Maximum Unsorted Subarray
# https://www.interviewbit.com/problems/maximum-unsorted-subarray/
#
# You are given an array (zero indexed) of N non-negative integers, A0, A1 ,…, AN-1.
#
# Find the minimum sub array Al, Al+1 ,…, Ar so if we sort(in ascending order) that sub array, then the whole array
#
# should get sorted.
#
# If A is already sorted, output -1.
#
# Example :
#
# Input 1:
#
# A = [1, 3, 2, 4, 5]
#
# Return: [1, 2]
#
# Input 2:
#
# A = [1, 2, 3, 4, 5]
#
# Return: [-1]
#
# In the above example(Input 1), if we sort the subarray A1, A2, then whole array A should get sorted.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def subUnsort(self, A):
        tmp_min = idx_min = float('inf')
        tmp_max = idx_max = -float('inf')

        for i, elem in enumerate(reversed(A)):
            tmp_min = min(elem, tmp_min)
            if elem > tmp_min:
                idx_min = i

        for i, elem in enumerate(A):
            tmp_max = max(elem, tmp_max)
            if elem < tmp_max:
                idx_max = i

        idx_min = len(A) - 1 - idx_min

        return [-1] if idx_max == idx_min else [idx_min, idx_max]

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.subUnsort([1, 2, 3, 4]))
    print(s.subUnsort([2, 6, 4, 8, 10, 9]))
    print(s.subUnsort([2, 1]))
    print(s.subUnsort([1, 3, 2, 4, 5]))
