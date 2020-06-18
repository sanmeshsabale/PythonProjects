print("Program to check whether your number is Prime or Not Prime")
num =int(input("Enter a number:"))

for i in range(2,num):
    if num % i ==0:
        print("Not prime")
        break


else:
    print("prime")
