# Stairs
# https://www.interviewbit.com/problems/stairs/
#
# You are climbing a stair case. It takes n steps to reach to the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
# Example :
#
# Input : 3
# Return : 3
#
# Steps : [1 1 1], [1 2], [2 1]
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : integer
    # @return an integer
    def climbStairs(self, A):
        result = [0] * A

        if A < 2:
            return A

        result[0], result[1] = 1, 2

        for i in range(2, A):
            result[i] = result[i - 1] + result[i - 2]

        return result[-1]

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #