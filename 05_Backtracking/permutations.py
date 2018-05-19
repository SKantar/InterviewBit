# Permutations
# https://www.interviewbit.com/problems/permutations/
#
# Given a collection of numbers, return all possible permutations.
#
# Example:
#
# [1,2,3] will have the following permutations:
#
# [1,2,3]
# [1,3,2]
# [2,1,3]
# [2,3,1]
# [3,1,2]
# [3,2,1]
#
#     NOTE
#
#         No two entries in the permutation sequence should be the same.
#         For the purpose of this problem, assume that all the numbers in the collection are unique.
#
#     Warning : DO NOT USE LIBRARY FUNCTION FOR GENERATING PERMUTATIONS.
#     Example : next_permutations in C++ / itertools.permutations in python.
#     If you do, we will disqualify your submission retroactively and give you penalty points.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def _permute(self, xs, low=0):
        xs = xs[:]
        if low + 1 >= len(xs):
            yield xs
        else:
            for p in self._permute(xs, low + 1):
                yield p
            for i in range(low + 1, len(xs)):
                xs[low], xs[i] = xs[i], xs[low]
                for p in self._permute(xs, low + 1):
                    yield p
                xs[low], xs[i] = xs[i], xs[low]

    def permute(self, A):
        return list(self._permute(A))
