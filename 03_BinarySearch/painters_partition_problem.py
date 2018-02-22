# Painter's Partition Problem
# https://www.interviewbit.com/problems/painters-partition-problem/
#
# You have to paint N boards of length {A0, A1, A2, A3 … AN-1}. There are K painters available
# and you are also given how much time a painter takes to paint 1 unit of board. You have to get
# this job done as soon as possible under the constraints that any painter will only paint
# continuous sections of board.
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

    def paint(self, A, B):

        l, r = max(A), sum(A)

        while l < r:

            mid = (l + r) // 2
            n = self.num_of_painters(A, mid)

            if n > B:
                l = mid + 1
            else:
                r = mid

        return l % 10000003

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()

    A = [10, 20, 30, 40]
    print(s.paint(A, 2))