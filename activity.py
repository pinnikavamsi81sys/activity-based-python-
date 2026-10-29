appliances = ["Fan", "TV", "AC"]
total = 0
for a in appliances:
    readings = list(map(int, input(f"{a} units for 7 days: ").split()))
    print(a, "weekly total:", sum(readings))
    total += sum(readings)
    for day in range(7):
        if readings[day] > 10:
            print("Day", day + 1, "high consumption:", a)
print("Total weekly consumption:", total)
print("Limit: 10 units per appliance per day")