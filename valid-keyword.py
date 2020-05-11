#Python code to demonstrate working of iskeyword() 
  
# importing "keyword" for keyword operations 
import keyword 
# initializing strings for testing while putting them in an array 
keys = ["for", "while", "sanmesh", "break", "sky", 
"elif", "assert", "Anil", "lambda","if","is","else", "whatever"] 
  
for i in range(len(keys)): 
     # checking which are keywords 
    if keyword.iskeyword(keys[i]): 
        print(keys[i] + " is python keyword") 
    else: 
        print(keys[i] + " is not a python keyword") 
