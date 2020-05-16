# Python program to demonstrate   
# accessing a element from a Dictionary  
  
# Creating a Dictionary  
Dict = {1: 'key', 'can': 'used', 3: 'inside'} 
  
# accessing a element using key 
print("Accessing a element using key:") 
print(Dict['can']) 
  
# accessing a element using key 
print("Accessing a element using key:") 
print(Dict[1])

# accessing a element using get() 
# method 
print("Accessing a element using get:") 
print(Dict.get(3))

# Creating a Dictionary 
Dict = {'Dict1': {1: 'price'}, 
        'Dict2': {'Name': 'For'}} 
  
# Accessing element using key 
print(Dict['Dict1']) 
print(Dict['Dict1'][1]) 
print(Dict['Dict2']['Name'])
