# Palindrome Partitioning II
# https://www.interviewbit.com/problems/palindrome-partitioning-ii/
#
# Given a string s, partition s such that every substring of the partition is a palindrome.
#
# Return the minimum cuts needed for a palindrome partitioning of s.
#
# Example :
# Given
# s = "aab",
# Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    def minCut(self, A):
        dp_p, dp_c = [[False] * len(A) for _ in range(len(A))], list()

        # Length 1
        for i in range(len(A)):
            dp_p[i][i] = True

        # Length 2
        for i in range(len(A) - 1):
            dp_p[i][i + 1] = A[i] == A[i + 1]

        # Length > 2
        for l in range(3, len(A) + 1):
            for i in range(0, len(A) - l + 1):
                j = i + l - 1
                dp_p[i][j] = A[i] == A[j] and dp_p[i + 1][j - 1]



        for i in range(len(A)):
            if dp_p[0][i]:
                dp_c.append(0)
            else:
                tmp = float('INF')
                for j in range(i):
                    if dp_p[j + 1][i] and dp_c[j]  < tmp:
                        tmp = dp_c[j]
                dp_c.append(tmp + 1)

        return dp_c[len(A) - 1]


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.minCut("aab"))
