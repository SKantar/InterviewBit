# Maximum Absolute Difference
# https://www.interviewbit.com/problems/maximum-absolute-difference/
#
# You are given an array of N integers, A1, A2 ,…, AN. Return maximum value of f(i, j) for all 1 ≤ i, j ≤ N.
#
# f(i, j) is defined as |A[i] - A[j]| + |i - j|, where |x| denotes absolute value of x.
#
# For example,
#
# A=[1, 3, -1]
#
# f(1, 1) = f(2, 2) = f(3, 3) = 0
# f(1, 2) = f(2, 1) = |1 - 3| + |1 - 2| = 3
# f(1, 3) = f(3, 1) = |1 - (-1)| + |1 - 3| = 4
# f(2, 3) = f(3, 2) = |3 - (-1)| + |2 - 3| = 5
#
# So, we return 5.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, A):
        max1 = max2 = -float('inf')
        min1 = min2 = float('inf')
        for x, i in enumerate(A):
            max1, min1 = max(max1, i + x), min(min1, i + x)
            max2, min2 = max(max2, i - x), min(min2, i - x)
        return max(max1 - min1, max2 - min2)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    A = [1, 3, -1]
    s = Solution()
    print(s.maxArr(A))

