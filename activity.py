n = int(input("Enter number of vehicles: "))
d = float(input("Enter journey distance (km): "))
p = float(input("Enter fuel price per litre: "))
r = float(input("Enter reserve fuel (litres): "))
costs = {}
for i in range(n):
    name = input("Vehicle name: ")
    m = float(input("Mileage (km/litre): "))
    fuel = d / m + r
    costs[name] = fuel * p
for name, cost in costs.items(): print(name, "Cost:", cost)
print("Lowest cost:", min(costs, key=costs.get))
