device_info = {"dev" : "router",
               "model" : 9000,
               "device_list" : ["R1","R2","R3"],
                "vendor_info" : {"name" : ["cisco","juniper","Avaya"],
                                  "add" : "bangalore"}}


>>> device_info['dev'] 
'router'
>>> device_info['device_list'] 
['R1', 'R2', 'R3']
>>> device_info['vendor_info'] 
{'name': 'cisco', 'add': 'bangalore'}
>>> ##to print R2
>>> device_info['device_list'][1] 
'R2'
>>> for items in evice_info['device_list']:
...     print(items)
... 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'evice_info' is not defined. Did you mean: 'device_info'?
>>> for items in device_info['device_list']: 
...     print(items)
... 
R1
R2
R3
>>> for k,v in device_info['vendor_info'].items():
...     print(k,v)
... 
name cisco
add bangalore
>>> for k,v in device_info.items():
...     print(k,v)
... 
dev router
model 9000
device_list ['R1', 'R2', 'R3']
vendor_info {'name': 'cisco', 'add': 'bangalore'}
>>>
>>> device_info = {"dev" : "router",
...                "model" : 9000,
...                "device_list" : ["R1","R2","R3"],
...                 "vendor_info" : {"name" : ["cisco","juniper"],
...                                   "add" : "bangalore"}}
>>> ##to print juniper in vendor_info
>>> 
>>> device_info["vendor_info"]['name'][1] 
'juniper'
>>> device_info = {"dev" : "router",
...                "model" : 9000,
...                "device_list" : ["R1","R2","R3"],
...                 "vendor_info" : {"name" : ["cisco","juniper","Avaya"],
...                                   "add" : "bangalore"}}
>>> device_info
{'dev': 'router', 'model': 9000, 'device_list': ['R1', 'R2', 'R3'], 'vendor_info': {'name': ['cisco', 'juniper', 'Avaya'], 'add': 'bangalore'}}
>>> if device_info["vendor_info"]['name'][1] == "juniper":
...     print("Juniper device")
... else:
... else:             nfo ))
  File "<stdin>", line 4
    else:
    ^
IndentationError: expected an indented block after 'else' statement on line 3
>>> if device_info["vendor_info"]['name'][1] == "juniper":
...     print("Juniper device")
... else:
...     print(device_info["vendor_info"]['name'])
... 
Juniper device
>>> if device_info["vendor_info"]['name'][1] == "fortigate": 
...     print("fortigate device")
... else:
...     print(device_info["vendor_info"]['name'])
... 
['cisco', 'juniper', 'Avaya']
>>> type(device_info)
<class 'dict'>
>>> device_info.keys()
dict_keys(['dev', 'model', 'device_list', 'vendor_info'])
>>> device_info["vendor_info"] 
{'name': ['cisco', 'juniper', 'Avaya'], 'add': 'bangalore'}
>>> device_info["vendor_info"].keys()
dict_keys(['name', 'add'])
>>> device_info["vendor_info"].values() 
dict_values([['cisco', 'juniper', 'Avaya'], 'bangalore'])