# Dungeon Princess
# https://www.interviewbit.com/problems/dungeon-princess/
#
# The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon.
# The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially
#  positioned in the top-left room and must fight his way through the dungeon to rescue the princess.
#
# The knight has an initial health point represented by a positive integer. If at any point his health
# point drops to 0 or below, he dies immediately.
#
# Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon
# entering these rooms; other rooms are either empty (0’s) or contain magic orbs that increase the
# knight’s health (positive integers).
#
# In order to reach the princess as quickly as possible, the knight decides to move only rightward
# or downward in each step.
#
# Write a function to determine the knight’s minimum initial health so that he is able to rescue
# the princess.
#
# For example, given the dungeon below, the initial health of the knight must be at least 7 if
# he follows the optimal path
#
# RIGHT-> RIGHT -> DOWN -> DOWN.
#
# Dungeon Princess: Example 1
#
#
#
# Input arguments to function:
# Your function will get an M*N matrix (2-D array) as input which represents the 2D grid as
# described in the question. Your function should return an integer corresponding to the
# knight’s minimum initial health required.
#
#
#
#  Note:
# The knight’s health has no upper bound.
# Any room can contain threats or power-ups, even the first room the knight enters and the
# bottom-right room where the princess is imprisoned.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def calculateMinimumHP(self, A):
        n, m = len(A), len(A[0]) if A else 0
        dp = [[1] * m for _ in range(n)]

        for j in range(m - 2, -1, -1):
            dp[-1][j] = max(1, dp[-1][j + 1] - A[-1][j + 1])

        for i in range(n - 2, -1, -1):
            dp[i][-1] = max(1, dp[i + 1][-1] - A[i + 1][-1])

        for i in range(n - 2, -1, -1):
            for j in range(m - 2, -1, -1):
                dp[i][j] = min(
                    max(1, dp[i + 1][j] - A[i + 1][j]),
                    max(1, dp[i][j + 1] - A[i][j + 1])
                )

        return max(1, dp[0][0] - A[0][0])

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.calculateMinimumHP([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]))


