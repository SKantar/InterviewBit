# Combination Sum
# https://www.interviewbit.com/problems/combination-sum/
#
# Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
#
# The same repeated number may be chosen from C unlimited number of times.
#
#     Note:
#
#         All numbers (including target) will be positive integers.
#         Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
#         The combinations themselves must be sorted in ascending order.
#         CombinationA > CombinationB iff (a1 > b1) OR (a1 = b1 AND a2 > b2) OR … (a1 = b1 AND a2 = b2 AND … ai = bi AND ai+1 > bi+1)
#         The solution set must not contain duplicate combinations.
#
# Example,
# Given candidate set 2,3,6,7 and target 7,
# A solution set is:
#
# [2, 2, 3]
# [7]
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
            tmp.append(A[i])
            ans.extend(self._combinationSum(A, B, tmp, sum_tmp + A[i], i))
            tmp.pop()

        return ans

    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def combinationSum(self, A, B):
        return self._combinationSum(list(set(A)), B, [], 0, 0)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum([2, 3, 6, 7], 7))