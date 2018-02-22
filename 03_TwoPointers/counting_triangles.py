# Counting Triangles
# https://www.interviewbit.com/problems/counting-triangles/
#
# You are given an array of N non-negative integers, A0, A1 ,…, AN-1.
# Considering each array element Ai as the edge length of some line segment, count the
# number of triangles which you can form using these array values.
#
# Notes:
#
#     You can use any value only once while forming each triangle. Order of choosing the edge
#     lengths doesn’t matter. Any triangle formed should have a positive area.
#
#     Return answer modulo 109 + 7.
#
# For example,
#
# A = [1, 1, 1, 2, 2]
#
# Return: 4
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : list of integers
    # @return an integer
    def nTriang(self, A):
        A = sorted(A)
        n, ans = len(A), 0
        for k in range(n - 2):
            j = k + 2
            for i in range(k + 1, n - 1):
                while j < n and A[k] + A[i] > A[j]:
                    j += 1

                ans += j - i - 1
        return ans % 1000000007

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    A = [1, 2, 3, 4, 5, 6]
    # A = [2, 2, 3, 4]
    # A = [1, 1, 1, 2, 2]
    print(s.nTriang(A))