######### From session-2 // 03/02/2024

>>> name = "netgindia"
>>> type(name)
<class 'str'>
>>> pin = 123456
>>> type(pin)
<class 'int'>
>>> pin[1] 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not subscriptable
>>> name[0]
'n'
>>> name[0:4] 
'netg'
>>> name
'netgindia'
>>> name = "netg india" 
>>> id(name)
2046877973744
>>> id(0)
140733182982552
>>>
>>> name
'netg india'
>>> help(str.upper)
Help on method_descriptor:

upper(self, /)
    Return a copy of the string converted to uppercase.
    
