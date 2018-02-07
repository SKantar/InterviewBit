# Max Non Negative SubArray
# https://www.interviewbit.com/problems/max-non-negative-subarray/
#
# Find out the maximum sub-array of non negative numbers from an array.
# The sub-array should be continuous. That is, a sub-array created by choosing
# the second and fourth element and skipping the third element is invalid.
#
# Maximum sub-array is defined in terms of the sum of the elements in the sub-array.
# Sub-array A is greater than sub-array B if sum(A) > sum(B).
#
# Example:
#
# A : [1, 2, 5, -7, 2, 3]
# The two sub-arrays are [1, 2, 5] [2, 3].
# The answer is [1, 2, 5] as its sum is larger than [2, 3]
#
# NOTE: If there is a tie, then compare with segment's length and return segment which has maximum length
# NOTE 2: If there is still a tie, then return the segment with minimum starting index
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        max_sum = max_left = max_right = -1
        tmp_sum = left = 0

        for i, elem in enumerate(A):
            if elem >= 0:
                tmp_sum += elem
            else:
                if tmp_sum > max_sum:
                    max_sum, max_left, max_right = tmp_sum, left, i
                tmp_sum = 0
                left = i + 1
        else:
            if tmp_sum > max_sum:
                max_left, max_right = left, len(A)

        return [] if max_left == max_right == -1 else A[max_left: max_right]

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.maxset([0, 0, -1, 0]))