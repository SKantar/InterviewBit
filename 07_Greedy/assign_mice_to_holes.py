# Assign Mice to Holes
# https://www.interviewbit.com/problems/assign-mice-to-holes/
#
# There are N Mice and N holes are placed in a straight line.
# Each hole can accomodate only 1 mouse.
# A mouse can stay at his position, move one step right from x to x + 1, or move one step left
# from x to x − 1. Any of these moves consumes 1 minute.
# Assign mice to holes so that the time when the last mouse gets inside a hole is minimized.
#
# Example:
#
# positions of mice are:
# 4 -4 2
# positions of holes are:
# 4 0 5
#
# Assign mouse at position x=4 to hole at position x=4 : Time taken is 0 minutes
# Assign mouse at position x=-4 to hole at position x=0 : Time taken is 4 minutes
# Assign mouse at position x=2 to hole at position x=5 : Time taken is 3 minutes
# After 4 minutes all of the mice are in the holes.
#
# Since, there is no combination possible where the last mouse's time is less than 4,
# answer = 4.
# Input:
#
# A :  list of positions of mice
# B :  list of positions of holes
# Output:
#
# single integer value
#  NOTE: The final answer will fit in a 32 bit signed integer.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from math import fabs
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def mice(self, A, B):
        A.sort(), B.sort()
        return int(max([fabs(b - a) for a, b in zip(A, B)]))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
A = [ -49, 58, 72, -78, 9, 65, -42, -3 ]
B = [ 30, -13, -70, 58, -34, 79, -36, 27 ]

print(Solution().mice(A, B))