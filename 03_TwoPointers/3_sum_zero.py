# 3 Sum Zero
# https://www.interviewbit.com/problems/3-sum-zero/
#
# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
# Find all unique triplets in the array which gives the sum of zero.
#
# Note:
#
#     Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
#     The solution set must not contain duplicate triplets.
#
#     For example, given array S = {-1 0 1 2 -1 -4},
#
#     A solution set is:
#     (-1, 0, 1)
#     (-1, -1, 2)
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# This gives TLE but it's also O^2 Solution
#
# class Solution:
#
#     def _inc(self, A, i, j):
#         i += 1
#         while i < j and A[i] == A[i - 1]:
#             i += 1
#         return i
#
#     def _dec(self, A, i, j):
#         i -= 1
#         while i > j and A[i] == A[i + 1]:
#             i -= 1
#         return i
#
#     def threeSum(self, A):
#         A.sort()
#
#         ans, a = list(), None
#         k, n = 0, len(A)
#         while k < n - 2:
#             a = A[k]
#             i, j = k + 1, n - 1
#
#             while i < j:
#                 summ = a + A[i] + A[j]
#                 if summ == 0:
#                     ans.append([a, A[i], A[j]])
#                     i, j = self._inc(A, i, j), self._dec(A, j, i)
#                 elif summ < 0:
#                     i = self._inc(A, i, j)
#                 else:
#                     j = self._dec(A, j, i)
#
#             k = self._inc(A, k, n - 2)
#
#         return ans
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Another Approach, Same idea
class Solution:

    def threeSum(self, A):
        A.sort()
        ans, a = set(), None
        k, n = 0, len(A)
        for k in range(n - 2):
            a = A[k]
            i, j = k + 1, n - 1

            while i < j:
                summ = a + A[i] + A[j]
                if summ == 0:
                    ans.add((a, A[i], A[j]))
                    i, j = i + 1, j - 1
                elif summ < 0:
                    i += 1
                else:
                    j -= 1
        return list(ans)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    import time
    s = Solution()
    A = [0, 0, 0]
    print(len(A))
    print(s.threeSum(A))
