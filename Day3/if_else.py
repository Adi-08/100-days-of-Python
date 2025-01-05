print("Welcome to the Rollercoaster")

height = int(input("Enter your height in cm: "))
bill =0
if height >= 120:
    print("You can ride the roller coaster!!")

    age = int(input("Enter your age: "))
    if age <= 12:
        bill= 200
        print("Child pay 200 rupees!!")
    elif age < 18:
        bill=250
        print("Youth pay 250 rupees!!")

    elif age >=45 and age <=55:
        bill = 0
        print("You have pay 0 rupees because you are from mid life crisis")
    else:
        bill = 300
        print("Adult pay 300 rupees!!")

    
    photo = input("You want photos? Y or N: ")
    if photo == "Y":
        print("Pay extra 30 rupees")
        bill += 30
        print(f"Your final bill is {bill}")
        

else:
    print("Sorry, your height does not match our requirement")