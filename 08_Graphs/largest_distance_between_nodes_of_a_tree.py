# Largest Distance between nodes of a Tree
# https://www.interviewbit.com/problems/largest-distance-between-nodes-of-a-tree/
#
# Find largest distance
#
# Given an arbitrary unweighted rooted tree which consists of N (2 <= N <= 40000) nodes. The goal of the problem
# is to find largest distance between two nodes in a tree. Distance between two nodes is a number of edges on a
# path between the nodes (there will be a unique path between any pair of nodes since it is a tree). The nodes
# will be numbered 0 through N - 1.
#
# The tree is given as an array P, there is an edge between nodes P[i] and i (0 <= i < N). Exactly one of the
# i’s will have P[i] equal to -1, it will be root node.
#
#     Example:
#     If given P is [-1, 0, 0, 0, 3], then node 0 is the root and the whole tree looks like this:
#
#           0
#        /  |  \
#       1   2   3
#                \
#                 4
#
#     One of the longest path is 1 -> 0 -> 3 -> 4 and its length is 3, thus the answer is 3. Note that
# there are other paths with maximal distance.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import sys
sys.setrecursionlimit(100000)

class Solution:

    @staticmethod
    def _max_2nd_max(max1, max2, new_item):
        if new_item > max1:
            return new_item, max1
        elif new_item > max2:
            return max1, new_item
        else:
            return max1, max2

    def _bfs(self, idx, conn):

        if idx not in conn:
            return 0, 1

        max1 = max2 = maxW = 0
        for child in conn[idx]:
            w, h = self._bfs(child, conn)
            max1, max2 = Solution._max_2nd_max(max1, max2, h)
            maxW = max(maxW, w)

        return (max(maxW, max1 + max2), max1 + 1) if idx != -1 else (maxW, max1 + 1)


    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        from collections import defaultdict
        conn = defaultdict(list)
        for i, e in enumerate(A):
            conn[e].append(i)
        return self._bfs(-1, conn)[0] if len(A) > 1 else 0

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #