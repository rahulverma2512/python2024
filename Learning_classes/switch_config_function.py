##switch config using list - simple program to add given commands list to all the interfaces
int_list = ["Gig0/1", "Gig0/2", "Gig0/3", "Gig0/4"]
int_config = ["switchport", "switchport mode access", "switchport access vlan 10"]
def switch_config(int_list,int_config):
    print("config t")
    for intf in int_list:
        print("=====================")
        print(f"interface {intf}")
        for config in int_config:
            print(config)
    print("\n### Switchport configuaration has been completed ###")

if __name__ == "__main__":
    switch_config(int_list,int_config)


a = 20
b = 30
def my_sum(a,b):
    s = a+b
    print(s)
    return s
if __name__ == "__main__":    
    my_sum(a,b)
