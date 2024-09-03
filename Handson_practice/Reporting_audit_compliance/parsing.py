import os
import yaml
from dotenv import load_dotenv
from netmiko import ConnectHandler

# Load environment variables from .env file
load_dotenv(dotenv_path="env_vars.env")

# Open YAML inventory file and load devices
with open("inv.yaml", 'r') as file:
    devices = yaml.safe_load(file)

# List of commands to execute on each device
listofcommands = ["show interface", "show vlan", "show cdp neighbors"]

for device in devices:
    # Retrieve environment variables for the current device
    username = os.getenv(device['username'])
    password = os.getenv(device['password'])
    secret = os.getenv(device['secret'])

    # Connect to the device using Netmiko
    net_connect = ConnectHandler(
        device_type=device['device_type'],
        host=device['host'],
        username=username,
        password=password,
        secret=secret  # Pass the enable secret
    )
    print(f"connecting to... {device['hostname']}.", '\n')

    # Execute commands and print output
    # for command in listofcommands:
    #     output = net_connect.send_command(command, use_textfsm=True)
    #     print(f"Device {device['hostname']} - Command: {command}")
    output = net_connect.send_command("show ip int bri", use_textfsm=True)
    print(output, '\n')

    # Disconnect from the device
    net_connect.disconnect()
    print(f"Disconnected from {device['hostname']}.", '\n')
        
