###17/02/2024 - session -4
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 
'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']>>>
>>> 
>>> help(str.split)
Help on method_descriptor:

split(self, /, sep=None, maxsplit=-1)
    Return a list of the substrings in the string, using sep as the separator string.

      sep
        The separator used to split the string.

        When set to None (the default value), will split on any whitespace
        character (including \n \r \t \f and spaces) and will discard
        empty strings from the result.
      maxsplit
        Maximum number of splits (starting from the left).
        -1 (the default value) means no limit.

    Note, str.split() is mainly useful for data that has been intentionally
    delimited.  With natural text that includes punctuation, consider using
    the regular expression module.

>>> ip = "10.2.3.4"
>>> ip
'10.2.3.4'
>>> new_ip = ip.spli(".") 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'str' object has no attribute 'spli'. Did you mean: 'split'?
>>> new_ip = ip.split(".") 
>>> new_ip
['10', '2', '3', '4']
>>>
>>> joined_ip = "".join(new_ip)
>>> joined_ip
'10234'
>>> joined_ip = ".".join(new_ip) 
>>> joined_ip
'10.2.3.4'
>>>
>>> var1 = "this// is my automation class"
>>> var1
'this// is my automation class'
>>> var1 = "this//is my automation class"  
>>> var1
'this//is my automation class'
>>>
>>> var1.split("//")
['this', 'is my automation class']
>>> "".join(var1.split("//"))
'thisis my automation class'
>>> " ".join(var1.split("//")) 
'this is my automation class'
>>> "  ".join(var1.split("//")) 
'this  is my automation class'
>>> " ".join(var1.split("//"))  
'this is my automation class'
>>> new_ip
['10', '2', '3', '4']
>>> len(new_ip)
4
>>> if len(new_ip) == 4
  File "<stdin>", line 1
    if len(new_ip) == 4
                       ^
SyntaxError: expected ':'
>>> if len(new_ip) == 4:
... print("valid IP")
  File "<stdin>", line 2
    print("valid IP")
    ^
IndentationError: expected an indented block after 'if' statement on line 1
>>> print("valid IP"):
  File "<stdin>", line 1
    print("valid IP"):
                     ^
SyntaxError: invalid syntax
>>> if len(new_ip) == 4:
... print("valid ip")
  File "<stdin>", line 2
    print("valid ip")
    ^
IndentationError: expected an indented block after 'if' statement on line 1
>>> if len(new_ip) == 4:
...     print("valid IP")
... else
  File "<stdin>", line 3
    else
        ^
SyntaxError: expected ':'
>>>                   P")
>>> 
>>> 
>>> ip
'10.2.3.4'
>>> ip.startswith("10")
True
>>> ip.startswith("20") 
False
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 
'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']>>>
>>> ip
'10.2.3.4'
>>> if ip.startswith("10")
  File "<stdin>", line 1
    if ip.startswith("10")
                          ^
SyntaxError: expected ':'
>>> if ip.startswith("10"):
...     pring("class A IP")
... else:
...     print("unknown")
... 
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
NameError: name 'pring' is not defined. Did you mean: 'print'?
>>>
>>> 
>>> description = " connected to server"
>>> description.endswith("server")
True
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 
'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']>>> description = " connected to server"
>>> description.find("server")
14
>>> print("14")
14
>>> description = " connected to server"
>>> "server" in description
True
>>> description = " connected to Server" 
>>> "server" in description
False
>>> description.lower()
' connected to server'
>>> "server" in description
False
>>> new_description = description.lower() 
>>> "server" in new_description
True
>>>
>>> "server" in "connected to server abc"
True
>>> if "server" in "connected to server abc":
...     print("string found")
... else:
...     print("string not found")
... 
string found
>>>
>>> 
>>> ip
'10.2.3.4'
>>> ip = " 10.2.3.4"
>>> ip.startswith("10")
False
>>>
>>> 
>>> ip = input("Enter your IP:")
Enter your IP: 10.2.3.4
>>> ip
' 10.2.3.4'
>>> ip = input("Enter your IP:")
Enter your IP:   10.2.3.4
>>> print(ip)
   10.2.3.4
>>> print(ip.strip) 
<built-in method strip of str object at 0x000002798D804770>
>>> print(ip.strip()) 
10.2.3.4
>>> ip.startswith("10")
False
>>>
>>> print(ip.strip) 
<built-in method strip of str object at 0x000002798D804770>
>>> print(ip.strip()) 
10.2.3.4
>>> print(ip.strip("4")) 
   10.2.3.
>>> print(ip.strip("1")) 
   10.2.3.4
>>> print(ip.strip(" 1")) 
0.2.3.4
>>> print(ip.strip("1"))  
   10.2.3.4
>>> print((ip.strip("1")).strip("1")) 
   10.2.3.4
>>> print((ip.strip("1")).strip("10")) 
   10.2.3.4
>>> print((ip.strip("")).strip("10"))  
   10.2.3.4
>>> print(ip.strip("").strip("10"))   
   10.2.3.4
>>>
>>> ip.strip("")                   
'   10.2.3.4'
>>> ip
'   10.2.3.4'
>>> ip.strip(" ") 
'10.2.3.4'
>>> print(ip.strip(" ").strip("10")) 
.2.3.4
>>>
>>> print(ip.strip(" ").strip("2"))  
10.2.3.4
>>>                                  
>>> 
>>> print(ip.strip(" ").strip((ip.find("2")("2")) 
... 
... 
...  
KeyboardInterrupt
>>> print(ip.strip(" ").strip("2"))
10.2.3.4
>>>
>>> str_var = "I%^&n**^^d89i665a#$ i89s &*G5r789e%^a*((t!"
>>> str_var.strip("%^&**^^")
'I%^&n**^^d89i665a#$ i89s &*G5r789e%^a*((t!'
>>> dir(str)                 
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 
'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']>>> str_var.isalpha()
False
>>> str = str_var.isalpha() 
>>> str
False
>>> str_var
'I%^&n**^^d89i665a#$ i89s &*G5r789e%^a*((t!'
>>> str_var.strip("%^&" ,"**^^d89i66")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: strip expected at most 1 argument, got 2
>>> help(str)                         
Help on bool object:

class bool(int)
 |  bool(x) -> bool
 |
 |  Returns True when the argument x is true, False otherwise.
 |  The builtins True and False are the only two instances of the class bool.
 |  The class bool is a subclass of the class int, and cannot be subclassed.
 |
 |  Method resolution order:
 |      bool
 |      int
 |      object
 |
 |  Methods defined here:
 |
 |  __and__(self, value, /)
 |      Return self&value.
 |
 |  __invert__(self, /)
^CTraceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<frozen _sitebuiltins>", line 103, in __call__
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\pydoc.py", line 2013, in __call__
    self.help(request)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\pydoc.py", line 2074, in help
    else: doc(request, 'Help on %s:', output=self._output, is_cli=is_cli)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\pydoc.py", line 1787, in doc
    pager(render_doc(thing, title, forceload))
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\pydoc.py", line 1581, in <lambda>
    return lambda text: tempfilepager(plain(text), 'more <')
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python312\Lib\pydoc.py", line 1634, in tempfilepager
    os.system(cmd + ' "' + filename + '"')
KeyboardInterrupt
>>> dir (str) 
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'is_integer', 'numerator', 'real', 'to_bytes']
>>>
>>> 
>>> dir(str)  
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'is_integer', 'numerator', 'real', 'to_bytes']
>>>
>>> 
>>> str_var
'I%^&n**^^d89i665a#$ i89s &*G5r789e%^a*((t!'
>>>
>>>        
>>> str.split(""\) 
  File "<stdin>", line 1
    str.split(""\)
                 ^
SyntaxError: unexpected character after line continuation character
>>> str_var.split("") 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: empty separator
>>> str_var.split(" ") 
['I%^&n**^^d89i665a#$', 'i89s', '&*G5r789e%^a*((t!']
>>>
>>> 
>>> ## extract - india is great for given string
>>> str_var = "I%^&n**^^d89i665a#$ i89s &*G5r789e%^a*((t!"
>>> 
>>> str_var[] 
  File "<stdin>", line 1
    str_var[]
            ^
SyntaxError: invalid syntax
>>> str_var[0] 
'I'
>>> str_var[]  
  File "<stdin>", line 1
    str_var[]
            ^
SyntaxError: invalid syntax
>>> str_var[1] 
'%'
>>> str_var[2] 
'^'
>>> for item in str_var
  File "<stdin>", line 1
    for item in str_var
                       ^
SyntaxError: expected ':'
>>> for item in str_var:
...     print(item)
... 
I
%
^
&
n
*
*
^
^
d
8
9
i
6
6
5
a
#
$

i
8
9
s

&
*
G
5
r
7
8
9
e
%
^
a
*
(
(
t
!
>>> for abc in str_var:  
...     print(abc)
... \
... for abc in str_var:
  File "<stdin>", line 4
    for abc in str_var:
    ^^^
SyntaxError: invalid syntax
>>> for abc in str_var:
...     print(item)     
...     print(abc)       
... 
!
I
!
%
!
^
!
&
!
n
!
*
!
*
!
^
!
^
!
d
!
8
!
9
!
i
!
6
!
6
!
5
!
a
!
#
!
$
!
 
!
i
!
8
!
9
!
s
!

!
&
!
*
!
G
!
5
!
r
!
7
!
8
!
9
!
e
!
%
!
^
!
a
!
*
!
(
!
(
!
t
!
!