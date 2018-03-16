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

        if not A:
            return 0

        prev_prev = prev = 1

        if A > 1:
            prev = 2

        for i in range(2, A):
            prev_prev, prev = prev, prev + prev_prev

        return prev

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.climbStairs(3))

