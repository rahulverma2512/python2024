######### From session-3 // 10/02/2024

PS D:\networking\network-automation\boot-camp> python
Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> name = device
Traceback (most recent call last):     
  File "<stdin>", line 1, in <module>  
NameError: name 'device' is not defined
>>> device = Router
Traceback (most recent call last):     
  File "<stdin>", line 1, in <module>  
NameError: name 'Router' is not defined
>>> device = "Router"
>>> device[0]
'R' 
>>> help(str.index)
Help on method_descriptor:

index(...)
    S.index(sub[, start[, end]]) -> int

    Return the lowest index in S where substring sub is found,
    such that sub is contained within S[start:end].  Optional
    arguments start and end are interpreted as in slice notation.

    Raises ValueError when the substring is not found.

>>> device.index('R')
0
>>> device.index('t') 
3
>>> device.index('t')
3
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> ping_command ="ping 10.1.1.1 source 10.1.1.2"
>>> print(ping_command)
ping 10.1.1.1 source 10.1.1.2
>>> ping_command.index("10"
... 
KeyboardInterrupt
>>> ping_command.index("10")
5
>>> ping_command.index("11") 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: substring not found
>>> ping_command.index("1")  
5
>>> ping_command.index("1")
5
>>> ping_command[5]        
'1'
>>>
>>> ping_command
'ping 10.1.1.1 source 10.1.1.2'
>>> ping_command.replace("1")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: replace expected at least 2 arguments, got 1
>>> ping_command.replace("1" ,"2") 
'ping 20.2.2.2 source 20.2.2.2'
>>> ping_command.replace('5'"1" ,"2") 
'ping 10.1.1.1 source 10.1.1.2'
>>> ping_command.replace('5' ,"2")    
'ping 10.1.1.1 source 10.1.1.2'
>>> ping_command
'ping 10.1.1.1 source 10.1.1.2'
>>> temp = ping_command.replace("1" ,"2")
>>> temp
'ping 20.2.2.2 source 20.2.2.2'
>>> ping_command
'ping 10.1.1.1 source 10.1.1.2'
>>> temp = ping_command.replace([5] ,"2")  
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: replace() argument 1 must be str, not list
>>> temp = ping_command.replace(('1') ,"2") 
>>> temp
'ping 20.2.2.2 source 20.2.2.2'
>>> temp = ping_command.replace(('5') ,"2") 
>>> temp
'ping 10.1.1.1 source 10.1.1.2'
>>> temp = ping_command.replace(('1' ,"2", count=1)  
  File "<stdin>", line 1
    temp = ping_command.replace(('1' ,"2", count=1)
                                           ^^^^^^^
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
>>> temp = ping_command.replace(('1' ,"2", count==1) 
... 
... 
KeyboardInterrupt
>>> temp
'ping 10.1.1.1 source 10.1.1.2'
>>> temp = ping_command.replace(('1' ,"2", count==1,) 
... 
KeyboardInterrupt
>>> temp = ping_command.replace(('1' ,"2", count=1,)  
  File "<stdin>", line 1
    temp = ping_command.replace(('1' ,"2", count=1,)
                                           ^^^^^^^
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
>>> temp = ping_command.replace(('1' ,"2", count=1, /) 
  File "<stdin>", line 1
    temp = ping_command.replace(('1' ,"2", count=1, /)
                                           ^^^^^^^
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
>>> temp = ping_command.replace(('1' ,"2", count:=1,)   
... 
KeyboardInterrupt
>>> temp = ping_command.replace(('1' ,"2", count:=1,)
... 
KeyboardInterrupt
>>>
KeyboardInterrupt
>>>
KeyboardInterrupt
>>> temp
'ping 10.1.1.1 source 10.1.1.2'
>>> temp = ping_command.replace(('1' ,"2", 2)         
... 
KeyboardInterrupt
>>> temp = ping_command.replace(('1' ,'2', 2) 
... temp
  File "<stdin>", line 1
    temp = ping_command.replace(('1' ,'2', 2)
                                ^^^^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>>
>>> temp = ping_command.replace('1' ,'2', 2)  
>>> temp
'ping 20.2.1.1 source 10.1.1.2'
>>> temp = ping_command.replace('1' ,'2', 3) 
>>> temp
'ping 20.2.2.1 source 10.1.1.2'
>>> temp = ping_command.replace('1' ,'2', 0) 
>>> temp
'ping 10.1.1.1 source 10.1.1.2'
>>> temp = ping_command.replace('1' ,'2', 1:3)) 
  File "<stdin>", line 1
    temp = ping_command.replace('1' ,'2', 1:3))
                                           ^
SyntaxError: invalid syntax
>>> temp = ping_command.replace('1' ,'2', 1:3) 
  File "<stdin>", line 1
    temp = ping_command.replace('1' ,'2', 1:3)
                                           ^
SyntaxError: invalid syntax
>>> temp = ping_command.replace('1' ,'2', 1,3) 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: replace expected at most 3 arguments, got 4
>>> temp = ping_command.replace('1' ,'2', 0)   
>>> temp
'ping 10.1.1.1 source 10.1.1.2'
>>> temp = ping_command.replace('1' ,'2' , 0) 
>>> temp
'ping 10.1.1.1 source 10.1.1.2'
>>> temp = ping_command.replace('1' ,'2' , 1) 
>>> temp
'ping 20.1.1.1 source 10.1.1.2'
>>> temp = ping_command.replace('1' ,'2' ,1-3 ) 
>>> temp
'ping 20.2.2.2 source 20.2.2.2'
>>> temp = ping_command.replace('1' ,'2' ,1-4 ) 
>>> temp
'ping 20.2.2.2 source 20.2.2.2'
>>> temp
'ping 20.2.2.2 source 20.2.2.2'
>>> temp = ping_command.replace('1' ,'2' ,1 )   
>>> temp
'ping 20.1.1.1 source 10.1.1.2'
>>> temp = ping_command.replace('1' ,'2' ,3-4 ) 
>>> temp
'ping 20.2.2.2 source 20.2.2.2'
>>> temp = ping_command.replace('1' ,'2' ,5-3 ) 
>>> temp
'ping 20.2.1.1 source 10.1.1.2'
>>> temp = ping_command.replace('1' ,'2' ,0 ,2 ) 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: replace expected at most 3 arguments, got 4
>>> temp = ping_command.replace('1' ,'2' ,0 ,2)  
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: replace expected at most 3 arguments, got 4
>>> temp = ping_command.replace('1' ,'2' ,10-)  
  File "<stdin>", line 1
    temp = ping_command.replace('1' ,'2' ,10-)
                                             ^
SyntaxError: invalid syntax
>>> temp = ping_command.replace('1' ,'2' ,10-7) 
>>> temp
'ping 20.2.2.1 source 10.1.1.2'
>>> temp = ping_command.replace('1' ,'2' ,2+2)     
>>> temp
'ping 20.2.2.2 source 10.1.1.2'

>>> ping_command
'ping 10.1.1.1 source 10.1.1.2'
>>> dst_ip = "10.1.1.1"
>>> src_ip = 10.1.1.2
  File "<stdin>", line 1
    src_ip = 10.1.1.2
                 ^^
SyntaxError: invalid syntax
>>> src_ip = "10.1.1.2"
>>> ping_command = "ping " + dst_ip + " source " + src_ip 
>>> ping_command
'ping 10.1.1.1 source 10.1.1.2'
>>> src_ip = "2.2.2.2"  
>>> dst_ip = "4.4.4.4"  
>>> ping_command       
'ping 10.1.1.1 source 10.1.1.2'
>>> ping_command = "ping " + dst_ip + " source " + src_ip
>>> src_ip = "10.1.1.2"
>>> src_ip = "2.2.2.2"
>>> dst_ip = "4.4.4.4"
>>> ping_command = "ping " + dst_ip + " source " + src_ip
>>> ping_command        
'ping 4.4.4.4 source 2.2.2.2'
>>>
>>> 
>>> ping_command
'ping 4.4.4.4 source 2.2.2.2'
>>> temp = ping_command.replace('1' ,'2' ,2+2)   
KeyboardInterrupt
>>> src_ip = "1.1.1.1" 
>>> src_ip = "3.3.3.3" 
>>> ping_command = "ping " + dst_ip + " source " + src_ip
>>> ping_command
'ping 4.4.4.4 source 3.3.3.3'
>>> 2+2
4
>>> a+b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'a' is not defined
>>> "a"+"b"
'ab'
>>> '2'+'2'
'22'
>>> type(2)
<class 'int'>
>>> type(3) 
<class 'int'>
>>> type("3") 
<class 'str'>
>>> 2 +"2" 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 2 + int("2")
4
>>> str(2) + 2  
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>> str(2) + "2"  
'22'
>>> var1 = 2 
>>> var2 = "2"
>>> var1+var2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> var1+int(var2)
4
>>> var1+int(var2) = new
  File "<stdin>", line 1
    var1+int(var2) = new
    ^^^^^^^^^^^^^^
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
>>> var1+int(var2) ==new
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'new' is not defined
>>> new==var1+int(var2) 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'new' is not defined
>>> new=var1+int(var2)  
>>> new
4
2
>>> var2
'2'
>>> str(var1)+var2
>>> vlan_id=10
>>> syntax="vlan"
>>> vlan_command=vlan_id+syntax
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> vlan_command=syntax+str(vlan_id)
>>> vlan_comman
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'vlan_comman' is not defined. Did you mean: 'vlan_command'?
>>> vlan_command
'vlan10'
>>> vlan_command
'vlan10'
>>> syntax="vlan "
>>> vlan_id=10
>>> vlan_command=vlan_id+syntax
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> vlan_command=syntax+str(vlan_id)
>>> vlan_command
'vlan 10'
>>> exit()
>>> ping_command = "ping 10.10.10.10 source 20.20.20.20"
>>> ping_command
'ping 10.10.10.10 source 20.20.20.20'
>>> ping_command = "ping {} source{}" 
>>> ping_command.format("3.3.3.3" ,"4.4.4.4")
'ping 3.3.3.3 source4.4.4.4'
>>> ping_command = "ping {} source {}" 
>>> ping_command.format("3.3.3.3" ,"4.4.4.4") 
'ping 3.3.3.3 source 4.4.4.4'
>>> vlan_command = "vlan {}"
>>> "vlan {}".format(10)
'vlan 10'
>>> "vlan {}".format(20) 
'vlan 20'
>>> "vlan {}".format(30) 
'vlan 30'
>>> "vlan {}".format(40) 
'vlan 40'
>>> vlan_command = "vlan {}"
>>> vlan_id = 10
>>> vlan_command.format(vlan_id)
'vlan 10'
>>> vlan_id = 20
>>> vlan_command.format(vlan_id)
'vlan 20'
>>> vlan_id = "10"
>>> vlan_command.format(vlan_id)
'vlan 10'
>>> vlan_id = 10
>>> vlan_command.format(vlan_id)
'vlan 10'
>>>
>>> 
>>> 
>>> ping_command = "ping 10.10.10.10 source 20.20.20.20"
>>> ping_command = "ping {} source {} "
>>> source = 1.1.1.1
  File "<stdin>", line 1
    source = 1.1.1.1
                ^^
SyntaxError: invalid syntax
>>> source = "1.1.1.1"
>>> Destination = "2.2.2.2"
>>> src_ip = "1.1.1.1"      
>>> dst_ip = "2.2.2.2"      
>>> ping_command.format(src_ip ,dst_ip)
'ping 1.1.1.1 source 2.2.2.2 '
>>> ping_command
'ping {} source {} '
>>> ping_command.format(src_ip ,dst_ip)
'ping 1.1.1.1 source 2.2.2.2 '
>>> src_ip = "3.3.3.3" 
>>> dst_ip = "4.4.4.4" 
>>> ping_command.format(src_ip ,dst_ip)
'ping 3.3.3.3 source 4.4.4.4 '
>>> ping_command
'ping {} source {} '
>>> ping_command = ping_command.format(src_ip ,dst_ip
... 
KeyboardInterrupt
>>>
KeyboardInterrupt
>>> ping_command = ping_command.format(src_ip ,dst_ip)
>>> ping_command
'ping 3.3.3.3 source 4.4.4.4 '
>>> dst_ip = "5.5.5.5"                                 
>>> src_ip = "4.4.4.4"                                 
>>> ping_command       
'ping 3.3.3.3 source 4.4.4.4 '
>>> ping_command = ping_command.format(src_ip ,dst_ip) 
>>> ping_command                                       
'ping 3.3.3.3 source 4.4.4.4 '
>>> src_ip = "4.4.4.4" 
>>> dst_ip = "5.5.5.5" 
>>> ping_command = ping_command.format(src_ip ,dst_ip)
>>> ping_command                                       
'ping 3.3.3.3 source 4.4.4.4 '
>>>
>>> vlan_command = vlan {}
  File "<stdin>", line 1
    vlan_command = vlan {}
                        ^
SyntaxError: invalid syntax
>>> vlan_command = "vlan {}"
>>> vlan_id = 10 
>>> vlan_config = f"vlan {vlan_id}"
>>> vlan_config
'vlan 10'
>>> ping_command = " ping {} source {}"
>>> src_ip = "2.2.2.2" 
>>> dst_ip = "3.3.3.3"
>>> f"ping {src_ip} source {dst_ip}
  File "<stdin>", line 1
    f"ping {src_ip} source {dst_ip}
    ^
SyntaxError: unterminated f-string literal (detected at line 1)
>>> f"ping {src_ip} source {dst_ip}"
'ping 2.2.2.2 source 3.3.3.3'
>>> ping_command
' ping {} source {}'
>>> f"ping {src_ip} source {dst_ip}"
'ping 2.2.2.2 source 3.3.3.3'
>>> src_ip = "4.4.4.4"               
>>> dst_ip = "5.5.5.5"               
>>> f"ping {src_ip} source {dst_ip}"
'ping 4.4.4.4 source 5.5.5.5'
>>>


>>> name.upper(1, 3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: str.upper() takes no arguments (2 given)
>>> name.upper()    
'NETG INDIA'
>>>
>>> a = 2
>>> b = "2"
>>> a + b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> a = 2
>>> b = 2
>>> a+b
4
>>> a = "2"
>>> b = "2"
>>> ab
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'ab' is not defined. Did you mean: 'a'?
>>> a*b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'str'
>>> a+b
'22'
>>> a-b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for -: 'str' and 'str'
>>> a = 2
>>> b = '2'
>>> a + int(b)
4
>>> a =2 
>>> b = '2'
>>> str(a)+b
'22'
>>>