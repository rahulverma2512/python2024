##list methods , tuppels and zip function.

>>> dir(list)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> intf_list = ["gig0/1","gig0/2","gig0/3","gig0/4"]
>>> intf_list
['gig0/1', 'gig0/2', 'gig0/3', 'gig0/4']
>>> intf_list[0] 
'gig0/1'
>>> intf_list[1] 
'gig0/2'
>>> intf_list[2]
'gig0/3'
>>> intf_list[0:2] 
['gig0/1', 'gig0/2']
>>> intf_list[0:3] 
['gig0/1', 'gig0/2', 'gig0/3']
>>> intf_list[0:4] 
['gig0/1', 'gig0/2', 'gig0/3', 'gig0/4']
>>> int_list2=["gig0/5",]  
KeyboardInterrupt
>>>
>>> int_list2=["gig0/5","gig0/6"] 
>>> intf_list
['gig0/1', 'gig0/2', 'gig0/3', 'gig0/4']
>>> intf_list.append(intf_list) 
>>> intf_list 
['gig0/1', 'gig0/2', 'gig0/3', 'gig0/4', [...]]
>>> intf_list.append(intf_list2) 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'intf_list2' is not defined. Did you mean: 'intf_list'?
>>> int_list2
['gig0/5', 'gig0/6']
>>> intf_list.append(intf_list2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'intf_list2' is not defined. Did you mean: 'intf_list'?
>>> intf_list.append(int_list2)  
>>> intf_list
['gig0/1', 'gig0/2', 'gig0/3', 'gig0/4', [...], ['gig0/5', 'gig0/6']]
>>> intf_list
['gig0/1', 'gig0/2', 'gig0/3', 'gig0/4', [...], ['gig0/5', 'gig0/6']]
>>> intf_list.clear()
>>> intf_list
[]
>>> intf_list=['gig0/1', 'gig0/2', 'gig0/3', 'gig0/4']
>>> 
>>> intf_list=['gig0/1', 'gig0/2', 'gig0/3', 'gig0/4']
>>> intf_list2 = intf_list.copy()
>>> intf_list2
['gig0/1', 'gig0/2', 'gig0/3', 'gig0/4']
>>> intf_list2.count("gig0/3") 
1
>>> help(list.count) 
Help on method_descriptor:

count(self, value, /)
    Return number of occurrences of value.

>>> intf_list2.count("gig0/5") 
0
>>> intf_list=['gig0/1', 'gig0/2', 'gig0/3', 'gig0/4',] 
>>> vlan_list=['10','10','20','20''20','30''30','30''40','40''40','40'] 
>>> vlan_list.count("10")                                              
2
>>> vlan_list.count("20") 
1
>>> vlan_list.count("40") 
1
>>> vlan_list=['10','10','20','20','20','30','30','30''40','40','40','40']
>>> vlan_list.count("40")
3
>>> vlan_list.count("10") 
2
>>> vlan_list.count("20") 
3
>>> vlan_list.count("30") 
2
>>> vlan_list=['10','10','20','20','20','30','30','30','40','40','40','40']  
>>> vlan_list.count("30")
3
>>> vlan_list.count("40") 
4
>>> dir(list) 
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> intf_list=['gig0/1', 'gig0/2', 'gig0/3', 'gig0/4']   
>>> vlan_list=['10','20','30','40']
>>> vlan_list.extend(intf_list) 
>>> vlan_list
['10', '20', '30', '40', 'gig0/1', 'gig0/2', 'gig0/3', 'gig0/4']
>>> intf_list.extend(vlan_list) 
>>> intf_list
['gig0/1', 'gig0/2', 'gig0/3', 'gig0/4', '10', '20', '30', '40', 'gig0/1', 'gig0/2', 'gig0/3', 'gig0/4']
>>> vlan_list
['10', '20', '30', '40', 'gig0/1', 'gig0/2', 'gig0/3', 'gig0/4']
>>> intf_list=['gig0/1', 'gig0/2', 'gig0/3', 'gig0/4']  
>>> vlan_list=['10','20','30','40']
>>> intf_list.extend(vlan_list)
>>> intf_list
['gig0/1', 'gig0/2', 'gig0/3', 'gig0/4', '10', '20', '30', '40']
>>> intf_list
['gig0/1', 'gig0/2', 'gig0/3', 'gig0/4', '10', '20', '30', '40']
>>> intf_list.index("10") 
4
>>> intf_list.index("0/3") 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: '0/3' is not in list
>>> intf_list.index("gig0/3") 
2
>>> intf_list.index("40")     
7
>>> len(intf_list) 
8
>>> intf_list=['gig0/1', 'gig0/2', 'gig0/3', 'gig0/4'] 
>>> vlan_list=['10','20','30','40']
>>> intf_list.insert(5, "gig0/5") 
>>> intf_list
['gig0/1', 'gig0/2', 'gig0/3', 'gig0/4', 'gig0/5']
>>> intf_list.insert(5, "gig0/5", "gig0/6") 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: insert expected 2 arguments, got 3
>>> intf_list.insert(5,6 "gig0/5", "gig0/6") 
  File "<stdin>", line 1
    intf_list.insert(5,6 "gig0/5", "gig0/6")
                       ^^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> intf_list.insert(5,6, "gig0/5", "gig0/6") 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: insert expected 2 arguments, got 4
>>> intf_list=['gig0/1', 'gig0/2', 'gig0/3', 'gig0/4'] 
>>> vlan_list=['10','20','30','40']
>>> intf_list2=['gig0/5', 'gig0/6'] 
>>> intf_list.insert(intf_list2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: insert expected 2 arguments, got 1
>>> intf_list.append(intf_list2) 
>>> intf_list
['gig0/1', 'gig0/2', 'gig0/3', 'gig0/4', ['gig0/5', 'gig0/6']]
>>> intf_list=['gig0/1', 'gig0/2', 'gig0/3', 'gig0/4'] 
>>> intf_list2=['gig0/5', 'gig0/6'] 
>>> intf_list.extend(intf_list2)
>>> intf_list
['gig0/1', 'gig0/2', 'gig0/3', 'gig0/4', 'gig0/5', 'gig0/6']
>>>
>>> 
>>> intf_list
['gig0/1', 'gig0/2', 'gig0/3', 'gig0/4', 'gig0/5', 'gig0/6']
>>> intf_list.remove('gig0/4', 'gig0/5') 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: list.remove() takes exactly one argument (2 given)
>>> intf_list.remove('gig0/4', 'gig0/5') 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: list.remove() takes exactly one argument (2 given)
>>> dir(list)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> intf_list                        
['gig0/1', 'gig0/2', 'gig0/3', 'gig0/4', 'gig0/5', 'gig0/6']
>>> intf_list.remove("gig0/4") 
>>> intf_list
['gig0/1', 'gig0/2', 'gig0/3', 'gig0/5', 'gig0/6']
>>> intf_list.pop
<built-in method pop of list object at 0x0000021D7229F2C0>
>>> intf_list
['gig0/1', 'gig0/2', 'gig0/3', 'gig0/5', 'gig0/6']
>>> help(list.pop) 
Help on method_descriptor:

pop(self, index=-1, /)
    Remove and return item at index (default last).

    Raises IndexError if list is empty or index is out of range.

>>> intf_list      
['gig0/1', 'gig0/2', 'gig0/3', 'gig0/5', 'gig0/6']
>>> intf_list.pop()
'gig0/6'
>>> intf_list       
['gig0/1', 'gig0/2', 'gig0/3', 'gig0/5']
>>> intf_list.pop()
'gig0/5'
>>> intf_list       
['gig0/1', 'gig0/2', 'gig0/3']
>>> intf_list.insert("gig0/4") 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: insert expected 2 arguments, got 1
>>> intf_list.insert(3,"gig0/4") 
>>> intf_list                    
['gig0/1', 'gig0/2', 'gig0/3', 'gig0/4']
>>> intf_list.reverse()
>>> intf_list
['gig0/4', 'gig0/3', 'gig0/2', 'gig0/1']
>>> intf_list.sort()
>>> intf_list        
['gig0/1', 'gig0/2', 'gig0/3', 'gig0/4']
>>> list1 = [1,6,2,8,3,4]
>>> list1.sort()
>>> list1
[1, 2, 3, 4, 6, 8]
>>>
>>> 
>>> list1 = [1,2,2,3,3,3,4,4,4,4]
>>> t1 = tupple(list1) 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'tupple' is not defined. Did you mean: 'tuple'?
>>> t1 = tuple(list1)  
>>> t1
(1, 2, 2, 3, 3, 3, 4, 4, 4, 4)
>>> list1
[1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
>>> set(list1)
{1, 2, 3, 4}
>>> a = ["10:11AM", "11:11AM", "12:11PM"]                                     
>>> b = [90, 80, 70]
>>> c = [1,2,3]
>>> x = zip(a, b, c)
>>> #use the tuple() function to display a readable version of the result:
>>> print(list(x)) 
[('10:11AM', 90, 1), ('11:11AM', 80, 2), ('12:11PM', 70, 3)]
>>>