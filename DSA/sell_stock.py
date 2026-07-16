# Problem
# You are given an array prices where prices[i] is the price of a stock on the ith day.
# You want to maximize your profit by choosing:
# One day to buy
# One future day to sell
# Return the maximum profit you can achieve.
# If no profit is possible, return 0.
prices = [7,1,5,3,6,4]

min_value = prices[0]   # Lowest price seen so far
profit = 0              # Maximum profit so far

for i in range(len(prices)):
    if prices[i] < min_value:
        min_value = prices[i]
    current_profit = prices[i] - min_value
    if current_profit > profit:
        profit = current_profit

print(profit)
    
