# Count Permutations of BST
# https://www.interviewbit.com/problems/count-permutations-of-bst/
#
# You are given two positive integers A and B. For all permutations of [1, 2, …, A], we create a BST. Count how many of these have height B.
#
# Notes:
#
# Values of a permutation are sequentially inserted into the BST by general rules i.e in increasing order of indices.
# Height of BST is maximum number of edges between root and a leaf.
# Return answer modulo 109 + 7.
# Expected time complexity is worst case O(N4).
# 1 ≤ N ≤ 50
# For example,
#
# A = 3, B = 1
#
# Two permutations [2, 1, 3] and [2, 3, 1] generate a BST of height 1.
# In both cases the BST formed is
#
#     2
#    / \
#   1   3
#
#
# Another example,
# A = 3, B = 2
# Return 4.
#
# Next question, can you do the problem in O(N3)?
#
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import math
from functools import wraps


def memo(f):
    cache = {}

    @wraps(f)
    def wrap(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    return wrap


class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def nCr(self, n, r):
        f = math.factorial
        return f(n) // (f(r) * f(n - r))

    def cntPermBST(self, n, height):
        return self.recurse(n, height)[0] % (10 ** 9 + 7)

    @memo
    def recurse(self, n, height):
        '''
            Tuple: (# correct height, # less than correct height)
        '''
        if n == 1 and height == 0:
            return [1, 0]
        elif n == 0 and height >= 0:
            return [0, 1]
        elif n == 0 or height == 0:
            return [0, 0]
        else:
            count = [0, 0]
            for i in range(1, n + 1):
                left = self.recurse(i - 1, height - 1)
                right = self.recurse(n - i, height - 1)
                num = left[0] * right[1] + right[0] * left[1] + left[0] * right[0]
                count[0] += self.nCr(n - 1, n - i) * num
                count[1] += self.nCr(n - 1, n - i) * left[1] * right[1]
            return count