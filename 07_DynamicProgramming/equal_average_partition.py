# Equal Average Partition
# https://www.interviewbit.com/problems/equal-average-partition/
#
# Given an array with non negative numbers, divide the array into two parts such that the
# average of both the parts is equal.
# Return both parts (If exist).
# If there is no solution. return an empty list.
#
# Example:
#
#
# Input:
# [1 7 15 29 11 9]
#
# Output:
# [9 15] [1 7 11 29]
#
# The average of part is (15+9)/2 = 12,
# average of second part elements is (1 + 7 + 11 + 29) / 4 = 12
#
#     NOTE 1: If a solution exists, you should return a list of exactly 2 lists of integers A
# and B which follow the following condition :
#
#         numElements in A <= numElements in B
#         If numElements in A = numElements in B, then A is lexicographically smaller than B
# ( https://en.wikipedia.org/wiki/Lexicographical_order )
#
#     NOTE 2: If multiple solutions exist, return the solution where length(A) is minimum.
# If there is still a tie, return the one where A is lexicographically smallest.
#
#     NOTE 3: Array will contain only non negative numbers.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from functools import wraps
import fractions

def memo(f):
    cache = {}

    @wraps(f)
    def wrap(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    return wrap


class Solution:
    # @param A : list of integers
    # @return a list of list of integers

    @memo
    def knapsack(self, i, num, tot):
        # Find num items in A that add up to tot
        if i > len(self.A) - 1 or num <= 0 or tot <= 0:
            return None
        elif num == 1 and self.A[i] == tot:
            return [self.A[i]]
        else:
            include = self.knapsack(i + 1, num - 1, tot - self.A[i])
            exclude = self.knapsack(i + 1, num, tot)

            if include:
                return [self.A[i]] + include
            elif exclude:
                return exclude

    def avgset(self, A):
        s, n = sum(A), len(A)
        gcd = fractions.gcd(s, n)
        num = n // gcd
        self.A = sorted(A)

        for i in range(num, n // 2 + 1, num):
            k = self.knapsack(0, i, s * i // n)
            if k is not None:
                temp = k[:]
                return [k, [i for i in self.A if not i in temp or temp.remove(i)]]
        return []

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
