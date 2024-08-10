print("Welcome to the tip calculator!")

# Getting the input from the user
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

# Calculating the total bill with tip
bill_with_tip = bill * (1 + tip / 100)

# Calculating the amount each person should pay
bill_per_person = bill_with_tip / people
final_amount = round(bill_per_person, 2)

# Displaying the final amount each person should pay
print(f"Each one of you has to pay: ${final_amount}")
