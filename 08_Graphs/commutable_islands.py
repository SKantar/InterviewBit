# Commutable Islands
#
# There are n islands and there are many bridges connecting them. Each bridge has
# some cost attached to it.
#
# We need to find bridges with minimal cost such that all islands are connected.
#
# It is guaranteed that input data will contain at least one possible scenario in which
# all islands are connected with each other.
#
# Example :
# Input
#
#          Number of islands ( n ) = 4
#          1 2 1
#          2 3 4
#          1 4 3
#          4 3 2
#          1 3 10
#
# In this example, we have number of islands(n) = 4 . Each row then represents a bridge
# configuration. In each row first two numbers represent the islands number which are connected
# by this bridge and the third integer is the cost associated with this bridge.
#
# In the above example, we can select bridges 1(connecting islands 1 and 2 with cost 1),
# 3(connecting islands 1 and 4 with cost 3), 4(connecting islands 4 and 3 with cost 2). Thus we
# will have all islands connected with the minimum possible cost(1+3+2 = 6).
# In any other case, cost incurred will be more.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


class Solution:

    class Edges(list):
        def __lt__(self, other):
            for i in [2, 0, 1]:
                if self[i] == other[i]:
                    continue
                return self[i] < other[i]


    class DisjoinSet:
        def __init__(self, i):
            self.parent = i
            self.lvl = 0

        def __repr__(self):
            return "{}<{}>".format(self.parent, self.lvl)

    @staticmethod
    def findSet(x, S):
        if S[x].parent == x:
            return x
        S[x].parent = Solution.findSet(S[x].parent, S)
        return S[x].parent

    @staticmethod
    def unionSet(a, b, S):
        set_a = Solution.findSet(a, S)
        set_b = Solution.findSet(b, S)

        if S[set_a].lvl < S[set_b].lvl:
            S[set_a].parent = set_b
        elif S[set_a].lvl > S[set_b].lvl:
            S[set_b].parent = set_a
        else:
            S[set_b].parent = set_a
            S[set_a].lvl += 1

    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        B.sort(key=Solution.Edges)
        S = [None] + [Solution.DisjoinSet(i + 1) for i in range(A)]
        components, weigth = A - 1, 0

        for edge in B:
            if components == 0:
                break

            start = Solution.findSet(edge[0], S)
            end = Solution.findSet(edge[1], S)

            if start == end:
                continue

            Solution.unionSet(start, end, S)
            components -= 1
            weigth += edge[2]

        return weigth