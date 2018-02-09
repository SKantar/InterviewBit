# Rearrange Array
# https://www.interviewbit.com/problems/rearrange-array/
#
# Rearrange a given array so that Arr[i] becomes Arr[Arr[i]] with O(1) extra space.
#
# Example:
#
# Input : [1, 0]
# Return : [0, 1]
#
#     Lets say N = size of the array. Then, following holds true :
#
#         All elements in the array are in the range [0, N-1]
#         N * N does not overflow for a signed integer
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : list of integers
    # Modify the array A which is passed by reference.
    # You do not need to return anything in this case.
    def arrange(self, A):
        n = len(A)
        for i in range(n):
            A[i] += (A[A[i]] % n) * n

        for i in range(n):
            A[i] //= n

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    A = [1, 0]
    s.arrange(A)
    print(A)