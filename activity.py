n = int(input("Enter number of households: "))
for i in range(n):
    units = int(input("Enter water units consumed: "))
    bill = 100 + units * 2 if units <= 100 else 100 + 200 + (units - 100) * 5
    if units > 200:
        bill += 50
    print("Water Bill:", bill)
    if units > 200:
        print("Excessive usage!")
    else:
        print("Normal usage")
