# Best Time to Buy and Sell Stocks
# https://www.interviewbit.com/problems/best-time-to-buy-and-sell-stocks-i/
#
# Say you have an array for which the ith element is the price of a given stock on day i.
#
# If you were only permitted to complete at most one transaction (ie, buy one and sell one
# share of the stock), design an algorithm to find the maximum profit.
#
# Example :
#
# Input : [1 2]
# Return :  1
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        minBuy = float('inf')  # minimun seen so far
        maxProf = 0
        for a in A:
            maxProf = max(maxProf, a - minBuy)
            minBuy = min(minBuy, a)
        return maxProf

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #