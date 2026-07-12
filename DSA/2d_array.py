# You are given a 2D array accounts.
# Each row represents a customer.
# Each column represents the money that customer has in a bank.
# Return the maximum wealth among all customers.

accounts = [[1,2,4],
            [3,2,1]]
max_wel = 0
for i in range(len(accounts)):
    amount = 0
    for j in range(len(accounts[i])):
        amount = amount + accounts[i][j]
   
    if max_wel < amount:
        max_wel = amount
print(f"Richest Customer Wealth {max_wel}")
        
    
    
