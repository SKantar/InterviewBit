# Distinct Numbers in Window
# https://www.interviewbit.com/problems/distinct-numbers-in-window/
#
# You are given an array of N integers, A1, A2 ,…, AN and an integer K. Return the of count of
# distinct numbers in all windows of size K.
#
# Formally, return an array of size N-K+1 where i’th element in this array contains number of
# distinct elements in sequence Ai, Ai+1 ,…, Ai+k-1.
#
# Note:
#
# If K > N, return empty array.
# For example,
#
# A=[1, 2, 1, 3, 4, 3] and K = 3
#
# All windows of size K are
#
# [1, 2, 1]
# [2, 1, 3]
# [1, 3, 4]
# [3, 4, 3]
#
# So, we return an array [2, 3, 3, 2].
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def dNums(self, A, B):
        from collections import defaultdict

        if len(A) < B:
            return []

        store = defaultdict(lambda : 0)
        result, dist = [], 0

        for i in range(B):
            if store[A[i]] == 0:
                dist += 1
            store[A[i]] += 1

        result.append(dist)
        for i in range(B, len(A)):
            store[A[i - B]] -= 1
            if store[A[i - B]] == 0:
                dist -= 1

            if store[A[i]] == 0:
                dist += 1
            store[A[i]] += 1

            result.append(dist)

        return result


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(Solution().dNums([1, 2, 1, 3, 4, 3], 3))




