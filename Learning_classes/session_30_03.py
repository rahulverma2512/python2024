###dictionary
site_d_dtls = {'site-name':'site-A', 'site-type': 'non-mpls', 'device-1' : 'cisco-R', 'device-2': 'firewall' , 'model-1': 8500 , 'model-2': '100D'}
site_d_dtls>>> site_d_dtls['site-A'] 
Traceback (most recent call last):   
  File "<stdin>", line 1, in <module>
KeyError: 'site-A'
>>> site_d_dtls[site-A]  
Traceback (most recent call last):   
  File "<stdin>", line 1, in <module>
NameError: name 'site' is not defined. Did you mean: 'aiter'? Or did you forget to import 'site'?
>>> site_d_dtls['site-name']
'site-A'
>>> site_d_dtls['site-Name'] 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'site-Name'
>>> site_d_dtls              
{'site-name': 'site-A', 'site-type': 'non-mpls', 'device-1': 'cisco-R', 'device-2': 'firewall', 'model-1': 8500, 'model-2': '100D'}
>>> site_d_dtls['model-1']   
8500
>>> type(site_d_dtls) 
<class 'dict'>
>>> site_d_dtls.items()
dict_items([('site-name', 'site-A'), ('site-type', 'non-mpls'), ('device-1', 'cisco-R'), ('device-2', 'firewall'), ('model-1', 8500), ('model-2', '100D')])
>>> for k,v in site_d_dtls:
...     print(k,v)
... 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: too many values to unpack (expected 2)
>>> for k,v in site_d_dtls.items():
...     print(k,v)
... 
site-name site-A
site-type non-mpls
device-1 cisco-R
device-2 firewall
model-1 8500
model-2 100D
>>> site_d_dtls.keys()
dict_keys(['site-name', 'site-type', 'device-1', 'device-2', 'model-1', 'model-2'])
>>> site_d_dtls.values() 
dict_values(['site-A', 'non-mpls', 'cisco-R', 'firewall', 8500, '100D'])
>>> site_d_dtls.key['device-1'] == 'cisco-R' 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'dict' object has no attribute 'key'. Did you mean: 'keys'?
>>> site_d_dtls['device-1'] == 'cisco-R'     
True
>>> site_d_dtls['device-1'] == 'cisco-s' 
False
>>> site_d_dtls['device-'] == 'cisco-s'  
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'device-'
>>> site_d_dtls.get['device-'] == 'cisco-s' 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> site_d_dtls.get("device-1")            
'cisco-R'
>>> site_d_dtls.get("device-")  
>>> site_d_dtls                 
{'site-name': 'site-A', 'site-type': 'non-mpls', 'device-1': 'cisco-R', 'device-2': 'firewall', 'model-1': 8500, 'model-2': '100D'}
>>> site_d_dtls.update({'model-2' : '100F'}) 
>>> site_d_dtls
{'site-name': 'site-A', 'site-type': 'non-mpls', 'device-1': 'cisco-R', 'device-2': 'firewall', 'model-1': 8500, 'model-2': '100F'}
>>> site_d_dtls.get("model-2" : "unknown") 
  File "<stdin>", line 1
    site_d_dtls.get("model-2" : "unknown")
                              ^
SyntaxError: invalid syntax
>>> site_d_dtls.get("model-2", "unknown")  
'100F'
>>> site_d_dtls.get("model-", "unknown")  
'unknown'
>>> dir(dict) 
['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
>>> site_d_dtls
{'site-name': 'site-A', 'site-type': 'non-mpls', 'device-1': 'cisco-R', 'device-2': 'firewall', 'model-1': 8500, 'model-2': '100F'}
>>> site_d_dtls.clear()
>>> site_d_dtls
{}
>>> site_d_dtls = {'site-name': 'site-A', 'site-type': 'non-mpls', 'device-1': 'cisco-R', 'device-2': 'firewall', 'model-1': 8500, 'model-2': '100F'}
>>> site_d_dtls
{'site-name': 'site-A', 'site-type': 'non-mpls', 'device-1': 'cisco-R', 'device-2': 'firewall', 'model-1': 8500, 'model-2': '100F'}
>>> help(dict.fromkeys) 
Help on built-in function fromkeys:

fromkeys(iterable, value=None, /) method of builtins.type instance
    Create a new dictionary with keys from iterable and values set to value.

>>> site = {"A","B","C"}
>>> device = {"1",'2','3'}
>>> site_device = dict.fromkeys(site,device) 
>>> site_device
{'C': {'3', '2', '1'}, 'B': {'3', '2', '1'}, 'A': {'3', '2', '1'}}
>>> site_d_dtls
{'site-name': 'site-A', 'site-type': 'non-mpls', 'device-1': 'cisco-R', 'device-2': 'firewall', 'model-1': 8500, 'model-2': '100F'}
>>> site_d_dtls.pop()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: pop expected at least 1 argument, got 0
>>> site_d_dtls.pop('0') 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: '0'
>>> site_d_dtls.pop('model-2') 
'100F'
>>> site_d_dtls                
{'site-name': 'site-A', 'site-type': 'non-mpls', 'device-1': 'cisco-R', 'device-2': 'firewall', 'model-1': 8500}
>>> site_d_dtls.update("model-2","100D")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: update expected at most 1 argument, got 2
>>> help(dict.update)                   
Help on method_descriptor:

update(...)
    D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
    If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
    If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
    In either case, this is followed by: for k in F:  D[k] = F[k]

>>> site_d_dtls.update({"model-2","100D"}) 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: dictionary update sequence element #0 has length 4; 2 is required
>>> site_d_dtls.update({"model-2" :"100D"}) 
>>> site_d_dtls
{'site-name': 'site-A', 'site-type': 'non-mpls', 'device-1': 'cisco-R', 'device-2': 'firewall', 'model-1': 8500, 'model-2': '100D'}