# Subsets II
# https://www.interviewbit.com/problems/subsets-ii/
#
# Given a collection of integers that might contain duplicates, S, return all possible subsets.
#
#  Note:
# Elements in a subset must be in non-descending order.
# The solution set must not contain duplicate subsets.
# The subsets must be sorted lexicographically.
# Example :
# If S = [1,2,2], the solution is:
#
# [
# [],
# [1],
# [1,2],
# [1,2,2],
# [2],
# [2, 2]
# ]
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    def _subsetsWithDup(self, A, tmp, left):

        ans = [tmp[:]]

        for i in range(left, len(A)):

            if i > left and A[i] == A[i - 1]:
                continue

            tmp.append(A[i])
            ans.extend(self._subsetsWithDup(A, tmp, i + 1))
            tmp.pop()

        return ans

    # @param A : list of integers
    # @return a list of list of integers
    def subsetsWithDup(self, A):
        A.sort()
        return self._subsetsWithDup(A, [], 0)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.subsetsWithDup([1, 2, 2]))



