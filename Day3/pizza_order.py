'''Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.

Based on a user's order, work out their final bill.

Small Pizza: 150
Medium Pizza: 200
Large Pizza: 250
Pepperoni for Small Pizza: +20
Pepperoni for Medium or Large Pizza: +30
Extra cheese for any size pizza: +15
'''


print("Welcome to Python Pizza Deliveries!!")

size =input("What size Pizza do you want? S, M, or L: ")
pepperoni = input("Do you want Pepperoni on your Pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese on your pizza? Y or N: ")

bill = 0

if size == "S":
    bill += 150

elif size == "M":
    bill += 200

elif size == "L":
    bill += 250

else:
    print("Enter valid right input")

if pepperoni == "Y":
    if size == "S" :
        bill +=20
    else:
        bill += 30

if extra_cheese == "Y":
        bill += 15

print(f"Your total bill is: {bill} !!")

    

