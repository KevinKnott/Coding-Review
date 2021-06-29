# Best Time to Buy and Sell Stock: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Initial thought here is to take the lowest price if you  see a lower one else check if the dif between lowest and cur is greater than max
#  This was correct however I didn't write the brute force which is that You can do a double for loop checking each combo
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        profit, lowest = 0, prices[0]

        for i in range(len(prices)):
            if prices[i] <= lowest:
                lowest = prices[i]
            else:
                profit = max(profit, prices[i] - lowest)

        return profit

# Score Card
# Did I need hints? N
# Did you finish within 30 min? Y
# Was the solution optimal? Yes this is an o(n) time and o(1) space which is optimal over brute force o(n^2)
# Were there any bugs? None :D
#  5 5 5 5 = 5
