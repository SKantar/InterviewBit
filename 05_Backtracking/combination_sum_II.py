# Combination Sum II
# https://www.interviewbit.com/problems/combination-sum-ii/
#
# Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
#
# Each number in C may only be used once in the combination.
#
#     Note:
#
#         All numbers (including target) will be positive integers.
#         Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
#         The solution set must not contain duplicate combinations.
#
# Example :
#
# Given candidate set 10,1,2,7,6,1,5 and target 8,
#
# A solution set is:
#
# [1, 7]
# [1, 2, 5]
# [2, 6]
# [1, 1, 6]
#
#     Warning : DO NOT USE LIBRARY FUNCTION FOR GENERATING COMBINATIONS.
#     Example : itertools.combinations in python.
#     If you do, we will disqualify your submission retroactively and give you penalty points.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution(object):

    def _combinationSum(self, A, B, tmp, sum_tmp, left):

        if sum_tmp == B:
            return [tmp[:]]

        if left == len(A) or sum_tmp > B:
            return []

        ans = list()
        for i in range(left, len(A)):
            if i > left and A[i] == A[i - 1]:
                continue
            tmp.append(A[i])
            ans.extend(self._combinationSum(A, B, tmp, sum_tmp + A[i], i + 1))
            tmp.pop()

        return ans

    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def combinationSum(self, A, B):
        A.sort()
        return self._combinationSum(A, B, [], 0, 0)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum([10, 1, 2, 7, 6, 1, 5], 8))