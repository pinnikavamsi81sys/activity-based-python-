material = float(input("Enter material cost: "))
labour = float(input("Enter labour charges: "))
wastage = float(input("Enter wastage cost: "))
machine = float(input("Enter machine cost: "))
selling = float(input("Enter total selling price: "))

total_cost = material + labour + wastage + machine
profit = selling - total_cost

print("\nTotal Manufacturing Cost:", total_cost)
print("Profit:", profit)

target = float(input("Enter target profit: "))

if profit >= target:
    print("Target Profit Achieved")
else:
    print("Target Profit Not Achieved")
