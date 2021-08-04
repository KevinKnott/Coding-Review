# Best Time to Buy and Sell Stock: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# So in this problem we are checking to see if we can find two peaks one low and one high
# so basically we check at every number and see if it is a new lo if not we check
# if we could get a better max by selling the diff between the lo and the current num

import math


class Solution:
    def maxProfit(self, prices) -> int:
        lo = math.inf
        result = 0

        for price in prices:
            if price < lo:
                lo = price
            else:
                result = max(result, price - lo)

        return result

# The above works and runs in o(N) time and o(1) space
# while we can't improve its worst case complexity
# we can make it slightly more efficient to do this we simply need to
# make lo automatically the lowest number and then return result if we only
# have 1 element
    def maxProfit(self, prices) -> int:
        if len(prices) <= 1:
            return 0

        lo, result = prices[0], 0

        for i in range(1, len(prices)):
            if prices[i] < lo:
                lo = prices[i]
            else:
                result = max(result, prices[i] - lo)

        return result

# The above changes is a nominally faster result so it isn't worth it really


# Score Card
# Did I need hints? N
# Did you finish within 30 min? 6
# Was the solution optimal? Yee
# Were there any bugs? Hard no
# 5 5 5 5 = 5
