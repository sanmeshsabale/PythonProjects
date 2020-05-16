Dict = { 5 : 'Welcome', 6 : 'To', 7 : 'world', 
        'A' : {1 : 'follow', 2 : 'life', 3 : 'rules'}, 
        'B' : {1 : 'my', 2 : 'Life'}} 
print("Initial Dictionary: ") 
print(Dict) 
  
# Deleting a Key value 
del Dict[6] 
print("\nDeleting a specific key: ") 
print(Dict) 
  
# Deleting a Key from 
# Nested Dictionary 
del Dict['A'][2] 
print("\nDeleting a key from Nested Dictionary: ") 
print(Dict)

Dict1 = { 5 : 'Welcome', 6 : 'To', 7 : 'world', 
        'A' : {1 : 'follow', 2 : 'life', 3 : 'rules'}, 
        'B' : {1 : 'my', 2 : 'Life'}} 
# Deleting a key  
# using pop() method 
pop_ele = Dict1.pop(5) 
print('\nDictionary after deletion: ' + str(Dict1)) 
print('Value associated to poped key is: ' + str(pop_ele))


Dict2 = { 5 : 'Welcome', 6 : 'To', 7 : 'world', 
        'A' : {1 : 'follow', 2 : 'life', 3 : 'rules'}, 
        'B' : {1 : 'my', 2 : 'Life'}} 
# Deleting an arbitrary key 
# using popitem() function 
pop_ele = Dict2.popitem() 
print("\nDictionary after deletion: " + str(Dict2)) 
print("The arbitrary pair returned is: " + str(pop_ele))

# Deleting entire Dictionary 
Dict2.clear() 
print("\nDeleting Entire Dictionary: ") 
print(Dict)
