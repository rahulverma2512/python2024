import os
import time
import json
import requests
import yaml
from dotenv import load_dotenv
from netmiko import ConnectHandler
from Service_now_functions import check_existing_incident, get_incident_details, update_servicenow_incident,servicenow_inc_creation,resolve_servicenow_incident

def service_now_workflow(yaml_file="inv.yaml", env_file="env_vars.env", commands=None):
    """
    This function loads environment variables, reads a YAML inventory file,
    connects to each device, and executes a list of commands using Netmiko.

    Args:
        yaml_file (str): Path to the YAML inventory file (default: "inv.yaml").
        env_file (str): Path to the environment variables file (default: "env_vars.env").
        commands (list): List of commands to execute on each device. If None, defaults to a predefined list.

    Returns:
        None
    """
    # Load environment variables from the .env file
    load_dotenv(dotenv_path=env_file)

    # Open YAML inventory file and load devices
    with open(yaml_file, 'r') as file:
        devices = yaml.safe_load(file)

    # Default list of commands if none provided
    if commands is None:
        commands = ["show ip int bri"]

    for device in devices:
        # Retrieve environment variables for the current device
        username = os.getenv(device['username'])
        password = os.getenv(device['password'])
        secret = os.getenv(device['secret'])

        try:
            # Connect to the device using Netmiko
            net_connect = ConnectHandler(
                device_type=device['device_type'],
                host=device['host'],
                username=username,
                password=password,
                secret=secret  # Pass the enable secret
            )
            print(f"Connecting to... {device['hostname']}.\n")

            # Execute each command in the list and print the output
            for command in commands:
                output = net_connect.send_command(command, use_textfsm=True)
                print(f"Device {device['hostname']} - Command: {command}")
                print(f"Precheck of interface status of Device : {device['hostname']}, '\n', {net_connect.send_command(command)}, '\n'" )
                
                # Check if output is a list and contains dictionaries
                if isinstance(output, list):
                    for interface_info in output:
                        #interface = interface_info.get('interface')
                        #print(interface_info.get('status'))
                        if interface_info.get('interface') == 'Ethernet0/1' and interface_info.get('status') == 'up':
                            #print("#######################Testing################")
                            shutdown_command = ["interface Ethernet0/1", "shutdown"]
                            net_connect.enable()
                            net_connect.send_config_set(shutdown_command)           
                            print(f"Shutdown command executed on {device['hostname']}:")
                            print(f"Interface {interface_info.get('interface')} is down on {device['hostname']}")
                            #net_connect.send_command("write memory")
                            #print(f"Configuration saved on {device['hostname']}.")
                
                time.sleep(15)
                output2 = net_connect.send_command(command, use_textfsm=True)
                for interface_info in output2:
                    interface = interface_info.get('interface')     
                    if interface_info.get('proto') == 'down':                
            # Check for existing incident and create a new one if none exists
                        incidents = check_existing_incident(interface, device['hostname'])
                        if not incidents:
                            sys_id = servicenow_inc_creation(interface, device['hostname'])
                        else:
                            # Retrieve the sys_id from the existing incidents
                            sys_id = incidents[0]['sys_id']
                        if sys_id:
                            # Gather outputs for incident update
                            show_interface_output = net_connect.send_command(f"show interfaces {interface}")
                            show_logg_output = net_connect.send_command(f"show logging | i {interface}")
                            show_clock_output = net_connect.send_command("show clock")

                            # Combine outputs into work notes
                            work_note = (
                                f"Output of 'show interfaces {interface}':\n{show_interface_output}\n"
                                # f"Output of 'show logging | i {interface}':\n{show_logg_output}\n"
                                f"Output of 'show clock':\n{show_clock_output}\n"
                            )
                            update_servicenow_incident(sys_id,incidents,work_note)  
                            #Remediation of down interface
                    #elif interface_info.get('interface') == 'Ethernet0/1' and interface_info.get('proto') == 'down':
                        noshut_command = ["interface Ethernet0/1", "no shutdown"]
                        net_connect.enable()
                        output3 = net_connect.send_config_set(noshut_command)
                        print(f"no shutdown command executed on {device['hostname']}:") 
                        print(f"Interface {interface_info.get('interface')} is up now on {device['hostname']}")
                        #print(f"interface status of Device : {device['hostname']} after remediation was applied, '\n', {output3}, '\n' " )
                time.sleep(15)  # wait for 5 seconds
                        #net_connect.send_command("write memory")
                        #print(f"Configuration saved on {device['hostname']}.")
                        
                        ####service_now_inc_update after noshut(incident)
                output4 = net_connect.send_command(command, use_textfsm=True)
                print(net_connect.send_command(command))
                for interface_info in output4:
                    interface = interface_info.get('interface')            
                    if interface_info.get('interface') == 'Ethernet0/1' and interface_info.get('status') == 'up': 
                        print("updating notes after link came up")
                        show_interface_output = net_connect.send_command(f"show interfaces {interface}")
                        show_logg_output = net_connect.send_command(f"show logging | i {interface}")
                        show_clock_output = net_connect.send_command("show clock")
                         # Combine outputs into work notes
                        work_note = (
                                f"Output of 'show interfaces {interface}':\n{show_interface_output}\n"
                                f"Output of 'show logging | i {interface}':\n{show_logg_output}\n"
                                f"Output of 'show clock':\n{show_clock_output}\n"
                            )
                        update_servicenow_incident(sys_id,incidents,work_note)
                        print(f"Issue has been fixed Incident: {incidents} will be resolved")
                        interface = "Ethernet0/1"
                        caller = "Rahul Verma"
                        resolve_servicenow_incident(sys_id, caller,interface)

            # Disconnect from the device
            net_connect.disconnect()
            print(f"Disconnected from {device['hostname']}.\n")

        except Exception as e:
            print(f"An error occurred with {device['hostname']}: {str(e)}")

# Example usage
service_now_workflow()


