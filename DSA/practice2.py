# Given a dictionary of products and their prices, find the product with the highest price.
fruit_price = {
    "apple": 100,
    "banana": 40,
    "ananas": 50
}

highest_fruit = ""
highest_price = 0

for fruit, price in fruit_price.items():
    if price > highest_price:
        highest_price = price
        highest_fruit = fruit

print(f"Product with highest price: {highest_fruit}")
print(f"Highest price: {highest_price}")