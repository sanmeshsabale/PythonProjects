Python 3.6.8 (tags/v3.6.8:3c6b436a57, Dec 24 2018, 00:16:47) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=10
>>> type(a)
<class 'int'>
>>> a=20.8
>>> type(a)
<class 'float'>
>>> a=10+5j
>>> type(a)
<class 'complex'>
>>> a='sanmesh'
>>> type(a)
<class 'str'>
>>> a=true
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    a=true
NameError: name 'true' is not defined
>>> a=True
>>> type(a)
<class 'bool'>
>>> int(True)
1
>>> int(False)
0
>>> a=[10,20,60,89]
>>> a=[10,20,90,89,55]
>>> type(a)
<class 'list'>
>>> s=(10,'sanmesh',55.2)
>>> type(s)
<class 'tuple'>
>>> a={'name':'sanmesh','state':'MH','Edu':'ME'}
>>> type(a)
<class 'dict'>
>>> a.keys()
dict_keys(['name', 'state', 'Edu'])
>>> a.values()
dict_values(['sanmesh', 'MH', 'ME'])
>>> a.get('name')
'sanmesh'
>>> a['state']
'MH'
>>> range(10)
range(0, 10)
>>> list(range(10,2))
[]
>>> list(range(2,20,5))
[2, 7, 12, 17]
>>> complex(10)
(10+0j)
>>> complex(50,8)
(50+8j)
>>> complex(0)
0j
>>> 
