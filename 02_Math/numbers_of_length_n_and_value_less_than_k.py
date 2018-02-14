# Numbers of length N and value less than K
# https://www.interviewbit.com/problems/numbers-of-length-n-and-value-less-than-k/
#
# Given a set of digits (A) in sorted order, find how many numbers of length B are possible
# whose value is less than number C.
#
#     NOTE: All numbers can only have digits from the given set.
#
# Examples:
#
# 	Input:
# 	  3 0 1 5
# 	  1
# 	  2
# 	Output:
# 	  2 (0 and 1 are possible)
#
# 	Input:
# 	  4 0 1 2 5
# 	  2
# 	  21
# 	Output:
# 	  5 (10, 11, 12, 15, 20 are possible)
#
# Constraints:
#
#     1 <= B <= 9, 0 <= C <= 1e9 & 0 <= A[i] <= 9
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer

    def n_to_l(self, A):
        l = []
        while A:
            l.append(A % 10)
            A //= 10
        return list(reversed(l))

    def calc_less_then(self, A):
        less_than = [0] * 10
        lc = 0
        for i in range(10):
            less_than[i] = lc
            lc += int(i in A)

        return less_than

    def solve(self, A, B, C):
        from math import pow
        less_than = self.calc_less_then(A)
        list_c = self.n_to_l(C)

        lead = 0 in A
        if len(list_c) > B:
            if B == 1:
                return len(A)
            else:
                return int(pow(len(A), B)) - lead * int(pow(len(A), B - 1))
        elif len(list_c) < B or not len(A):
            return 0
        else:
            res = 0
            for e in list_c:
                B = B - 1
                if less_than[e] != 0:
                    res += (less_than[e] - lead)  * int(pow(len(A), B))

                if e not in A:
                    break

                lead = 0
            return res

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #