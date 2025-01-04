# In Python, primitive data types are the most basic building blocks of data. 
# They represent single values and are not composed of other types. Here are the primitive data types in Python:
'''
1. Integer (int)
represent whole number like 10,-5, 0

2. Floating point number (float)
represent decimal number or real number like 23.3, -2.0, 0.0

3. Complex number (complex)
represent numbers with real and imaginary part like 2 + 3j

4. String (str)
Represents text data, enclosed in single or double quotes like "Python" ,'Code'

5. Boolean (bool)
Represents truth values: True or False.

6. NoneType (none)
Represents the absence of a value or a null value.
'''

# Check Data types using type() function

num = 20
print(type(num)) # int

x = 25.90
print(type(x)) # float

y = True
print(type(y)) # bool

name ="Aditya"
print(type(name)) # str

# Type convertion

a = 20

name = "Aditya"
print(name + " "+ str( a) ) # We have converted integer into string 

'''
f - string
To specify a string as an f-string, simply put an f in front of the string literal, 
and add curly brackets {} as placeholders for variables and other operations.

'''
new_name = "Rocky"
grade = "B"

print(f"{new_name} has score {grade} Grade")