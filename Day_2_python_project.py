print("Welcome to the Tip Calculator")
# Total bill
bill = int(input("How much was the bill? $"))
# get percentage 
tip = int(input("How much tip would you like to leave ? 10, 12, 15? "))
# get the number of people to split bill
people = int(input("How many people to split the bill? "))
#Calculate the percentage
tip_percent = tip/100
# Get the tip total
total_tip = bill * tip_percent
# Add the tip to the total bill
total_bill_tip = bill + total_tip
#Get Split the total bill + tip between the number of people.
bill_per_person = total_bill_tip / people
# Get the final amount and out put it to the 2 decimal places
final_amount = round(bill_per_person,2)
final_amount = "{:.2f}".format(bill_per_person)
# Print the amount to the user.
print(f"Each person should pay: $ {final_amount}")