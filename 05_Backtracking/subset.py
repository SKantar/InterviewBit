# Subset
# https://www.interviewbit.com/problems/subset/
#
# Given a set of distinct integers, S, return all possible subsets.
#
#  Note:
# Elements in a subset must be in non-descending order.
# The solution set must not contain duplicate subsets.
# Also, the subsets should be sorted in ascending ( lexicographic ) order.
# The list is not necessarily sorted.
# Example :
#
# If S = [1,2,3], a solution is:
#
# [
#   [],
#   [1],
#   [1, 2],
#   [1, 2, 3],
#   [1, 3],
#   [2],
#   [2, 3],
#   [3],
# ]
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:

    def _subsets(self, A, tmp, left):
        ans = [tmp[:]]

        for i in range(left, len(A)):
            tmp.append(A[i])
            ans.extend(self._subsets(A, tmp, i + 1))
            tmp.pop()

        return ans

    # @param A : list of integers
    # @return a list of list of integers
    def subsets(self, A):
        A.sort()
        return self._subsets(A, [], 0)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.subsets([1, 2, 3]))