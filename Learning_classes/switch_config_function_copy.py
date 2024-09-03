from switch_config_function import my_sum    #selective import
import switch_config_function

intf = ["Gig0/1", "Gig0/2", "Gig0/3", "Gig0/4"]
commands = ["switchport", "switchport mode access", "switchport access vlan 10"]

switch_config_function.switch_config(intf,commands)

p = 10
q = 20
my_sum(p,q)