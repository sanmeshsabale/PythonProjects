# Removal of elements in a List 

List = ['s','A','N','M','E','S', 
        'H','S','A','B','A','L','E'] 
print("Intial List: ") 
print(List) 
  
# using Slice operation 
Sliced_List = List[3:8] 
print("\nSlicing elements in a range 3-8: ") 
print(Sliced_List) 
  

Sliced_List = List[5:] 
print("\nElements sliced from 5th "
      "element till the end: ") 
print(Sliced_List) 
  

Sliced_List = List[:] 
print("\nPrinting all elements using slice operation: ") 
print(Sliced_List)

#NEGATIVE SLICING

Sliced_List = List[:-6] 
print("\nElements sliced till 6th element from last: ") 
print(Sliced_List) 
  
# Print elements of a range 
# using negative index List slicing 
Sliced_List = List[-6:-1] 
print("\nElements sliced from index -6 to -1") 
print(Sliced_List) 
  
# Printing elements in reverse 
# using Slice operation 
Sliced_List = List[::-1] 
print("\nPrinting List in reverse: ") 
print(Sliced_List)
