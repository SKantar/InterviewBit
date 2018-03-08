class Solution(object):
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def twoSum(self, A, B):
        dp = dict()

        for i, a in enumerate(A):
            if a in dp:
                return dp[a] + 1, i + 1
            if B - a not in dp:
                dp[B - a] = i
        return []

if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))