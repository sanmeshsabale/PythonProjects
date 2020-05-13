

print("Welcome to the Multiplication and Exponential table")
# Multiplication table (from 1 to 10) in Python

num = int(input("Which Number u want: "))

# To take input from the user
# num = int(input("Display multiplication table of? "))

# Iterate 10 times from i = 1 to 10
for i in range(1, 11):
   print(num, 'x', i, '=', num*i)
