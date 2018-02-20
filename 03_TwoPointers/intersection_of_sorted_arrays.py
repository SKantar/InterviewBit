# Intersection Of Sorted Arrays
# https://www.interviewbit.com/problems/intersection-of-sorted-arrays/
#
# Find the intersection of two sorted arrays.
# OR in other words,
# Given 2 sorted arrays, find all the elements which occur in both the arrays.
#
# Example :
#
# Input :
#     A : [1 2 3 3 4 5 6]
#     B : [3 3 5]
#
# Output : [3 3 5]
#
# Input :
#     A : [1 2 3 3 4 5 6]
#     B : [3 5]
#
# Output : [3 5]
#
#     NOTE : For the purpose of this problem ( as also conveyed by the sample case ), assume that elements that
#            appear more than once in both arrays should be included multiple times in the final output.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers
    def intersect(self, A, B):
        i = j = 0
        res = []
        while i < len(A) and j < len(B):
            if A[i] == B[j]:
                res.append(A[i])
                i += 1
                j += 1
            elif A[i] < B[j]:
                i += 1
            else:
                j += 1
        return res

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
if __name__ == "__main__":
    A = [1, 2, 3, 3, 4, 5, 6]
    B = [3, 5]

    s = Solution()
    print(s.intersect(A, B))