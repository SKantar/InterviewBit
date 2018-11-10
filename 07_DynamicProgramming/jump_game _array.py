# Jump Game Array
# https://www.interviewbit.com/problems/jump-game-array/
#
# Given an array of non-negative integers, you are initially positioned at the first index of the array.
#
# Each element in the array represents your maximum jump length at that position.
#
# Determine if you are able to reach the last index.
#
# For example:
# A = [2,3,1,1,4], return 1 ( true ).
#
# A = [3,2,1,0,4], return 0 ( false ).
#
# Return 0/1 for this problem
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : list of integers
    # @return an integer
    def canJump(self, A):
        maxReached = 0

        for i, a in enumerate(A):
            if i > maxReached:
                return 0
            maxReached = max(maxReached, i + a)

        return 1

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    print(Solution().canJump([2, 3, 1, 1, 4]))
    print(Solution().canJump([3, 2, 1, 0, 4]))

