# Best Time to Buy and Sell Stock: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Simply loop through numbers and check all numbers after for greatest difference


class init():
    # This is not optimal as it is an O(n^2) solution
    def maxProfit1(self, prices):
        profit = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                profit = max(profit, prices[j] - prices[i])

        return profit

    # Can we do this in one pass?
    # This works as I expected and is in o(n) time and o(1) space
    def maxProfit2(self, prices):
        # keep lowest we have seen so far
        # Check to see if your low is a new low
        # if it is reset max
        # return highest profit?

        maxProfit = 0
        low, high = 0, 0

        for i in range(len(prices)):
            if prices[i] < prices[low]:
                maxProfit = max(maxProfit, prices[high] - prices[low])
                low = i
                high = i
            else:
                if prices[high] < prices[i]:
                    high = i
                    maxProfit = max(maxProfit, prices[high] - prices[low])

        return maxProfit

    def maxProfitOptimal(self, prices):
        # This could be improved by taking the peaks only so if we have a new low do something
        # and if we have a new high we need to do something
        maxProfit = 0
        low = float('inf')

        for i in range(len(prices)):
            if prices[i] < low:
                low = prices[i]
            elif (prices[i] - low > maxProfit):
                maxProfit = prices[i] - low

        return maxProfit


# Score Card
# Did I need hints? For a slighlty more optimal also O(n) time yes but not really
# Did you finish within 30 min? Y
# Was the solution optimal? Y
# Were there any bugs? N
#  4 5 5 5 = 4.75
