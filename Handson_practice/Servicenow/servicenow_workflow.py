import requests
import json
from requests.auth import HTTPBasicAuth
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Cisco SD-WAN details
vmanage_host = "10.10.20.90"
username = 'admin'
password = 'C1sco12345'

# Initialize a session
session = requests.session()
# Disable SSL warnings (if using self-signed certs)
requests.packages.urllib3.disable_warnings()

login_url = f"https://{vmanage_host}:443/j_security_check"
login_data = {
    'j_username': username,
    'j_password': password
}

# Login and fetch cookies
response = session.post(login_url, data=login_data, verify=False)
print(response)

if response.status_code != 200 or 'Set-Cookie' not in response.headers:
    print("Login Failed")
    exit()
else:
    print("Login Successful")

# Debug: print cookies and headers to understand what's set
#print("Cookies after login:", session.cookies.get_dict())
#print("Response headers after login:", response.headers)

# Get CSRF token directly from token endpoint
csrf_url = f"https://{vmanage_host}/dataservice/client/token"
csrf_response = session.get(csrf_url, verify=False)

if csrf_response.status_code == 200:
    csrf_token = csrf_response.text
    print("CSRF token retrieved successfully:", csrf_token)
else:
    print("Failed to retrieve CSRF token from token endpoint:", csrf_response.status_code, csrf_response.text)
    csrf_token = None

# Ensure the token is available
if not csrf_token:
    print("Failed to get CSRF token")
    exit()


# Function to get device UUID for cEdge
def get_device_uuid(hostname):
    device_url = f"https://{vmanage_host}:443/dataservice/device"
    response = session.get(device_url, verify=False)
    if response.status_code == 200:
        devices = response.json()
        print(devices)
        # print(devices['data'])
        for device in devices['data']:
            if device['host-name'] == hostname and device['device-type'] == 'vedge':
                return device['uuid']
    return None

# Get UUID for a specific cEdge device
hostname = "Site1-cEdge01"
#device_uuid = get_device_uuid(hostname)
#print(device_uuid)

if hostname:
    interface_status_url = f"https://{vmanage_host}:443/dataservice/device/interface?deviceId=10.10.1.13"

    # Send GET request to the API
    response = session.get(interface_status_url, verify=False)
    devices = response.json()
    #print(devices)

    # Check if the request was successful
    if response.status_code == 200:
        interface_data = response.json()
        print(type(interface_data['data'][0]))
        for data in interface_data['data']:
            if data['ifname'] == 'Tunnel2':
                print(data['if-admin-status'])
                print("code working till linne 85")

# Function to shutdown Tunnel2 interface
def shutdown_interface(hostname):
    # Create CLI template to shutdown interface Tunnel2
    cli_template = {
    "templateName": "Test_Shutdown_Tunnel2",
    "templateDescription": "Shutdown Tunnel2 Interface",
    "deviceType": "vedge-C8000V",  # Replace with the correct device type
    "configType": "cli",
    "factoryDefault": False,
    "templateContent": """
 system
 system-ip             10.10.1.13
 overlay-id            1
 site-id               1001
 no transport-gateway enable
 port-offset           0
 control-session-pps   300
 admin-tech-on-failure
 sp-organization-name  DevNet_SD-WAN_Sandbox
 organization-name     DevNet_SD-WAN_Sandbox
 port-hop
 track-transport
 track-default-gateway
 console-baud-rate     115200
 no on-demand enable
 on-demand idle-timeout 10
 vbond 10.10.20.80 port 12346
!
service timestamps debug datetime msec
service timestamps log datetime msec
service tcp-keepalives-in
service tcp-keepalives-out
no service tcp-small-servers
no service udp-small-servers
hostname Site1-cEdge01
username admin privilege 15 secret 9 $9$2FUE2VIE2/II2E$37hmPFGj.uMd7ESq8VXUVE39GsQXDIHJ4FGC4EzJSyE
username developer privilege 15 secret 9 $9$3/2E2/EJ1l.J2.$7AEvjJTRNm1Dq0qsNYqhDCULqHfuQUTvk/8AyoE3Y4o
vrf definition 1
 rd 1:1
 address-family ipv4
  route-target export 1:1
  route-target import 1:1
  exit-address-family
 !
 address-family ipv6
  exit-address-family
 !
!
vrf definition Mgmt-intf
 rd 1:512
 address-family ipv4
  route-target export 1:512
  route-target import 1:512
  exit-address-family
 !
 address-family ipv6
  exit-address-family
 !
!
ip arp proxy disable
no ip finger
no ip rcmd rcp-enable
no ip rcmd rsh-enable
no ip domain lookup
no ip dhcp use class
no ip ftp passive
ip route 0.0.0.0 0.0.0.0 10.10.23.9
ip route 0.0.0.0 0.0.0.0 10.10.23.41
ip route vrf Mgmt-intf 0.0.0.0 0.0.0.0 10.10.20.254
ip scp server enable
ip bootp server
no ip source-route
no ip ssh bulk-mode
no ip http server
no ip http secure-server
ip nat settings central-policy
ipv6 unicast-routing
ipv6 rip vrf-mode enable
cdp run
interface GigabitEthernet1
 description   port.sbx-mgmt
 no shutdown
 arp timeout 1200
 vrf forwarding Mgmt-intf
 ip address 10.10.20.174 255.255.255.0
 no ip redirects
 ip mtu    1500
 load-interval 30
 mtu           1500
 negotiation auto
exit
interface GigabitEthernet2
 description   mpls-link
 no shutdown
 arp timeout 1200
 ip address 10.10.23.10 255.255.255.252
 no ip redirects
 ip mtu    1500
 load-interval 30
 mtu           1500
 negotiation auto
exit
interface GigabitEthernet3
 description   port.site1-sw01
 no shutdown
 arp timeout 1200
 vrf forwarding 1
 ip address 10.10.21.1 255.255.255.0
 no ip redirects
 ip mtu    1500
 load-interval 30
 mtu           1500
 negotiation auto
exit
interface GigabitEthernet4
 description   internet-link
 no shutdown
 arp timeout 1200
 ip address 10.10.23.42 255.255.255.252
 no ip redirects
 ip mtu    1500
 load-interval 30
 mtu           1500
 negotiation auto
exit
interface Tunnel2
 shutdown
 ip unnumbered GigabitEthernet2
 no ip redirects
 ipv6 unnumbered GigabitEthernet2
 no ipv6 redirects
 tunnel source GigabitEthernet2
 tunnel mode sdwan
exit
interface Tunnel4
 no shutdown
 ip unnumbered GigabitEthernet4
 no ip redirects
 ipv6 unnumbered GigabitEthernet4
 no ipv6 redirects
 tunnel source GigabitEthernet4
 tunnel mode sdwan
exit
control-plane
!
clock timezone UTC 0 0
logging persistent size 104857600 filesize 10485760
no logging monitor
logging buffered 512000
logging console
aaa authentication login default local
aaa authorization exec default local
aaa server radius dynamic-author
!
snmp-server ifindex persist
fhrp version vrrp v3
line aux 0
 stopbits 1
!
line con 0
 speed    115200
 stopbits 1
!
line vty 0 4
 transport input ssh
!
line vty 5 80
 transport input ssh
!
lldp run
nat64 translation timeout tcp 3600
nat64 translation timeout udp 300
sdwan
 interface GigabitEthernet2
  tunnel-interface
   encapsulation ipsec weight 1
   no border
   color mpls
   no last-resort-circuit
   no low-bandwidth-link
   no vbond-as-stun-server
   vmanage-connection-preference 5
   port-hop
   carrier                       default
   nat-refresh-interval          5
    hello-interval                1000
   hello-tolerance               12
   allow-service all
   no allow-service bgp
   allow-service dhcp
   allow-service dns
   allow-service icmp
   no allow-service sshd
   no allow-service netconf
   no allow-service ntp
   no allow-service ospf
   no allow-service stun
   allow-service https
   no allow-service snmp
   no allow-service bfd
  exit
 exit
 interface GigabitEthernet4
  tunnel-interface
   encapsulation ipsec weight 1
   no border
   color public-internet
   no last-resort-circuit
   no low-bandwidth-link
   no vbond-as-stun-server
   vmanage-connection-preference 5
   port-hop
   carrier                       default
   nat-refresh-interval          5
    hello-interval                1000
   hello-tolerance               12
   allow-service all
   no allow-service bgp
   allow-service dhcp
   allow-service dns
   allow-service icmp
   no allow-service sshd
   no allow-service netconf
   no allow-service ntp
   no allow-service ospf
   no allow-service stun
   allow-service https
   no allow-service snmp
   no allow-service bfd
  exit
 exit
 appqoe
  no tcpopt enable
  no dreopt enable
  no httpopt enable
 !
 omp
  no shutdown
  send-path-limit  4
  ecmp-limit       4
  graceful-restart
  no as-dot-notation
  timers
   holdtime               60
   advertisement-interval 1
   graceful-restart-timer 43200
   eor-timer              300
  exit
  address-family ipv4
   advertise connected
   advertise static
  !
  address-family ipv6
   advertise connected
   advertise static
  !
 !
!
bfd default-dscp 48
bfd app-route multiplier 6
bfd app-route poll-interval 600000
security
 ipsec
  rekey          86400
  replay-window  512
  integrity-type esp ip-udp-esp
 !
!
sslproxy
 no enable
 rsa-key-modulus      2048
 certificate-lifetime 730
 eckey-type           P256
 ca-tp-label          PROXY-SIGNING-CA
 settings expired-certificate  drop
 settings untrusted-certificate drop
 settings unknown-status       drop
 settings certificate-revocation-check none
 settings unsupported-protocol-versions drop
 settings unsupported-cipher-suites drop
 settings failure-mode         close
 settings minimum-tls-ver      TLSv1
 dual-side optimization enable
!

""",
    #"deviceModels": "vedge-C8000V"  # Replace with the correct device model
    }
    
    url = f"https://{vmanage_host}/dataservice/template/device/cli"
    headers = {
            'Content-Type': 'application/json',
            'X-XSRF-TOKEN': csrf_token  # Include CSRF Token in the header
        }

    simple_cli_template = {
    "templateName": "Simple_Test_Template",
    "templateDescription": "Simple test template",
    "deviceType": "vedge-C8000V",  # Use a valid device type
    "configType": "cli",
    "factoryDefault": False,
    "templateContent": "interface Tunnel2\nshutdown\nexit\n"
    }

    response = session.post(url, headers=headers, json=simple_cli_template, verify=False)
    print(response.status_code, response.text)

    # Create CLI Template using vManage API
    if csrf_token:
        url = f"https://{vmanage_host}/dataservice/template/device/cli"
        headers = {
            'Content-Type': 'application/json',
            'X-XSRF-TOKEN': csrf_token  # Include CSRF Token in the header
        }

        response = session.post(url, headers=headers, json=cli_template, verify=False)
        
        if response.status_code == 200:
            print("CLI template created successfully.")
            template_response = response.json()
            print(json.dumps(template_response, indent=4))
        else:
            print("Failed to create CLI template:", response.status_code, response.text)
            

        # Push the CLI template to the vEdge
        url = f"https://{vmanage_host}:443/dataservice/template/device/config/input"
        headers = {
            'Content-Type': 'application/json',
            'X-XSRF-TOKEN': csrf_token  # Include CSRF Token in the header
        }

        response = session.post(url, headers=headers, json=cli_template, verify=False)

        if response.status_code == 200:
            print("working till line 133")
            # Apply the CLI template
            apply_url = f"https://{vmanage_host}:443/dataservice/device/action/configuration/attachfeature"
            payload = {
                "deviceTemplateList": [
                    {
                        "templateId": cli_template['templateName'],
                        "device": [
                            {
                                "deviceId": hostname,
                                "deviceIP": "10.10.1.13"
                            }
                        ]
                    }
                ]
            }

            apply_response = session.post(apply_url, headers=headers, json=payload, verify=False)

            if apply_response.status_code == 200:
                print(f"Shutdown command sent to Tunnel2 on device with UUID: {hostname}")
                return True
            else:
                print(f"Failed to apply configuration: {apply_response.text}")
                return False
        else:
            print(f"Failed to create CLI template: {response.text}")
            return False

# Function to check interface status
def check_interface_status(hostname):
    interface_status_url = f"https://{vmanage_host}:443/dataservice/device/interface?deviceId=10.10.1.13"
    headers = {
        'Content-Type': 'application/json',
        'X-XSRF-TOKEN': csrf_token  # Include CSRF Token in the header
    }
    
    response = session.get(interface_status_url, headers=headers, verify=False)

    if response.status_code == 200:
        interface_data = response.json()
        for data in interface_data['data']:
            if data['ifname'] == 'Tunnel2':
                print(f"Tunnel2 interface admin status: {data['if-admin-status']}")
                return data['if-admin-status']
    else:
        print("Failed to get interface status.")
        return None


# Main logic
hostname = "Site1-cEdge01"
#device_uuid = get_device_uuid(hostname)
#get_device_uuid(hostname)
if hostname:
    # Step 1: Shutdown Tunnel2 interface
    if shutdown_interface(hostname):
        # Wait a few seconds to let configuration propagate
        time.sleep(10)
        # Step 2: Check interface status
        check_interface_status(hostname)
else:
    print("Device UUID not found.")