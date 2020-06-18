Python 3.6.8 (tags/v3.6.8:3c6b436a57, Dec 24 2018, 00:16:47) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a='sanmesh'
>>> s in a
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    s in a
NameError: name 's' is not defined
>>> print(s in a)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print(s in a)
NameError: name 's' is not defined
>>> list1=["one","two","three"]
>>> print('two' in list1)
True
>>> print('five' in list1)
False
>>> print('two' not in list1)
False
>>> x="My name is SANMESH!!!"
>>> print('s' in x)
True
>>> a=100
>>> b=20
>>> print(a is b)
False
>>> print(a is not b)
True

>>> 
