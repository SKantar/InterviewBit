# Best Time to Buy and Sell Stocks II
# https://www.interviewbit.com/problems/best-time-to-buy-and-sell-stocks-ii/
#
# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete as many transactions as you
# like (ie, buy one and sell one share of the stock multiple times). However, you may not engage
# in multiple transactions at the same time (ie, you must sell the stock before you buy again).
#
# Example :
#
# Input : [1 2 3]
# Return : 2
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    def maxProfit(self, A):
        sol = 0
        for i in range(1, len(A)):
            sol += max(0, A[i] - A[i - 1])
        return sol

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #