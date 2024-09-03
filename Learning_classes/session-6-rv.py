######List practice
##program to check valid ip range
# ip = input("enter your ip :")
# stored_ip = ip.split(".")
# if 0< int(stored_ip[0]) <=255 and  int(stored_ip[1]) <=255 and int(stored_ip[2]) <=255 and  int(stored_ip[3]) <=255:
#     print("valid ip")
# else:
#     print("invalid ip")
######
# vlan_id = ['10','20','30','40']
# >>> vlan_id[0]
# '10'
# >>> vlan_id[2]
# '30'
# >>> vlan_id[1]
# '20'
# >>> len(vlan_id)
# 4

vlan_id = ['10','20','30','40']
for item in vlan_id:
    print(item)