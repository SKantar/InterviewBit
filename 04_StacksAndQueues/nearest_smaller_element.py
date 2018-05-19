# Nearest Smaller Element
# https://www.interviewbit.com/problems/nearest-smaller-element/
#
# Given an array, find the nearest smaller element G[i] for every element A[i] in the array such
# that the element has an index smaller than i.
#
# More formally,
#
# G[i] for an element A[i] = an element A[j] such that
#     j is maximum possible AND
#     j < i AND
#     A[j] < A[i]
#
# Elements for which no smaller element exist, consider next smaller element as -1.
#
# Example:
#
# Input : A : [4, 5, 2, 10, 8]
# Return : [-1, 4, -1, 2, 2]
#
# Example 2:
#
# Input : A : [3, 2, 1]
# Return : [-1, -1, -1]
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def prevSmaller(self, A):
        tmp = -1
        stack = list()
        result = list()

        for e in A:
            if e > tmp:
                stack.append(e)
                result.append(tmp)
            else:
                while stack and stack[-1] >= e:
                    stack.pop()
                result.append(stack[-1] if stack else -1)
                stack.append(e)
            tmp = e
        return result
