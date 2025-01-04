'''
The body mass index (BMI) is a measure used in medicine to see if someone is underweight or overweight. 
This is the formula used to calculate it:

bmi is equal to the person's weight divided by the person's height squared.
'''
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))

bmi =round(weight / (height**2), 2)
print(bmi)