print("Welcome to the MPH to MPS Conversion Application.")

#User Input
mph=float(input("What is your speed in miles per hour:"))

#Convert to mps
mps=mph*0.4474

#rounding to 2 decimals only
mps=round(mps,2)

print("Your Speed in Miles per second is "+ str(mps)+".")
