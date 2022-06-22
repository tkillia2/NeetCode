class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, profit = 0, 0
        for sell in range(len(prices)):
            if prices[sell] < prices[buy]: # if you get to a lower buying point switch
                buy = sell
            # check the maximum profit the previous val or the new possible value
            profit = max(profit, prices[sell] - prices[buy])
        return profit

'''
What is happening?
writing the code this way will prevent buy from ever overcoming (being more to the right) of sell

if the selling point is ever lower than the buying point update that "selling" point to the new buying point
**this is okay because each max profit would have been computed prior to this and given the chance to be stored as the max

calling max(profit, profit equation) will allow for an easy check using built in python functions to see if the new max is greater without dealing with if/else statements
'''
