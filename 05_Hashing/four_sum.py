# 4 Sum
# https://www.interviewbit.com/problems/4-sum/
#
# Given an array S of n integers, are there elements a, b, c, and d in S such that
# a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
#
#  Note:
# Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
# The solution set must not contain duplicate quadruplets.
# Example :
# Given array S = {1 0 -1 0 -2 2}, and target = 0
# A solution set is:
#
#     (-2, -1, 1, 2)
#     (-2,  0, 0, 2)
#     (-1,  0, 0, 1)
# Also make sure that the solution set is lexicographically sorted.
# Solution[i] < Solution[j] iff Solution[i][0] < Solution[j][0] OR (Solution[i][0] == Solution[j][0]
# AND ... Solution[i][k] < Solution[j][k])
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def fourSum(self, A, B):
        from collections import defaultdict
        sums, ans = list(), set()

        for i in range(len(A) - 1):
            for j in range(i + 1, len(A)):
                sums.append((A[i] + A[j], i, j))

        dp = defaultdict(list)
        for s, *spair in sums:
            spair = set(spair)
            for pair in dp[B - s]:
                if not pair & spair:
                    ans.add(tuple(sorted([A[x] for x in spair | pair])))
            dp[s].append(spair)
        return sorted(list(ans))



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.fourSum([ 23, 20, 0, 21, 3, 38, 35, -6, 2, 5, 4, 21 ], 29))





