# Points on the Straight Line
# https://www.interviewbit.com/problems/points-on-the-straight-line/
#
# Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
#
# Sample Input :
#
# (1, 1)
# (2, 2)
# Sample Output :
#
# 2
# You will be give 2 arrays X and Y. Each point is represented by (X[i], Y[i])
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    def _gcd(self, A, B):
        while B:
            A, B = B, A % B
        return A

    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def maxPoints(self, A, B):
        from collections import defaultdict

        if len(A) < 2:
            return len(A)

        maxP, dp = 0, defaultdict(lambda : 0)
        for i in range(len(A) - 1):
            currP = overlapP = verticalP = 0
            for j in range(i + 1, len(A)):
                if A[j] == A[i] and B[j] == B[i]:
                    overlapP += 1
                elif A[j] == A[i]:
                    verticalP += 1
                else:
                    diffX = A[j] - A[i]
                    diffY = B[j] - B[i]
                    g = self._gcd(diffX, diffY)

                    diffX, diffY = diffX // g, diffY // g

                    dp[(diffY, diffX)] += 1
                    currP = max(currP, dp[(diffY, diffX)])
                currP = max(currP, verticalP)
            maxP = max(maxP, currP + overlapP + 1)
            dp.clear()
        return maxP

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


