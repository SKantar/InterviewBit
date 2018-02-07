# Find Duplicate in Array
# https://www.interviewbit.com/problems/find-duplicate-in-array/
#
# Given a read only array of n + 1 integers between 1 and n, find one number that repeats in linear time using less
# than O(n) space and traversing the stream sequentially O(1) times.
#
# Sample Input:
#
# [3 4 1 4 1]
#
# Sample Output:
# 1
#
# If there are multiple possible answers ( like in the sample case above ), output any one.
#
# If there is no duplicate, output -1
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:

    # @param A : tuple of integers
    # @return an integer
    # def repeatedNumber(self, A):
    #     slow, fast = A[0], A[A[0]]
    #     try:
    #         while slow != fast:
    #             slow, fast = A[slow], A[A[fast]]
    #     except Exception:
    #         return -1
    #     fast = 0
    #     while slow != fast:
    #         slow, fast = A[slow], A[fast]
    #     return slow

    # @param A : tuple of integers
    # @return an integer
    # def repeatedNumber(self, A):
    #     hash = dict()
    #
    #     for elem in A:
    #         if elem in hash:
    #             return elem
    #         else:
    #             hash[elem] = True
    #     return -1

    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        A = list(A)
        for a in A:
            if A[abs(a) - 1] < 0:
                return abs(a)
            else:
                A[abs(a) - 1] *= -1
        return -1

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.repeatedNumber([1, 1, 2, 3]))