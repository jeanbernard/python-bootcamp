print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
split = int(input("How many people to split the bill? "))

tip_amount = round(total_bill * (percentage / 100), 2)
amt_per_person = (total_bill + tip_amount) / split
amt_per_person = "{:.2f}".format(amt_per_person)
print(f"Each person should pay: ${amt_per_person}")