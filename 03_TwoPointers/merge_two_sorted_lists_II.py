# Merge Two Sorted Lists II
# https://www.interviewbit.com/problems/merge-two-sorted-lists-ii/
#
# Given two sorted integer arrays A and B, merge B into A as one sorted array.
#
#     Note: You have to modify the array A to contain the merge of A and B. Do not output anything in your code.
#     TIP: C users, please malloc the result into a new array and return the result.
#
# If the number of elements initialized in A and B are m and n respectively, the resulting
# size of array A after your code is executed should be m + n
#
# Example :
#
# Input :
#          A : [1 5 8]
#          B : [6 9]
#
# Modified A : [1 5 6 8 9]
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return A modified after the merge
    def merge(self, A, B):
        n, m = len(A), len(B)
        i = j = 0

        while i < n:
            if j < m and B[j] < A[i]:
                A.insert(i, B[j])
                j, n = j + 1, n + 1
            i += 1

        while j < m:
            A.append(B[j])
            j += 1

        return A

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":

    A = [1, 5, 8]
    B = [6, 9]

    s = Solution()
    s.merge(A, B)

    print(A)