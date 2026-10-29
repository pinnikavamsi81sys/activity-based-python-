venue = float(input("Enter venue cost: "))
equipment = float(input("Enter equipment cost: "))
catering = float(input("Enter catering cost per person: "))
transport = float(input("Enter transport cost: "))
cert = float(input("Enter certificate cost per person: "))
sponsor = float(input("Enter sponsorship amount: "))
fee = float(input("Enter registration fee per person: "))
cost = venue + equipment + transport
n = int((cost - sponsor) / (fee - catering - cert)) + 1
print("Total cost for", n, "participants:", cost + n * (catering + cert), "\nBreak-even participants:", n, "\nSponsorship shortfall:", max(0, cost - sponsor))

