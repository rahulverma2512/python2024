import os
import requests
import json
import yaml
from dotenv import load_dotenv
from netmiko import ConnectHandler

import os
import requests
env_file="env_vars.env"
load_dotenv(dotenv_path=env_file)

def get_incident_details(sys_ids):
    """
    Function to retrieve details of multiple incidents using their sys_id.

    Args:
        sys_ids (list or str): The sys_id(s) of the incidents.

    Returns:
        list: A list of dictionaries containing details of the incidents if found, empty list otherwise.
    """
    if isinstance(sys_ids, str):
        sys_ids = [sys_ids]

    servicenow_instance = os.getenv('SERVICENOW_INSTANCE')
    servicenow_user = os.getenv('SERVICENOW_USER')
    servicenow_password = os.getenv('SERVICENOW_PASSWORD')

    incident_details_list = []

    for sys_id in sys_ids:
        url = f"https://{servicenow_instance}.service-now.com/api/now/table/incident/{sys_id}"
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"  # Ensure request is for JSON response
        }

        try:
            response = requests.get(url, auth=(servicenow_user, servicenow_password), headers=headers)
            if response.status_code == 200:
                result = response.json().get('result', None)
                if result:
                    incident_details_list.append(result)
                else:
                    print(f"No details found for incident with sys_id: {sys_id}.")
            elif response.status_code == 404:
                print(f"Incident with sys_id {sys_id} not found. HTTP Status: 404. Response: {response.text}")
            elif response.status_code == 403:
                print(f"Access forbidden for sys_id {sys_id}. HTTP Status: 403. Response: {response.text}")
            elif response.status_code == 400:
                print(f"Bad request for sys_id {sys_id}. HTTP Status: 400. Response: {response.text}")
            else:
                print(f"Failed to retrieve incident details for sys_id {sys_id}. HTTP Status: {response.status_code}. Response: {response.text}")

        except requests.exceptions.RequestException as e:
            print(f"An error occurred while retrieving incident details for sys_id {sys_id}: {str(e)}")

    return incident_details_list

def get_incident_state(sys_id):
    """
    Function to fetch the state of an incident by sys_id.

    Args:
        sys_id (str): The sys_id of the incident to fetch.

    Returns:
        int: The state of the incident or None if an error occurs.
    """
    servicenow_instance = os.getenv('SERVICENOW_INSTANCE')
    servicenow_user = os.getenv('SERVICENOW_USER')
    servicenow_password = os.getenv('SERVICENOW_PASSWORD')

    url = f"https://{servicenow_instance}.service-now.com/api/now/table/incident"
    
    query = {
        'sysparm_query': f'sys_id={sys_id}',
        'sysparm_fields': 'state'
    }

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    try:
        response = requests.get(url, auth=(servicenow_user, servicenow_password), headers=headers, params=query)
        if response.status_code == 200:
            results = response.json().get('result', [])
            if results:
                state = results[0].get('state', None)
                return int(state) if state is not None else None
            else:
                print("No incident found with the provided sys_id.")
                return None
        else:
            print(f"Failed to retrieve incident state. HTTP Status: {response.status_code}. Response: {response.text}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while retrieving incident state: {str(e)}")
        return None


def check_existing_incident(interface, hostname):
    """
    Function to check if existing ServiceNow incidents already exist for a given interface and hostname.

    Args:
        interface (str): The name of the interface (e.g., 'Ethernet0/1').
        hostname (str): The hostname of the device.

    Returns:
        list: A list of dictionaries containing incident_number, sys_id, and state for the found incidents.
    """
    servicenow_instance = os.getenv('SERVICENOW_INSTANCE')
    servicenow_user = os.getenv('SERVICENOW_USER')
    servicenow_password = os.getenv('SERVICENOW_PASSWORD')

    url = f"https://{servicenow_instance}.service-now.com/api/now/table/incident"
    query = {
        'short_description': f"Interface {interface} is down on {hostname}",
        'active': 'true'
    }
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    incidents = []  # Initialize the list to hold incident details

    try:
        response = requests.get(url, auth=(servicenow_user, servicenow_password), headers=headers, params=query)
        if response.status_code == 200:
            results = response.json().get('result', [])
            if results:
                for incident in results:
                    sys_id = incident.get('sys_id', 'Unknown')
                    state = get_incident_state(sys_id)
                    if state in [1, 2, 3]:  # Only consider states 1 (New), 2 (In Progress), 3 (On Hold)
                        incident_number = incident.get('number', 'Unknown')
                        incidents.append({'number': incident_number, 'sys_id': sys_id, 'state': state})
                        print(f"Existing incident found: Number: {incident_number}, Sys_ID: {sys_id}, State: {state}")
                return incidents  # Return all found incidents in the specified states
            else:
                print(f"No existing incident found for {hostname} - Interface {interface}. Creating new incident....")
                return []
        else:
            print(f"Failed to check existing incidents. Status Code: {response.status_code}, Response: {response.text}")
            return []
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while checking existing incidents for {hostname} - Interface {interface}: {str(e)}")
        return []




def update_servicenow_incident(sys_id, incident_number, work_note):
    """
    Function to update a specific ServiceNow incident with a work note using sys_id.

    Args:
        sys_id (str): The sys_id of the incident to update.
        incident_number (str): The number of the incident to update.
        work_note (str): The work note to add to the incident.

    Returns:
        None
    """
    servicenow_instance = os.getenv('SERVICENOW_INSTANCE')
    servicenow_user = os.getenv('SERVICENOW_USER')
    servicenow_password = os.getenv('SERVICENOW_PASSWORD')

    # URL to update the incident using sys_id
    url = f"https://{servicenow_instance}.service-now.com/api/now/v1/table/incident/{sys_id}?sysparm_exclude_ref_link=true"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    update_data = {
        'work_notes': work_note
    }

    try:
        # Update the incident with the work note
        response = requests.patch(url, auth=(servicenow_user, servicenow_password), headers=headers, json=update_data)
        if response.status_code == 200:
            print(f"Incident: {incident_number[0]['number']}  updated successfully.")
        else:
            print(f"Failed to update incident: {incident_number} with sys_id: {sys_id}. Status Code: {response.status_code}, Response: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while updating incident: {incident_number} with sys_id: {sys_id}: {str(e)}")



def servicenow_inc_creation(interface, hostname):
    """
    This function creates a ServiceNow incident for a specified interface and hostname.

    Args:
        interface (str): The name of the interface.
        hostname (str): The hostname of the device.

    Returns:
        None
    """
    # Load environment variables for ServiceNow
    servicenow_instance = os.getenv('SERVICENOW_INSTANCE')
    servicenow_user = os.getenv('SERVICENOW_USER')
    servicenow_password = os.getenv('SERVICENOW_PASSWORD')

    # ServiceNow API URL for creating incidents
    url = f"https://{servicenow_instance}.service-now.com/api/now/table/incident"

    # Data to be sent to ServiceNow API
    data = {
        "short_description": f"Interface {interface} is down on {hostname}",
        "description": f"The interface {interface} on device {hostname} is currently down. Please investigate.",
        "caller" : "Rahul Verma",
        "category": "Network",
        "subcategory": "IP Address",
        "Configuration item" : {hostname},
        "priority": "3"
    }

    # Headers for the API request
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    # Send a POST request to ServiceNow API to create an incident
    response = requests.post(url, auth=(servicenow_user, servicenow_password), headers=headers, json=data)

    if response.status_code == 201:
        incident_details = response.json().get('result', {})
        sys_id = incident_details.get('sys_id')
        incident_number = incident_details.get('number')
        print(f"Incident created successfully. Sys_id: {sys_id}, Incident Number: {incident_number}")
        return sys_id
    else:
        print(f"Failed to create incident. Status Code: {response.status_code}, Response: {response.text}")
        return None


import os
import requests
import json

def resolve_servicenow_incident(sys_id, caller,interface):
    """
    Function to resolve a specific ServiceNow incident with the given information.

    Args:
        sys_id (str): The sys_id of the incident to update.
        caller (str): The name of the caller to set.
        config_item (str): The configuration item related to the incident.
        interface (str): The interface that came up.

    Returns:
        None
    """
    servicenow_instance = os.getenv('SERVICENOW_INSTANCE')
    servicenow_user = os.getenv('SERVICENOW_USER')
    servicenow_password = os.getenv('SERVICENOW_PASSWORD')

    # URL to update the incident using sys_id
    url = f"https://{servicenow_instance}.service-now.com/api/now/table/incident/{sys_id}?sysparm_exclude_ref_link=true"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    
    # Data to update the incident
    update_data = {
        'caller_id': "rahul verma",
        'incident_state': '6',  # Assuming '6' is the code for 'Resolved' state
        'resolution_code': 'Solution provided',
        'close_notes': f"Interface {interface} came up. Resolving ticket."
    }

    try:
        # Send the PATCH request to update the incident
        response = requests.patch(url, auth=(servicenow_user, servicenow_password), headers=headers, json=update_data)
        if response.status_code == 200:
            print(f"Incident with incident: {incident_number} resolved successfully.")
        else:
            print(f"Failed to resolve incident with sys_id {sys_id}. Status Code: {response.status_code}, Response: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while resolving incident with sys_id {sys_id}: {str(e)}")