# Painter's Partition Problem
# https://www.interviewbit.com/problems/painters-partition-problem/
#
# You have to paint N boards of length {A0, A1, A2, A3 … AN-1}. There are K painters available
# and you are also given how much time a painter takes to paint 1 unit of board. You have to get
# this job done as soon as possible under the constraints that any painter will only paint
# contiguous sections of board.
#
#         2 painters cannot share a board to paint. That is to say, a board
#         cannot be painted partially by one painter, and partially by another.
#         A painter will only paint contiguous boards. Which means a
#         configuration where painter 1 paints board 1 and 3 but not 2 is
#         invalid.
#
# Return the ans % 10000003
#
# Input :
# K : Number of painters
# T : Time taken by painter to paint 1 unit of board
# L : A List which will represent length of each board
#
# Output:
#      return minimum time to paint all boards % 10000003
#
# Example
#
# Input :
#   K : 2
#   T : 5
#   L : [1, 10]
#
# Output : 50
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:

    def num_of_painters(self, A, B):
        n, s = 1, 0
        for elem in A:
            s += elem
            if s > B:
                n, s = n + 1, elem
        return n

    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def paint(self, A, B, C):
        C = list(map(lambda x: x * B, C))
        l, r = max(C), sum(C)

        while l < r:

            mid = (l + r) // 2
            n = self.num_of_painters(C, mid)

            if n > A:
                l = mid + 1
            else:
                r = mid

        return l % 10000003

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()

    A = 3
    B = 10
    C = [640, 435, 647, 352, 8, 90, 960, 329, 859]

    print(s.paint(A, B, C))