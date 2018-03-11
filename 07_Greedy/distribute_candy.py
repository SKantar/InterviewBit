# Distribute Candy
# https://www.interviewbit.com/problems/distribute-candy/
#
# There are N children standing in a line. Each child is assigned a rating value.
#
#  You are giving candies to these children subjected to the following requirements:
# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# What is the minimum candies you must give?
#
# Sample Input :
#
# Ratings : [1 2]
# Sample Output :
#
# 3
# The candidate with 1 rating gets 1 candy and candidate with rating cannot get 1 candy as 1 is
# its neighbor. So rating 2 candidate gets 2 candies. In total, 2+1 = 3 candies need to be given out.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : list of integers
    # @return an integer
    def candy(self, A):
        candies = [1]

        for i in range(1, len(A)):
            candies.append(candies[-1] + 1 if A[i] > A[i - 1] else 1)

        result = candies[-1]
        for i in range(len(A) - 2, -1, -1):
            curr = candies[i + 1] + 1 if A[i] > A[i + 1] else 1
            result += max(curr, candies[i])
            candies[i] = curr

        return result

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.candy([1, 2]))


