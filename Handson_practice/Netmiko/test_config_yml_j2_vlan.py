import yaml,jinja2,os
from netmiko import ConnectHandler
config_file = open("test_jinja_data_vlan.yml",'r')
data = yaml.safe_load(config_file)
config_file.close()

inv_file = open("inv_vlan_conf.yml",'r')
devices = yaml.safe_load(inv_file)
inv_file.close()
# print(data)

# print("vlan", data["vlans"][1])


#load jinja2 template from file
template_loader = jinja2.FileSystemLoader(searchpath=".")
env = jinja2.Environment(loader=template_loader)
template = env.get_template("testjinja_vlan.j2")
# # print(template)

# render the template with the data
file = open("test_jinja_wr_vlan.conf",'w')
rendered_output = template.render(conf_data=data)
output_file = file.write(rendered_output)
config_list = rendered_output.splitlines()
file.close()
# print(rendered_output)
# print(config_list)
# config2_file = open("test_jinja_wr_vlan.conf","r")
# config_list = config2_file.readlines()

# print(config_list)

# devices = [{
#     'device_type': 'cisco_ios',
#     'host': '192.168.10.148',  # IP address of the device
#     'username': 'sw',
#     'password': 'sw',
#     'port': 22,  # default SSH port
#     'secret': 'sw'  # enable password if applicable
#     },
# {
#     'device_type': 'cisco_ios',
#     'host': '192.168.10.147',  # IP address of the device
#     'username': 'sw',
#     'password': 'sw',
#     'port': 22,  # default SSH port
#     'secret': 'sw'  # enable password if applicable
#     }
# ]

# # Establish SSH connection
# switches = ['sw1','sw2']
# for sw in switches:

user = os.getenv('username')
password = os.getenv('password')  
    
for device in devices:
    print("Connecting to device:",device['hostname'],'\n')
    print("Connected successfully!",'\n')
    # net_connect = ConnectHandler(**device) #use code from line 34 to 50
    # net_connect = ConnectHandler(device_type=device['device_type'],host=device['host'],username='sw',password='sw') #uses inv_vlan_conf.yml
 
#in bash export below environment variable
    #export username = sw
    #export password = sw
    net_connect = ConnectHandler(device_type=device['device_type'],host=device['host'],username=user,password=password)#to connect use git bash and then run python file
    net_connect.enable()  # Enter enable mode if needed


    
# # Example: sending a command and printing output
    # output = net_connect.send_command("show vlan")
# # output = net_connect.send_config_set(config_list)
    output = net_connect.send_config_from_file("test_jinja_wr_vlan.conf")
    output2 = net_connect.send_command("show vlan bri")
    print(output2)
# print("*******Pushing configuration:**********")
# # print(output)
    
# # Disconnect from the device
    net_connect.disconnect()
    print("Disconnected from device.",'\n')
