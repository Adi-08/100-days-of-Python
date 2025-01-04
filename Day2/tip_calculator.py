# Project 2 Tip calculator 

print("Welcome to the tip calculator!")

T_bill = float(input("what was the total bill? ")) #take totl bill as input from user 

tip = float(input("How much tip would you like to give? ")) # ask user how much tip would you like to give
final_bill = T_bill + tip # add that tip to the total bill

split = float(input("How many people to split the bill? ")) # split the final bill 

per_person = round(final_bill / split, 2) 


print("Each person should pay:", per_person)
