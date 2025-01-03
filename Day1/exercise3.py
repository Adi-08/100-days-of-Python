"""
We have 2 variables glass1 and glass2. 
glass1 contains milk and glass2 contains juice. 
Write  a code to switch the contents of the variables. You are not allowed to type the words "milk" or "juice". 
You are only allowed to use variables to solve this exercise.
"""
# Given is:
glass1 = "milk"
glass2 = "juice"

# We can solve this exercise many different way 
# 1. By using 3rd variable 

# temp = glass1
# glass1 = glass2
# glass2 = temp

# 2. Without using 3rd variable
glass1, glass2 = glass2, glass1
print(glass1)