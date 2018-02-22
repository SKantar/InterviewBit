# Max Continuous Series of 1s
# https://www.interviewbit.com/problems/max-continuous-series-of-1s/
#
# You are given with an array of 1s and 0s. And you are given with an integer M, which signifies number of flips allowed.
# Find the position of zeros which when flipped will produce maximum continuous series of 1s.
#
# For this problem, return the indices of maximum continuous series of 1s in order.
#
# Example:
#
# Input :
# Array = {1 1 0 1 1 0 0 1 1 1 }
# M = 1
#
# Output :
# [0, 1, 2, 3, 4]
#
# If there are multiple possible solutions, return the sequence which has the minimum start index.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def maxone(self, A, B):
        res = [(0, 0)] #sum of 0s and 1s at every point
        for elem in A:
            res.append((
                res[-1][0] + (elem == 0),
                res[-1][1] + (elem == 1)
            ))

        max = maxi = maxj = 0
        i, j = 0, 1
        while j < len(res):
            if res[j][0] - res[i][0] <= B:
                tmp = (res[j][1] - res[i][1]) + (res[j][0] - res[i][0])
                if tmp > max:
                    max = tmp
                    maxi = i
                    maxj = j
                j += 1
            else:
                i += 1

        return list(range(maxi, maxj))


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
if __name__ == "__main__":

    A = [1, 1, 0, 1, 1, 0, 0, 1, 1, 1]
    M = 1

    s = Solution()
    print(s.maxone(A, M))
