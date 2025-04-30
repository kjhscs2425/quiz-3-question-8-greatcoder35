import json

# read `expenses.json`
with open("expenses.json", "r") as file:
    expenses = json.load(file)

# get and print total "price" for all expenses at the "pet store"
total_price = 0
for item in expenses.get("pet store", []):  
    total_price += item.get("price", 0)  

print(f"total expenses for {total_price}")