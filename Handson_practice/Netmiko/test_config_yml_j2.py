import yaml,jinja2
from netmiko import ConnectHandler
config_file = open("test_jinja_data.yml",'r')
data = yaml.safe_load(config_file)
# print(data)
# print("vlan", data["vlans"][1])


#load jinja2 template from file
template_loader = jinja2.FileSystemLoader(searchpath=".")
env = jinja2.Environment(loader=template_loader)
template = env.get_template("testjinja.j2")
# # print(template)

# render the template with the data
file = open("test_jinja_wr.conf",'w')
rendered_output = template.render(conf_vlan=data)
output_file = file.write(rendered_output)
file.close()
# print(type(rendered_output))

config2_file = open("test_jinja_wr.conf","r")
config_list = config2_file.readlines()
# # print(config_list)

device = {
    'device_type': 'cisco_ios',
    'host': '192.168.10.148',  # IP address of the device
    'username': 'sw2',
    'password': 'sw2',
    'port': 22,  # default SSH port
    'secret': 'sw2'  # enable password if applicable
    }

# Establish SSH connection
print("Connecting to device...")
net_connect = ConnectHandler(**device)
net_connect.enable()  # Enter enable mode if needed
print("Connected successfully!")
    
# Example: sending a command and printing output
# output = net_connect.send_command("show vlan")
# output = net_connect.send_config_set(config_list)
output = net_connect.send_config_from_file("test_jinja_wr.conf")
output2 = net_connect.send_command("show vlan bri")
print(output2)
print("*******Pushing configuration:**********")
# print(output)
    
# Disconnect from the device
net_connect.disconnect()
print("Disconnected from device.")


