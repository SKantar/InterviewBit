# Largest Continuous Sequence Zero Sum
# https://www.interviewbit.com/problems/largest-continuous-sequence-zero-sum/
#
# Find the largest continuous sequence in a array which sums to zero.
#
# Example:
#
#
# Input:  {1 ,2 ,-2 ,4 ,-4}
# Output: {2 ,-2 ,4 ,-4}
#
#  NOTE : If there are multiple correct answers, return the sequence which occurs first in the array.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    def lszero(self, A):
        dp, currS = dict(), 0
        maxI = maxL = 0


        for i, a in enumerate(A):
            currS += a

            if currS is 0:
                maxL, maxI = i + 1, 0

            if currS in dp:
                if i - dp[currS] > maxL:
                    maxL, maxI = i - dp[currS], dp[currS] + 1
            else:
                dp[currS] = i

        return A[maxI: maxI + maxL]

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == '__main__':
    s = Solution()
    print(s.lszero([15, -2, 2, -8, 1, 7, 10, 13]))
    print(s.lszero([1, 2, 0, 3]))
    print(s.lszero([1, 2, -2, 4, -4]))
