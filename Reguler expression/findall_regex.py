import re
print(" extract all mobile numbers present in input.txt where numbers are mixed with normal text data ")
f1=open("input.txt","r")
f2=open("output.txt","w")
for line in f1: 
    list=re.findall("[7-9]\d{9}",line)
for n in list:
    f2.write(n+"\n")
print("Extracted all Mobile Numbers into output.txt")
f1.close()
f2.close()
