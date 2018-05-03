# Best Time to Buy and Sell Stocks III
# https://www.interviewbit.com/problems/best-time-to-buy-and-sell-stocks-iii/
#
# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete at most two transactions.
#
# Note:
# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
#
# Example :
#
# Input : [1 2 1 2]
# Output : 2
#
# Explanation :
#   Day 1 : Buy
#   Day 2 : Sell
#   Day 3 : Buy
#   Day 4 : Sell
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        buy1, sell1 = -float('INF'), 0
        buy2, sell2 = -float('INF'), 0

        for a in A:
            sell2 = max(sell2, a + buy2)
            buy2 = max(buy2, sell1 - a)
            sell1 = max(sell1, a + buy1)
            buy1 = max(buy1, -a)

        return sell2

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #