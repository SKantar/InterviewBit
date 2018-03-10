# N max pair combinations
# https://www.interviewbit.com/problems/n-max-pair-combinations/
#
# Given two arrays A & B of size N each.
# Find the maximum n elements from the sum combinations (Ai + Bj) formed from elements in array A and B.
#
# For example if A = [1,2], B = [3,4], then possible pair sums can be 1+3 = 4 , 1+4=5 , 2+3=5 , 2+4=6
# and maximum 2 elements are 6, 5
#
# Example:
#
# N = 4
# a[]={1,4,2,3}
# b[]={2,5,1,6}
#
# Maximum 4 elements of combinations sum are
# 10   (4+6),
# 9    (3+6),
# 9    (4+5),
# 8    (2+6)
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class MaxHeap(tuple):
    def __lt__(self, other):
        return self[0] > other[0]


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        from heapq import heappush, heappop
        A.sort(reverse=True)
        B.sort(reverse=True)

        heap, finished = list(), set()

        heappush(heap, MaxHeap((A[0] + B[0], (0, 0))))
        finished.add((0, 0))

        ans = []

        for i in range(len(A)):
            s, idx = heappop(heap)
            ia, ib = idx
            ans.append(s)

            if ia + 1 < len(A) and (ia + 1, ib) not in finished:
                heappush(heap, MaxHeap((A[ia + 1] + B[ib], (ia + 1, ib))))
                finished.add((ia + 1, ib))

            if ib + 1 < len(B) and (ia, ib + 1) not in finished:
                heappush(heap, MaxHeap((A[ia] + B[ib + 1], (ia, ib + 1))))
                finished.add((ia, ib + 1))

        return ans

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.solve([1, 4, 2, 3], [2, 5, 1, 6]))