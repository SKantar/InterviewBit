# Intersecting Chords in a Circle
# https://www.interviewbit.com/problems/intersecting-chords-in-a-circle/
#
# Given a number N, return number of ways you can draw N chords in a circle with 2*N points such that no 2 chords intersect.
# Two ways are different if there exists a chord which is present in one way and not in other.
#
# For example,
#
# N=2
# If points are numbered 1 to 4 in clockwise direction, then different ways to draw chords are:
# {(1-2), (3-4)} and {(1-4), (2-3)}
#
# So, we return 2.
#
# Notes:
#
#     1 ≤ N ≤ 1000
#     Return answer modulo 109+7.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    import sys
    sys.setrecursionlimit(100000000)

    def _chordCntUtil(self, A, dp):
        if not A:
            return 1

        if dp[A] is None:
            ans = 0
            for i in range(A):
                ans = ans + self._chordCntUtil(i, dp) * self._chordCntUtil(A - 1 - i, dp)
            dp[A] = ans % 1000000007

        return dp[A]

    # @param A : integer
    # @return an integer
    def chordCnt(self, A):
        dp = [None] * (A + 1)
        return self._chordCntUtil(A, dp)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.chordCnt(17))