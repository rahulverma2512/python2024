import os
import json
import requests
import yaml
from dotenv import load_dotenv
from netmiko import ConnectHandler
from Service_now_functions import check_existing_incident, get_incident_details, update_servicenow_incident,servicenow_inc_creation

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
                print(output, '\n')
                
                # Check if output is a list and contains dictionaries
                if isinstance(output, list):
                    for interface_info in output:
                        interface = interface_info.get('interface')
                        if interface_info.get('interface') == 'Ethernet0/1' and interface_info.get('status') == 'up':
                            shutdown_command = ["interface Ethernet0/1", "shutdown"]
                            net_connect.enable()
                            output2 = net_connect.send_config_set(shutdown_command)
                            print(f"Interface {interface_info.get('interface')} is down on {device['hostname']}")
                            print(f"Shutdown command executed on {device['hostname']}:")
                            print(output2)
                            net_connect.send_command("write memory")
                            print(f"Configuration saved on {device['hostname']}.")
                        elif interface_info.get('proto') == 'down':
                            # Check for existing incident and create a new one if none exists
                            sys_id = check_existing_incident(interface, device['hostname'])
                            if not sys_id:
                                sys_id = servicenow_inc_creation(interface, device['hostname'])
                            servicenow_instance = os.getenv('SERVICENOW_INSTANCE')
                            servicenow_user = os.getenv('SERVICENOW_USER')
                            servicenow_password = os.getenv('SERVICENOW_PASSWORD')
                            sys_id = 'cfaf56e453509e107d27f7e0a0490ee7'
                            url = f"https://{servicenow_instance}.service-now.com/api/now/v1/table/incident/{sys_id}?sysparm_exclude_ref_link=true"
                            # Perform the PUT request to update the incident
 

                            #if sys_id:
                                # Gather outputs for incident update
                            show_interface_output = net_connect.send_command(f"show interfaces {interface}")
                            show_logg_output = net_connect.send_command(f"show logg | i {interface}")
                            show_clock_output = net_connect.send_command("show clock")

                                # Combine outputs into work notes
                            work_note = (
                                f"Output of 'show interfaces {interface}':\n{show_interface_output}\n"
                                f"Output of 'show logg | i {interface}':\n{show_logg_output}\n"
                                f"Output of 'show clock':\n{show_clock_output}\n"
                                )
                            response = requests.put(
                                    url,
                                    auth=(servicenow_user, servicenow_password),
                                    headers={'Content-Type': 'application/json', 'Accept': 'application/json'},
                                    data=json.dumps({'work_notes': work_note})  # Use JSON with key 'work_notes'
                                )
                                
                                # Check the response
                            if response.status_code == 200:
                                print("Incident updated successfully:")
                                print(json.dumps(response.json(), indent=4))
                            else:
                                print(f"Failed to update the incident. Status code: {response.status_code}")
                                print(response.text)

                                # Update the incident with the command outputs
                                #update_servicenow_incident(sys_id, work_note)                            #######show_interface(interface)
                            #####service_now_inc_update(incident)
                            ####interface_noshut(hostname,interface)
                            #####service_now_inc_update after noshut(incident)
                        #elif interface_info.get('interface') == 'Ethernet0/1' and interface_info.get('status') == 'up':
                                #####service_now_inc_close(incident)

                            # Save the configuration (optional)
                        
            #print(output, '\n')
            # Disconnect from the device
            net_connect.disconnect()
            print(f"Disconnected from {device['hostname']}.\n")

        except Exception as e:
            print(f"An error occurred with {device['hostname']}: {str(e)}")

# Example usage
service_now_workflow()


