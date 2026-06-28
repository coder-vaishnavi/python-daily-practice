# Import the math module and use it to:

# Find the square root of 144
# Calculate sin(90°) (hint: use math.radians())
# Install and import the requests module (if available) and use it to fetch data from "https://api.github.com".
import math
import requests

print(f"square of 144 is {math.sqrt(144)}")

print(f"Calculate sin(90°) is {math.sin(math.radians(90))}")


response = requests.get("https://api.github.com")

print(response.status_code)
print(response.json())