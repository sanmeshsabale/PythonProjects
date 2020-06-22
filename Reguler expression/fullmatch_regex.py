import re
print("check whether the given string is Yava language identifier or not?")
s=input("Enter Identifier:")
m=re.fullmatch("[a-k][0369][a-zA-Z0-9#]*",s)
if m!= None:
    print(s,"is valid Identifier")
else:
    print(s,"is invalid Identifier") 
