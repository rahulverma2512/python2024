##switch config using list - simple program to add given commands list to all the interfaces
int_list = ["Gig0/1", "Gig0/2", "Gig0/3", "Gig0/4"]
int_config = ["switchport", "switchport mode access", "switchport access vlan 10"]
print("config t")
for intf in int_list:
    print("=====================")
    print(f"interface {intf}")
    for config in int_config:
        print(config)
print("\n### Switchport configuaration has been completed ###")



# ##switch config using list -  program to add given access command to gig0/1-3 and trunk commands to Gig0/4
# int_list = ["Gig0/1", "Gig0/2", "Gig0/3", "Gig0/4"]
# int_config = ["switchport", "switchport mode access", "switchport access vlan 10"]
# int_trunk_config = ["switchport", "switchport mode trunk", "switchport trunk allowed vlan add 10"]

# print("config t")
# for intf in int_list:
#     print("=====================")
#     print(f"interface {intf}")
#     if intf == "Gig0/1" or intf == "Gig0/2" or intf == "Gig0/3":
#         print(f"Description towards access ports" )
#         for config in int_config:
#             print(config)
#     else:
#         print(f"Description towards agg switch" )
#         for trunk in int_trunk_config:
    
#             print(trunk)
# print("\n### Switchport configuaration has been completed ###")

# ##switch config using list -  program to add given access command to gig0/1-3 and respective vlans and trunk commands to Gig0/4
# int_list = ["Gig0/1", "Gig0/2", "Gig0/3", "Gig0/4"]
# vlan_list = ["10", "20", "30"]
# int_config = ["switchport", "switchport mode access", "switchport access vlan"]
# int_trunk_config = ["switchport", "switchport mode trunk", "switchport trunk allowed vlan add"]

# print("config t")
# for intf in int_list:
#     print("=====================")
#     print(f"interface {intf}")
#     if intf == "Gig0/1" or intf == "Gig0/2" or intf == "Gig0/3":
#         print(f"Description towards access ports" )
#         for config in int_config[0:2]:
#             print(config)
#     for vlan in vlan_list:
#         for intf in int_list[0:2]:
#             print(f"switchport access vlan {vlan}")
    
# int_list = ["Gig0/1", "Gig0/2", "Gig0/3", "Gig0/4"]
# vlan_list = ["10", "20", "30"]
# int_config = ["switchport", "switchport mode access", "switchport access vlan"]
# int_trunk_config = ["switchport", "switchport mode trunk", "switchport trunk allowed vlan add"]

# print("config t\n")

# for intf in int_list:
#     print(f"interface {intf}")
#     print("=====================")
#     if intf in ["Gig0/1", "Gig0/2", "Gig0/3"]:
#         print("Description towards access ports")
#         for config in int_config[0:2]:
#             print(config)
#     if intf == "Gig0/1":
#         print(f"switchport access vlan {vlan_list[0]}\n")
#     elif intf == "Gig0/2":
#         print(f"switchport access vlan {vlan_list[1]}\n")
#     elif intf == "Gig0/3":
#         print(f"switchport access vlan {vlan_list[2]}\n")
#     else:
#         print("Description towards agg switch")
#         for config2 in int_trunk_config[0:2]:
#             print(config2)
#         print("switchport trunk allowed vlan add " + ",".join(vlan_list))

# print("\n### Switchport configuration has been completed ###\n")                
                        

# ####### multile switch config with realistic cli view
# sw_list = ["sw1", "sw2", "sw3"]
# int_list = ["Gig0/1", "Gig0/2", "Gig0/3", "Gig0/4"]
# vlan_list = ["10", "20", "30"]
# int_config = ["switchport", "switchport mode access", "switchport access vlan"]
# int_trunk_config = ["switchport", "switchport mode trunk", "switchport trunk allowed vlan add"]
# for sw in sw_list:
#     print("\nConfiguring", sw)
#     print("***************")
#     print(sw,"#config t")
#     # print(sw,"(config)#exit\n")
#     for intf in int_list:
#         print(sw,f"(config)#interface {intf}")
#         if intf in ["Gig0/1", "Gig0/2", "Gig0/3"]:
#             print(sw,"(config-if)#Description towards access ports")
#             for config in int_config[0:2]:
#                 print(sw,f"(config-if)#",config)
#         if intf == "Gig0/1":
#             print(sw,f"(config-if)#switchport access vlan {vlan_list[0]}\n")
#         elif intf == "Gig0/2":
#             print(sw,f"(config-if)#switchport access vlan {vlan_list[1]}\n")
#         elif intf == "Gig0/3":
#             print(sw,f"(config-if)#switchport access vlan {vlan_list[2]}\n")
#         else:
#             print(sw,"(config-if)#Description towards agg switch")
#             for config2 in int_trunk_config[0:2]:
#                 print(sw,f"(config-if)#",config2)
#             print(sw,f"(config-if)switchport trunk allowed vlan add " + ",".join(vlan_list))
# print("\n### Switchport configuration has been completed ###\n")

#####multile switch config with just send commands
# sw_list = ["sw1", "sw2", "sw3"]
# int_list = ["Gig0/1", "Gig0/2", "Gig0/3", "Gig0/4"]
# vlan_list = ["10", "20", "30"]
# int_config = ["switchport", "switchport mode access", "switchport access vlan"]
# int_trunk_config = ["switchport", "switchport mode trunk", "switchport trunk allowed vlan add"]
# for sw in sw_list:
#     print("\nConfiguring", sw)
#     print("***************")
#     print(sw,"#config t")
#     for intf in int_list:
#         print(f"interface {intf}")
#         if intf in ["Gig0/1", "Gig0/2", "Gig0/3"]:
#             print("Description towards access ports")
#             for config in int_config[0:2]:
#                 print(config)
#         if intf == "Gig0/1":
#             print(f"switchport access vlan {vlan_list[0]}\n")
#         elif intf == "Gig0/2":
#             print(f"switchport access vlan {vlan_list[1]}\n")
#         elif intf == "Gig0/3":
#             print(f"switchport access vlan {vlan_list[2]}\n")
#         else:
#             print("Description towards agg switch")
#             for config2 in int_trunk_config[0:2]:
#                 print(config2)
#             print(f"switchport trunk allowed vlan add " + ",".join(vlan_list))
# print("\n### Switchport configuration has been completed ###\n")


## Configuration of multiple sites
# site_list = ["site-A", "site-B", "site-C"]
# sw_list = ["sw1", "sw2", "sw3"]
# int_list = ["Gig0/1", "Gig0/2", "Gig0/3", "Gig0/4"]
# vlan_list = ["10", "20", "30"]
# int_config = ["switchport", "switchport mode access", "switchport access vlan"]
# int_trunk_config = ["switchport", "switchport mode trunk", "switchport trunk allowed vlan add"]

# for site in site_list:
#     print("configuring", site)
#     print("$$$$$$$$$$$$$$$$$$$$$$$$")
#     for sw in sw_list:
# #     print("Configuring", sw)
#     print("***************")
#     print("config t\n")

# for intf in int_list:
#     print(f"interface {intf}")
#     print("=====================")
#     if intf in ["Gig0/1", "Gig0/2", "Gig0/3"]:
#         print("Description towards access ports")
#         for config in int_config[0:2]:
#             print(config)
#     if intf == "Gig0/1":
#         print(f"switchport access vlan {vlan_list[0]}\n")
#     elif intf == "Gig0/2":
#         print(f"switchport access vlan {vlan_list[1]}\n")
#     elif intf == "Gig0/3":
#         print(f"switchport access vlan {vlan_list[2]}\n")
#     else:
#         print("Description towards agg switch")
#         for config2 in int_trunk_config[0:2]:
#             print(config2)
#         print("switchport trunk allowed vlan add " + ",".join(vlan_list))
# print("\n### Switchport configuration has been completed ###\n")