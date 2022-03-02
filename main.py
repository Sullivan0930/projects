

print("Welcome to the tip calculator.")
bill = input("What was the total bill? $" )
percentage = input("What percentage would you like to give? 10, 12, or 15? " )
people = input("How many people are splitting the bill? ")
tip = float(bill) * (int(percentage) / 100)
eachPay = (float(bill) + float(tip)) / int(people) 
total = float(round(eachPay,2))
print(f"Each person should pay:${total}")
