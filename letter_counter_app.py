 #Letter Counter App

print("Welcome to the letter Counter App")
#Get User Input
name=input("What is your name:").title().strip()
print("Hello,"+ name+ "!")
print("I will count  the number of times that a specific letter occurs ina message")
message=input("Please enter a message")
letter=input("  Which letter would you like to count the occurances of:")

message=message.lower()
letter=letter.lower()

letter_count=message.count(letter)
print(name+", your messgae has"+str(letter_count)+" "+letter+''s in it.")
