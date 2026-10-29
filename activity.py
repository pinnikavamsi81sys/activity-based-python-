stock = {"Idly": 20, "Dosa": 15, "Juice": 10}
price = {"Idly": 20, "Dosa": 40, "Juice": 30}
sales = 0
for i in range(int(input("Number of orders: "))):
    item = input("Enter item: ").title()
    qty = int(input("Enter quantity: "))
    if item in stock and qty > 0 and qty <= stock[item]:
        bill = qty * price[item]; sales += bill; stock[item] -= qty
        print("Bill:", bill)
    else: print("Item unavailable or insufficient stock")
print("Total sales:", sales, "\nRemaining stock:", stock)

