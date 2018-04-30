# Kth Manhattan Distance Neighbourhood
# https://www.interviewbit.com/problems/kth-manhattan-distance-neighbourhood/
#
# Given a matrix M of size nxm and an integer K, find the maximum element in the K manhattan distance neighbourhood for all elements in nxm matrix.
# In other words, for every element M[i][j] find the maximum element M[p][q] such that abs(i-p)+abs(j-q) <= K.
#
# Note: Expected time complexity is O(N*N*K)
#
# Constraints:
#
# 1 <= n <= 300
# 1 <= m <= 300
# 1 <= K <= 300
# 0 <= M[i][j] <= 1000
# Example:
#
# Input:
# M  = [[1,2,4],[4,5,8]] , K = 2
#
# Output:
# ans = [[5,8,8],[8,8,8]]
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return a list of list of integers
    def solve(self, A, B):

        if not B:
            return []

        dp, n, m = [B], len(B), len(B[0])

        for k in range(1, A + 1):
            dp.append([])
            for i in range(n):
                dp[k].append([])
                for j in range(m):
                    dp[k][i].append(max(
                        dp[k - 1][i - 1][j] if i > 0 else 0,
                        dp[k - 1][i + 1][j] if i < n - 1 else 0,
                        dp[k - 1][i][j - 1] if j > 0 else 0,
                        dp[k - 1][i][j + 1] if j < m - 1 else 0,
                        dp[k - 1][i][j]
                    ))
        return dp[-1]

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == '__main__':
    A, B = 2, [[1, 2, 4], [4, 5, 8]]
    s = Solution()
    print(s.solve(A, B))