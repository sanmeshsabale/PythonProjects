# Creating a Set 
set1 = set([1, 2, 3, 4, 5, 6,  
            7, 8, 9, 10, 11, 12]) 
print("Intial Set: ") 
print(set1) 
  
# Removing elements from Set 
# using Remove() method 
set1.remove(5) 
set1.remove(6) 
print("\nSet after Removal of two elements: ") 
print(set1) 
  
# Removing elements from Set 
# using Discard() method 
set1.discard(8) 
set1.discard(9) 
print("\nSet after Discarding two elements: ") 
print(set1) 
  
# Removing elements from Set 
# using iterator method 
for i in range(1, 5): 
    set1.remove(i) 
print("\nSet after Removing a range of elements: ") 
print(set1)

sett1 = set([11, 12, 13, 14, 15, 16,  
            17, 18, 19, 120, 121, 122])

# Removing element from the  
# Set using the pop() method 
sett1.pop() 
print("\nSet after popping an element: ") 
print(sett1)


set12 = set([1,2,3,4,5]) 
print("\n Initial set: ") 
print(set1) 
  
  
# Removing all the elements from  
# Set using clear() method 
set12.clear() 
print("\nSet after clearing all the elements: ") 
print(set12)


# Creating a Set 
String = ('G', 'e', 'e', 'k', 's', 'F', 'o', 'r') 
  
Fset1 = frozenset(String) 
print("\nThe FrozenSet is: ") 
print(Fset1) 
  
# To print Empty Frozen Set 
# No parameter is passed 
print("\nEmpty FrozenSet: ") 
print(frozenset())
