import re
print(" check whether the given number is valid mobile number or not? ")
n=input("Enter number:")
m=re.fullmatch("[7-9]\d{9}",n)
if m!= None:
    print("Valid Mobile Number")
else:
    print("Invalid Mobile Number") 
